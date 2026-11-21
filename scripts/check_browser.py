"""Exercise the built learning site at a GitHub Pages-style project subpath."""
import argparse
import functools
import http.server
import json
import os
import threading
from pathlib import Path
from playwright.sync_api import sync_playwright
from validate import search_probes

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
PREFIX = "/sdlc-delivery-map/"


class ProjectSite(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if not self.path.startswith(PREFIX):
            self.send_error(404)
            return
        self.path = self.path[len(PREFIX) - 1:]
        super().do_GET()

    def log_message(self, *args):
        pass


def check_search(page, base, topics, integration):
    for query, key in search_probes(integration).items():
        page.goto(base + "topics.html")
        page.locator("#topic-search").fill(query)
        route = f"topics/{key}.html"
        link = page.locator(f'.topic-row:visible a[href="{route}"]')
        assert link.count() == 1, f"{query!r} should find {key}"
        link.click()
        page.wait_for_url(base + route)
        assert page.locator("h1").inner_text() == topics[key]["title"]
        if topics[key].get("kind") == "deep-dive":
            assert page.get_by_role("heading", name=topics[key]["detail"][0]["title"], exact=True).is_visible()


def check_detail_routes(page, base, lessons):
    titles = {item["id"]: item["title"] for item in lessons}
    for item in lessons:
        if item.get("kind") != "deep-dive":
            continue
        parent = item["parent"]
        page.goto(base + f"topics/{parent}.html")
        link = page.locator("#go-deeper").get_by_role("link", name=item["title"], exact=True)
        link.focus()
        page.keyboard.press("Enter")
        page.wait_for_url(base + f'topics/{item["id"]}.html')
        assert page.locator("h1").inner_text() == item["title"]
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth + 1"), item["id"]
        page.set_viewport_size({"width": 1440, "height": 900})
        for section in item["detail"]:
            jump = page.get_by_role("navigation", name="On this page").get_by_role(
                "link", name=section["title"], exact=True)
            destination = jump.get_attribute("href")
            assert destination.startswith("#") and page.locator(destination).count() == 1
        page.set_viewport_size({"width": 390, "height": 844})
        summary = page.locator(".mobile-contents summary")
        summary.focus()
        page.keyboard.press("Enter")
        mobile_toc = page.get_by_role("navigation", name="On this page")
        failure = mobile_toc.locator('a[href="#worked-failure"]')
        failure.focus()
        page.keyboard.press("Enter")
        page.wait_for_url(base + f'topics/{item["id"]}.html#worked-failure')
        parent_link = page.get_by_role("navigation", name="Breadcrumb").get_by_role(
            "link", name=titles[parent], exact=True)
        parent_link.focus()
        page.keyboard.press("Enter")
        page.wait_for_url(base + f"topics/{parent}.html")


def check_flow_routes(page, base, lessons):
    flows = [item for item in lessons if item.get("kind") == "flow"]
    assert len(flows) == 6
    page.goto(base + "tour.html#flows")
    links = page.locator("#flows a")
    assert links.evaluate_all("(links) => links.map(a => a.getAttribute('href'))") == [
        f"topics/{flow['id']}.html" for flow in flows
    ]
    links.first.focus()
    page.keyboard.press("Enter")
    for index, item in enumerate(flows):
        page.wait_for_url(base + f'topics/{item["id"]}.html')
        assert page.locator("h1").inner_text() == item["title"]
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth + 1")
        assert page.locator("#next-decision .handoffs a").count() == len(item["touches"])
        overview = item["touches"][0]
        page.locator(f'#next-decision a[href="../topics/{overview}.html"]').click()
        page.locator(f'#related-flows a[href="../topics/{item["id"]}.html"]').click()
        if index + 1 < len(flows):
            page.get_by_role("navigation", name="Reading order").get_by_role("link", name="Next topic").click()


def check_build_reading_order(page, base):
    order = ("local-dev-loop", "branch-commit-conventions", "code-review-practice",
             "ci-integration-tests", "merge-rules", "image-build")
    page.goto(base + "topics/ci-security-checks.html")
    pilot_pager = page.get_by_role("navigation", name="Reading order")
    assert pilot_pager.get_by_role("link", name="Next topic").count() == 0
    page.goto(base + f"topics/{order[0]}.html")
    for prior, current in zip(order, order[1:]):
        pager = page.get_by_role("navigation", name="Reading order")
        pager.get_by_role("link", name="Next topic").click()
        page.wait_for_url(base + f"topics/{current}.html")
        previous_link = pager.get_by_role("link", name="Previous topic")
        assert previous_link.get_attribute("href") == f"{prior}.html"


def check_figure_labels(page, base):
    scripts = Path(__file__).resolve().parent
    measure = (scripts / "figure_label_bounds.js").read_text()
    fixture = scripts / "tests/fixtures/regression-card.svg"
    page.set_content(fixture.read_text())
    assert any("bottom of its box" in error for error in page.evaluate(measure)), (
        "The original regression-scope card must fail its bottom padding check")
    page.locator("rect").evaluate("rect => rect.setAttribute('height', '132')")
    assert not page.evaluate(measure), "Increasing the card height should clear the label"
    page.locator("text").evaluate("label => label.setAttribute('x', '330')")
    assert any("right of its box" in error for error in page.evaluate(measure)), (
        "A label outside its box must still be checked against that box")

    figures = sorted((ROOT / "site/assets/figures").rglob("*.svg"))
    assert figures, "No instructional figures found"
    errors = []
    for width, height in ((1280, 900), (320, 812)):
        page.set_viewport_size({"width": width, "height": height})
        for figure in figures:
            route = figure.relative_to(ROOT / "site").as_posix()
            response = page.goto(base + route)
            assert response.ok, f"Missing built figure: {route}"
            errors.extend(f"{route} at {width}px: {error}" for error in page.evaluate(measure))
    assert not errors, "\n".join(errors)
    print(f"Checked label bounds in {len(figures)} instructional figures at desktop and phone widths")


def main(integration=False):
    lessons = [item for file in sorted((ROOT / "content").glob("[0-9][0-9]-*.json"))
               for item in json.loads(file.read_text())]
    handler = functools.partial(ProjectSite, directory=str(DIST))
    with http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler) as server:
        threading.Thread(target=server.serve_forever, daemon=True).start()
        base = f"http://127.0.0.1:{server.server_port}{PREFIX}"
        try:
            with sync_playwright() as runtime:
                options = {}
                if os.getenv("PLAYWRIGHT_CHROMIUM_EXECUTABLE"):
                    options["executable_path"] = os.environ["PLAYWRIGHT_CHROMIUM_EXECUTABLE"]
                browser = runtime.chromium.launch(**options)
                page = browser.new_page(viewport={"width": 1280, "height": 900})
                errors = []
                page.on("pageerror", lambda e: errors.append(str(e)))
                page.on("response", lambda r: errors.append(f"{r.status} {r.url}") if r.url.startswith(base) and r.status >= 400 else None)
                page.goto(base)
                all_regions = json.loads((ROOT / "content/hotspots.json").read_text())
                anchors = page.locator("#delivery-map a.map-link")
                assert anchors.count() == len(all_regions), "Every region needs a map link"
                assert page.locator("#zoom-in").count() == page.locator("#zoom-out").count() == 1
                page.locator("#zoom-in").click()
                assert page.locator("#zoom-level").inner_text() == "125%"
                page.locator("#zoom-out").click()
                page.locator("#zoom-fit").click()
                assert page.locator("#zoom-level").inner_text() == "100%"
                page.locator("#map-expand").click()
                assert page.get_by_role("dialog").count() == 1
                page.keyboard.press("Escape")
                assert page.get_by_role("dialog").count() == 0
                target = anchors.first.get_attribute("href")
                anchors.first.focus()
                page.keyboard.press("Enter")
                page.wait_for_url(base + target)
                assert page.locator("h1").inner_text().strip()
                page.go_back()
                page.get_by_role("link", name="Record UAT decision", exact=True).click()
                assert page.locator("h1").inner_text() == "Record UAT decision"
                assert page.locator(".crumb .phase-name").inner_text() == "Build & Prove"
                assert page.locator(".crumb .activity-tag").inner_text() == "UAT"
                return_link = page.get_by_role("link", name="Return to the map", exact=True)
                card_target = return_link.get_attribute("href").split("#")[1]
                return_link.click()
                assert page.locator(f"#{card_target}").get_attribute("aria-label") == "Record UAT decision"
                page.go_back()
                assert "Edition " in page.locator("footer small").inner_text()
                page.emulate_media(color_scheme="light")
                badge = page.locator(".activity-tag")
                light_ink = badge.evaluate("el => getComputedStyle(el).color")
                page.locator("#theme-toggle").click()
                assert page.locator("html").get_attribute("data-theme") == "dark"
                assert badge.evaluate("el => getComputedStyle(el).color") != light_ink
                page.goto(base + "topics.html")
                search = page.locator("#topic-search")
                assert page.get_by_label("Section", exact=True).count() == 1
                check_search(page, base, {item["id"]: item for item in lessons}, integration)
                page.goto(base + "topics.html")
                search.fill("unfindable-test-phrase")
                assert page.locator(".topic-row:visible").count() == 0
                search.fill(lessons[0]["title"])
                page.locator(".topic-row:visible").first.wait_for()
                page.reload()
                assert page.locator("#topic-search").input_value() == lessons[0]["title"]
                page.locator("#clear-search").click()
                phase = "Prove"
                page.locator("#phase-select").select_option(phase)
                assert page.locator(".topic-row:visible").count() == sum(
                    t["phase"] == phase and t.get("kind", "overview") == "overview" for t in lessons)
                page.goto(base + "tour.html")
                assert page.locator("#tour-stops a").count() > 1
                define_links = page.locator("#intent .tour-deeper a")
                expected = [f"topics/{item['id']}.html" for item in lessons
                            if item.get("kind") == "deep-dive" and item["phase"] == "Define"]
                assert define_links.evaluate_all("(links) => links.map(a => a.getAttribute('href'))") == expected
                for section_phase, stop in (("Prove", "qualification"), ("Release", "release")):
                    order = [item["id"] for item in lessons
                             if item.get("kind") == "deep-dive" and item["phase"] == section_phase]
                    page.goto(base + f"tour.html#{stop}")
                    links = page.locator(f"#{stop} .tour-deeper a")
                    assert links.evaluate_all("(links) => links.map(a => a.getAttribute('href'))") == [
                        f"topics/{key}.html" for key in order
                    ]
                    links.first.focus()
                    page.keyboard.press("Enter")
                    page.wait_for_url(base + f"topics/{order[0]}.html")
                    for previous, current in zip(order, order[1:]):
                        pager = page.get_by_role("navigation", name="Reading order")
                        pager.get_by_role("link", name="Next topic").click()
                        page.wait_for_url(base + f"topics/{current}.html")
                        assert pager.get_by_role("link", name="Previous topic").get_attribute("href") == f"{previous}.html"
                page.set_viewport_size({"width": 375, "height": 812})
                for route in ("index.html", "topics.html", "tour.html", target, "topics/uat-decision.html"):
                    page.goto(base + route)
                    assert page.evaluate("document.documentElement.scrollWidth <= innerWidth + 1"), f"Viewport overflow: {route}"
                page.set_viewport_size({"width": 390, "height": 844})
                check_detail_routes(page, base, lessons)
                check_build_reading_order(page, base)
                check_flow_routes(page, base, lessons)
                plain = browser.new_context(java_script_enabled=False)
                text_page = plain.new_page()
                text_page.goto(base)
                text_page.locator("#text-view").click()
                assert text_page.locator(".topic-row:visible").count() == len(lessons)
                text_page.locator(".topic-row a").first.click()
                assert text_page.locator("#article #sources a").count() > 0
                plain.close()
                check_figure_labels(page, base)
                assert not errors, "; ".join(errors)
                browser.close()
        finally:
            server.shutdown()
    print("Desktop and mobile route, map, keyboard, zoom and search checks passed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--integration", action="store_true", help="also require the full edition search probes")
    main(parser.parse_args().integration)

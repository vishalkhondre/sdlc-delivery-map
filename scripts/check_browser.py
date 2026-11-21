"""Exercise the built learning site at a GitHub Pages-style project subpath."""
import functools
import http.server
import json
import os
import threading
from pathlib import Path
from playwright.sync_api import sync_playwright

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


def main():
    lessons = [item for file in sorted((ROOT / "content").glob("0*.json"))
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
                page.goto(base + "topics.html")
                search = page.locator("#topic-search")
                search.fill("unfindable-test-phrase")
                assert page.locator(".topic-row:visible").count() == 0
                search.fill(lessons[0]["title"])
                page.locator(".topic-row:visible").first.wait_for()
                page.reload()
                assert page.locator("#topic-search").input_value() == lessons[0]["title"]
                page.locator("#clear-search").click()
                phase = "Prove"
                page.locator("#phase-select").select_option(phase)
                assert page.locator(".topic-row:visible").count() == sum(t["phase"] == phase for t in lessons)
                page.goto(base + "tour.html")
                assert page.locator("#tour-stops a").count() > 1
                page.set_viewport_size({"width": 375, "height": 812})
                for route in ("index.html", "topics.html", "tour.html", target):
                    page.goto(base + route)
                    assert page.evaluate("document.documentElement.scrollWidth <= innerWidth + 1"), f"Viewport overflow: {route}"
                plain = browser.new_context(java_script_enabled=False)
                text_page = plain.new_page()
                text_page.goto(base)
                text_page.locator("#text-view").click()
                assert text_page.locator(".topic-row:visible").count() == len(lessons)
                text_page.locator(".topic-row a").first.click()
                assert text_page.locator("#article #sources a").count() > 0
                plain.close()
                assert not errors, "; ".join(errors)
                browser.close()
        finally:
            server.shutdown()
    print("Desktop and mobile route, map, keyboard, zoom and search checks passed")


if __name__ == "__main__":
    main()

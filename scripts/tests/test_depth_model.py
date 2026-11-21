"""Exercise the model's failure paths with small source and HTML fixtures."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
import validate


class DepthModelTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        parent = {key: "Example" for key in validate.TEXT_FIELDS}
        parent.update(id="ci", phase="Build", steps=["Open the checks."], inputs=["Pull request."],
                      sources=[{"url": "https://example.org/a", "title": "Specification"}])
        text = {"type": "text", "value": "The configuration check failed."}
        self.child = dict(parent, id="ci-config", kind="deep-dive", parent="ci",
                          sources=parent["sources"] + [{"url": "https://example.org/b", "title": "Policy"}],
                          detail=[{"id": key, "title": key.title(), "blocks": [text]}
                                  for key in ("trigger", "config", "result", "worked-failure")])
        self.table = {"type": "table", "caption": "Result", "columns": ["Check", "Status"],
                      "rows": [["config", "failed"]]}
        self.child["detail"][2]["blocks"].append(self.table)
        self.flow = dict(parent, id="flow-results", kind="flow", touches=["ci", "ci-config"])
        self.topics = {item["id"]: item for item in (parent, self.child, self.flow)}

    def check(self, item):
        validate.validate_lesson(self.root, item, self.topics)

    def test_depth_and_flow(self):
        for item in self.topics.values():
            self.check(item)
        for patch in ({"parent": "other"}, {"parent": "flow-results"},
                      {"sources": self.child["sources"][:1]}, {"detail": self.child["detail"][:3]}):
            with self.subTest(patch=patch), self.assertRaises(ValueError):
                self.check(dict(self.child, **patch))
        self.child["detail"][-1]["id"] = "more"
        with self.assertRaisesRegex(ValueError, "worked-failure"):
            self.check(self.child)
        for patch in ({"touches": []}, {"touches": ["missing"]}, {"parent": "ci"}):
            with self.subTest(patch=patch), self.assertRaises(ValueError):
                self.check(dict(self.flow, **patch))

    def test_samples_need_consistent_columns_and_reproducible_configuration(self):
        self.table["rows"] = [["failed"]]
        with self.assertRaisesRegex(ValueError, "matching"):
            self.check(self.child)
        self.child["detail"][2]["blocks"].pop()
        with self.assertRaisesRegex(ValueError, "code or table"):
            self.check(self.child)
        cases = [{"type": "list", "ordered": "false", "items": ["one"]},
                 {"type": "callout", "label": "Important", "value": "Example"},
                 {"type": "code", "language": "python", "caption": "Setting", "value": "x = 1"},
                 {"type": "raw", "value": "<b>Demo</b>"}]
        for block in cases:
            with self.subTest(block=block), self.assertRaises(ValueError):
                validate.check_block(self.root, block, "ci-config")

    def test_figure_must_resolve_inside_figure_directory_and_include_source(self):
        folder = self.root / "site/assets/figures"
        folder.mkdir(parents=True)
        diagram = folder / "jobs.svg"
        diagram.write_text("<svg/>")
        figure = {"type": "figure", "src": "assets/figures/jobs.svg", "caption": "Build jobs",
                  "alt": "Two parallel checks", "text_equivalent": "Both checks must finish."}
        with self.assertRaisesRegex(ValueError, "source"):
            validate.check_block(self.root, figure, "ci-config")
        diagram.with_suffix(".mmd").write_text("flowchart TD\nstart --> tests")
        validate.check_block(self.root, figure, "ci-config")
        validate.check_block(self.root, dict(figure, text_equivalent=["First lint.", "Then merge."]), "ci-config")
        for change in ({"alt": ""}, {"text_equivalent": ""}, {"src": "../jobs.svg"},
                       {"src": "assets/figures/%2e%2e/jobs.svg"}, {"src": "https://example.org/jobs.svg"}):
            with self.subTest(change=change), self.assertRaises(ValueError):
                validate.check_block(self.root, dict(figure, **change), "ci-config")

    def test_explicit_kiwi_behavior_requires_reader_visible_evidence_basis(self):
        block = {"type": "callout", "label": "Tool behavior", "value": "Kiwi records the execution."}
        self.child["detail"][0]["blocks"].append(block)
        with self.assertRaisesRegex(ValueError, "Kiwi version"):
            self.check(self.child)
        block["value"] += (" Kiwi TCMS 17.2 behavior is drawn from its documentation and published source code. "
                           "This example has not been demonstrated on a live Kiwi TCMS and Jira setup.")
        self.check(self.child)

    def test_numbered_discovery_includes_tens_and_excludes_non_lessons(self):
        folder = self.root / "content"
        folder.mkdir()
        for name, data in (("01-build.json", ["a"]), ("10-flows.json", ["b"]),
                           ("dataset.json", {}), ("hotspots.json", [{"id": "region"}])):
            (folder / name).write_text(json.dumps(data))
        self.assertEqual(validate.lessons(self.root), ["a", "b"])

    def test_deeper_card_and_search_are_checked_in_their_own_elements(self):
        overview = validate.HTMLLinks()
        overview.feed('<a href="ci-config.html">Sidebar</a>')
        index = validate.HTMLLinks()
        probes = validate.search_probes(False)
        for target in set(probes.values()):
            words = " ".join(k for k, v in probes.items() if v == target)
            index.feed(f'<article class="topic-row" data-text="{words}">'
                       f'<a href="topics/{target}.html">Lesson</a></article>')
        pages = {self.root / "topics/ci.html": overview, self.root / "topics.html": index}
        with self.assertRaisesRegex(ValueError, "Go deeper"):
            validate.check_discovery(self.root, pages, self.topics.values(), False)
        overview.feed('<section id="go-deeper"><h2>Go deeper</h2>'
                      '<a href="ci-config.html">Configuration check</a></section>')
        validate.check_discovery(self.root, pages, self.topics.values(), False)
        # A sidebar can link to related pages, but only actual children belong in Go deeper.
        original_children = overview.deeper_links.copy()
        for extra in ("ci-config.html", "flow-results.html"):
            with self.subTest(extra=extra), self.assertRaisesRegex(ValueError, "Go deeper"):
                overview.deeper_links = original_children + [extra]
                validate.check_discovery(self.root, pages, self.topics.values(), False)
        overview.deeper_links = original_children
        index.feed('<article class="topic-row" data-text="SonarQube">'
                   '<a href="topics/ci-static-analysis.html">Static analysis</a></article>')
        with self.assertRaisesRegex(ValueError, "quality gate"):
            validate.check_discovery(self.root, pages, self.topics.values(), False)

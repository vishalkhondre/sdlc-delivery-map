import json
from pathlib import Path
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
import check_release
import release_snapshot
import validate


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "content/reviews").mkdir(parents=True)
        (self.root / "release").mkdir()
        (self.root / "site").mkdir()
        (self.root / "content/VERSION").write_text("1.0.0\n")
        (self.root / "content/CHANGELOG.md").write_text("# Changes\n\n## 1.0.0\n\nLearner edition.\n")
        self.report = self.root / "content/reviews/1.0.0.md"
        self.report.write_text("\n".join(f"{r}: ACCEPT" for r in check_release.VERDICTS))
        (self.root / "release/sections.yml").write_text('"1.0": {section: Learning map, pages: [index.html]}')

    def test_source_and_review_changes_invalidate_acceptance(self):
        initial = check_release.expected(self.root)
        (self.root / "site/generate.py").write_text("print('new template')")
        changed = check_release.expected(self.root)
        self.assertNotEqual(initial, changed)
        self.report.write_text(self.report.read_text() + "\nReviewed a second time.")
        self.assertNotEqual(changed, check_release.expected(self.root))

    def test_binding_does_not_invalidate_itself(self):
        initial = check_release.expected(self.root)
        (self.root / check_release.BINDING).write_text(json.dumps(initial))
        self.assertEqual(initial, check_release.expected(self.root))

    def test_each_review_required(self):
        self.report.write_text("Accuracy: ACCEPT\nEditorial: ACCEPT")
        with self.assertRaisesRegex(ValueError, "Confidentiality"):
            check_release.expected(self.root)

    def test_notes_follow_version_and_section(self):
        self.assertIn("Learner edition", release_snapshot.notes("v1.0.0", self.root))
        with self.assertRaisesRegex(ValueError, "does not match"):
            release_snapshot.notes("v2.0.0", self.root)


class LinkTests(unittest.TestCase):
    def test_project_path_and_fragment(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "content").mkdir()
            (root / "dist").mkdir()
            for filename in ("tour.html", "topics.html", "references.html"):
                (root / "dist" / filename).write_text('<h1 id="start">Section</h1>')
            home = root / "dist/index.html"
            home.write_text('<a href="tour.html#start">Tour</a>')
            validate.links(root)
            for broken in ("tour.html#gone", "/tour.html", "missing.html"):
                home.write_text(f'<a href="{broken}">Tour</a>')
                with self.assertRaises(ValueError):
                    validate.links(root)


if __name__ == "__main__":
    unittest.main()

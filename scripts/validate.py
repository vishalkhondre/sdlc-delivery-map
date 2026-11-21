"""Check the public lesson inventory and every locally generated HTML destination."""
import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
TEXT_FIELDS = ("id", "title", "phase", "summary", "owner", "evidence", "example", "failure", "measure")
PHASES = {"Define", "Build", "Prove", "Release", "Learn", "Reference"}
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD|FIXME|lorem ipsum)\b", re.I)


def lessons(root):
    return [lesson for file in sorted((root / "content").glob("0*.json"))
            for lesson in json.loads(file.read_text())]


def source(root):
    items = lessons(root)
    if not items:
        raise ValueError("No lessons found in content/0*.json")
    ids = set()
    for item in items:
        key = item.get("id")
        if not isinstance(key, str) or not re.fullmatch(r"[a-z][a-z0-9-]*", key) or key in ids:
            raise ValueError(f"Missing, repeated or invalid lesson ID: {key!r}")
        ids.add(key)
        for field in TEXT_FIELDS:
            if not isinstance(item.get(field), str) or not item[field].strip():
                raise ValueError(f"{key}: missing {field}")
        if item["phase"] not in PHASES:
            raise ValueError(f"{key}: unknown phase")
        for field in ("steps", "inputs"):
            values = item.get(field, [])
            if not isinstance(values, list) or not values or not all(isinstance(v, str) and v.strip() for v in values):
                raise ValueError(f"{key}: {field} must hold one or more useful strings")
        if not item.get("sources"):
            raise ValueError(f"{key}: cite primary public sources")
        for ref in item["sources"]:
            uri = urlsplit(ref.get("url", ""))
            if not ref.get("title") or uri.scheme != "https" or not uri.hostname:
                raise ValueError(f"{key}: invalid source {ref}")
        if PLACEHOLDER.search(json.dumps(item)):
            raise ValueError(f"{key}: unresolved placeholder in published material")
    regions = json.loads((root / "content/hotspots.json").read_text())
    if not regions:
        raise ValueError("Map has no clickable regions")
    for region in regions:
        if region["id"] not in ids or not region["label"].strip():
            raise ValueError(f"Unresolved map destination: {region}")
        x, y, w, h = [region[k] for k in ("x", "y", "w", "h")]
        if min(x, y) < 0 or min(w, h) <= 0 or x + w > 2048 or y + h > 1735:
            raise ValueError(f"Hotspot outside map: {region}")
    print(f"Validated {len(items)} lessons and {len(regions)} map regions")


class HTMLLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            if attrs["id"] in self.ids:
                raise ValueError(f"Duplicate HTML id {attrs['id']}")
            self.ids.add(attrs["id"])
        for name in ("href", "xlink:href", "src", "poster"):
            if attrs.get(name):
                self.links.append(attrs[name])


def links(root):
    dist = (root / "dist").resolve()
    pages = {}
    for path in sorted(dist.rglob("*.html")):
        parser = HTMLLinks()
        try:
            parser.feed(path.read_text())
        except ValueError as exc:
            raise ValueError(f"{path.relative_to(dist)}: {exc}") from exc
        pages[path] = parser
    required = [dist / name for name in ("index.html", "tour.html", "topics.html", "references.html")]
    required.extend(dist / "topics" / (i["id"] + ".html") for i in lessons(root))
    for page in required:
        if page not in pages:
            raise ValueError(f"Missing route {page.relative_to(dist)}")
    checked = 0
    for page, parsed in pages.items():
        for link in parsed.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            if url.path.startswith("/"):
                raise ValueError(f"{page.name}: root-relative link breaks repository Pages hosting: {link}")
            target = (page.parent / unquote(url.path)).resolve() if url.path else page
            if target.is_dir():
                target = target / "index.html"
            if not target.is_relative_to(dist) or not target.is_file():
                raise ValueError(f"{page.relative_to(dist)}: unresolved link {link}")
            if url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                raise ValueError(f"{page.relative_to(dist)}: missing anchor in {link}")
            checked += 1
    print(f"Validated {checked} local references across {len(pages)} HTML pages")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("check", choices=("source", "links"))
    args = parser.parse_args()
    try:
        {"source": source, "links": links}[args.check](ROOT)
    except (ValueError, KeyError, OSError) as err:
        parser.exit(1, str(err) + "\n")

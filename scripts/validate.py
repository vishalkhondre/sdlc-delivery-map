"""Check the public lesson inventory and every locally generated HTML destination."""
import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
TEXT_FIELDS = ("id", "title", "phase", "summary", "owner", "evidence", "example", "failure", "measure")
PHASES = {"Define", "Build", "Prove", "Release", "Learn", "Reference"}
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD|FIXME|lorem ipsum)\b", re.I)


def lessons(root):
    return [lesson for file in sorted((root / "content").glob("[0-9][0-9]-*.json"))
            for lesson in json.loads(file.read_text())]


ID = re.compile(r"[a-z][a-z0-9-]*")
LABELS = {"Principle", "Tool behavior", "Team policy", "Common mistake"}
CORRECTION_PROBES = {"rollback": "recover", "median": "measure",
                     "feature flag": "rollout", "security": "qa-tests"}
PILOT_PROBES = {"unit test": "ci-unit-tests", "lint": "ci-lint-format", "coverage": "ci-coverage",
                "SonarQube": "ci-static-analysis", "quality gate": "ci-static-analysis"}
PROVE_PROBES = {"bug": "defect-report", "severity": "defect-lifecycle",
                      "regression": "regression-scope", "test case": "test-case-design"}
FLOW_PROBES = {"Jira status": "flow-jira-status"}
INTEGRATION_PROBES = {"hotfix": "hotfix-flow"}


def search_probes(integration):
    probes = {**CORRECTION_PROBES, **PILOT_PROBES, **PROVE_PROBES, **FLOW_PROBES}
    if integration:
        probes.update(INTEGRATION_PROBES)
    return probes


def useful(value):
    return isinstance(value, str) and bool(value.strip())


def strings(values):
    return isinstance(values, list) and bool(values) and all(useful(value) for value in values)


def require_text(obj, fields, where):
    for field in fields:
        if not useful(obj.get(field)):
            raise ValueError(f"{where}: missing or empty {field}")


def check_kiwi_disclosure(item):
    # The source references and Tool behavior callouts identify product-specific material.
    # Reviewers still verify the substance of the disclosure and any unlabelled claims.
    detail = item.get("detail", [])
    callouts = [block["value"] for section in detail for block in section["blocks"]
                if block["type"] == "callout" and block["label"] == "Tool behavior"]
    cited = any(urlsplit(ref["url"]).hostname in {"kiwitcms.readthedocs.io", "kiwitcms.org"}
                for ref in item["sources"])
    prose = " ".join(json.dumps(item.get(field, ""), ensure_ascii=False)
                     for field in (*TEXT_FIELDS, "inputs", "steps", "detail")).lower()
    if not re.search(r"\bkiwi\b", prose) or not (cited or any("kiwi" in c.lower() for c in callouts)):
        return
    if not (re.search(r"\bkiwi(?: tcms)?\s+(?:version\s+|v)?\d+\.\d+", prose)
            and "documentation" in prose and "source" in prose and "jira" in prose
            and re.search(r"\b(?:not|never|no|without)\b[^.!?]{0,120}\blive\b", prose)):
        raise ValueError(f"{item['id']}: disclose the Kiwi version, documentation/source basis and live Jira verification status")


def check_figure(root, block, where):
    require_text(block, ("src", "caption", "alt"), where)
    equivalent = block.get("text_equivalent")
    if not (useful(equivalent) or strings(equivalent)):
        raise ValueError(f"{where}: text_equivalent must be prose or a nonempty list")
    src = block["src"]
    if not re.fullmatch(r"assets/figures/(?:[\w-]+/)*[\w.-]+\.svg", src, re.ASCII):
        raise ValueError(f"{where}: expected a local SVG under assets/figures, got {src!r}")
    figures = (root / "site/assets/figures").resolve()
    image = root / "site" / src
    if (not figures.is_relative_to(root.resolve()) or not image.resolve().is_relative_to(figures)
            or not image.is_file()):
        raise ValueError(f"{where}: missing or out-of-directory figure {src}")
    if not any(file.is_file() and file.resolve().is_relative_to(figures)
               for file in (image.with_suffix(ext) for ext in (".mmd", ".py", ".js", ".sh", ".r", ".R", ".rb", ".ts", ".mjs"))):
        raise ValueError(f"{where}: {src} needs a same-stem Mermaid or drawing script source")


def check_block(root, block, where):
    if not isinstance(block, dict):
        raise ValueError(f"{where}: expected a block object")
    kind = block.get("type")
    if kind == "text":
        require_text(block, ("value",), where)
    elif kind == "list":
        if not isinstance(block.get("ordered"), bool) or not strings(block.get("items")):
            raise ValueError(f"{where}: list needs a boolean ordered value and nonempty items")
    elif kind == "table":
        require_text(block, ("caption",), where)
        columns, rows = block.get("columns"), block.get("rows")
        if not strings(columns) or not isinstance(rows, list) or not rows or not all(
                strings(row) and len(row) == len(columns) for row in rows):
            raise ValueError(f"{where}: table needs column headings and matching nonempty rows")
    elif kind == "code":
        require_text(block, ("language", "caption", "value"), where)
        if block["language"].lower() not in {"text", "plaintext", "log", "output"} and not re.search(
                r"\billustrative\b", block["caption"], re.I):
            raise ValueError(f"{where}: label stack-dependent code illustrative in its caption")
    elif kind == "callout":
        require_text(block, ("label", "value"), where)
        if block["label"] not in LABELS:
            raise ValueError(f"{where}: unknown callout label {block['label']!r}")
    elif kind == "figure":
        check_figure(root, block, where)
    else:
        raise ValueError(f"{where}: unknown block type {kind!r}")
    return kind


def check_detail(root, item, kind):
    key = item["id"]
    sections = item.get("detail", [])
    if not isinstance(sections, list):
        raise ValueError(f"{key}: detail must be a list of sections")
    if kind == "deep-dive" and len(sections) < 4:
        raise ValueError(f"{key}: deep dive needs at least four detail sections")
    section_ids, block_types = set(), set()
    for section in sections:
        if not isinstance(section, dict):
            raise ValueError(f"{key}: expected a detail section object")
        require_text(section, ("id", "title"), key)
        sid = section["id"]
        where = f"{key}#{sid}"
        if not ID.fullmatch(sid) or sid in section_ids:
            raise ValueError(f"{where}: invalid or duplicate detail section ID")
        section_ids.add(sid)
        blocks = section.get("blocks")
        if not isinstance(blocks, list) or not blocks:
            raise ValueError(f"{where}: section needs content blocks")
        for index, block in enumerate(blocks, 1):
            block_types.add(check_block(root, block, f"{where} block {index}"))
    if kind == "deep-dive":
        if not {"table", "code"}.intersection(block_types):
            raise ValueError(f"{key}: deep dive needs a code or table block")
        if "worked-failure" not in section_ids:
            raise ValueError(f"{key}: deep dive needs a worked-failure detail section")


def validate_lesson(root, item, by_id):
    key = item["id"]
    require_text(item, TEXT_FIELDS, key)
    if item["phase"] not in PHASES:
        raise ValueError(f"{key}: unknown phase")
    for field in ("steps", "inputs"):
        if not strings(item.get(field)):
            raise ValueError(f"{key}: {field} must hold one or more useful strings")
    kind = item.get("kind", "overview")
    if kind not in ("overview", "deep-dive", "flow"):
        raise ValueError(f"{key}: unknown lesson kind {kind!r}")
    if "audience" in item and not strings(item["audience"]):
        raise ValueError(f"{key}: audience must name at least one reader")
    if kind == "deep-dive":
        parent = item.get("parent")
        if not useful(parent) or parent not in by_id or by_id[parent].get("kind", "overview") != "overview":
            raise ValueError(f"{key}: deep dive needs an existing overview parent")
    elif "parent" in item:
        raise ValueError(f"{key}: only a deep dive can have a parent")
    if kind == "flow":
        touches = item.get("touches")
        if not strings(touches) or key in touches or len(set(touches)) != len(touches) or set(touches) - by_id.keys():
            raise ValueError(f"{key}: touches must list distinct, existing lessons other than itself")
    elif "touches" in item:
        raise ValueError(f"{key}: only a flow can declare touches")
    refs = item.get("sources")
    if not isinstance(refs, list) or not refs:
        raise ValueError(f"{key}: cite primary public sources")
    for ref in refs:
        if not isinstance(ref, dict):
            raise ValueError(f"{key}: expected a source object")
        require_text(ref, ("title", "url"), key)
        uri = urlsplit(ref["url"])
        if uri.scheme != "https" or not uri.hostname or re.search(r"[\\\s]", ref["url"]):
            raise ValueError(f"{key}: invalid HTTPS source {ref}")
    if kind == "deep-dive" and len({ref["url"] for ref in refs}) < 2:
        raise ValueError(f"{key}: deep dive requires at least two distinct HTTPS sources")
    check_detail(root, item, kind)
    check_kiwi_disclosure(item)
    if PLACEHOLDER.search(json.dumps(item)):
        raise ValueError(f"{key}: unresolved placeholder in published material")


def source(root):
    items = lessons(root)
    if not items:
        raise ValueError("No lessons found in content/[0-9][0-9]-*.json")
    by_id = {}
    for item in items:
        key = item.get("id") if isinstance(item, dict) else None
        if not useful(key) or not ID.fullmatch(key) or key in by_id:
            raise ValueError(f"Missing, repeated or invalid lesson ID: {key!r}")
        by_id[key] = item
    for item in items:
        validate_lesson(root, item, by_id)
    regions = json.loads((root / "content/hotspots.json").read_text())
    if not regions:
        raise ValueError("Map has no clickable regions")
    for region in regions:
        if region["id"] not in by_id or not region["label"].strip():
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
        self.section_stack = []
        self.deeper_links = []
        self.rows = {}
        self.row_text = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            if attrs["id"] in self.ids:
                raise ValueError(f"Duplicate HTML id {attrs['id']}")
            self.ids.add(attrs["id"])
        for name in ("href", "xlink:href", "src", "poster"):
            if attrs.get(name):
                self.links.append(attrs[name])
        if tag == "section":
            self.section_stack.append(attrs.get("id"))
        if tag == "article" and "topic-row" in attrs.get("class", "").split():
            self.row_text = attrs.get("data-text", "").casefold()
        if tag == "a" and attrs.get("href"):
            if "go-deeper" in self.section_stack:
                self.deeper_links.append(attrs["href"])
            if self.row_text is not None:
                self.rows[attrs["href"]] = self.row_text

    def handle_endtag(self, tag):
        if tag == "section" and self.section_stack:
            self.section_stack.pop()
        if tag == "article":
            self.row_text = None


def check_discovery(dist, pages, items, integration):
    for item in items:
        if item.get("kind") == "deep-dive":
            parent = dist / "topics" / (item["parent"] + ".html")
            children = {urljoin(parent.as_uri(), href) for href in pages[parent].deeper_links}
            child = dist / "topics" / (item["id"] + ".html")
            if child.as_uri() not in children:
                raise ValueError(f"{parent.name}: Go deeper section needs a link to {child.name}")
    index = pages[dist / "topics.html"]
    probes = search_probes(integration)
    for query, target in probes.items():
        text = index.rows.get(f"topics/{target}.html", "")
        if not all(word in text for word in query.lower().split()):
            raise ValueError(f"Topic search {query!r} must find {target}")
    print(f"Validated {len(probes)} search queries against their intended index destinations")


def links(root, integration=False):
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
    items = lessons(root)
    required.extend(dist / "topics" / (i["id"] + ".html") for i in items)
    for page in required:
        if page not in pages:
            raise ValueError(f"Missing route {page.relative_to(dist)}")
    checked = 0
    for page, parsed in pages.items():
        for link in parsed.links:
            url = urlsplit(link)
            if url.scheme in ("https", "http") and url.hostname:
                continue
            if url.scheme or url.netloc or "\\" in unquote(url.path):
                raise ValueError(f"{page.name}: unsafe link {link}")
            if unquote(url.path).startswith("/"):
                raise ValueError(f"{page.name}: root-relative link breaks repository Pages hosting: {link}")
            target = (page.parent / unquote(url.path)).resolve() if url.path else page
            if target.is_dir():
                target = target / "index.html"
            if not target.is_relative_to(dist) or not target.is_file():
                raise ValueError(f"{page.relative_to(dist)}: unresolved link {link}")
            if url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                raise ValueError(f"{page.relative_to(dist)}: missing anchor in {link}")
            checked += 1
    if items:
        check_discovery(dist, pages, items, integration)
    print(f"Validated {checked} local references across {len(pages)} HTML pages")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("check", choices=("source", "links"))
    parser.add_argument("--integration", action="store_true", help="also require the full edition search probes")
    args = parser.parse_args()
    try:
        if args.check == "source":
            source(ROOT)
        else:
            links(ROOT, args.integration)
    except (ValueError, KeyError, OSError) as err:
        parser.exit(1, str(err) + "\n")

"""Produce a portable field-guide PDF from the reviewed inventory without a browser."""
import argparse
import json
import subprocess
from collections import defaultdict
from pathlib import Path
from tempfile import TemporaryDirectory
from xml.sax.saxutils import escape, quoteattr

from pypdf import PdfWriter
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.platypus import (BaseDocTemplate, Frame, Image, KeepTogether, PageBreak,
                                PageTemplate, Paragraph, Preformatted, Spacer, Table, TableStyle)

from release_snapshot import version_for

ROOT = Path(__file__).resolve().parents[1]
BODY = colors.HexColor("#243642")
NAVY = colors.HexColor("#152e43")
TEAL = colors.HexColor("#166962")
MUTED = colors.HexColor("#4f626c")
REPO = "https://github.com/vishalkhondre/sdlc-delivery-map"
UPSTREAM = "https://github.com/vishalkhondre/ai-sdlc-map/tree/60e0864f54b727eb582332ce1a4932ad89378266"
WORKED_FILES = ("qualification-record.json", "one-day-cohort.csv")
WIDTH = A4[0] - 38 * mm
STYLES = {}


def style(key, size, leading, color=BODY, *, bold=False, after=6):
    STYLES[key] = ParagraphStyle(key, fontName="Helvetica-Bold" if bold else "Helvetica",
                                 fontSize=size, leading=leading, textColor=color,
                                 spaceAfter=after, alignment=TA_LEFT, splitLongWords=1)


style("title", 31, 35, NAVY, bold=True, after=12)
style("lesson-title", 25, 29, NAVY, bold=True, after=8)
style("label", 8.5, 12, TEAL, bold=True, after=3)
style("caption", 8.5, 12, TEAL, bold=True, after=3)
STYLES["caption"].keepWithNext = True
style("body", 10.3, 14, after=5)
style("small", 9, 12, MUTED, after=4)
style("lead", 12.2, 16.5, BODY, after=9)
style("detail", 14, 18, NAVY, bold=True, after=6)
STYLES["detail"].keepWithNext = True
STYLES["code"] = ParagraphStyle("code", fontName="Courier", fontSize=8, leading=11, spaceAfter=6)


class Book(BaseDocTemplate):
    def afterFlowable(self, flowable):
        mark = getattr(flowable, "bookmark", None)
        if mark:
            self.canv.bookmarkPage(mark)
            self.canv.addOutlineEntry(flowable.getPlainText(), mark, level=0)


def paragraph(text, key="body"):
    return Paragraph(escape(text), STYLES[key])


def block(label, text):
    return KeepTogether([paragraph(label, "label"), paragraph(text)])


def figure_image(asset, render_dir):
    source = ROOT / "site" / asset
    target = render_dir / Path(asset).with_suffix(".png")
    if not target.exists():
        target.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["inkscape", str(source), "--export-type=png",
                        "--export-width=1500", f"--export-filename={target}"], check=True)
    width, height = ImageReader(str(target)).getSize()
    scale = min(WIDTH / width, 225 * mm / height)
    return Image(str(target), width=width * scale, height=height * scale)


def detail_content(section, render_dir):
    yield paragraph(section["title"], "detail")
    for entry in section["blocks"]:
        kind = entry["type"]
        if kind == "text":
            yield paragraph(entry["value"])
        elif kind == "callout":
            yield block(entry["label"], entry["value"])
        elif kind == "list":
            for i, item in enumerate(entry["items"], 1):
                yield paragraph((f"{i}. " if entry["ordered"] else "• ") + item)
        elif kind == "code":
            yield paragraph(entry["caption"], "caption")
            yield Preformatted(entry["value"], STYLES["code"], maxLineLength=96)
        elif kind == "figure":
            yield KeepTogether([paragraph(entry["caption"], "label"), figure_image(entry["src"], render_dir)])
            equivalent = entry["text_equivalent"]
            if isinstance(equivalent, list):
                for item in equivalent:
                    yield paragraph("• " + item)
            else:
                yield paragraph(equivalent)
        elif kind == "table":
            yield paragraph(entry["caption"], "caption")
            grid = [[paragraph(cell, "label") for cell in entry["columns"]]]
            grid.extend([paragraph(cell, "small") for cell in row] for row in entry["rows"])
            table = Table(grid, colWidths=[WIDTH/len(grid[0])] * len(grid[0]),
                          repeatRows=1, splitInRow=1, spaceAfter=7)
            table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                                       ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e6f2f0")),
                                       ("LINEBELOW", (0, 0), (-1, -1), .35, colors.HexColor("#c6d5d6"))]))
            yield table


def make_pdf(tag, out, *, preview=False):
    if preview and tag is not None:
        raise ValueError("Supply either a release tag or --preview")
    label = "Integration preview" if preview else "Edition " + version_for(tag)
    source_ref = "refs/heads/edition/1.1.0" if preview else f"refs/tags/{tag}"
    with TemporaryDirectory(prefix="sdlc-guide-") as render_dir:
        scratch = Path(render_dir)
        manuscript = scratch / "guide.pdf"
        build_guide(label, manuscript, scratch, source_ref)
        writer = PdfWriter(clone_from=str(manuscript))
        for name in WORKED_FILES:
            writer.add_attachment(name, (ROOT / "site/assets/examples" / name).read_bytes())
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("wb") as target:
            writer.write(target)
    print(f"Wrote the complete field guide to {out}")


def external_link(url, title):
    return f'<a href={quoteattr(url)} color="#166962">{escape(title)}</a>'


def build_guide(label, out, render_dir, source_ref):
    topics = [t for path in sorted((ROOT / "content").glob("[0-9][0-9]-*.json"))
              for t in json.loads(path.read_text())]
    by_id = {topic["id"]: topic for topic in topics}
    children = defaultdict(list)
    for topic in topics:
        if topic.get("parent"):
            children[topic["parent"]].append(topic["id"])
    image_file = ROOT / "site/assets/delivery-map.png"
    doc = Book(str(out), pagesize=A4, leftMargin=19*mm, rightMargin=19*mm,
               topMargin=19*mm, bottomMargin=19*mm,
               title=f"The SDLC Delivery Map — {label}", author="Vishal Khondre")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="body",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)

    def footer(canvas, book):
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor("#c6d5d6"))
        canvas.line(19*mm, 15*mm, A4[0] - 19*mm, 15*mm)
        canvas.setFillColor(MUTED)
        canvas.setFont("Helvetica", 8)
        canvas.drawString(19*mm, 10*mm, f"The SDLC Delivery Map   /   {label}")
        canvas.drawRightString(A4[0]-19*mm, 10*mm, str(book.page))
        canvas.restoreState()

    doc.addPageTemplates([PageTemplate(id="guide", frames=[frame], onPage=footer)])
    story = [paragraph(f"FIELD GUIDE  /  {label.upper()}", "label"),
             paragraph("The SDLC Delivery Map", "title"),
             paragraph("Follow one feature from its business objective to production and the next product decision.", "lead"),
             paragraph("Use the bookmarks or topic index to follow the evidence from role to role. Public references at the end of each lesson open the supporting material."),
             Spacer(1, 4*mm), Image(str(image_file), width=WIDTH, height=WIDTH*1735/2048),
             Spacer(1, 3*mm),
             Paragraph("Original lessons, figures and data by Vishal Khondre · " +
                       external_link("https://creativecommons.org/licenses/by/4.0/", "CC BY 4.0") +
                       ". The site tooling uses the " + external_link(REPO + "/blob/main/LICENSE", "MIT License") +
                       ". Its design and publishing approach adapt Vishal Khondre’s " +
                       external_link(UPSTREAM, "AI SDLC Map") + ".", STYLES["small"]),
             PageBreak(), paragraph("Topic index", "title")]

    def topic_link(key):
        return f'<a href={quoteattr("#" + key)} color="#166962">{escape(by_id[key]["title"])}</a>'

    kinds = {"overview": "Overview", "deep-dive": "Deep dive", "flow": "Flow"}
    for kind, name in kinds.items():
        story.append(paragraph(name, "detail"))
        for topic in topics:
            if topic.get("kind", "overview") == kind:
                story.append(Paragraph(f'{topic_link(topic["id"])}  ·  {escape(topic["phase"])}', STYLES["body"]))
    for topic in topics:
        heading = paragraph(topic["title"], "lesson-title")
        heading.bookmark = topic["id"]
        story.extend([PageBreak(), paragraph(f'{topic["phase"]}  /  {kinds[topic.get("kind", "overview")]}'.upper(), "label"), heading,
                      paragraph(topic["summary"], "lead"), block("RESPONSIBLE ROLE", topic["owner"])])
        if topic.get("audience"):
            story.append(block("AUDIENCE", ", ".join(topic["audience"])))
        for field, section_label in [("inputs", "BEFORE YOU BEGIN"), ("steps", "HOW IT WORKS")]:
            rows = [paragraph(txt if field == "inputs" else f"{i}. {txt}")
                    for i, txt in enumerate(topic[field], 1)]
            story.append(KeepTogether([paragraph(section_label, "label"), rows[0]]))
            story.extend(rows[1:])
        if topic["id"] in {"evidence-record", "outcome-analysis"}:
            download_root = f"https://raw.githubusercontent.com/vishalkhondre/sdlc-delivery-map/{source_ref}/site/assets/examples/"
            links = [external_link(download_root + name, name) for name in WORKED_FILES]
            story.append(KeepTogether([paragraph("DOWNLOAD THE WORKED DATA", "label"),
                                       Paragraph(" · ".join(links), STYLES["small"]),
                                       paragraph("Both files are also included in the PDF attachments.", "small")]))
        for section in topic.get("detail", []):
            story.extend(detail_content(section, render_dir))
        for key, name in [("evidence", "HANDOFF EVIDENCE"), ("example", "WORKED EXAMPLE"),
                          ("failure", "WHEN IT FAILS"), ("measure", "WHAT TO MEASURE")]:
            story.append(block(name, topic[key]))
        for section_label, keys in (("GO DEEPER", children.get(topic["id"], [])),
                                    ("OVERVIEW", [topic["parent"]] if topic.get("parent") else []),
                                    ("STEPS IN THIS FLOW", topic.get("touches", []))):
            if keys:
                rows = [Paragraph(topic_link(key), STYLES["small"]) for key in keys]
                story.append(KeepTogether([paragraph(section_label, "label"), rows[0]]))
                story.extend(rows[1:])
        refs = [Paragraph(external_link(r["url"], r["title"]), STYLES["small"]) for r in topic["sources"]]
        story.append(KeepTogether([paragraph("PUBLIC SOURCES", "label"), *refs]))
    doc.build(story)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preview", action="store_true", help="Build an untagged integration preview")
    parser.add_argument("tag", nargs="?")
    parser.add_argument("out", type=Path)
    args = parser.parse_args()
    if args.preview == bool(args.tag):
        parser.error("provide a release tag or --preview")
    make_pdf(args.tag, args.out, preview=args.preview)

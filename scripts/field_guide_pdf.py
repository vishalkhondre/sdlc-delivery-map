"""Produce a portable field-guide PDF from the reviewed inventory without a browser."""
import argparse
import json
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, Frame, Image, KeepTogether, PageBreak,
                                PageTemplate, Paragraph, Preformatted, Spacer, Table, TableStyle)

from release_snapshot import version_for

ROOT = Path(__file__).resolve().parents[1]
BODY = colors.HexColor("#243642")
NAVY = colors.HexColor("#152e43")
TEAL = colors.HexColor("#166962")
MUTED = colors.HexColor("#4f626c")
WIDTH = A4[0] - 38 * mm
STYLES = {}


def style(key, size, leading, color=BODY, *, bold=False, after=6):
    STYLES[key] = ParagraphStyle(key, fontName="Helvetica-Bold" if bold else "Helvetica",
                                 fontSize=size, leading=leading, textColor=color,
                                 spaceAfter=after, alignment=TA_LEFT, splitLongWords=1)


style("title", 31, 35, NAVY, bold=True, after=12)
style("lesson-title", 25, 29, NAVY, bold=True, after=8)
style("label", 8.5, 12, TEAL, bold=True, after=3)
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


def detail_content(section):
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
            yield paragraph(entry["caption"], "label")
            yield Preformatted(entry["value"], STYLES["code"], maxLineLength=96)
        elif kind == "figure":
            yield block(entry["caption"], entry["text_equivalent"])
        elif kind == "table":
            yield paragraph(entry["caption"], "label")
            grid = [[paragraph(cell, "label") for cell in entry["columns"]]]
            grid.extend([paragraph(cell, "small") for cell in row] for row in entry["rows"])
            table = Table(grid, colWidths=[WIDTH/len(grid[0])] * len(grid[0]),
                          repeatRows=1, splitInRow=1, spaceAfter=7)
            table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                                       ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e6f2f0")),
                                       ("LINEBELOW", (0, 0), (-1, -1), .35, colors.HexColor("#c6d5d6"))]))
            yield table


def make_pdf(tag, out):
    version = version_for(tag)
    topics = [t for path in sorted((ROOT / "content").glob("[0-9][0-9]-*.json"))
              for t in json.loads(path.read_text())]
    image_file = ROOT / "site/assets/delivery-map.png"
    doc = Book(str(out), pagesize=A4, leftMargin=19*mm, rightMargin=19*mm,
               topMargin=19*mm, bottomMargin=19*mm,
               title=f"The SDLC Delivery Map {version}", author="The SDLC Delivery Map")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="body",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)

    def footer(canvas, book):
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor("#c6d5d6"))
        canvas.line(19*mm, 15*mm, A4[0] - 19*mm, 15*mm)
        canvas.setFillColor(MUTED)
        canvas.setFont("Helvetica", 8)
        canvas.drawString(19*mm, 10*mm, f"The SDLC Delivery Map   /   {version}")
        canvas.drawRightString(A4[0]-19*mm, 10*mm, str(book.page))
        canvas.restoreState()

    doc.addPageTemplates([PageTemplate(id="guide", frames=[frame], onPage=footer)])
    story = [paragraph(f"FIELD GUIDE  /  EDITION {version}", "label"),
             paragraph("The SDLC Delivery Map", "title"),
             paragraph("Follow one feature from its business objective to production and the next product decision.", "lead"),
             paragraph("Use the bookmarks or topic index to follow the evidence from role to role. Public references at the end of each lesson open the supporting material."),
             Spacer(1, 4*mm), Image(str(image_file), width=WIDTH, height=WIDTH*1735/2048),
             PageBreak(), paragraph("Topic index", "title")]
    for topic in topics:
        href = quoteattr("#" + topic["id"])
        story.append(Paragraph(f'<a href={href} color="#166962">{escape(topic["title"])}</a>'
                               f'  ·  {escape(topic["phase"])}', STYLES["body"]))
    for topic in topics:
        heading = paragraph(topic["title"], "lesson-title")
        heading.bookmark = topic["id"]
        story.extend([PageBreak(), paragraph(topic["phase"].upper(), "label"), heading,
                      paragraph(topic["summary"], "lead"), block("RESPONSIBLE ROLE", topic["owner"])])
        for field, label in [("inputs", "BEFORE YOU BEGIN"), ("steps", "HOW IT WORKS")]:
            rows = [paragraph(txt if field == "inputs" else f"{i}. {txt}")
                    for i, txt in enumerate(topic[field], 1)]
            story.append(KeepTogether([paragraph(label, "label"), rows[0]]))
            story.extend(rows[1:])
        for section in topic.get("detail", []):
            story.extend(detail_content(section))
        for key, name in [("evidence", "HANDOFF EVIDENCE"), ("example", "WORKED EXAMPLE"),
                          ("failure", "WHEN IT FAILS"), ("measure", "WHAT TO MEASURE")]:
            story.append(block(name, topic[key]))
        refs = [Paragraph(f'<a href={quoteattr(r["url"])} color="#166962">{escape(r["title"])}</a>',
                          STYLES["small"]) for r in topic["sources"]]
        story.append(KeepTogether([paragraph("PUBLIC SOURCES", "label"), *refs]))
    out.parent.mkdir(parents=True, exist_ok=True)
    doc.build(story)
    print(f"Wrote {len(topics)} complete lessons to {out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tag")
    parser.add_argument("out", type=Path)
    args = parser.parse_args()
    make_pdf(args.tag, args.out)

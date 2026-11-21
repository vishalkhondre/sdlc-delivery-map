"""Draw the source-to-QA evidence trail for the fictional accepted build."""
from html import escape
from pathlib import Path

parts = ['''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 664 526" role="img" aria-labelledby="title desc">
<title id="title">From the reviewed change to the QA result</title>
<desc id="desc">Follow the integrated commit to build-418, the published digest and platform, the QA configuration, and the observed routing and authorization results. The scan, component list and build provenance describe the image.</desc>
<defs><marker id="tip" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5 0 7z" fill="#15636c"/></marker></defs>
<rect width="664" height="526" rx="12" fill="#f4f7f9"/>''']


def text(x, y, words, size=16, bold=False, color="#173251"):
    weight = "bold" if bold else "normal"
    parts.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" '
                 f'font-weight="{weight}" font-size="{size}" fill="{color}">{escape(words)}</text>')


def card(y, title, record, decision=False):
    color = "#deefec" if decision else "white"
    parts.append('<g data-label-box="">')
    parts.append(f'<rect x="22" y="{y}" width="319" height="66" rx="7" fill="{color}" stroke="#9aafbd"/>')
    text(36, y + 26, title, 19, True)
    text(36, y + 51, record)
    parts.append("</g>")


def arrow(path):
    parts.append(f'<path d="{path}" fill="none" stroke="#15636c" stroke-width="2" marker-end="url(#tip)"/>')


text(22, 35, "From the reviewed change to the QA result", 23, True)
rows = [
    ("Integrate the change", "PR-42 · commit 3ab862b…"),
    ("Build and publish", "build-418 · one recorded candidate"),
    ("Identify the artifact", "sha256:041f649d… · linux/amd64"),
    ("Check what runs in QA", "qa-r17 · configuration qa-routing-3"),
    ("Record observed behavior", "qa-204 · AC-01 and AC-02"),
]
for i, (title, record) in enumerate(rows):
    y = 59 + 92 * i
    card(y, title, record, decision=i == len(rows) - 1)
    if i:
        arrow(f"M173 {y - 24} V{y - 5}")
arrow("M342 183 H377")
parts.append('<g data-label-box=""><rect x="383" y="132" width="260" height="223" rx="7" fill="#eef1f6" stroke="#b2c1d0"/>')
text(397, 161, "Evidence about the image", 17, True)
for i, (label, answer) in enumerate([
        ("Scan", "Which known risks were found?"),
        ("Component list (SBOM)", "What was packaged?"),
        ("Build provenance", "How and from what was it built?")]):
    y = 198 + 60 * i
    text(397, y, label, 16, True)
    text(397, y + 22, answer, 15)
parts.append("</g>")
text(22, 513, "The test result links the running image and its configuration to what QA observed.", 15)
parts.append("</svg>")
Path(__file__).with_suffix(".svg").write_text("\n".join(parts) + "\n")

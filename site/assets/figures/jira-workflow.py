"""Regenerate the illustrative Jira status diagram using Python's standard library."""
from html import escape
from pathlib import Path

parts = ['''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 545" role="img" aria-labelledby="title desc">
<title id="title">Feature and defect status in Jira</title>
<desc id="desc">Two independent workflows. The feature waits for business acceptance and the bug closes after retesting. Reopening the bug clears the resolution.</desc>
<defs><marker id="arrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0 L7 3.5 L0 7z" fill="#17666e"/></marker></defs>
<rect width="680" height="545" rx="12" fill="#f5f7fa"/><path d="M311 24v465" stroke="#b7c8d7"/>''']


def label(x, y, text, size=16, bold=False):
    weight = "bold" if bold else "normal"
    parts.append(f'<text x="{x}" y="{y}" fill="#183456" font-family="Arial, sans-serif" '
                 f'font-size="{size}" font-weight="{weight}">{escape(text)}</text>')


def status(x, y, text, width=158):
    parts.append('<g data-label-box="">')
    parts.append(f'<rect x="{x}" y="{y}" width="{width}" height="36" rx="6" '
                 'fill="white" stroke="#98adbe"/>')
    label(x + 10, y + 24, text, 16, True)
    parts.append("</g>")


def arrow(path):
    parts.append(f'<path d="{path}" fill="none" stroke="#17666e" stroke-width="2" marker-end="url(#arrow)"/>')


label(22, 35, "Feature · CC-123", 21, True)
label(329, 35, "Bug · CC-131", 21, True)
label(22, 60, "Tracks delivery of automatic routing")
label(329, 60, "Tracks the authorization defect")
feature = ["In development", "In review", "Ready for QA", "In QA", "In UAT", "Ready for release", "Released"]
for index, name in enumerate(feature):
    y = 84 + 61 * index
    status(22, y, name)
    if index:
        arrow(f"M98 {y - 25} V{y - 4}")
arrow("M180 350 H202 V318 H163 V325")
label(207, 342, "Hold until", 14)
label(207, 361, "accepted", 14)

for index, name in enumerate(["New", "Triaged", "In progress", "Ready for retest", "Closed"]):
    y = 84 + 78 * index
    status(329, y, name)
    if index:
        arrow(f"M392 {y - 42} V{y - 4}")
status(531, 162, "Deferred", 128)
arrow("M487 172 H527")
arrow("M531 188 H491")
status(531, 318, "Reopened", 128)
arrow("M487 336 H527")
arrow("M590 318 V258 H491")
arrow("M487 414 H590 V358")
label(401, 377, "Retest passed", 14)
label(508, 442, "Clear resolution", 14)
label(508, 459, "when reopening", 14)
label(333, 458, "Resolution: Fixed", 14)
label(22, 528, "A separate issue link records that the bug blocks the feature.", 16)
parts.append("</svg>")
Path(__file__).with_suffix(".svg").write_text("\n".join(parts) + "\n")

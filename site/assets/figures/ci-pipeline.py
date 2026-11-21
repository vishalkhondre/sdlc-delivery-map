"""Render the dependency graph for the imaginary PR-42 workflow."""
from html import escape
from pathlib import Path

parts = ['''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 514" role="img" aria-labelledby="title desc">
<title id="title">Checks on PR-42</title>
<desc id="desc">Five jobs start independently. Unit tests supply coverage data to a sixth job.
Five required results feed the merge rule. The type check is informational.</desc>
<defs><marker id="arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0 6 3 0 6z" fill="#28747c"/></marker></defs>
<rect width="640" height="514" rx="12" fill="#f3f6f8"/>''']


def label(x, y, value, size=17, color="#152f50", bold=False, center=False):
    weight = "bold" if bold else "normal"
    anchor = "middle" if center else "start"
    parts.append(f'<text x="{x}" y="{y}" fill="{color}" font-family="Arial,sans-serif" '
                 f'font-weight="{weight}" font-size="{size}" text-anchor="{anchor}">{escape(value)}</text>')


def box(x, y, width, height, title, note, background="#ffffff", border="#b2c2cf"):
    parts.append('<g data-label-box="">')
    parts.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="8" '
                 f'fill="{background}" stroke="{border}"/>')
    label(x + 13, y + 24, title, bold=True)
    label(x + 13, y + 45, note, size=15)
    parts.append("</g>")


def path(d, arrow=True):
    end = ' marker-end="url(#arrow)"' if arrow else ""
    parts.append(f'<path d="{d}" fill="none" stroke="#28747c" stroke-width="2"{end}/>')


label(20, 32, "PR-42 opens or changes", size=23, bold=True)
label(20, 58, "Each row starts independently on a runner.", size=17)
label(20, 91, "CHECK", size=13, bold=True)
label(273, 91, "FOLLOW-ON CHECK", size=13, bold=True)
label(492, 91, "BRANCH RULE", size=13, bold=True)
box(20, 105, 164, 58, "Unit tests", "Test merge tree")
box(273, 105, 176, 58, "New-line coverage", "Changed lines")
path("M184 125 H269")
label(228, 151, "coverage.json", size=13, center=True)
box(20, 178, 220, 58, "Lint", "Test merge tree")
box(20, 251, 220, 58, "Quality gate", "PR head and target")
box(20, 324, 220, 58, "Dependency review", "PR dependency changes")
box(20, 421, 220, 58, "Type check", "Test merge tree")
# The unit result and its dependent coverage job are required separately.
path("M184 109 V98 H463 V222", arrow=False)
for d in ("M449 138 H463", "M240 207 H463", "M240 280 H463", "M240 353 H463 V222"):
    path(d, arrow=False)
path("M463 222 H484")
box(489, 191, 140, 61, "Merge rule", "5 required", "#d9efec", "#5a918d")
path("M240 451 H484")
box(489, 421, 140, 58, "Advisory", "Informational", "#e7ebf1")
label(20, 500, "A failed required result holds the merge. Read the job before changing the code.", size=15)
parts.append("</svg>")
Path(__file__).with_suffix(".svg").write_text("\n".join(parts) + "\n")

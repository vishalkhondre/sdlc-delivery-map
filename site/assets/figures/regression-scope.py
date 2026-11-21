"""Draw the two example requalification paths. Run with Python 3."""
from html import escape
from pathlib import Path

parts = ['''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 650 636" role="img" aria-labelledby="title desc">
<title id="title">Choose the evidence to collect after a failure</title>
<desc id="desc">A code repair creates a new candidate. A mapping repair retains the image and changes configuration. Both paths require fresh observations before promotion.</desc>
<defs><marker id="tip" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10z" fill="#296474"/></marker></defs>
<rect width="650" height="636" rx="12" fill="#f3f6f8"/>''']


def label(x, y, words, size=17, bold=False):
    weight = 700 if bold else 400
    parts.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" font-weight="{weight}" fill="#183452">{escape(words)}</text>')


def box(x, y, width, height, title, lines, color="white"):
    parts.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="9" stroke="#99aeba" fill="{color}"/>')
    label(x+14, y+30, title, 20, True)
    for index, line in enumerate(lines):
        label(x+14, y+58+24*index, line)


def arrow(path):
    parts.append(f'<path d="{path}" fill="none" stroke="#296474" stroke-width="2.5" marker-end="url(#tip)"/>')


label(22, 39, "What changed after the failure?", 25, True)
box(22, 62, 606, 90, "Hold promotion", ["Record the failed observation, image and configuration.", "Identify the cause before choosing the scope."])
arrow("M324 152V174H168V195")
arrow("M324 174H481V195")
box(22, 198, 293, 111, "Code changed", ["TC-04 failed in qa-196.", "PR-41 creates build-415", "with a new image digest."], "#e7effa")
box(335, 198, 293, 111, "UAT mapping changed", ["uat-80 rejected unit B routing.", "Keep the build-418 digest.", "Correct the mapping."], "#e5f3ef")
arrow("M168 309V342")
arrow("M481 309V342")
box(22, 345, 293, 134, "Confirm and check nearby", ["qa-198 retests TC-04 and", "authorized decisions. Later,", "qualify the integrated", "build-418 in qa-204."])
box(335, 345, 293, 134, "Recheck affected behavior", ["qa-209 checks mapping and", "permissions. Repeat in uat-r9", "with uat-routing-6. The new", "decision is uat-82: accepted."])
arrow("M168 479V503H324V526")
arrow("M481 479V503H324")
box(22, 530, 606, 90, "Business handoff", ["Qualified changes can enter or resume business testing.", "Retain earlier results and record each decision on its own evidence."])
parts.append("</svg>")
Path(__file__).with_suffix(".svg").write_text("\n".join(parts) + "\n")

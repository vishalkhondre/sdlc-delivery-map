"""Draw the example CC-131 state transitions. Run with Python 3."""
from html import escape
from pathlib import Path

parts = ['''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 654" role="img" aria-labelledby="title desc">
<title id="title">Who moves CC-131 after a QA failure?</title>
<desc id="desc">Triage accepts or defers the bug. A repair goes to QA. The triage owner closes after a passing retest, or reopens when evidence shows the defect persists.</desc>
<defs><marker id="tip" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#235e70"/></marker></defs>
<rect width="620" height="654" rx="12" fill="#f3f6f8"/>''']


def text(x, y, words, size=17, weight=400):
    parts.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" font-weight="{weight}" fill="#183452">{escape(words)}</text>')


def state(x, y, name, evidence, tint="#ffffff"):
    parts.append(f'<rect x="{x}" y="{y}" width="244" height="67" rx="8" stroke="#97acba" fill="{tint}"/>')
    text(x + 14, y + 27, name, 20, 700)
    text(x + 14, y + 52, evidence)


def arrow(path):
    parts.append(f'<path d="{path}" fill="none" stroke="#235e70" stroke-width="2.5" marker-end="url(#tip)"/>')


text(24, 39, "CC-131 · Authorization defect", 25, 700)
text(24, 68, "Jira states in the example team's workflow")
state(24, 93, "New", "QA reports TC-04 · qa-196")
state(24, 184, "Triaged", "QA and product assess")
state(329, 184, "Deferred", "Resolution stays unset")
state(24, 284, "In progress", "Developer fixes the cause")
state(24, 382, "Ready for retest", "QA receives build-415")
state(329, 382, "Reopened", "Failure still observable", "#fff2e3")
state(24, 499, "Closed", "Resolution set to Fixed", "#e2f3ef")
for top, bottom in ((160,181),(251,281),(351,379),(449,496)):
    arrow(f"M145 {top}V{bottom}")
arrow("M268 203H326")
arrow("M329 237H271")
arrow("M268 406H326")
arrow("M451 382V317H271")
arrow("M268 534H451V452")
text(339, 558, "Recurrence")
text(159, 479, "qa-198 passes")
text(24, 609, "The triage owner records closure after reviewing the retest.", 17, 700)
text(24, 634, "Keep the original failure and the repair result on their own builds.")
parts.append("</svg>")
Path(__file__).with_suffix(".svg").write_text("\n".join(parts) + "\n")

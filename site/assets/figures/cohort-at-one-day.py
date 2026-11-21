"""Plot the four one-day counts from the field guide's worked cohort."""
import csv
from pathlib import Path

from flow_drawing import Drawing, MUTED

source = Path(__file__).resolve().parents[1] / "examples" / "one-day-cohort.csv"
with source.open(encoding="utf-8", newline="") as stream:
    cohort = list(csv.DictReader(stream))
total = len(cohort)
assignments = [int(r["correct_assignment_minutes"]) for r in cohort if r["correct_assignment_minutes"]]
decisions = sum(bool(r["decision_minutes"]) for r in cohort)
open_requests = sum(r["open_at_one_day"] == "true" for r in cohort)
within_window = sum(t <= 2 for t in assignments)

d = Drawing(468, 389, "Where were the requests at one day?",
            "Four bars use the same submitted cohort. The dashed line marks half the cohort.")
d.text(16, 61, f"All {total} submissions had 24 hours of follow-up.", 18, color=MUTED)
left, width = 170, 244
half = left + width / 2
d.text(half, 92, "50%", 16, True, center=True)
rows = [
    ("Submitted", total, "#1b2a4e"),
    ("Assigned correctly", len(assignments), "#0f7c82"),
    ("Decided", decisions, "#316594"),
    ("Still open", open_requests, "#75608f"),
]
for i, (label, value, color) in enumerate(rows):
    y = 105 + 40 * i
    d.text(16, y + 16, label, 17)
    d.items.append(f'<rect x="{left}" y="{y}" width="{width}" height="20" fill="#dce3e6"/>')
    d.items.append(f'<rect x="{left}" y="{y}" width="{width * value / total:.2f}" '
                   f'height="20" fill="{color}"/>')
    d.text(424, y + 16, str(value), 18, True)
# Two strokes keep the dashed reference visible on dark bars and light tracks.
for color, weight, dash in [("#f5f7f6", 4, ""), ("#273848", 2, ' stroke-dasharray="5 4"')]:
    d.items.append(f'<path d="M{half} 97V251" stroke="{color}" stroke-width="{weight}"{dash}/>')
d.text(16, 276, "Decided and open split the cohort.", 17, color=MUTED)
d.text(16, 298, "Assignment is measured on the same requests.", 17, color=MUTED)
d.card(16, 313, 436, f"{within_window} of {total} assigned correctly within two minutes",
       [f"The {len(assignments)} correct assignments took {min(assignments)}–{max(assignments)} minutes."], kind="decision")
d.save(__file__)

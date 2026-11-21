"""Draw the four arrow styles and show a real handoff for each."""
from flow_drawing import Drawing, MUTED

d = Drawing(462, 425, "Follow an arrow on the map",
            "Four labeled arrow styles, each with its line pattern and an example from the feature.")
entries = [
    ("Next step in the same lane", "Solid navy", "#1b2a4e", False,
     "Feature branch → Open pull request"),
    ("Handoff between lanes", "Solid teal", "#0f7c82", False,
     "Open pull request → Run CI checks"),
    ("Failure or recovery path", "Dashed red", "#a34a3d", True,
     "Failed QA verification → Hold release"),
    ("Linked record or evidence", "Dashed gray", "#758295", True,
     "Record UAT decision → Validation summary"),
]
for i, (title, style, color, dashed, example) in enumerate(entries):
    top = 49 + i * 92
    d.items.append(f'<g data-label-box=""><rect x="16" y="{top}" width="430" '
                   'height="82" rx="7" stroke="#a5b5bc" fill="#fff"/>')
    y = top + 22
    pattern = ' stroke-dasharray="6 4"' if dashed else ""
    d.items.append(f'<path d="M29 {y}h45" stroke="{color}" stroke-width="2.5"{pattern}/>')
    d.items.append(f'<path d="M72 {y - 5}l11 5 -11 5z" fill="{color}"/>')
    d.text(96, y + 5, title, 18, True)
    d.text(29, top + 49, style, 16, color=MUTED)
    d.text(29, top + 70, example, 17)
    d.items.append("</g>")
d.save(__file__)

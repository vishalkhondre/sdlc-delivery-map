"""Shared layout primitives for the five record-flow figures. All units are SVG pixels."""
from html import escape
from pathlib import Path

INK = "#162f40"
MUTED = "#425c69"
EDGE = "#345765"
PALETTE = {
    "record": ("#ffffff", "#92a5ae"),
    "hold": ("#fff0e1", "#aa622a"),
    "actual": ("#e1f0e9", "#4e816c"),
    "decision": ("#e7eef7", "#61809d"),
    "option": ("#f6f5fa", "#80758b"),
}


class Drawing:
    def __init__(self, width, height, title, description):
        self.width = width
        self.height = height
        self.items = [
            '<svg xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
            f'<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>',
            '<defs><marker id="tip" viewBox="0 0 9 10" refX="8" refY="5" markerWidth="9" '
            'markerHeight="10" markerUnits="userSpaceOnUse" orient="auto">'
            f'<path d="M0 0 L9 5 L0 10 z" fill="{EDGE}"/></marker></defs>',
            f'<path fill="#f5f7f6" d="M0 0H{width}V{height}H0z"/>',
        ]
        self.text(16, 32, title, 23, bold=True)

    def text(self, x, baseline, value, size=17, bold=False, color=INK, center=False):
        anchor = "middle" if center else "start"
        weight = "700" if bold else "400"
        self.items.append(f'<text x="{x}" y="{baseline}" font-family="Arial, sans-serif" '
                          f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" '
                          f'fill="{color}">{escape(value)}</text>')

    def path(self, route, head=True, dashed=False):
        marker = ' marker-end="url(#tip)"' if head else ''
        pattern = ' stroke-dasharray="5 4"' if dashed else ''
        self.items.append(f'<path d="{route}" fill="none" stroke="{EDGE}" stroke-width="2" '
                          f'stroke-linejoin="round"{marker}{pattern}/>')

    def lanes(self, headers, top, bottom):
        lane_width = self.width / len(headers)
        for i, header in enumerate(headers):
            if i:
                x = lane_width * i
                self.items.append(f'<path d="M{x} {top}V{bottom}" stroke="#c9d3d5"/>')
            self.text(lane_width * (i + .5), top + 19, header, 16, True, MUTED, True)

    def card(self, x, y, width, heading, lines=(), kind="record", size=17):
        # A consistent baseline rhythm leaves room for ascenders and descenders.
        fill, stroke = PALETTE[kind]
        h = 43 + 22 * len(lines)
        dash = ' stroke-dasharray="5 4"' if kind == "option" else ''
        self.items.append(f'<g data-label-box=""><rect x="{x}" y="{y}" width="{width}" '
                          f'height="{h}" rx="7" fill="{fill}" stroke="{stroke}" '
                          f'stroke-width="1.5"{dash}/>')
        self.text(x + 12, y + 26, heading, size, True)
        for i, line in enumerate(lines):
            self.text(x + 12, y + 51 + i * 22, line, size, color=MUTED)
        self.items.append('</g>')
        return y + h

    def save(self, source):
        Path(source).with_suffix(".svg").write_text("\n".join([*self.items, "</svg>", ""]), encoding="utf-8")

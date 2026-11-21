---
name: diagrammer
description: "Make the approved swimlane navigable and maintain its text equivalent."
---

# Diagrammer

1. Use the 2048-by-1735 reference coordinate system for new or adjusted hotspots.
2. Give every clickable region a meaningful label and a destination in the lesson inventory.
3. Check visual alignment at fit and zoom, keyboard order, branch semantics and the alternate text route.
4. Keep the reader able to navigate the same material without relying on color or pointer input.

## Return

Updated map assets or hotspot records with a tested equivalent navigation route.

Commit each instructional figure as SVG alongside its editable source (.mmd or generation script). Supply alt text and a text equivalent that names each decision and route. Inspect readability at phone width.

## Render and inspect every figure

1. Regenerate each instructional SVG from its editable source. Render **every** edition figure, including unchanged figures, at its natural dimensions and at the article’s phone width. Inspect the fixed raster map at fit and at full size. Compare the actual rendered output with the text equivalent.
2. Follow the last line of every card to its bottom and right borders. Leave visible space on every side. Check labels outside cards against connector lines, dividers and the canvas. Inspect split and join points for missing, duplicate or reversed arrowheads. Use an unmarked connector at a merge and one arrow into the destination.
3. Mark each labeled box as a group (`<g data-label-box="">`) containing its rectangle and its text. Leave free captions and connector labels outside these groups. Run the browser validator on the built edition. It measures rendered SVG text bounds; raster labels and the meaning of arrows require visual inspection.
4. Record the figures, sizes, defects and rechecks in the diagrammer handoff. A passing link check establishes only that the asset can be opened.

// Executed by Playwright in each instructional SVG after its fonts have loaded.
async () => {
  await document.fonts.ready;
  const svg = document.querySelector("svg");
  if (!svg || !svg.viewBox.baseVal.width || !svg.viewBox.baseVal.height) {
    return ["Missing SVG viewBox"];
  }

  const padding = 6; // Diagram units, independent of the rendered image size.
  const tolerance = 0.01; // Matrix round-off when scaled to the browser viewport.
  const errors = [];
  const visible = element => !element.closest("defs, clipPath, mask, marker, symbol") &&
    element.getClientRects().length && getComputedStyle(element).visibility === "visible";
  const labels = [...svg.querySelectorAll("text")].filter(visible);
  if (!labels.length) errors.push("No rendered text labels to measure");

  // Compare glyphs with their box in one coordinate system, including any
  // transforms on a label, its panel, or their ancestors.
  function boundsIn(element, space) {
    const {x, y, width, height} = element.getBBox();
    const transform = space.getScreenCTM().inverse().multiply(element.getScreenCTM());
    const corners = [[x, y], [x + width, y], [x, y + height], [x + width, y + height]]
      .map(([cx, cy]) => new DOMPoint(cx, cy).matrixTransform(transform));
    return {
      left: Math.min(...corners.map(p => p.x)), right: Math.max(...corners.map(p => p.x)),
      top: Math.min(...corners.map(p => p.y)), bottom: Math.max(...corners.map(p => p.y)),
    };
  }

  function clearances(bounds, box) {
    return {
      left: bounds.left - box.x, right: box.x + box.width - bounds.right,
      top: bounds.top - box.y, bottom: box.y + box.height - bounds.bottom,
    };
  }

  function check(label, gaps, minimum, container) {
    for (const [side, gap] of Object.entries(gaps)) {
      if (gap < minimum - tolerance) {
        errors.push(`"${label.textContent}" has ${gap.toFixed(1)} units at the ${side} of its ${container} (requires ${minimum})`);
      }
    }
  }

  const panels = new Map();
  for (const group of svg.querySelectorAll("g[data-label-box]")) {
    const rects = group.querySelectorAll(":scope > rect");
    if (rects.length !== 1 || !group.querySelector("text")) {
      errors.push("A data-label-box group must have one direct rect and its text");
    } else {
      panels.set(group, rects[0]);
    }
  }

  const canvas = svg.viewBox.baseVal;
  const boxes = [...svg.querySelectorAll("rect")].filter(visible).filter(rect => {
    // Exclude the page background that encloses the entire viewBox.
    const gaps = clearances(boundsIn(rect, svg), canvas);
    return Object.values(gaps).some(gap => gap > tolerance);
  });

  for (const label of labels) {
    check(label, clearances(boundsIn(label, svg), canvas), 0, "canvas");
    const panel = panels.get(label.closest("g[data-label-box]"));
    if (panel) {
      check(label, clearances(boundsIn(label, panel), panel.getBBox()), padding, "box");
      continue;
    }

    // A missing group must not turn a boxed label into an unchecked caption.
    for (const rect of boxes) {
      const bounds = boundsIn(label, rect);
      const box = rect.getBBox();
      if (bounds.left < box.x + box.width && bounds.right > box.x &&
          bounds.top < box.y + box.height && bounds.bottom > box.y) {
        errors.push(`"${label.textContent}" overlaps a box outside its data-label-box group`);
        break;
      }
    }
  }
  return errors;
}

"""Generate the pre-merge repair and its unresolved branch."""
from flow_drawing import Drawing

d = Drawing(440, 544, "PR-42: a hypothetical failed check",
    "In this hypothetical example, open the failed required check and inspect its output and tested revision. Push the fix to PR-42 and "
    "inspect the new run. A red or missing required result blocks merge. A green result returns the PR to "
    "review. CC-123 links to the PR and preserves links to the failed and passing runs.")
d.card(16, 54, 408, "Open the failed required check", ["Inspect the tested revision. The unit check found", "an empty assignment history after submission."], "hold")
d.path("M220 141V163")
d.card(16, 164, 408, "Fix the cause on the same PR", ["Push to PR-42 and open the new run."])
d.path("M220 229V251")
d.card(16, 252, 408, "Did the required check pass?", ["Match the result to the updated revision."], "decision")
d.path("M220 317V334", head=False)
d.path("M220 334H114V356")
d.path("M220 334H326V356")
d.card(16, 357, 196, "Red or missing", ["Keep merge blocked.", "Inspect and repair."], "hold")
d.card(228, 357, 196, "Passed", ["Resume PR review.", "Check merge rules."], "actual")
d.text(16, 482, "CC-123 stays In review.", 18, True)
d.text(16, 506, "Link PR-42 and its failed and passing runs here.")
d.text(16, 527, "This pre-merge repair stays on the story.")
d.save(__file__)

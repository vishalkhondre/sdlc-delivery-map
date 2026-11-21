"""Generate the owner handoffs during the limited production pilot."""
from flow_drawing import Drawing

d = Drawing(456, 905, "Respond to the wrong recipient",
    "The on-call responder finds wrong routing on prod-r41. The responder declares INC-7 and halts exposure. The Service Owner takes coordination "
    "and tracks eight requests. The Service Owner links the incident and change record, and the responder investigates. Actual "
    "route: correct mapping on the same image; smoke prod-r42 with prod-routing-11. A hypothetical code "
    "fault takes the hotfix route with a new digest. The Service Owner verifies seven reassignments and one "
    "retained authorized decision, owns any gaps, and reviews the incident. Expansion follows observation.")
d.text(16, 59, "INC-7 during the limited pilot")
d.lanes(["On-call / operator", "Service Owner"], 80, 854)
d.card(14, 116, 202, "prod-r41 smoke", ["Wrong recipient on", "prod-routing-10.", "Declare INC-7 and", "halt expansion."], "hold")
d.path("M216 167H238")
d.card(240, 116, 202, "Coordinate INC-7", ["Track eight affected", "requests. Link the", "incident to the repair", "change or defect."], "hold")
d.path("M341 247V266H115V284")
d.card(14, 285, 202, "Mapping or code?", ["Compare the group", "in the approved map", "with the active map", "and image identity."], "decision")
d.path("M216 340H238", dashed=True)
d.card(240, 285, 202, "Alternative · code", ["Route a code fault to", "emergency review.", "A hotfix needs a new", "digest, qualification", "and authorization."], "option")
d.path("M115 416V458")
d.card(14, 459, 202, "Actual · mapping", ["Correct the group.", "Keep the same image.", "Deploy prod-r42 with", "prod-routing-11."], "actual")
d.path("M115 590V610")
d.card(14, 611, 202, "Smoke prod-r42", ["Verify the digest and", "mapping. Submit and", "observe the rule pick", "the right approver."], "actual")
d.path("M216 667H238")
d.card(240, 611, 202, "Reconcile all eight", ["Seven reassigned.", "One prior authorized", "decision retained.", "Own any open gaps."], "actual")
d.path("M341 742V762")
d.card(240, 763, 202, "Review INC-7", ["Record repair, impact", "and follow-up."], "actual")
d.text(16, 885, "Expand only after observing the corrected pilot.", 18, True)
d.save(__file__)

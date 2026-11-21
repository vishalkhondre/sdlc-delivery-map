"""Draw the urgent code-fix route from a compatible base through production."""
from flow_drawing import Drawing

d = Drawing(
    474, 1276, "Which code can we repair safely?",
    "Hypothetical urgent code repair. INC-7 used a configuration change. Identify "
    "the serving revision, code and data, then decide whether main is suitable. "
    "If main is safe, start from it. Otherwise verify the source of production and "
    "branch from its matching release tag. Review the fix, build a new digest, "
    "repeat the failing check and adjacent routing and authorization tests, and "
    "obtain business acceptance. The emergency authority records the decision, "
    "scope and an owner and deadline for any deferred test. In a limited pilot, "
    "smoke-test the actual revision and first recipient. Hold expansion on failure. "
    "After success, verify affected requests and observe the pilot. The QA lead must "
    "pass the deferred export test before the Service Owner can expand exposure. "
    "Missing or failed evidence holds expansion. Carry "
    "a release-branch fix back to main under review or verify an existing fix. "
    "Close follow-ups with evidence."
)
d.text(16, 60, "Hypothetical code fix. INC-7 used a mapping correction.")
d.card(16, 81, 442, "Can main safely repair the running service?", [
    "Match the running revision to its source and data.",
    "Check for unrelated changes before picking a base."
], "decision")
d.path("M237 168V184", head=False)
d.path("M237 184H121V204")
d.path("M237 184H353V204")
d.card(16, 205, 210, "Yes · use main", [
    "Start from reviewed",
    "main at a compatible",
    "commit."
])
d.card(248, 205, 210, "No · use release", [
    "Branch from the tag",
    "verified against the",
    "running version."
])
d.path("M121 314V332H353V314", head=False)
d.path("M237 332V351")
d.card(16, 352, 442, "Review the repair and build a fresh image", [
    "Peer-review the small change. Run required checks.",
    "Keep the incident, commit and new digest linked."
])
d.path("M237 439V460")
d.card(16, 461, 442, "Qualify the new digest", [
    "Repeat the failure, nearby routing and permissions.",
    "Get a business decision for the corrected behavior."
])
d.path("M237 548V569")
d.card(16, 570, 442, "Authorize the emergency scope", [
    "Name the digest, settings, risk and recovery path.",
    "Give each permitted deferral an owner and deadline.",
    "Missing evidence or authority keeps the hold."
])
d.path("M237 679V700")
d.card(16, 701, 442, "Did the limited pilot route correctly?", [
    "Send a controlled request to the serving revision.",
    "Check its first assignment against the approved rule."
], "decision")
d.path("M237 788V804", head=False)
d.path("M237 804H121V824")
d.path("M237 804H353V824")
d.card(16, 825, 210, "No · hold expansion", [
    "Contain exposure.",
    "Recover service and",
    "reconcile requests.",
    "Requalify any repair."
], "hold")
d.card(248, 825, 210, "Yes · observe", [
    "Check affected work.",
    "Keep the pilot limited",
    "while the team reviews",
    "its observations."
], "actual")
d.path("M353 956V977")
d.card(16, 978, 442, "Before wider exposure", [
    "QA must pass the deferred export test.",
    "The Service Owner checks that result and the pilot.",
    "Expand only if both pass. Otherwise keep the hold."
], "decision")
d.path("M237 1087V1108")
d.card(16, 1109, 442, "Keep the shipped fix on main", [
    "Release-branch fix? Return it through a reviewed PR.",
    "Already on main? Verify inclusion without reapplying.",
    "Link the completed checks and follow-up evidence."
])
d.text(16, 1257, "A new build needs its own acceptance and authorization.", 16)
d.save(__file__)

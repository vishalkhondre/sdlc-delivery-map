"""Generate the configuration and code decision fork after UAT rejection."""
from flow_drawing import Drawing

d = Drawing(456, 636, "Recover from a UAT rejection",
    "uat-80 rejected the candidate on uat-r8 because unit B reached unit A’s approver. Hold release. "
    "The actual mapping repair kept build-418, followed by qa-209 and a new decision, uat-82 on uat-r9. "
    "A hypothetical code repair requires a new build and digest, QA qualification, and another business decision. "
    "Either route that fails stays on hold and retains uat-80.")
d.card(16, 55, 424, "uat-80 rejected · hold release", ["uat-r8 with uat-routing-5 sent Purchasing unit B", "to unit A’s approver."], "hold")
d.path("M228 142V163")
d.card(16, 164, 424, "What caused the wrong recipient?", ["Inspect the mapping, digest and assignment event."], "decision")
d.path("M228 229V245", head=False)
d.path("M228 245H117V263")
d.path("M228 245H339V263", dashed=True)
d.card(16, 264, 202, "Actual · mapping", ["Correct the UAT map.", "Keep build-418 and", "its original digest."], "actual")
d.card(238, 264, 202, "Alternative · code", ["Repair reviewed code.", "Publish a new build", "and digest."], "option")
d.path("M117 373V394")
d.path("M339 373V394", dashed=True)
d.card(16, 395, 202, "qa-209 → uat-82", ["QA rechecks routing", "and permissions.", "Business repeats the", "scenario on uat-r9", "with uat-routing-6.", "uat-82 accepts."], "actual")
d.card(238, 395, 202, "Fresh qualification", ["Run QA against the", "new digest. Repeat", "UAT on that candidate.", "The signatory makes", "a new decision."], "option")
d.text(16, 604, "If either route fails, keep the release on hold.", 18, True)
d.text(16, 627, "Retain uat-80 alongside the new evidence.")
d.save(__file__)

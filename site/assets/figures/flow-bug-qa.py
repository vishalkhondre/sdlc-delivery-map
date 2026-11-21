"""Generate the role swimlane for the failed increment, repair and later integration."""
from flow_drawing import Drawing

d = Drawing(510, 833, "Who hands off QA defect CC-131?",
    "Developer publishes PR-40 as build-412. Kiwi execution TC-04 in qa-196 fails and stores the CC-131 URL. "
    "Triage links the Jira issue to CC-123 and holds promotion. PR-41 yields a fresh image, build-415. "
    "In qa-198 a new TC-04 execution confirms denial. A separate check verifies authorized approval. If requested and permitted, an "
    "optional comment on CC-131 links back to the Kiwi run and identifies the execution. The triage owner "
    "closes as Fixed or reopens after a failed retest. QA lead releases the hold only on success. PR-42 "
    "later integrates the change as build-418, which gets its own qa-204 qualification.")
d.text(16, 59, "One pipeline builds all three increments (main-release-build).")
d.lanes(["Developer / build", "QA / Kiwi TCMS", "Triage / Jira"], 78, 764)

d.card(8, 115, 150, "PR-40", ["First increment", "build-412", "ad1985a0…"])
d.path("M158 157H178")
d.card(180, 115, 150, "qa-196 · failed", ["TC-04 allowed", "an unauthorized", "decision. Store", "the CC-131 URL."], "hold", 16)
d.path("M330 157H350")
d.card(352, 115, 150, "CC-131", ["Link bug to the", "CC-123 story.", "Hold promotion."], "hold")
d.path("M427 224V263H83V285")

d.card(8, 286, 150, "PR-41", ["Repair the code.", "New build-415", "653039af…"])
d.path("M158 327H178")
d.card(180, 286, 150, "qa-198 · retest", ["TC-04 denied.", "Link CC-131.", "Also verify valid", "approval."], "actual", 16)
d.card(352, 286, 150, "Optional link", ["Jira comment", "links to qa-198", "and names the", "Kiwi execution."], "option", 16)
d.path("M352 350H332", dashed=True)
d.path("M255 417V439H427V461")

d.card(352, 462, 150, "Review retest", ["On pass, set", "Closed with", "resolution Fixed."], "actual", 16)
d.path("M352 517H332")
d.card(180, 462, 150, "Release hold", ["QA lead checks", "the evidence."], "actual", 16)
d.path("M427 571V603", dashed=True)
d.card(352, 604, 150, "If retest fails", ["Set Reopened.", "Clear resolution.", "Keep the hold."], "option", 16)
d.path("M255 549V579H83V603")
d.card(8, 604, 150, "Later · PR-42", ["Integrate and", "build again.", "build-418", "041f649d…"])
d.path("M158 652H178")
d.card(180, 604, 150, "qa-204", ["Qualify the", "integrated image", "on its own digest."], "actual", 16)
d.text(16, 785, "Keep qa-196. The optional link points from Jira back to Kiwi.", 16)
d.text(16, 810, "Adding the comment requires reporter selection and permission.", 16)
d.save(__file__)

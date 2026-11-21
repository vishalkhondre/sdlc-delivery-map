"""Generate the decision path for retiring an old routing field."""
from flow_drawing import Drawing

diagram = Drawing(
    468, 985, "When can the old field go?",
    "Hypothetical routing-field migration. Add the new field and retain the old one. "
    "During overlap, preserve the old read path and keep both representations consistent. "
    "Drain old-only writers before the final catch-up and comparison. "
    "Backfill and reconcile stored requests, including open work. Preserve current "
    "ownership and earlier decisions. Read from the new field after verification and "
    "observe the cutover. Compare field values while both still receive all writes. "
    "After equality passes, retire old-dependent rollback versions and deploy new-only "
    "code. At the final gate, check current assignments against authoritative business "
    "records and the approved rule. Confirm every reader, writer and eligible rollback "
    "version can operate without the old field. Hold removal if any check fails."
)
diagram.text(16, 60, "Illustrative change to the approval-routing data.")
diagram.card(16, 83, 436, "Expand the schema", [
    "Add the new field. Keep the existing field readable."
])
diagram.path("M234 148V171")
diagram.card(16, 172, 436, "Run compatible readers and writers", [
    "Read the old field. Write both fields together.",
    "Track any old writer that still updates only one."
])
diagram.path("M234 259V282")
diagram.card(16, 283, 436, "Backfill and reconcile", [
    "Fill older rows. Drain old writers and catch up.",
    "Recheck open work, owners and decision history."
])
diagram.path("M234 370V393")
diagram.card(16, 394, 436, "Switch reads and observe", [
    "Read the new field after reconciliation passes.",
    "Keep dual writes during the rollback window."
])
diagram.path("M234 481V504")
diagram.card(16, 505, 436, "Before ending dual writes", [
    "Compare both fields while both are still current.",
    "If they agree, retire old-dependent rollback versions",
    "and deploy new-only code. Otherwise hold here."
])
diagram.path("M234 614V637")
diagram.card(16, 638, 436, "Safe to retire the old field?", [
    "Do current assignments match the business record",
    "and approved rule? Can every reader, writer and",
    "eligible rollback version run without the old field?"
], "decision")
diagram.path("M234 747V771", head=False)
diagram.path("M234 771H121V803")
diagram.path("M234 771H347V803")
diagram.card(16, 804, 210, "Yes · contract", [
    "Remove the old field.",
    "Verify the surviving",
    "read and write paths."
], "actual")
diagram.card(242, 804, 210, "No · hold", [
    "Keep both fields.",
    "Resolve the gap and",
    "repeat verification."
], "hold")
diagram.text(16, 944, "Once writes update only the new field, the old value", 16)
diagram.text(16, 966, "can be stale. Use the assignment record to check owners.", 16)
diagram.save(__file__)

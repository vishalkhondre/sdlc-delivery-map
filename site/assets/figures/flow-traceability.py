"""Generate the forward and reverse evidence trail across the production gate."""
from flow_drawing import Drawing

d = Drawing(452, 851, "Follow the accepted image",
    "Follow PR-42 and its integrated commit to build-418, its linux/amd64 digest, qa-204, rejected uat-80, "
    "qa-209 and accepted uat-82. The Release Manager verifies the recorded authorization for the digest. The operator checks the observed "
    "digest and configuration on prod-r42, then links smoke. On mismatch hold rollout. From smoke, follow "
    "each prior record back to the integrated commit. The same digest routed differently on prod-r41.")
d.text(16, 60, "Read down to delivery, or up from smoke to source.")
d.card(16, 79, 420, "PR-42 → integrated source", ["Commit 3ab862bc… feeds build-418."])
d.path("M226 144V163")
d.card(16, 164, 420, "build-418 → published image", ["sha256:041f649d… for linux/amd64.", "Compare the full digest in each record."])
d.path("M226 251V270")
d.card(16, 271, 420, "QA → business decision", ["qa-204 passes. uat-80 rejects the UAT mapping.", "qa-209 rechecks the rule and permissions.", "uat-82 accepts on uat-r9 with uat-routing-6."])
d.path("M226 380V401")
d.card(16, 402, 420, "May we deploy?", ["Release Manager reviews QA, UAT and mapping.", "Authorization for 1.3.0 names sha256:041f649d…"], "decision")
d.path("M226 489V510")
d.card(16, 511, 420, "What ran?", ["Operator reads prod-rollout-87 and prod-r42.", "Observed image matches the authorized digest.", "Active configuration is prod-routing-11."], "actual")
d.path("M226 620V641")
d.card(16, 642, 420, "Smoke → exposure decision", ["The rule assigns the designated test approver.", "The owner observes routing before expanding."], "actual")
d.text(16, 763, "Digest mismatch? Hold rollout and investigate.", 18, True)
d.text(16, 790, "prod-r41 used the same image with prod-routing-10.")
d.text(16, 813, "It sent a controlled request to the wrong recipient.")
d.save(__file__)

# Independent accuracy review of the six flows

I read the six generated topic pages and their five SVGs, including the visible labels, descriptions and the HTML text equivalents. I compared the pages with the signed-off inventory, the depth requirements and reader questions in sections 5 and 10 of the plan, the existing Jira and Prove lessons, the canonical fictional dataset and both built downloads. I opened the cited primary documentation for all six topics.

## Findings in the first build

| Location | Finding and requested correction |
| --- | --- |
| CI, Jira handoff | The PR-42 example described the build-412 QA failure as occurring “later.” PR-40 and PR-41 precede PR-42 in the shared pipeline. Identify build-412 as the earlier candidate and retain the hypothetical status of the PR-42 failure. |
| QA, build-415 row and figure description | One execution was said to verify both TC-04 and the allowed path. TC-04 exercises the unrelated employee. Keep its new execution separate from the adjacent allowed-path check in the same run. Expose the human status transition and the independent resolution on both outcomes. |
| QA, sources | The link labelled “Issue tracker integration” opens the Kiwi 17.2 “tcms.issuetracker package” index. Use the module name, with the adjacent source links supplying the actual implementation. |
| UAT, evidence | The download gives the designated representative's role for both decisions. It does not name a person. The closing evidence paragraph should promise the signatory role. |
| Production, incident swimlane | The first figure said the Service Owner declared the incident, while the lesson assigned declaration to the on-call responder. Align the lane, SVG description and HTML text with the example's declaration and coordination roles. |
| Traceability, alternative text | The SVG description attributed authorization to the Release Manager as an observed personal act. The visible box correctly assigns the manager the review, and the download supplies a standard-change policy, date and digest. Distinguish role from recorded approval. Express the UAT repair as a mapping change on the same image. |

## Independent evidence checks

- The seven Jira rows give the last mover as Developer, Developer, Developer, QA Lead, Business Analyst, Release Manager and Release Manager. The first Jira status is unspecified in the source. The seven resulting statuses are In development, In review, Ready for QA, In QA, In UAT, Ready for release and Released. The uat-80 hold and first production attempt preserve the prior status. Jira History, Development evidence and a human transition serve distinct purposes.
- GitHub's workflow-event, variables, workflow-log and rerun documentation supports the distinction between the PR head, the temporary test merge, the head actually checked out, and the integrated source. A repaired push in the illustrated workflow starts a new run. A rerun keeps the event's SHA/ref and run ID and increases the attempt. The run IDs, proposed SHA and temporary merge SHA are absent from the case. The named required and informational checks match the accepted CI pilot.
- The published Kiwi 17.2 JIRA adapter creates the issue with an originating execution URL in its description and stores the returned Jira URL as a defect reference on that execution. A prefilled form needs human completion and verification. For an existing issue, TestExecution.add_link stores the reference. Optional write-back requires a matching configured defect tracker, enabled credentials, permissions and a request to add the comment. The comment identifies the execution and links to the run. Neither path moves the feature or bug. The flow's QA and UAT lessons disclose version, published-source basis and absence of a live joint demonstration.
- I matched every full SHA/digest printed in the six HTML pages against the dataset. PR-40/build-412 fails in qa-196; PR-41/build-415 confirms the repair in qa-198. The accepted source is PR-42 at 3ab862bc3190549bff7df2e0c1a02c9cc11459e4. Build-418 publishes sha256:041f649df9da0e8f01adbfb779b80fef6aef2fad08edecb62f2de49858ccec5c for linux/amd64. The fixture supplies no second platform digest. Docker's platform manifests and index relationship matter before treating different reported digests as a mismatch.
- In qa-204, R-17's assignment actor is routing-rule, the recipient is Purchasing approver, the requester's denied attempt leaves it pending, and the authorized decision is recorded. This evidence is AC-01/AC-02. The earlier unrelated-employee failure belongs to its own candidate. qa-209 is a summary of mapping and permission rechecks without a separate timestamp, QA config or individual request record.
- On build-418's digest, uat-80 rejects unit B going to unit A's approver on uat-r8/uat-routing-5. The corrected UAT settings, qa-209 and repeated scenario produce uat-82 on uat-r9/uat-routing-6. The new-code route is hypothetical. Authorization follows at 12:00 UTC on 12 March, under the recorded standard-change policy. The tag marks the accepted commit. The download contains neither an individual approver nor a GitHub environment protection log.
- The two prod-rollout-87 attempts use the authorized image. prod-r41/prod-routing-10 sends a controlled request to the wrong recipient. Corrected prod-r42/prod-routing-11 passes smoke and two hours of observation before expansion. Seven reassignments plus one retained authorized decision account for the eight INC-7 cases. The corrected pilot was 24/24 within two minutes, excluding two controlled submissions. I recalculated the CSV independently: 100 requests with 1,440 minutes each; 92 assignments in 3–19 minutes; zero assignments within two minutes; EX-093–EX-100 missing correct assignments; 40 decided and 60 open. The median was unreached at 24 hours. The later eight cases are outside INC-7.

These checks used fictional public records and published product behavior. They did not involve a live Jira, Kiwi, CI or production deployment.

**Initial verdict: return for correction** of the six findings above. The accepted evidence and candidate sequence otherwise agree. Final disposition follows the rebuilt-page recheck.

## Recheck and final verdict

I reread the rebuilt pages after the revisions. The PR-42 failure is hypothetical and build-412 precedes it. The QA table and diagram now distinguish the fresh TC-04 confirmation from the allowed-path check in qa-198. The text gives Closed/Fixed and Reopened/empty as distinct outcomes for the human triage decision, and the corrected reference uses the actual Kiwi module name. The UAT evidence field names the signatory role. The production figure assigns declaration and containment to the responder, then coordination and reconciliation to the Service Owner. The traceability text keeps the digest constant through the mapping repair, and the final SVG description assigns verification of the recorded authorization to the Release Manager. I compared all five served SVGs byte-for-byte with their reviewed originals.

**Final verdict: accept.** All six first-build findings are closed. The full SHA and three digests, the two UAT decisions, the deployment authorization boundary, and the three populations remain consistent across the reviewed pages and records.

Reviewed SHA-256 values:

- content/10-flows.json — b7191fb74f588674f136ec59950d9d37e4d3c64ebe1dcb70c2cb5ce231f446e6

- site/assets/figures/flow-bug-ci.svg — 7dbb6efa9f6bb4d0206a9438f8b3730f05e807acc0b078e1ad68dad19ea8cc19

- site/assets/figures/flow-bug-prod.svg — 0f6610d4e15ab178db0ab44d58a02cea093a4bddbfba3d20443195295bbb28fb

- site/assets/figures/flow-bug-qa.svg — 54f9dea7dc1ebadd56f517edcc7e41a459872e5d0f283043641fae65715b7bd1

- site/assets/figures/flow-bug-uat.svg — 23fd600b79fce5435b6105a87278c956679fa5aad4738530906508139650ed9c

- site/assets/figures/flow-traceability.svg — 0ddca75dd9e81dc16740a0ec8f7664251e0ff6af18cb96262bcc629373948e8d

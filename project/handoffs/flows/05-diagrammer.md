# Flow diagram review

The five flow lessons have original SVGs and same-stem Python sources in `site/assets/figures`. The sources share `flow_drawing.py`. The Jira status flow uses a seven-row table. Each SVG has a title and description. Each corresponding lesson supplies alt text and a text route through the decisions.

| Figure | Natural size | Route checked |
|---|---|---|
| flow-bug-ci | 440 × 544 | A hypothetical failed PR-42 check leads to repair on the same PR. A passing replacement returns to review. A required result that's red or missing keeps merge blocked. CC-123 retains the evidence. |
| flow-bug-qa | 510 × 833 | The Developer/build, QA/Kiwi and Triage/Jira lanes trace three increments. The failed execution points to CC-131. An optional comment in Jira points back to the retest and identifies the execution. qa-198 confirms TC-04 denial and separately checks authorized approval. A triage decision closes or reopens the bug. |
| flow-bug-uat | 456 × 636 | The rejected uat-80 record leads to cause analysis. The recorded mapping repair retains the image, links qa-209, repeats UAT on uat-r9 and reaches uat-82. The alternative code path needs a new digest and fresh QA and business decisions. |
| flow-bug-prod | 456 × 905 | The responder declares INC-7 and halts expansion. The Service Owner coordinates impact and reconciliation. The actual repair changes the mapping on the same image. The alternative code fault goes through hotfix qualification and authorization. The ledger accounts for all eight requests. |
| flow-traceability | 452 × 851 | Records lead from PR-42 to build-418, qualification, recorded authorization, observed prod-r42 and smoke. Following the records backward identifies the integrated source. The prod-r41 comparison illustrates two different routing results for one digest. |

I regenerated the five flow files, compared their decisions and directions with the lesson text equivalents and inspected raster renders of all ten instructional SVGs at natural size and 365 pixels wide. I checked card edges, headings, captions, lane dividers, arrow directions and junctions. The marks on dashed branches appear at their destinations. The optional Jira comment link points toward Kiwi. All text in the new SVGs fits within its canvas. The map was inspected at phone fit and in four full-size quadrants of the 2048 × 1735 original. At phone fit, its fine print needs zoom or the text route.

Local Inkscape measurements cover 144 label lines in 36 new boxes. The smallest painted inset in each flow figure is 10.5 SVG units. Across all ten figures the minimum is 8.6 units in the existing Jira workflow. The SVGs use responsive view boxes. During review I corrected the incident declaration lane, distinguished separate denial and approval observations, marked the PR-42 failure hypothetical, and clarified that the Release Manager checks the recorded authorization. I regenerated and rechecked the affected assets.

A separate local Chromium launch stopped before rendering when its process socket was denied by the environment. The measurements above are from Inkscape. The repository browser check provides the independent Chromium measurement in CI.

# Independent accuracy review · ACCEPT · 21 November 2026

I reviewed the nine rendered Prove lessons and both SVGs against the shared dataset, the downloadable qualification record and the primary sources cited on the pages. I traced the three builds and checked every full digest in the rendered samples. I also checked the two UAT decision times, the acting roles and the distinction between a plan, an expected result and a recorded execution.

| Reader check | Finding |
| --- | --- |
| Q8 | The CC-123 plan groups TC-01/02 under AC-01. On build-418, qa-204 identifies the routing actor and recipient, a denied requester and an authorized approval. The summary supplies criterion-level evidence for AC-01/02 only. An unrelated-employee result on build-418 and the proposed AC-03 timing results cannot be inferred. The 120-second inclusive boundary, the 121-second miss and the 30/100-second counterexample match the fixture. |
| Q9–10 | TC-04 failed in qa-196 on build-412 when an unrelated employee recorded a decision. The defect URL on the Kiwi execution and the Jira relation “CC-131 blocks CC-123” have separate endpoints. The QA lead assesses severity and the Product Owner agrees priority with QA. The bug and feature retain distinct states. |
| Q11–13 | qa-198 confirms TC-04 and checks the authorized path on build-415. The triage owner closes the bug. build-418 qualifies separately in qa-204. A new pre-decision finding holds sign-off and preserves the earlier pass. uat-80 rejected unit B reaching unit A. The corrected mapping retains the build-418 digest. qa-209 rechecks mapping and permissions. uat-82 records a fresh, scoped business acceptance on uat-r9/uat-routing-6. |
| Configuration and recovery | The accepted production baseline is prod-r42/prod-routing-11. INC-7 accounts for eight earlier requests, seven reassigned and one authorized decision retained. prod-routing-12, the illustrative group identifiers, planned checks and reversal are prospective. GitHub environment approval and the team's distinct business and QA decisions remain separate. |

I checked Kiwi 17.2’s Test Cases and Test Runs guides and its published TestRun, TestExecution and Jira tracker code. API-created Jira issues include the originating execution URL and leave a defect URL on the execution. For an existing Jira issue the optional comment requires a recognized defect URL, an enabled integration and the necessary permissions. The comment points to the run and names the execution. It does not establish the retest verdict. All eight lessons that describe Kiwi behavior disclose the version, evidence basis and absence of a live Kiwi/Jira demonstration.

I rechecked the corrected HTML and rendered figures. The plan lesson now requires confirmed cases for a new run. The defect report labels the 5 March timestamp as the report time. The bug diagram shows the Closed-to-Reopened recurrence transition. In the regression diagram, uat-82 belongs to the corrected UAT mapping branch and the common handoff describes business testing. The revised Jira relation reads in the correct direction.

**Verdict: accept.** No open accuracy findings. This was a review of published mechanisms and fictional records. No live Kiwi, Jira or deployment test was conducted.

Reviewed SHA-256 values, computed from the accepted files:

- content/08-deep-prove.json — ae7448dee7bce1f54c0221fb4091be46944c94e4c106686713e171a80bb4db64
- site/assets/figures/defect-lifecycle.svg — 390746184dfc140dfc63dedf76aa271193636a935a9ed7479f955ecaa32a22e0
- site/assets/figures/regression-scope.svg — be2b7f4bae598fbec4752e57c04277c7223fcb41764d3849c2a3ccbd774f656b

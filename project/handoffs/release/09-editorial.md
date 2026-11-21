# Independent editorial review of Release

**Verdict: pass after corrections.** A separate reviewer started from the generated tour, opened all seven Release lessons in inventory order, and then read the approval and migration lessons as direct entries. The review used the built pages and their linked primary sources, the shared fictional dataset, the Release inventory and the plan's depth and acceptance criteria. No provider job, database migration, support publication or incident was executed.

## Reader tasks and depth checks

The twelve columns follow DEPTH-PLAN §5. P = found and checked in the generated lesson. The column numbers mean 1 trigger/place/time, 2 inputs/access, 3 illustrative setting, 4 observable output, 5 gate and owner, 6 first failure action, 7 Jira link/status, 8 fictional worked failure, 9 two errors with consequences, 10 principle/tool/policy labels, 11 transfer to another tool, 12 two or more primary sources checked. The last column identifies the setting, output and decision a reader can recover.

| Page ID | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | Reader's decision |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| versioning-and-fix-version | P | P | P | P | P | P | P | P | P | P | P | P | Match 1.3.0, v1.3.0 and the full commit on build-418. The coordinator holds publication on a tag pointing to the earlier repair. |
| change-approval | P | P | P | P | P | P | P | P | P | P | P | P | Read standard, normal and emergency routes against a protected job and noon authorization. On uat-80's rejection, the Release Manager keeps CC-123 In UAT. |
| deploy-workflow-anatomy | P | P | P | P | P | P | P | P | P | P | P | P | Compare the selected package, pinned traffic, staged revision, effective mapping and first recipient. The operator retains the failed attempt and pauses expansion. |
| rollout-strategies | P | P | P | P | P | P | P | P | P | P | P | P | Choose a named purchasing group for the proposed pilot. The Service Owner uses the corrected two-hour population and serving errors before expansion. |
| rollback-rollforward | P | P | P | P | P | P | P | P | P | P | P | P | Compare revision, configuration, flag and forward repair against current data. Check both fresh routing and the business disposition of each previously affected purchase. |
| data-change-coordination | P | P | P | P | P | P | P | P | P | P | P | P | Read the compatibility matrix, SQL comparison and one returned rehearsal row. The migration owner holds the switch, drains the late writer and rechecks saved ownership. |
| release-notes-practice | P | P | P | P | P | P | P | P | P | P | P | P | Use the release scope and Service Owner's audience decision to draft a note for buyers, approvers and support. The Release Manager corrects a universal availability claim during a hold. |

Each opening uses two or three sentences and starts with a recognizable decision about a purchasing request or release. The technical examples follow that introduction. The Release Manager owns the feature transition, the operator stages and checks a revision, and the Service Owner owns expansion and unresolved exposure. The notes give support an appropriately private reporting route. The proposed flag and migration examples are identified as design exercises.

## Acceptance questions, answered from the built Release pages

| §10 | Learner answer and location | Inference or boundary |
|---|---|---|
| 14 | In the illustrative workflow, the Release Manager moves CC-123 from In UAT to Ready for release when the accepted candidate, mapping review, release identity and authorization line up. It stays there during prod-r41's hold. The Release Manager moves it to Released after the corrected rollout, controlled test and observation. See versioning-and-fix-version, change-approval and deploy-workflow-anatomy. | Steps 6–7 are explicit. The first five steps belong to the earlier cross-phase workflow and were outside this review. |
| 15 | Jira's Fix versions field puts CC-123 in the planned 1.3.0 scope. Git's v1.3.0 tag names the integrated source commit. The GitHub release publishes notes and associated artifacts for that tag. I would follow the build-418 receipt from the commit to the accepted package and the rollout record for actual availability. See versioning-and-fix-version, “Read the three records side by side” and “Check the actual target.” | None. |
| 16 | The change authority preauthorizes the standard procedure. The Release Manager verifies this candidate and target fit it. The designated change authority decides a normal change, and the designated emergency authority decides an expedited exception. The illustrated GitHub job references the protected production environment. An eligible member of its reviewer list approves, the initiator cannot self-approve, and administrator bypass is disallowed. A separate verification job checks the approved evidence before the environment gate. After the wait and immediately before changing the cloud service, the production job must re-read the authoritative approval and hold on revocation, expiry or a changed selection. The fixture supplies the role and digest but no named individual or provider approval event. See change-approval and deploy-workflow-anatomy. | None. The rule for deployment initiators and a policy about independent code authorship are explained separately. |
| 17 | The recovery decision requires the business owner to verify the intended recipients and group membership, an applicable change authorization, effective-setting readback and a fresh controlled submission. See rollback-rollforward and change-approval. | Release supplies prerequisites and verification. The complete next-week routing-table change and its continuing ownership belong to Learn. |
| 18 | Compare the actor and actual first recipient at submission with the independently approved unit-to-approver mapping. A request can be assigned promptly to the wrong group. The mismatch on the controlled request stopped expansion. See rollout-strategies and rollback-rollforward. | None for the signal and the Release response. Ongoing monitoring belongs to Learn. |
| 19 | A code correction needs a new identified build, qualification and applicable authorization. The incident lead records urgency and the emergency authority decides on retained and deferred checks and residual risk. See change-approval and rollback-rollforward. | These pages supply the Release guardrails. They do not establish a full code-hotfix path or a general list of tests that may be omitted. |
| 20 | The two-hour corrected pilot included 24 eligible submissions. The later one-day review studied another 100. Fast assignment in the pilot does not establish a faster purchasing decision. See rollout-strategies and release-notes-practice. | The CSV calculation, 40 decisions and CC-100 product choice are Learn work. No complete answer claimed here. |

The seven lessons preserve the distinction between build-412's failure, build-415's verified repair and build-418's qualified integration. They preserve qa-204, rejected uat-80, affected qa-209 and accepted uat-82. Both production attempts used the accepted image. The corrected mapping changed the outcome. The 24 eligible pilot submissions exclude the two controlled submissions. Seven reassignments and one retained decision resolve the eight incident requests. The eight later cohort exceptions have a separate owner and investigation.

## Navigation, figure and sources

The tour's Release stop has seven direct links. All local destinations and fragment IDs on the seven built pages resolved, including table-of-contents entries, parent lessons, related decisions, tour and map returns. Heading order, skip link, focusable section targets, native disclosure for the migration text description, mobile breakpoints and horizontal table/code scrolling were checked in the generated markup and CSS. An interactive Chromium run could not start because the environment denied its local socket. Actual browser keyboard traversal and device layout were not verified in this editorial pass.

The migration SVG was rendered and read at 440 pixels wide. The boxes, arrows, labels and hold/contract outcomes were legible and consistent with the neighboring matrix and text description, including the transition from final equality checking to checking current business state.

For §5.12 the reviewer opened and checked these sources linked by the pages on 2026-11-21:

| Lesson | Primary documentation spot-checks |
|---|---|
| Versioning | Atlassian, Manage versions (Fix versus Affects versions); Git, git-rev-parse (peel to a commit); GitHub, About releases (tag and release). |
| Approval | GitHub, Deployments and environments (eligible reviewer, initiator and environment rule); Atlassian, Change management types (change routes). |
| Deployment | GitHub, Configuring OpenID Connect in Azure (permission and token exchange); Azure, Container Apps Deploy Action (the imageToDeploy input accepts an existing image). The explicit script supplies checks the action does not establish about a business recipient. |
| Rollout | Microsoft, Traffic splitting in Azure Container Apps (revision weights and labels); Microsoft, Understand feature management using Azure App Configuration (application-evaluated targeting). |
| Recovery | AWS, Ensuring rollback safety during deployments (mixed-version compatibility); Google SRE Workbook, Incident Response (defined incident ownership). |
| Data | PostgreSQL, Modifying Tables and Comparison Functions and Operators (adding a column and comparing nullable values); AWS, Ensuring rollback safety during deployments (compatibility before retiring older versions). |
| Notes | GitHub, Automatically generated release notes and About releases (PR-based notes and release tags); Atlassian, Manage versions (work-item scope). |

## Findings and independent recheck

1. **Reader impact: moderate.** The original migration diagram compressed a final comparison and retirement into a single gate. A reader could infer equal old/new values were required after new-only writes began. The author split the pre-switch equality check from post-switch business-state verification. The rebuilt SVG, matrix and disclosure now agree, and each failure path keeps the old field.
2. **Reader impact: minor.** Recovery offered historical attempt times without an actionable estimate for a new responder. The rebuilt lesson specifies an illustrative ten-minute containment and verification-planning exercise, a two-hour observation block and named ownership for reconciliation that outlasts restoration.
3. **Reader impact: minor.** Direct entrants encountered UAT or smoke terminology before an explicit gloss on the versioning, approval and notes routes. Rechecked the rebuilt prerequisites: the first two expand user acceptance testing, and the notes page explains both terms in ordinary language.
4. **Updated examples checked.** The staged deployment now reads the exact revision with a bounded loop and leaves the business smoke test to an actual controlled request. The notes draft asks for a reference, unit, time and observed group through a private support channel. Its availability statement stays within the evidence.

No editorial correction remains open within these seven pages. The Learn section has its own Gate 3 review before Gate 4 integration approval.

# Learn editorial review

**Verdict — pass.** I entered through the Learn stop on the guided tour and read the six generated lessons in order. I also started directly at the alert, hotfix and outcome pages. The six introductions establish the buyer’s problem in two or three sentences. A reader can identify who holds expansion, who accounts for purchases already affected and who decides whether to change the product. The evidence distinguishes INC-7, a hypothetical emergency code repair and the later product cohort throughout.

## Reader tasks and acceptance questions

The answers below come from the built pages. The question numbers are from the depth plan, section 10. Each answer is explicit. The cohort arithmetic was independently reproduced.

| Question | Page | Reader’s answer |
|---|---|---|
| 18. Which signal catches a wrong recipient when no purchase is waiting for an assignee? | alert-design, rule inputs and rules; instrumentation, event contract | Compare the first committed assignment’s actor and recipient with the required automatic actor and the purchasing owner’s independent mapping effective at submission. One unresolved discrepancy pages on the first matching evaluation even if the unassigned count is zero. An unknown expectation makes verification incomplete. Inspect the matching request, revision and configuration, hold expansion, and retain the discrepancy until reconciled. |
| 19. What can the team shorten for an urgent production code repair? | hotfix-flow, base selection, qualification and verification | Contain the harm and verify a code fault against running code, settings and data. Choose main only if its whole change set is safe to ship. Otherwise branch from the verified compatible release tag. Peer-review the repair, run required checks and build a fresh digest. On that digest repeat the failure, adjacent routing, permissions and compatibility checks, obtain business acceptance and emergency production authorization, and verify the limited deployment. A documented exception can postpone the unaffected historical export test with a named owner and deadline. QA must pass it before the Service Owner expands exposure. Wider or unknown impact requires full applicable qualification. Reconcile affected requests and return a release-branch fix to main through review, or verify it is already there. INC-7 itself used a mapping correction on the same image. |
| 20. How do 40 decisions lead to the decision on CC-100? | outcome-analysis, population through worked failure; feedback-to-backlog, decision entry and proposed trial | Begin with all 100 distinct eligible exposed submissions, each observed for 1,440 minutes. Forty have a decision and 60 were open, so the fiftieth decision had not occurred by the cutoff. The one-day target was missed. The exact median and change from the two-day baseline remain unknown. There were 92 correct assignments at 3–19 minutes, none within two minutes, and eight with none recorded. The Product Owner keeps routing and records the missed objective on CC-100. The Service Owner investigates the late and missing assignments. The analyst prepares evidence for proposed child CC-140, whose testable hypothesis concerns supporting details. CC-123 stays Released. |

For Q20 I copied the Python directly from the generated outcome page and followed its link to the CSV. Its five output lines matched the displayed example, including EX-093 through EX-100, the 11-minute assignment milestone and the unreached decision milestone. A separate count from the file confirmed the assignment range and the 40/60 split. With a scratch copy changed to only 480 minutes of follow-up for one submission, the program stopped and requested reconciliation. The lesson distinguishes this immature observation from a request observed for the whole day and still open. Dropping the open requests or assigning each a 1,440-minute decision would both change the answer.

The proposed CC-140 trial gives its exposed and comparison groups the same enrollment and full follow-up rules. The Product Owner’s example rule for continuing requires at least half the exposed group to receive a decision by day one, a lower open share than the comparison group, and passing routing and access checks. No observed result is assigned to CC-140.

### Related Release and Learn questions

| Question | Built answer page | Reader’s answer |
|---|---|---|
| 14. Who moves CC-123? | flow-jira-status, seven-step table | 1 developer → In development, prior status unspecified; 2 developer → In review; 3 developer → Ready for QA; 4 QA lead → In QA; 5 business analyst → In UAT; 6 Release Manager → Ready for release; 7 Release Manager → Released after corrected smoke and observation. The failed attempt holds Ready for release. |
| 15. What does each version record mean? | versioning-and-fix-version | Jira fix version 1.3.0 groups planned delivery scope. Git tag v1.3.0 names the source commit. The GitHub release publishes notes and evidence against that tag. Runtime exposure comes from the deployment and observation records. |
| 16. Who authorizes production and where? | change-approval; hotfix-flow | The Release Manager checks the standard change and the designated change authority decides exceptional cases. The deployment job references the protected production environment, whose eligible reviewer and protection rules govern the gate. Business acceptance and the operator’s execution have different owners. |
| 17. What happens to a later routing-table edit? | config-change-qualification | Open a new change related to CC-123. Compare the actual baseline with the proposed version. The purchasing owner verifies the group and the QA lead exercises first assignment, neighboring unchanged routing and permitted/denied decisions on the accepted image. The authorized reviewer decides on the change and its reversal plan. The operator verifies the live setting and controlled request. The Service Owner accounts for already-routed work. |

## Twelve-item depth check

P means checked in the generated lesson. Columns follow section 5 of the depth plan in order. “Callouts” covers principle, tool behavior and team policy. “Sources” requires two or more publisher pages checked this session.

| Lesson | 1 Trigger, place, duration | 2 Inputs, rights | 3 Illustrative settings | 4 Output | 5 Rule, owner, effect | 6 First action | 7 Jira link, status | 8 Worked failure | 9 Two errors, effects | 10 Callouts | 11 Transfer | 12 Sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| instrumentation | P | P | P | P | P | P | P | P | P | P | P | P |
| alert-design | P | P | P | P | P | P | P | P | P | P | P | P |
| incident-lifecycle | P | P | P | P | P | P | P | P | P | P | P | P |
| hotfix-flow | P | P | P | P | P | P | P | P | P | P | P | P |
| outcome-analysis | P | P | P | P | P | P | P | P | P | P | P | P |
| feedback-to-backlog | P | P | P | P | P | P | P | P | P | P | P | P |

| Lesson | Evidence used to assess the matrix |
|---|---|
| instrumentation | The rehearsal gives the operator ten minutes to recover one request from restricted records. The sample settings and paired logs expose the actor, recipient, independent expectation, revision and configuration. A premature log can describe a write that never committed. Reading expected and actual from the active lookup can make a misroute agree with itself. |
| alert-design | The thirty-second verifier, two-minute persistence rule, three-minute missing-evidence rule, route excerpt and received message distinguish several clocks. The Service Owner accepts the safeguard after a ten-minute drill. Zero backlog could hide wrong recipients, and a successful scrape could conceal a stalled comparison. |
| incident-lifecycle | The first ten minutes of the rehearsal cover containment, the command handoff and a support update. The timeline and review distinguish fresh recovery from seven reassignments and one authorized decision retained. Reading the latest assignee would erase an earlier failure. Closing on an alert clear could strand work. |
| hotfix-flow | The fifteen-minute intake, candidate hold record, qualification table, figure and follow-up show both source choices. The defect workflow distinguishes failed and passed retests. An unsafe main can strand existing data during recovery, and reusing a previous green result can authorize an untested package. |
| outcome-analysis | A ten-minute local exercise combines population settings, real runnable Python and displayed output. Filtering to completed decisions discards the longest waits. Treating blanks as completed events manufactures a median. The Power Query alternative accepts typed tabular data and groups rows. Choosing the cohort, handling blanks and applying the decision rule still require the analyst and Product Owner. |
| feedback-to-backlog | A half-hour review uses an example field set, a concrete decision entry and a proposed acceptance/measurement contract. A form redesign based only on decided cases could miss an unserved queue. Reusing INC-7 for the eight later cases would attach unresolved work to a completed reconciliation. |

I independently opened the OpenTelemetry Signals and Logs Data Model pages, Prometheus alerting rules and Alertmanager configuration, Google SRE incident response and postmortems, Google SRE release engineering and Git cherry-pick, NIST on censored data and Microsoft Learn on Power Query Group By, and the GOV.UK discovery and performance-measurement guides. The full publisher URLs are in the lessons and the Learn source register. Power Query supports count rows and grouped aggregation. Applying its median operation directly to populated decision times would answer a different question.

## Findings and recheck

| Reader impact | Finding on first read | Result in the revised build |
|---|---|---|
| Moderate | In three lessons a reader could find the evidence but had to infer which Jira link to add. | Instrumentation names web links to the observation and deployment on CC-123. Alert design distinguishes a configured “relates to” work-item link from an external incident URL and adds the rollout web link. Hotfix names the new defect’s “relates to” link and the incident/change web links. |
| Moderate | “Eligible” in the outcome calculation was circular on direct entry. | The instructions now screen new purchases from in-scope units subject to automatic routing at submission. Readers verify eligibility and exposure against submission and deployment records before joining outcomes. CC-100 is introduced as the epic grouping work toward the objective. |
| Minor | The alert example sent the reader “below” for rules and a notification that appear earlier. | The positional instruction was removed. The worked example still distinguishes the observed controlled failure from the illustrative alert implementation. |

I visually inspected the revised hotfix figure. Both source choices lead through review and fresh qualification. A failed pilot holds expansion. The successful branch keeps the pilot limited until QA passes the deferred export test and the Service Owner checks the results. The accompanying text conveys the same decisions and owners.

All six overview “Go deeper” links, breadcrumbs, previous/next steps, action links, map regions, tour anchors and both download targets resolve in the built site. The incident page also reaches the production defect flow. Each page has a skip link, focusable content target and mobile contents link to its worked failure. Local Chromium could not start because the execution environment denied a socket. These local checks establish document structure and link destinations; interactive keyboard and viewport results belong to the hosted browser run.

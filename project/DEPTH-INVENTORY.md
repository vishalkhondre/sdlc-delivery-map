# Depth inventory for edition 1.1.0

**Gate 1 approved · Architect inventory · 21 November 2026**

The 53 overview pages remain the entry points for the map's 139 regions. This inventory adds 40 deep dives (6 Define, 12 Build, 9 Prove, 7 Release, 6 Learn) and six flows. The map still has seven numbered steps. A new reader can enter through an overview and its “Go deeper” list. A reader tracking a particular record can enter a flow from the index or a linked lesson. The proposed total is 99 pages of lesson content.

## How to read the inventory

Each row names a unique lesson ID, its existing parent, who needs the answer and who owns the decision or evidence in the fictional team. “Start” identifies prior knowledge or a record to open. “Next” identifies the recipient or next decision. “If” gives the failure route the author must demonstrate. The final column lists **primary-source research targets**, described by subject, pending verification. These links do not constitute claim checks. At authoring, open the relevant page, identify the product edition and configuration, capture its actual title, URL and access date, and tie the source to the precise claim. Substitute another relevant primary document if a target moves or fails to support the claim.

All records come from `content/dataset.json` and the two downloads under `site/assets/examples/`. Each deep dive must meet all twelve items in [the depth standard](DEPTH-PLAN.md#5-depth-standard-definition-of-done-for-a-deep-dive). Plan for four or more detail sections, a sample setting paired with observable output, a worked failure, exact blocking scope and actor, Jira status and link type, two mistakes and their consequences, and what transfers to another tool. Identify the trigger, location, duration, inputs and permissions. Separate principle, tool behavior and team policy with labelled callouts. Label each stack-dependent sample illustrative and explain it in plain language. The first two sections must work for a business analyst. A success state or Jira transition described below is a proposed teaching example subject to the shared record and the owner's decisions.

## Decide & Define · 6 deep dives

| ID · parent | Reader / accountable role | Subtopics and sample artifacts | Start, next and failure | Research targets |
|---|---|---|---|---|
| `jira-issue-types` · `tool-jira` | BA, developer / BA maintains the feature, Product Owner owns its objective | Distinguish epic, feature or story, task, sub-task and bug in the example hierarchy. Compare parent-child with linked work. Show CC-100 and CC-123 field tables with type, parent, component, labels, fix version and link purpose. | Start with the CC-100 objective. Give the linked feature to refinement. If a bug is attached only by label, replace the ambiguous association with the configured issue link. | [Jira work types][jt], [Jira issue links][jl] |
| `jira-workflow` · `tool-jira` | BA, QA lead / workflow owner maintains transitions, named actors move issues | Compare story and bug states, permitted transitions, actor, evidence and resolution. Show a status table alongside a transition diagram including reopen. State which moves are manual in this example. | Start with the two work types. Give the status vocabulary to the seven-step flow. If a reopened issue still has a completed resolution, check the transition and repair the record. | [Jira workflows][jw], [Jira resolutions][jr] |
| `refinement-ready` · `define` | BA, engineer / Product Owner decides readiness with the team | Split routing from reminders, capture eligible request type, dependencies, open assumptions and a brief sizing conversation. Show a CC-123 ready checklist with named owners. | Start with the observed wait on CC-100. Hand a bounded story to design and criteria. If no owner can supply the approver mapping, return the dependency to refinement. | [Scrum Guide on refinement][scrum], [GOV.UK discovery][disc] |
| `design-decision` · `phase-build` | BA, developer / technical lead with routing-rule owner | Compare synchronous and queued directory lookup, timing, idempotent retry and no-match behavior. Locate executable logic and editable mapping, including change permissions. Show a one-page decision record with alternatives, choice, owner and consequences. | Start with the eligible submission and directory dependency. Hand the selected contract to tests and configuration review. If lookup repeats or finds no match, specify the safe state and recovery owner. | [AWS architecture decision records][adr], [AWS on idempotent retries][retry] |
| `nonfunctional-criteria` · `criteria` | BA, QA / Product Owner agrees threshold with Service Owner | Define start event, correct recipient, inclusive two-minute deadline and eligible population for proposed AC-03. Add one paragraph on authorization, auditable decisions and accessible approver controls. Show a threshold proposal and boundary observations. | Start with AC-01/02 and the timing evidence. Hand AC-03 to case design. An assignment at 120 seconds passes; the first correct assignment at 121 seconds misses the inclusive deadline. Distinguish the corrected 24-request pilot from the later cohort. | [GOV.UK performance metrics][metrics], [W3C accessibility criteria][wcag] |
| `criteria-to-tests` · `criteria` | BA, QA engineer / QA lead maintains traceability | Given-When-Then for AC-01 automatic recipient and AC-02 authorized decision, including denial and unchanged pending state. Show criterion → case → run/result table with actor, candidate and configuration. Identify any absent evidence explicitly. | Start with the signed criteria. Give trace rows to QA and UAT. If the tester assigns the approver manually, reject the AC-01 result and rerun from a fresh submission. | [Cucumber Gherkin reference][gherkin], [Kiwi Test Plans][kiwi-plans] |

## Build · 12 deep dives

The pilot uses the six rows marked **pilot**. The other six belong to the later Build section. CI observes a proposed revision. Merge policy decides whether those observations are sufficient. The build published for qualification has its own identity.

| ID · parent | Reader / accountable role | Subtopics and sample artifacts | Start, next and failure | Research targets |
|---|---|---|---|---|
| `local-dev-loop` · `branch` | Developer / change author | Run tests and lint before push, install and invoke a pre-commit hook, inspect local tool versions and staged files. Show hook configuration and matching local output. Explain differences in runner, clean checkout, environment and selected tests. | Start with feature branch and declared dependencies. Push a passing local change for CI. If only the laptop passes, compare the runner's revision and invocation before editing the test. | [pre-commit configuration][hooks], [pytest invocation][pytest] |
| `branch-commit-conventions` · `branch` | Developer, BA / change author | Show a CC-123 branch, an example commit message and a PR reference. Describe the linked development panel and its integration prerequisites. Distinguish a Jira key from a revision identifier. | Start with the feature key. Give the branch and source history to the reviewer. If the work is absent in Jira, check the key and integration, then verify the actual link. | [Jira development data][jdev], [GitHub flow][ghflow] |
| `code-review-practice` · `pull-request` | Developer, reviewer / peer reviewer | Review scope, diff size, rule behavior, tests and ownership. Contrast comment, approve and request changes, designated code owners and stale approvals after a push. Show a PR-42 description and a reviewer/author thread on the manually assigned fixture. | Start with CC-123 and AC-01/02. Return the corrected diff for review and merge checks. If the test bypasses routing, request changes and verify a fresh approval where policy requires it. | [GitHub PR reviews][reviews], [GitHub code owners][owners], [protected branches][protect] |
| `ci-pipeline-anatomy` · `ci` **pilot** | BA, developer / CI maintainer | Diagram trigger → jobs → steps on runners, dependencies, parallel jobs, cache versus retained artifact and tested PR revision. Show annotated workflow, pipeline figure and PR checks list naming required and informational results. | Start with PR-42. Send named check results to merge policy. If a required job is missing or evaluated another revision, inspect its event, checkout and run before allowing merge. | [GitHub workflow syntax][wf], [GitHub checks and branch protection][protect] |
| `ci-unit-tests` · `ci` **pilot** | Developer, QA / change author | Define the unit and the boundary replaced by a test double. Show two illustrative arrange/act/assert tests for routing and permission denial, a failing report with expected/actual and the file to inspect. Address flaky results and misleading manual fixtures. | Start with AC-01/02 and a PR check. Open the failed job and test, correct the behavior or assertion, rerun on the PR. If reruns disagree, preserve the evidence and investigate nondeterminism. | [pytest assertions][assert], [pytest flaky tests][flaky], [Python test doubles][mock] |
| `ci-lint-format` · `ci` **pilot** | Developer / change author, with CI maintainer for rule scope | Compare a linter warning, a formatter change and a type error. Show rule configuration and annotated findings with file, line, rule and exit behavior. Which fixes can be automatic? Which job warns or blocks? | Start with the failing check. Inspect the diff and rule scope. For a finding in an untouched file, reproduce at the tested revision, agree scoped repair or tracked cleanup with its owner, then meet the configured merge rule. | [Ruff linter][ruff], [Ruff formatter][format], [mypy checks][mypy] |
| `ci-coverage` · `ci` **pilot** | Developer, reviewer / CI maintainer owns configured gate | Measure line and branch execution, distinguish overall from new-code denominator. Show coverage summary plus threshold setting for the component actually enforcing it. Trace 31 of 50 new-code lines (62%) vs 80% to a required result. Show how a manual assignment and weak assertion can still cover the lines. | Start with the test run and base revision. Give merge rules the measured result. If below threshold, inspect missing branches and add behavior-sensitive tests. If 100% with a weak oracle, repair the test anyway. | [coverage.py branch measurement][cov], [coverage.py configuration][covconf], [SonarQube gate conditions][sonargate] |
| `ci-static-analysis` · `ci` **pilot** | Developer, reviewer / quality gate owner | Trace scanner step → issues → new-code conditions → quality gate → reported PR check and required rule. Verify issue types, severity model and edition-specific PR decoration. Show scanner configuration, failing and passing gate results and the authorized false-positive disposition. | Start with PR analysis and its baseline. Send result for the exact PR revision to merge policy. If a new bug-type issue fails the gate, investigate the finding, fix or record a justified false positive, rerun and retain the trail. | [SonarQube quality gates][sonargate], [SonarQube PR analysis][sonarpr], [SonarQube issue handling][sonarissues], [GitHub required checks][protect] |
| `ci-security-checks` · `ci` **pilot** | Developer, security reviewer / designated security triager | Separate dependency, secret and static security findings by input, signal and scope. Show a synthetic dependency alert, policy outcome and Jira triage note with affected version, exposure, owner and retest. | Start with PR dependency change. Pass required checks to merge or assign informational findings by policy. If a dependency blocks, assess reachability, update or mitigate under recorded authority, rescan and link the result. | [GitHub dependency review][deps], [secret scanning][secrets], [code scanning][scan] |
| `ci-integration-tests` · `ci` | Developer, QA / change author | Exercise a real boundary on a CI runner using a service container, isolated fixtures and reset state. Explain startup/IO cost and location in the pipeline. Show the test submitting an eligible request, then reading the assignment record, actor and recipient. | Start with unit-tested routing. Hand the result to merge checks. If persistence or lookup differs, inspect service readiness, fixture and stored record before deciding whether code or environment failed. | [GitHub service containers][services], [pytest fixtures][fixtures] |
| `merge-rules` · `merge` | Developer, reviewer / repository rules owner | Show a main-branch rule table for reviews, required checks, up-to-date branch or merge queue and enforcement. Compare squash, rebase and merge commit by the resulting commit identity. | Start with approved PR and current results. Give the integrated commit to the candidate build. If base advances or approval becomes stale, re-evaluate under the selected rule before merging. | [GitHub protected branches][protect], [merge queues][queue], [merge methods][methods] |
| `image-build` · `build` | Developer, platform engineer / build maintainer | Dockerfile inputs, stages, tag and immutable digest, platform, image scan, SBOM and build attestation. Show build/publish job plus push output and the recorded digest of build-418. | Start with integrated commit. Supply the recorded artifact to QA by digest. If the pulled platform or digest differs from the record, hold promotion and reconcile the manifest and build output. | [Dockerfile reference][dockerfile], [Docker image digests][digest], [Docker build attestations][attest] |

## Prove · 9 deep dives

| ID · parent | Reader / accountable role | Subtopics and sample artifacts | Start, next and failure | Research targets |
|---|---|---|---|---|
| `test-management-structure` · `tool-test` | BA, QA engineer / QA lead | Show a Kiwi Test Plan containing cases, a Test Run for a build, and the TestExecution for each case exercised in that run. Group cases by criterion as a team convention. Distinguish manual observations from imported automation results. Show the CC-123 plan, case IDs, and an execution linked to a Jira defect. | Start with CC-123 and criteria. Pass stable case IDs to test design and execution. If a case exists without a run for the selected candidate, mark evidence missing. | [Kiwi Test Plans][kiwi-plans], [Kiwi Test Runs][kiwi-runs], [Jira issue links][jl] |
| `test-case-design` · `qa-tests` | QA engineer, BA / QA lead | Show TC-01 through TC-06 as six rows with criterion, precondition, role, data, steps, expected observation and relevant boundaries. Include equivalence classes for mapping, AC-02 denied decisions and AC-03 timing. | Start with criteria and the cases selected from the Kiwi Test Plan. Give executable cases to QA. If a requester denial leaves the state changed or an approver was set by hand, record failure or invalid setup as applicable. | [ISTQB test design syllabus][ctfl], [Kiwi Test Cases][kiwi-cases] |
| `test-data-identities` · `qa-tests` | QA engineer / QA fixture owner | Matrix of synthetic requester, designated approver, unauthorized user and fixture administrator. Identify setup rights, expected action, forbidden action and reset state. Check the actor that assigned the request. | Start with cases and environment. Give clean role-specific fixtures to execution. If a bypass account supplies assignment or decision, invalidate the result and rerun as the representative identity. | [NIST role-based access control][rbac], [Kiwi Test Cases][kiwi-cases] |
| `qa-test-types` · `qa-tests` | Developer, QA lead / QA lead chooses coverage | Run schedule table for smoke, functional, regression, exploratory and automated end-to-end tests. Include trigger, environment, scope, duration and what each result establishes. | Start with a digest, mapping and fixtures. Hand candidate-specific observations to the QA decision. If smoke passes but the wrong unit receives work, hold and run the functional and affected regression cases. | [ISTQB testing syllabus][ctfl], [Kiwi Test Runs][kiwi-runs] |
| `defect-report` · `hold` | QA engineer, developer / QA reporter with triage owners | Full fictional BUG CC-131 with steps, expected/actual, environment, configuration, digest, evidence, affected criterion, link to CC-123 and each issue's current status. Compare severity (impact) and priority (ordering), decision makers and duplicate linkage. | Start at the failed TC-04 execution in qa-196. Show its defect URL pointing to CC-131 and inspect the evidence in Jira. Triage separately links CC-131 to CC-123 in Jira. Hand the report to triage and put delivery on hold. If the report lacks candidate identity, recover the QA run before assigning a fix. | [Kiwi Jira reporting][kiwi-jira], [Kiwi execution links][kiwi-links], [ISTQB defect reporting][ctfl], [Jira issue links][jl], [Jira priorities][priority] |
| `defect-lifecycle` · `hold` | QA lead, Product Owner, developer / triage lead | Show bug state diagram New through Closed and a triage table for acceptance, duplicate, deferred, cannot reproduce and reopen. Identify who assesses severity, sets priority, supplies a candidate and verifies closure. | Start with CC-131 and the linked feature. QA records a new execution in qa-198 and attaches the existing CC-131 URL. Show when Kiwi can add a comment to Jira. The triage owner changes Jira status after reviewing the retest and preserves qa-196 on close or reopen. | [Jira workflows][jw], [Jira resolutions][jr], [Kiwi tracker comments][kiwi-comments], [ISTQB defect management][ctfl] |
| `regression-scope` · `hold` | QA lead, release manager / QA lead | Decision figure for code change vs mapping edit, affected boundary, retained historical evidence, confirmation test, adjacent regression and entry back to UAT. Include a new observation after QA pass but before UAT decision. | Start with failure, digest and config. Give QA's explicit rerun scope and results to the signatory. A code change needs a new digest. For uat-80, correct the mapping on the same digest, link qa-209 and obtain a new decision. | [ISTQB confirmation/regression testing][ctfl], [Kiwi Test Runs][kiwi-runs], [safe deployment guidance][safe] |
| `uat-planning` · `uat-runtime` | BA, business representative / designated business signatory | Show a UAT plan and uat-82 sign-off record. Cover real workflow, representative participants, entry/exit criteria, configuration, observed recipient, acceptance scope and signatory. | Start with the identified QA-qualified candidate. Give signed acceptance to release policy. On uat-80 rejection, hold, investigate the mapping, requalify, then repeat the business scenario. | [ISTQB acceptance testing definition][ctaccept], [Kiwi Test Runs][kiwi-runs] |
| `config-change-qualification` · `policy` | Rule maintainer, QA, release manager / configuration owner | Show a post-release change request for prod-routing-12 with mapping diff, requester, authorized reviewer, affected units/roles, tests, sign-off, implementation and reversal. Keep it distinct from prod-routing-11 in the accepted chain. | Start with the live mapping and change request. Hand a reviewed and tested config to rollout and smoke. If a different group is selected, halt and restore the known mapping, then recheck affected requests. | [Azure safe deployment guidance][safe], [GitHub deployment environments][env] |

## Release · 7 deep dives

| ID · parent | Reader / accountable role | Subtopics and sample artifacts | Start, next and failure | Research targets |
|---|---|---|---|---|
| `versioning-and-fix-version` · `release-plan` | BA, developer, release coordinator / release manager | Map CC-123's Jira fix version, v1.3.0 Git tag and GitHub release to purpose, owner, commit and evidence. Separate planning/publication, deployment and user availability. Describe version-number conventions and their assumptions. | Start with qualified build and intended scope. Hand the mapping to publication. If the tag identifies another commit, pause publication and resolve the candidate discrepancy. | [Jira versions][versions], [Git tags][tag], [GitHub releases][ghrelease], [SemVer specification][semver] |
| `change-approval` · `policy` | Release manager, operator / production change authority | Compare standard versus normal change and emergency exception, separation of duties and enforcement at the environment. Show policy table plus approval record stating actor, decision, digest, configuration review and conditions. | Start with candidate QA and business decision. Give authorization for that digest to the deployment job. If evidence is missing or approver is ineligible, hold or follow the recorded authorized exception path. | [GitHub deployment environments][env], [Azure safe deployment guidance][safe] |
| `deploy-workflow-anatomy` · `rollout` | Platform engineer, release manager / deployment maintainer | Annotate job trigger, environment gate, scoped secrets or federated cloud login, deploy by digest, await readiness and inspect running revision/config. Pair the illustrative job with a deployment record showing what actually ran. | Start with approved digest. Hand observed revision to smoke and monitoring. If readiness fails or runtime digest differs, halt expansion and enter recovery. | [GitHub Azure OIDC][oidc], [Azure revisions][revisions], [GitHub deployment environments][env] |
| `rollout-strategies` · `rollout` | Product Owner, operator / service owner | Compare single revision, traffic split and feature flag in a table with deployment, eligible exposure, observation, reversibility and cost. Explain the choice for a small service and who can widen exposure. | Start with authorized candidate and recovery plan. Give the selected exposure group to observation. If wrong recipients appear in the pilot, stop expansion and isolate exposure. | [Azure traffic splitting][traffic], [Google SRE canarying][canary], [Azure feature flags][flags] |
| `rollback-rollforward` · `recover` | On-call operator / Service Owner owns recovery | Decision table for restoring a revision, reverting config, disabling a flag or rolling forward. Inspect data compatibility and affected requests. Show a recovery record with before/after revisions, config, digest, smoke and reconciliation. | Start with observed harm and actual state. Hand a verified healthy state to incident review. If the older version cannot read new data, pick a compatible mitigation or forward fix and verify recovery. | [Azure revisions][revisions], [Azure safe deployment guidance][safe], [Google SRE incident response][incident] |
| `data-change-coordination` · `release-plan` | Developer, data owner / migration owner | Worked expand-and-contract sequence for a routing field. Show schema/revision compatibility matrix including existing open requests, backfill verification, cutover and retirement of the old representation. | Start with existing readers, writers and open work. Give a compatibility decision to rollout/recovery. If an old revision cannot serve existing records, hold contraction and retain the compatible representation. | [AWS deployment rollback safety][compat], [PostgreSQL schema changes][alter] |
| `release-notes-practice` · `notes` | Release writer, BA / release manager | Trace merged PRs and issue keys into reader-facing v1.3.0 draft notes. Identify audience, eligible request type, availability or exposure status, known limits and evidence links. | Start with release scope and known rollout state. Give verified wording to users/support. If publication precedes exposure, correct any claim that all users can already use routing. | [GitHub generated release notes][ghnotes], [GitHub releases][ghrelease] |

## Learn · 6 deep dives

| ID · parent | Reader / accountable role | Subtopics and sample artifacts | Start, next and failure | Research targets |
|---|---|---|---|---|
| `instrumentation` · `observe` | Engineer, operator / service instrumentation owner | Distinguish logs, metrics and traces. Show assignment event schema and synthetic log lines with request correlation, expected/actual role, assignment actor, time, revision and config. Describe low-cardinality aggregate signals and how to find one request's trace. | Start with deployment record and rule contract. Give comparable events to alerts and cohort analysis. If wrong assignments look successful, add or reconcile the independent expected-recipient signal. | [OpenTelemetry signals][signals], [OpenTelemetry log data model][logs] |
| `alert-design` · `alert` | On-call operator / Service Owner sets response policy | Show alert rule and notification with threshold, window, severity, route, quiet hours and missing-data handling. Compare late/missing assignment with wrong-but-assigned recipient mismatch using an independent expected mapping or controlled check. | Start with identifiable assignment observations. Page or queue the assigned responder under policy. If the backlog stays empty during misrouting, open the mismatch signal and inspect a correlated request. | [Prometheus alert rules][prom], [Google SRE monitoring][monitor] |
| `incident-lifecycle` · `incident` | Service team, Product Owner / incident commander and Service Owner | INC-7 timeline and review document. Name declaration, containment, communications, verification, reconciliation and follow-up Jira owners. Track eight affected pilot requests, seven reassigned and one authorized decision retained. | Start with the failed controlled observation on prod-r41. Give restored service and reconciled requests to review. If new requests recover but old ones remain misassigned, keep reconciliation open. | [Google SRE incident response][incident], [Google SRE postmortems][post] |
| `hotfix-flow` · `recover` | On-call developer, release manager / emergency change authority | Hotfix path figure from released tag or suitable main, expedited peer review, permitted reduced vs full qualification, fresh digest, approval, rollout and back-merge. Show a **hypothetical code defect** distinct from the configuration repair in INC-7. | Start with the production version and severity decision. Hand fresh qualification and authorization to deployment, then reconcile history. If main has unrelated unsafe changes, choose a compatible release base and propagate the fix back. | [Google SRE release engineering][engineering], [GitHub protected branches][protect], [Azure safe deployment guidance][safe] |
| `outcome-analysis` · `measure` | BA, Product Owner / Product Owner owns interpretation | Work from the CSV: eligibility and exposure, one full day per submission, blanks, event timing, denominator and incomplete follow-up. Show 40/100 decided, 60 open, 92 correct assignments (3–19 minutes), eight without a recorded correct assignment. Show why the one-day decision median was not reached. | Start with the separate 100-submission cohort. Give CC-100 the missed target and limitations. If an analysis drops open records or assigns them a decision time, recompute using every eligible submission. | [GOV.UK performance metrics][metrics], [NIST censored observations][censor] |
| `feedback-to-backlog` · `feedback` | BA, Product Owner / Product Owner | Show the proposed CC-140 story linked to CC-100 with observation, hypothesis, criterion, measure, cohort and review owner. Distinguish investigation of handoff/decision delay from Service Owner reconciliation of the eight later requests without correct assignment. | Start with the missed one-day target and user feedback. Send the bounded follow-up to refinement. If the evidence cannot locate the delay, collect missing observations before choosing a feature. | [GOV.UK discovery][disc], [GOV.UK performance metrics][metrics], [Jira issue links][jl] |

### Evidence to show in the QA defect flow

QA starts at the failed execution of TC-04 in run qa-196. The failure belongs to this execution against build-422. Check the configured Jira project, issue type and permissions before filing.

| Situation | Kiwi record | Jira record |
|---|---|---|
| New defect, Jira API creation succeeds | Reporting from the execution stores the new Jira issue URL as a defect reference on that execution. | The generated description includes the originating execution URL. QA supplies the actual observation. Triage links CC-131 to feature CC-123 as a separate Jira action. |
| CC-131 already exists | Add its issue URL to the execution as a defect. Record a separate execution on retest and retain the original failure. | If the reporter selects **Add comment to Issue tracker** and the configured adapter has permission, Kiwi can append the run URL and execution identifier as a comment. Verify that comment when the handoff requires it. |
| Jira reporting opens a prefilled form | After submission, confirm that the execution contains the resulting issue URL. Add it manually if missing. | Verify creation, project, issue type and originating evidence before triage. |

Draw the execution-to-issue reference separately from the optional comment in the other direction. Show the issue-to-feature link and the triage owner's close or reopen decision separately. A passing execution supplies retest evidence. This example assumes no automatic status synchronization. [Issue-tracker integration][kiwi-trackers] · [Jira adapter][kiwi-jira] · [Execution links][kiwi-links] · [Report and comment content][kiwi-comments]

**What transfers.** With another tool such as PractiTest, preserve the case, execution, candidate, defect and retest identities. Verify that tool's link and write-back behavior before illustrating it.

## Six flows · no parent

The `touches` column is the proposed list of lesson IDs for the flow record. All are existing overview IDs, so the flow is navigable in its own section before the remaining sections ship. The short paths and swimlanes below will use the team policy vocabulary agreed in `jira-workflow`.

| Flow ID · record | Reader / accountable role | Touches | Handoffs, sample artifact and failure branch | Research targets |
|---|---|---|---|---|
| `flow-jira-status` · CC-123 | BA, learner following a feature / BA maintains the linked story, each transition has a named actor | `branch`, `pull-request`, `build`, `qa-tests`, `uat-decision`, `release`, `rollout`, `tool-jira` | Start with a ready feature. Build a status-by-step table for the **seven numbered map headers**: 1 commit a change, 2 check the feature PR, 3 merge and build, 4 verify in QA, 5 business acceptance, 6 publish GitHub release, 7 deploy to Prod. Give status before/after, actor, evidence and authority. Show where status stays put, who most recently moved it and why a rejection holds or returns the story. End with deployment evidence linked to CC-123. | [Jira workflows][jw], [Jira development data][jdev] |
| `flow-bug-ci` · red check | Developer, reviewer / PR author | `branch`, `pull-request`, `ci`, `merge` | Short path figure: open failed check on the proposed revision → inspect output → fix and push on the same PR → examine new run → resume review. Show retained failed run alongside the passing run and linked PR on CC-123. In this example no separate Jira bug is created for a pre-merge fix. Persistently red stays blocked. | [GitHub workflow syntax][wf], [GitHub protected branches][protect] |
| `flow-bug-qa` · BUG CC-131 | QA engineer, developer / QA lead releases the hold after retest | `qa-tests`, `hold`, `branch`, `pull-request`, `merge`, `build`, `digest`, `qa-revision`, `uat-promotion`, `tool-jira`, `tool-test` | Swimlane from TC-04 failing in qa-196 on build-422 → execution stores the Jira CC-131 URL → triage links CC-131 to CC-123 in Jira → hold → PR-47 → maintenance build-423, new digest → qa-198 confirmation and regression → closure. Show the optional Jira confirmation comment, new Kiwi retest execution, and human close or reopen decision. Integrated PR-42/build-418 comes later and gets its own qa-204. Compare dates and workflow names across the independent build sequences. | [Kiwi Jira reporting][kiwi-jira], [Kiwi execution links][kiwi-links], [ISTQB confirmation and defect management][ctfl], [Jira issue links][jl], [Docker digests][digest] |
| `flow-bug-uat` · uat-80 | QA lead, business representative / business signatory owns the new decision | `qa-tests`, `uat-runtime`, `uat-decision`, `hold`, `build`, `digest`, `validation-summary` | Decision figure from uat-80 rejection to cause analysis. Actual route: UAT mapping correction, same image, affected QA checks in qa-209, repeat scenario in uat-r9, new uat-82 acceptance. Alternative code fault: new build/digest, QA and UAT on that candidate. Preserve the rejected record if either path fails. | [ISTQB acceptance terminology][ctaccept], [Kiwi Test Runs][kiwi-runs], [Azure revisions][revisions] |
| `flow-bug-prod` · INC-7 | On-call responder, release manager / Service Owner | `smoke`, `alert`, `incident`, `recover`, `policy`, `rollout`, `deployment-record`, `tool-jira` | Swimlane from wrong recipient on prod-r41 through declaration and exposure halt. Show incident-to-defect/change linkage, decision between a config repair and a code hotfix, the actual config repair, smoke on prod-r42, reconciliation of seven reassignments and one retained authorized decision, and incident review. If reconciliation fails, retain ownership. The code branch is an alternative scenario. | [Google SRE incident response][incident], [Google SRE postmortems][post], [Azure safe deployments][safe] |
| `flow-traceability` · accepted digest | BA, release reviewer / release manager for authorization, operator for observed state | `pull-request`, `merge`, `build`, `digest`, `qa-tests`, `uat-decision`, `policy`, `rollout`, `deployment-record`, `smoke`, `evidence-record` | Evidence-chain figure: PR-42/integrated commit → build-418 → published digest → qa-204 and qa-209 → uat-82 after uat-80 → authorized digest → actual prod-r42/config → smoke. Mark the two questions “May we deploy?” and “What ran?” Trace both ways and hold on digest mismatch. The same digest can produce different recipients under different configuration. | [Docker digests][digest], [GitHub deployment environments][env], [Azure revisions][revisions] |

## Six additions to existing overview pages

| Overview ID | Planned figure or table | What a reader must be able to recover from it |
|---|---|---|
| `evidence-record` | Reuse the evidence-chain figure from `flow-traceability`. | Trace actual digest to integrated commit and differentiate an authorization record from an observation of a running revision. |
| `hold` | Reuse the requalification decision from `regression-scope`. | Follow code and config fixes to their appropriate QA rerun and fresh UAT decision. |
| `measure` | Horizontal bars on one common 0–100 scale with a 50% reference. Label submitted 100, correctly assigned by one day 92, decided 40, open 60. | Read each count against the same 100 submissions. Assigned overlaps decided and open. Only decided plus open partitions the cohort. |
| `handoffs` | Legend figure with labels and arrow styles from the approved map. | Distinguish solid navy next step, solid teal cross-lane handoff, dashed red failure/recovery and dashed gray evidence link, including through text alone. |
| `policy` | Table with a row each for QA result, business acceptance and production authorization. | For each row identify the question, decision owner and record, including the distinct signatory and change authority. |
| `environments` | Dev, QA, UAT and Prod table. | Read purpose, decision and evidence for each environment. Connect QA and UAT records to their candidate and config, and Prod to its actual revision. |

Commit authored SVGs with their source and meaningful alt text, caption and a complete text equivalent. Use HTML tables with column headers for tabular additions. Retain all existing map destinations, image and IDs under the proposed default.

## Delivery order and dependency checks

| Gate or section | Authoring order | Evidence required to leave the section |
|---|---|---|
| Gate 1 | Owner approved the inventory and all four decisions. | Agreed scope and stack; no deep dives are authored at this gate. Bring the owner-merged 1.0.2 corrections forward before pilot authoring. |
| Gate 2 · model and CI pilot | `ci-pipeline-anatomy` → `ci-unit-tests` → `ci-lint-format` → `ci-coverage` → `ci-static-analysis` → `ci-security-checks`. | First learner journey: enter through `ci`, open the red unit check, locate the failing assertion on PR-42, repair the bypassing fixture, read new-code coverage, identify blocking vs informational results and the actor who can move the PR forward. Return through the parent. Exercise the five pilot probes, keyboard/small-screen route and all seven Build questions. |
| Gate 3 · Define | Issue types → workflow → ready feature → design decision → nonfunctional criteria → criteria to tests. | The reader can connect CC-100 to a bounded CC-123 story and distinguish proposed AC-03 from recorded qa-204 evidence. |
| Gate 3 · remaining Build | `local-dev-loop`, `branch-commit-conventions`, `code-review-practice`, `ci-integration-tests`, `merge-rules`, `image-build`. | From branch and proposed revision, locate a reviewed integrated commit and the artifact QA actually receives. |
| Gate 3 · Prove | Test management → case design → identities → test types → defect report → lifecycle → regression scope → UAT planning → config-change qualification. | Demonstrate the pre-release code fix and same-digest UAT mapping fix as separate paths. Validate Q8–13 against built pages. |
| Gate 3 · Flows | Jira status → CI failure → QA defect → UAT rejection → production incident → digest trace. | Trace one record through each lane and check both directions of the accepted evidence chain. Use existing Release/Learn overview destinations until their child pages ship. |
| Gate 3 · Release | Versioning → change approval → deploy workflow → rollout strategies → rollback/rollforward → data coordination → release notes. | Verify candidate, authorization, running identity, exposure and availability wording against the release records. |
| Gate 3 · Learn | Instrumentation → alert design → incident lifecycle → hotfix → outcome analysis → backlog. | Recover the wrong-recipient signal, reconcile INC-7, reproduce counts from the separate later CSV and link the proposed CC-140 follow-up to CC-100. |
| Gate 3 · overview figures | Evidence chain, requalification, cohort, handoffs, policy and environments. | Compare each visual with its text equivalent and source, then follow the parent page on a small screen. |
| Integration and release | Integrate index, tour, cross-links and PDF after section acceptance. Release candidate and binding follow the separate Gate 4 approval. | Check all 20 learner questions, all 14 probes and retained correction checks on the built site. |

At the model change, update the four numbered-file readers together (`site/generate.py`, `scripts/validate.py`, `scripts/check_browser.py`, `scripts/field_guide_pdf.py`). Plan `07-deep-build.json` for Define and Build, `08-deep-prove.json` for Prove, `09-deep-release.json` for Release and Learn, and `10-flows.json` for flows. Exclude `dataset.json` and `hotspots.json` from lesson loading. Retain all ten mandatory baseline fields, assign every deep dive one overview parent, and render its breadcrumb, “Go deeper” links, detail headings, searchable text and tour entry under the model/integration work specified in the plan.

### Intentional overlap

- The Jira workflow deep dive defines the example statuses and permitted transitions. The Jira flow applies those statuses to one story across all seven map steps. The bug lifecycle page owns triage, resolution and reopening for the linked defect.
- Case design defines TC-01–TC-06. The traceability page connects criteria to results. Test management explains where those records live. Preserve the same six IDs, including TC-05 at 120 seconds and TC-06 at 121 seconds, and the same manual-assignment trap from `criteria` to `smoke`.
- CI explains results at a PR revision. Merge rules names the repository policy owner and enforcement. The accepted build page identifies the artifact; the digest flow reuses that identity and the overview evidence diagram. A coverage collector's overall percentage cannot stand in for the example's new-code gate.
- `hold` owns the common failure destination on the map. The regression page owns the decision figure. The QA and UAT flows follow the distinct evidence for code and configuration changes.
- `incident-lifecycle` owns INC-7 and the eight pilot reconciliations. `outcome-analysis` owns the later 100-submission denominator. The corrected pilot counts 24 eligible requests plus two excluded smoke submissions. The separate later cohort has eight requests without a correct assignment by 24 hours. `feedback-to-backlog` owns the product decision and proposed follow-up.

## Learner acceptance and search

These are intended answer pages for [the 20 acceptance questions](DEPTH-PLAN.md#10-acceptance-questions). At each later gate an independent editorial reviewer must open the built page, find an explicit answer and record the actual page. An inventory row is a planned check, never a passing review.

| Q | Reader task | Planned answer page |
|---|---|---|
| 1 | Locate a red unit test, read the failing assertion and identify who fixes it. | `ci-unit-tests` |
| 2 | Resolve a lint failure in an untouched file. | `ci-lint-format` |
| 3 | Explain who set the 80% new-code policy and whether 62% blocks. | `ci-coverage` |
| 4 | Explain why 100% execution with direct assignment fails to test automatic routing. | `ci-coverage`, with the corrected fixture in `ci-unit-tests` |
| 5 | Find the failing SonarQube gate on the PR and the recorded false-positive disposition. | `ci-static-analysis` |
| 6 | Triage a vulnerable library and record the blocking decision in Jira. | `ci-security-checks` |
| 7 | Identify required and informational checks on the PR. | `ci-pipeline-anatomy` (pilot); later `merge-rules` adds repository settings |
| 8 | Find AC-01 cases and candidate-specific result for each criterion, identifying any gap. | `test-management-structure`, `criteria-to-tests` |
| 9 | File the QA bug, link the feature and explain each issue's status. | `defect-report` |
| 10 | Identify impact and priority decision makers. | `defect-lifecycle` |
| 11 | Identify the rerun scope, digest and disposition of the earlier pass. | `regression-scope` |
| 12 | Handle a defect discovered between a QA pass and the UAT decision. | `regression-scope` |
| 13 | Trace the UAT config correction and compare the code-defect route. | `regression-scope`, then `flow-bug-uat` |
| 14 | Read CC-123 status, actor and evidence at all seven numbered map steps. | `flow-jira-status` |
| 15 | Locate the Jira fix version, Git tag and GitHub release and explain each. | `versioning-and-fix-version` |
| 16 | Identify who can authorize Prod and where the rule is enforced. | `change-approval` |
| 17 | Route a future production mapping edit for review and qualification. | `config-change-qualification` |
| 18 | Detect a wrong recipient with no unassigned backlog. | `alert-design` |
| 19 | Choose the hotfix route and explain permitted qualification reductions. | `hotfix-flow` |
| 20 | Reproduce the 40/100 result and trace the new decision to CC-100. | `outcome-analysis`, `feedback-to-backlog` |

| Stage | Queries and observable result |
|---|---|
| Every stage after corrections | Preserve “rollback” → `recover`, “median” → `measure`, and correction search coverage for “feature flag” and “security”. Confirm the named target appears where specified. |
| Six-lesson CI pilot | Each returns at least one relevant topic: **unit test**, **lint**, **coverage**, **SonarQube**, **quality gate**. Exercise the index as a reader and follow the result to its detail. |
| Integration | Retain the five pilot probes and add **bug**, **severity**, **regression**, **test case**, **Jira status**, **hotfix**, **rollback**, **feature flag**, **median**. All 14 must return a topic. Test the 20 questions separately; a search hit alone cannot pass a question. |

## Approved owner decisions

| Decision | Approved choice |
|---|---|
| 1. Which technology stack should the code, test and configuration samples use? | A Python service with pytest, Ruff and coverage.py. Label each stack-dependent sample illustrative. |
| 2. Test management example (settled) | The owner selected **Kiwi TCMS**. Keep “Test Management Tool” on the map. |
| 3. Which static analysis product should the authors research and illustrate? | SonarQube for quality gates, new-code conditions and PR analysis. Declare the cited edition and check every product claim against its documentation. |
| 4. Should edition 1.1.0 revise the approved map image? | Keep the existing map. Reach deep dives from the overview parent, topic index and tour. Consider proposed map changes separately for 1.2.0. |

### Source handoff

The labels in the inventory identify research topics, not quotations of source titles. The following SonarSource pages were opened on **21 November 2026** to locate potential pilot evidence in the same Server 2025.1 LTA documentation set: [Quality gates][sonargate], [Introduction (Pull request analysis)][sonarpr] and [Editing issues][sonarissues]. Confirm the chosen product edition, operating mode, feature availability, repository enforcement and example policy together before authoring. The Kiwi sources below were also opened and checked on 21 November 2026. Other links remain research targets for their authoring passes.

[jt]: https://support.atlassian.com/jira-cloud-administration/docs/what-are-issue-types/
[jl]: https://support.atlassian.com/jira-software-cloud/docs/link-issues/
[jw]: https://support.atlassian.com/jira-software-cloud/docs/what-are-jira-workflows/
[jr]: https://support.atlassian.com/jira-cloud-administration/docs/what-are-issue-statuses-priorities-and-resolutions/
[scrum]: https://scrumguides.org/scrum-guide.html
[disc]: https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works
[adr]: https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/welcome.html
[retry]: https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/
[metrics]: https://www.gov.uk/service-manual/measuring-success/how-to-set-performance-metrics-for-your-service
[wcag]: https://www.w3.org/TR/WCAG22/
[gherkin]: https://cucumber.io/docs/gherkin/reference
[hooks]: https://pre-commit.com/#pre-commit-configyaml---top-level
[pytest]: https://docs.pytest.org/en/stable/how-to/usage.html
[jdev]: https://support.atlassian.com/jira-cloud-administration/docs/what-development-data-can-i-view-in-jira-software/
[ghflow]: https://docs.github.com/en/get-started/using-github/github-flow
[reviews]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews
[owners]: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
[protect]: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
[wf]: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
[assert]: https://docs.pytest.org/en/stable/how-to/assert.html
[flaky]: https://docs.pytest.org/en/stable/explanation/flaky.html
[mock]: https://docs.python.org/3/library/unittest.mock.html
[ruff]: https://docs.astral.sh/ruff/linter/
[format]: https://docs.astral.sh/ruff/formatter/
[mypy]: https://mypy.readthedocs.io/en/stable/getting_started.html
[cov]: https://coverage.readthedocs.io/en/latest/branch.html
[covconf]: https://coverage.readthedocs.io/en/latest/config.html
[sonargate]: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/analysis-functions/quality-gates
[sonarpr]: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/pull-request-analysis/introduction
[sonarissues]: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/issues/managing
[deps]: https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review
[secrets]: https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning
[scan]: https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning
[services]: https://docs.github.com/en/actions/use-cases-and-examples/using-containerized-services/about-service-containers
[fixtures]: https://docs.pytest.org/en/stable/how-to/fixtures.html
[queue]: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue
[methods]: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github
[dockerfile]: https://docs.docker.com/reference/dockerfile/
[digest]: https://docs.docker.com/dhi/explore/security-concepts/digests/
[attest]: https://docs.docker.com/build/metadata/attestations/
[ctfl]: https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf
[rbac]: https://csrc.nist.gov/projects/role-based-access-control
[priority]: https://support.atlassian.com/jira-cloud-administration/docs/manage-priorities/
[safe]: https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments
[ctaccept]: https://glossary.istqb.org/en_US/term/acceptance-testing/1
[env]: https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments
[versions]: https://support.atlassian.com/jira-cloud-administration/docs/manage-versions/
[tag]: https://git-scm.com/book/en/v2/Git-Basics-Tagging
[ghrelease]: https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
[semver]: https://semver.org/spec/v2.0.0.html
[oidc]: https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-azure
[revisions]: https://learn.microsoft.com/en-us/azure/container-apps/revisions
[traffic]: https://learn.microsoft.com/en-us/azure/container-apps/traffic-splitting
[canary]: https://sre.google/workbook/canarying-releases/
[flags]: https://learn.microsoft.com/en-us/azure/azure-app-configuration/concept-feature-management
[incident]: https://sre.google/workbook/incident-response/
[compat]: https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments/
[alter]: https://www.postgresql.org/docs/current/ddl-alter.html
[ghnotes]: https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes
[signals]: https://opentelemetry.io/docs/concepts/signals/
[logs]: https://opentelemetry.io/docs/specs/otel/logs/data-model/
[prom]: https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/
[monitor]: https://sre.google/sre-book/monitoring-distributed-systems/
[post]: https://sre.google/sre-book/postmortem-culture/
[engineering]: https://sre.google/sre-book/release-engineering/
[censor]: https://www.itl.nist.gov/div898/handbook/apr/section2/apr215.htm

[kiwi-plans]: https://kiwitcms.readthedocs.io/en/stable/guide/testplan.html
[kiwi-cases]: https://kiwitcms.readthedocs.io/en/stable/guide/testcase.html
[kiwi-runs]: https://kiwitcms.readthedocs.io/en/stable/guide/testrun.html
[kiwi-trackers]: https://kiwitcms.readthedocs.io/en/stable/modules/tcms.issuetracker.html
[kiwi-jira]: https://kiwitcms.readthedocs.io/en/stable/_modules/tcms/issuetracker/types.html#JIRA
[kiwi-links]: https://kiwitcms.readthedocs.io/en/stable/_modules/tcms/rpc/api/testexecution.html#add_link
[kiwi-comments]: https://kiwitcms.readthedocs.io/en/stable/_modules/tcms/issuetracker/base.html#IssueTrackerType.add_testexecution_to_issue

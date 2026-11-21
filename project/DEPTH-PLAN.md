# SDLC Delivery Map: depth edition (1.1.0) plan and execution guide

**For:** the AI maintainer (ChatGPT) working in `vishalkhondre/sdlc-delivery-map`
**Owner:** Vishal Khondre
**Baseline:** commit `c8993e1`, edition 1.0.1 (53 lessons, 139 map regions, one diagram)
**Suggested location in the repo:** `project/DEPTH-PLAN.md`

---

## 0. How the owner uses this file

1. Commit this file to the repository as `project/DEPTH-PLAN.md` (or attach it to the ChatGPT session together with the repository).
2. Paste the **kickoff prompt** from section 13 into ChatGPT.
3. ChatGPT works phase by phase and **stops at every gate** in section 9. At each gate you reply with one of the gate prompts in section 13.
4. You make the four owner decisions in section 2 at Gate 1. Defaults are given, so "use the defaults" is a valid answer.

Everything below is addressed to the maintainer.

---

## 1. Why this edition exists

Edition 1.0.1 explains decisions, handoffs and evidence well. It does not explain what actually happens inside each step. Across all 53 lessons the words "unit test", "lint", "SonarQube", "static analysis" and "quality gate" never appear. Jira workflow statuses, the defect lifecycle and test-management structure are barely touched.

Three things in the repository caused this. You must change all three.

| Cause in edition 1 | Where | Change for this edition |
|---|---|---|
| The diagram was the table of contents, so each box got exactly one lesson. | `project/APPROACH.md` | The diagram stays the table of contents for the **overview** layer. A new **deep-dive** layer hangs under it. Scope for the deep-dive layer comes from the inventory in section 6, not from the diagram. |
| The lesson template is ten short fields. Median lesson is about 290 words. | `templates/pages/lesson.md`, `site/generate.py` | Extend the content model with a `detail` section that holds sub-sections, tables, code samples and figures (section 4). |
| The owner reviewed once, at the very end. | `CLAUDE.md`, `project/GROUND-RULES.md` rule 6, `section-pipeline` skill | Replace with the gates in section 9. The owner approves the inventory before authoring and reviews a pilot section before the rest is written. |

### Goal

A learner who reads a deep dive can answer: what runs, where it runs, what the configuration looks like, what the output looks like, what makes it pass or fail, who acts on a failure, and what gets recorded in Jira.

### What must not change

- The existing 53 lesson IDs and URLs. Other pages and the map link to them.
- The fictional approval-routing feature (CC-100, CC-123, AC-01, AC-02) and the existing record IDs (PR-42, build-418, qa-204, uat-80, uat-82, prod-r41, prod-r42, INC-7).
- The "manual assignment" thread that runs through `criteria`, `pull-request`, `qa-tests`, `uat-decision` and `smoke`.
- The cohort treatment in `measure` (40 of 100, open requests stay in the cohort).
- The habit of marking team policy as policy ("in this example").
- The map image and its 139 regions, unless Gate 1 approves a map revision.

### Non-goals

- A product manual for any tool. Teach the mechanism with one concrete example, then say what transfers.
- Agile ceremonies, estimation and capacity planning beyond the short treatment in D-02.
- Real company data, real ticket links or internal names. Ground rule 1 still applies.

---

## 2. Owner decisions needed at Gate 1

Present these four questions with the defaults. Do not start authoring until they are answered.

| # | Decision | Default if the owner says "use the defaults" |
|---|---|---|
| 1 | Technology stack for code, test and config samples | Python service: pytest, Ruff, coverage.py. State on every sample that the stack is illustrative. |
| 2 | Test management tool used in examples | Keep the map's generic "Test Management Tool". Use Azure Test Plans as the named example, since edition 1 already cites it. |
| 3 | Static analysis product | SonarQube, described at the level of quality gate, new-code conditions and pull request analysis. Verify every product claim against the vendor documentation for the edition you cite. |
| 4 | Map revision | No change to the image in 1.1.0. Deep dives are reached from their parent lesson, the topic index and the tour. Propose map changes separately for 1.2.0. |

---

## 3. Phase 0 corrections carried over from the independent review

These are defects in edition 1.0.1. Fix them first, in their own pull request, before any new content.

| # | Defect | Fix | Check |
|---|---|---|---|
| C1 | `qualification-record.json` cites an "agreed two-minute routing window". In `one-day-cohort.csv`, correct assignment takes 3 to 19 minutes and EX-093 to EX-100 are never assigned. `feedback` says assignment "now happens promptly". | Make the window and the CSV agree. Explain the eight unassigned requests in `evidence-record` (what they are, who owns them). | Minimum, maximum and blank count in the CSV each match a sentence in the lesson. |
| C2 | Topic search indexes only title, summary, evidence, owner and map labels. "rollback", "median", "feature flag" and "security" return 0 topics. | Add steps, example, failure and measure text to each row's `data-text` in `topic_index()`. | "rollback" returns Recover service. "median" returns Measure the outcome. |
| C3 | The home title "From Feature Commit to Production" understates the scope. | Retitle the home H1 and page title (for example "From business problem to production outcome"). The map banner may stay. | Title and H1 match the intro sentence. |
| C4 | "ISTQB · Acceptance testing and business rules" (9 lessons) links to a certification overview that defines none of the terms it is cited for. | Replace with an ISTQB glossary or syllabus page that contains the definition. Use each source's real title. | Open the link and find the cited definition on the page. |
| C5 | The site shows no edition or commit. | Print edition and short commit in the footer. | Visible on every page. |
| C6 | "Return to the map" lands on the step header, not the card. `service-retirement` is linked from nowhere but the index. The index filter is labelled "Phase" with six values while the map has three bands. | Use the card region as the return target. Link retirement from `feedback`. Rename the filter "Section". | Click through on the built site. |

---

## 4. Content model and site changes

### 4.1 Two layers

| Layer | `kind` | Purpose | Count |
|---|---|---|---|
| Overview | `overview` (default when the key is absent) | One per map box. Decision, handoff, evidence. The 53 existing lessons. | 53 |
| Deep dive | `deep-dive` | What happens inside one step, with samples. | about 45 |
| Flow | `flow` | One artifact followed across steps (a bug, a Jira issue, a test case). | 6 |

### 4.2 Schema additions

Keep all ten existing fields mandatory on every lesson, so the validator and release tooling keep working. Add these optional keys:

```json
{
  "id": "ci-unit-tests",
  "kind": "deep-dive",
  "parent": "ci",
  "audience": ["Developer", "QA Engineer"],
  "detail": [
    {
      "id": "what-runs",
      "title": "What runs",
      "blocks": [
        {"type": "text", "value": "..."},
        {"type": "list", "ordered": true, "items": ["...", "..."]},
        {"type": "table", "caption": "...", "columns": ["...", "..."], "rows": [["...", "..."]]},
        {"type": "code", "language": "yaml", "caption": "...", "value": "..."},
        {"type": "figure", "src": "assets/figures/ci-pipeline.svg", "alt": "...", "caption": "...", "text_equivalent": "..."},
        {"type": "callout", "label": "Team policy", "value": "..."}
      ]
    }
  ]
}
```

Rules:

- `parent` must be an existing lesson ID. A deep dive's parent is an overview lesson. A flow has no parent and lists `touches: [lesson ids]`.
- `callout.label` is one of `Principle`, `Tool behavior`, `Team policy`, `Common mistake`.
- Every `figure` has `alt` and a `text_equivalent` that carries the same information in prose or a list.
- Every `code` block names its language and is labelled illustrative when it depends on the stack decision.
- Put new lessons in new files (`content/07-deep-build.json`, `08-deep-prove.json`, `09-deep-release.json`, `10-flows.json`). `load()` reads `content/0*.json`, so widen the glob and keep ordering explicit.

### 4.3 Generator changes (`site/generate.py`)

1. Render `detail` after "How it works" on deep-dive and flow pages: sub-headings, tables, `<pre><code>`, figures with captions, callouts.
2. On every overview page with children, add a **"Go deeper"** section listing its deep dives. On every deep dive, add a breadcrumb back to the parent.
3. Add `Deep dive` and `Flow` to the index groups. Keep the existing six.
4. Add the on-page table of contents entries for `detail` sub-sections.
5. Extend `TOUR` so each stop lists its deep dives under a "Go deeper" line.
6. Keep the generator standard-library only. Figures are committed SVG files in `site/assets/figures/`, each with its source (`.mmd` or the script that drew it) beside it. Do not add a client-side diagram library.

### 4.4 Validator changes (`scripts/validate.py`)

Add checks that fail the build when:

- a `parent` or `touches` ID does not exist;
- a deep dive has fewer than four `detail` sections, or lacks at least one `code` or `table` block and one worked failure;
- a figure file is missing, or lacks `alt` or `text_equivalent`;
- a deep dive's sources are fewer than two, or any is not HTTPS;
- an overview lesson with children is missing its "Go deeper" links in the built page;
- any search probe in section 10 returns zero results.

### 4.5 Agent and rule updates

Update these files in the same pull request as the schema change:

| File | Change |
|---|---|
| `project/APPROACH.md` | Describe the two layers and the gates. Remove "one owner review at the end". |
| `project/GROUND-RULES.md` rule 6 | Replace with: the owner approves the depth inventory and reviews the pilot section and each later section summary. |
| `CLAUDE.md` | Same change to the delegation paragraph. Point to this plan. |
| `templates/pages/lesson.md` | Add the `detail` keys and the depth standard from section 5. |
| `.claude/skills/architect/SKILL.md` | Output is a depth inventory with sub-topics and sample artifacts per lesson, not only topic IDs. |
| `.claude/skills/author/SKILL.md` | Add the depth standard and the block types. |
| `.claude/skills/external-researcher/SKILL.md` | Every tool-behavior claim needs a primary source checked in this session, with the date. |
| `.claude/skills/accuracy-reviewer/SKILL.md` | Check every sample: would this configuration and this output plausibly occur together? Check numbers across records. |
| `.claude/skills/editorial-reviewer/SKILL.md` | Run the acceptance questions in section 10 as a learner. |
| `.claude/skills/diagrammer/SKILL.md` | Add figure authoring: SVG, source file, alt text, text equivalent. |
| `.claude/skills/section-pipeline/SKILL.md` | Add the gates and the per-section report. |

---

## 5. Depth standard: definition of done for a deep dive

A deep dive is done only when it contains all of the following. The author checks this list; the editorial reviewer checks it again.

1. **What runs and when.** The trigger, the place it runs (laptop, CI runner, QA environment), and how long it normally takes.
2. **What it needs.** Inputs, configuration and permissions.
3. **A sample configuration.** A short, realistic file or setting (workflow step, test, rule, Jira field set). Labelled illustrative.
4. **A sample output.** What the person actually sees: a failing test report, a coverage summary, a quality gate result, a bug ticket, a test run.
5. **The pass or fail rule.** The exact condition, who set it, and whether it blocks the merge, the promotion or nothing.
6. **Who acts on a failure**, and what they do first.
7. **What is recorded in Jira** and which status changes, with the link type.
8. **A worked failure** using the fictional feature and the shared dataset in section 7.
9. **At least two common mistakes**, each with the consequence.
10. **Labels** for principle, tool behavior and team policy, as callouts.
11. **What transfers** to a different tool, in two or three sentences.
12. **Two or more primary sources**, opened and checked in this session.

Length follows from the list. Expect 700 to 1,500 words plus samples. Do not pad to reach a number and do not cut a required item to stay short.

---

## 6. Depth inventory

IDs are proposals. The architect confirms them at Gate 1. "Samples" names the artifacts the lesson must show.

### 6.1 Decide & Define

| ID | Parent | Must cover | Samples |
|---|---|---|---|
| `jira-issue-types` | `tool-jira` | Epic, feature or story, task, sub-task, bug. Parent and child links. Which fields matter for delivery (fix version, component, labels, links). | CC-100 and CC-123 field tables |
| `jira-workflow` | `tool-jira` | Statuses and transitions for a story and for a bug. Who moves each one. What evidence each transition needs. Status versus resolution. | Status table, transition diagram |
| `refinement-ready` | `define` | From request to a ready story: splitting, a definition of ready, sizing in brief, dependencies. | Ready checklist for CC-123 |
| `design-decision` | `phase-build` | Synchronous versus queued routing lookup. Idempotent retries. No-match handling. Where rules live (code or configuration) and who may change them. Recording the decision. | One-page decision record |
| `nonfunctional-criteria` | `criteria` | Turning "prompt assignment" into a measurable criterion (the routing time window). Authorization, audit trail, accessibility of the approver view in one paragraph. | AC-03 proposal with a threshold |
| `criteria-to-tests` | `criteria` | Traceability from AC to test cases to runs. Given-When-Then examples for AC-01 and AC-02, including the negative case. | Traceability table |

### 6.2 Build (Dev)

| ID | Parent | Must cover | Samples |
|---|---|---|---|
| `local-dev-loop` | `branch` | Running tests and linters before pushing. Pre-commit hooks. Why local green is not CI green. | Hook config, local run output |
| `branch-commit-conventions` | `branch` | Branch naming with the Jira key. Commit messages. How the key links commits, branches and PRs to the issue. | Example branch, commit, linked dev panel description |
| `code-review-practice` | `pull-request` | What a reviewer checks. Review states (comment, approve, request changes). Code owners. Stale approvals after a push. Review size. | PR description for PR-42, review comment thread |
| `ci-pipeline-anatomy` | `ci` | Workflow file, triggers, jobs, steps, runners, caching, artifacts. Which revision is tested. Required versus optional checks. Order and parallelism. | Annotated workflow file, checks list on a PR, pipeline figure |
| `ci-unit-tests` | `ci` | What a unit test is and is not. Arrange, act, assert. Tests for the routing rule and the permission check. Test doubles. Reading a failure. Flaky tests. | Two tests, a failing report |
| `ci-lint-format` | `ci` | Linter versus formatter versus type checker. What each catches. Rule configuration. Auto-fix. Failing the job versus warning. | Rule config, annotated lint output |
| `ci-coverage` | `ci` | Line and branch coverage. How it is measured. Overall versus new-code thresholds. What coverage cannot tell you (the manual-assignment test that asserts the wrong thing can still be covered). | Coverage summary, threshold config |
| `ci-static-analysis` | `ci` | SonarQube analysis in CI. Issue types and severities. Quality gate and new-code conditions. Pull request decoration. Making the gate a required check. False positives and how they are recorded. | Scanner step, quality gate result (failed and passed) |
| `ci-security-checks` | `ci` | Dependency scanning, secret scanning, static security testing. What blocks and what is triaged. Handling a vulnerable dependency. | Alert example, triage note in Jira |
| `ci-integration-tests` | `ci` | Tests that cross a boundary (database, directory lookup). Service containers. Test data. Why they are slower and where they run. | Integration test that submits a request and reads the assignment record |
| `merge-rules` | `merge` | Branch protection or rulesets. Required reviews and checks. Up-to-date requirement and merge queue. Squash, rebase, merge commit and what each does to commit identity. | Rule table for `main` |
| `image-build` | `build` | Dockerfile basics. Tags versus digest. Image scan. SBOM and build attestation in brief. Publishing and recording the digest. | Build job, push output with digest |

### 6.3 Prove (QA and UAT)

| ID | Parent | Must cover | Samples |
|---|---|---|---|
| `test-management-structure` | `tool-test` | Test plan, suite, case, run, result. Requirement-based suites. Manual versus automated results. Linking to Jira. | Plan and suite layout for CC-123 |
| `test-case-design` | `qa-tests` | Writing a case: preconditions, data, steps, expected result. Equivalence classes and boundaries for routing rules. Negative cases for AC-02. | TC-01 to TC-06 in a table |
| `test-data-identities` | `qa-tests` | Test accounts and roles. Synthetic data. Resetting state. Why a bypassing test account proves nothing. | Identity matrix |
| `qa-test-types` | `qa-tests` | Smoke, functional, regression, exploratory and automated end-to-end. When each runs and what it can conclude. | Run schedule table |
| `defect-report` | `hold` | A good bug report: steps, expected, actual, environment, digest, evidence. Severity versus priority. Duplicate handling. | BUG CC-131 in full |
| `defect-lifecycle` | `hold` | Bug statuses from New to Closed. Triage. Reopen. Cannot reproduce. Deferred. Who decides each. | Status diagram, triage table |
| `regression-scope` | `hold` | Choosing what to rerun after a fix. Code fix versus configuration fix. When an earlier QA pass no longer counts. | Requalification decision figure |
| `uat-planning` | `uat-runtime` | Scenarios, participants, entry and exit criteria, sign-off record. What a signatory is accepting. | UAT plan, sign-off record uat-82 |
| `config-change-qualification` | `policy` | The routing rule is configuration. How a mapping edit after release is requested, reviewed, tested and recorded. | Change request for `prod-routing-12` |

### 6.4 Release

| ID | Parent | Must cover | Samples |
|---|---|---|---|
| `versioning-and-fix-version` | `release-plan` | Version numbers. Jira fix version. Git tag. GitHub release. How the three stay in step. The three meanings of "release". | Mapping table for v1.3.0 |
| `change-approval` | `policy` | Standard versus normal change. Environment protection rules and required reviewers. Separation of duties. Emergency path. | Policy table, approval record |
| `deploy-workflow-anatomy` | `rollout` | The deployment job: environment, secrets, cloud login, deploy by digest, wait for readiness, record the revision. | Annotated deploy workflow |
| `rollout-strategies` | `rollout` | Single revision, traffic split, feature flag. Exposure versus deployment. Choosing one for a small service. | Comparison table |
| `rollback-rollforward` | `recover` | Restoring a revision, restoring configuration, disabling a flag, rolling forward. Data compatibility. Decision criteria. | Decision table, recovery record |
| `data-change-coordination` | `release-plan` | Schema changes that must work with the old and new version. Existing open requests. Order of operations. | Expand-and-contract example |
| `release-notes-practice` | `notes` | From merged PRs to reader-facing notes. Audience. Availability wording. | Draft notes for v1.3.0 |

### 6.5 Learn (operate and improve)

| ID | Parent | Must cover | Samples |
|---|---|---|---|
| `instrumentation` | `observe` | Logs, metrics and traces for this feature. The assignment event and its fields. Correlating a request to a revision. | Event schema, sample log lines |
| `alert-design` | `alert` | From symptom to alert rule: threshold, window, severity, routing, quiet hours, missing data. Wrong-but-assigned requests and how they are detected. | Alert rule, notification text |
| `incident-lifecycle` | `incident` | Declare, mitigate, communicate, reconcile, review. Roles. Timeline. Review document and follow-up actions in Jira. | INC-7 timeline and review |
| `hotfix-flow` | `recover` | A production defect that needs a code change: branch from the released tag or from main, expedited review, full or reduced qualification, back-merge. | Hotfix path figure |
| `outcome-analysis` | `measure` | Building the cohort from submissions. The query logic in words. Reading the CSV. Median with incomplete follow-up. | Worked calculation from the CSV |
| `feedback-to-backlog` | `feedback` | Turning the outcome decision into new work with its own criterion and measure. | New story linked to CC-100 |

### 6.6 Flows (cross-cutting)

| ID | Follows | Must cover | Figure |
|---|---|---|---|
| `flow-jira-status` | CC-123 | The issue's status at every map step, who moved it, and the evidence attached at that point. | Status-by-step table aligned to the seven map steps |
| `flow-bug-ci` | A failing check | Found in CI: no Jira bug, fix on the same PR, failed run stays in history. | Short path |
| `flow-bug-qa` | BUG CC-131 | Found in QA: bug raised, linked to CC-123, hold, fix branch, PR, new digest, retest, regression, close. | Swimlane |
| `flow-bug-uat` | uat-80 | Found in UAT: rejection, cause analysis, configuration fix or code fix, requalification, new decision. | Decision figure |
| `flow-bug-prod` | INC-7 | Found in Prod: incident, mitigation, bug, hotfix or configuration change, reconciliation, review. | Swimlane |
| `flow-traceability` | One digest | Commit to build to digest to QA to UAT to authorization to revision to smoke. Records that permit deployment versus records that prove what ran. | Evidence-chain figure |

### 6.7 Figures to add to existing overview lessons

| Page | Figure |
|---|---|
| `evidence-record` | Evidence chain (same figure as `flow-traceability`) |
| `hold` | Requalification decision |
| `measure` | Cohort bar: 100 submitted, assigned, decided, open, with the 50 percent line |
| `handoffs` | The four arrow styles from the map legend |
| `policy` | Table: QA result, business acceptance, production authorization (question, owner, record) |
| `environments` | Table: purpose, decision and evidence for Dev, QA, UAT, Prod |

---

## 7. Shared fictional dataset

All samples must agree with each other and with the two existing downloads. Maintain one file, `content/dataset.json`, and reference it from the accuracy review. Extend it; do not contradict it.

| Record | Existing or new | Notes |
|---|---|---|
| CC-100, CC-123, AC-01, AC-02 | Existing | Do not rename. |
| AC-03 | New | Routing time window. Must match the CSV after correction C1. |
| PR-42, commit `3ab862b…`, build-418, digest `sha256:041f…` | Existing | The accepted candidate. |
| qa-204, qa-209, uat-80 (rejected), uat-82 (accepted) | Existing | The UAT rejection was a configuration fault with the same image. |
| TC-01 to TC-06 | New | Map each to AC-01, AC-02 or AC-03. |
| BUG CC-131, PR-47, build-423 | New | A QA-found code defect on an earlier candidate, so the code-fix path has its own worked example. It must predate build-418 and must not alter the existing accepted chain. |
| v1.3.0, prod-r41 (halted), prod-r42, INC-7 | Existing | Eight requests reconciled: seven reassigned, one decision retained. |
| `one-day-cohort.csv` | Existing | 100 rows, 40 decided, 60 open, 92 assigned. |

---

## 8. How to run the agent roles

The files in `.claude/agents/` and `.claude/skills/` are Claude Code definitions. They do not run by themselves in ChatGPT. Use them as role briefs and follow this procedure.

1. **One role per pass.** For each section, run the roles in this order: architect, source researcher, external researcher, author, diagrammer, site builder, then the three reviewers.
2. **Read the role's `SKILL.md` at the start of the pass** and state which role you are in.
3. **Write a handoff file at the end of each pass** to `project/handoffs/<section>/<nn>-<role>.md` with: what you produced, evidence, open questions, and what the next role needs. The next role reads only the handoff files and the repository, not your earlier reasoning.
4. **Reviewers start cold.** If your runtime can start a separate agent or a fresh context, use one for each reviewer and give it only the built pages, the sources and the rubric. If it cannot, run the review as a separate pass and record in the review file that author and reviewer were the same session. The repository rule stands: a review record must describe the review that actually occurred.
5. **The author fixes findings; the reviewer rechecks.** Record both.
6. **Never bind a review you did not perform.** Run `python scripts/check_release.py bind` only after Gate 4.

If you have a shell and write access (Codex or agent mode), run the commands yourself. If you only have chat, produce complete file contents or patches and list the commands for the owner to run, then wait for the output.

---

## 9. Phases and gates

Work on a branch per phase. Open a pull request per phase. Do not push to `main` and do not deploy. Stop at each gate and post the report in section 11.

| Phase | Work | Output | Gate |
|---|---|---|---|
| 0. Orient | Read `README.md`, `CLAUDE.md`, `project/*`, this plan, all lessons, both downloads. Run the checks in the README. Change nothing. | Baseline report: counts, check results, anything in this plan that conflicts with the repository. | **Gate 0:** owner confirms the baseline. |
| 1. Corrections | Section 3, C1 to C6. | PR "Edition 1.0.2 corrections". | Owner merges. No separate gate. |
| 2. Inventory | Architect pass over section 6. Confirm IDs, parents, order, sub-topics, samples, sources to check. Extend the dataset. | `project/DEPTH-INVENTORY.md`, `content/dataset.json`, the four owner questions. | **Gate 1:** owner approves the inventory and answers section 2. |
| 3. Model and pilot | Section 4 changes. Then author the CI section only: `ci-pipeline-anatomy`, `ci-unit-tests`, `ci-lint-format`, `ci-coverage`, `ci-static-analysis`, `ci-security-checks`. Full pipeline and reviews. | PR "Deep-dive model and CI pilot", with a built preview or screenshots. | **Gate 2:** owner reads the pilot and says deeper, shallower or right. Adjust the depth standard before continuing. |
| 4. Sections | In this order: Define (6.1), rest of Build (6.2), Prove (6.3), Flows (6.6), Release (6.4), Learn (6.5), Figures (6.7). One PR per section. | Section PR plus the gate report. | **Gate 3 (repeats):** owner replies "continue" or lists changes. |
| 5. Integration | Tour "Go deeper" lines, index groups, search probes, cross-links, small-screen and keyboard check, PDF field guide. | PR "Edition 1.1.0 integration". | None. |
| 6. Release | Three reviews of the whole edition, `content/reviews/1.1.0.md`, `content/VERSION`, `CHANGELOG.md`, `release/sections.yml`. | Release candidate PR. | **Gate 4:** owner approves. Then bind and tag. |

Checks to run before every pull request, from the repository root:

```sh
python scripts/validate.py source
python site/generate.py
python scripts/validate.py links
python -m unittest discover -s scripts/tests -v
python scripts/check_browser.py
```

---

## 10. Acceptance questions

The editorial reviewer answers each question using only the built site, and records the page where the answer was found. A question that needs inference is a finding.

**Build**

1. A pull request shows a red check named "unit tests". Where do I look, what does a failure look like, and who fixes it?
2. The linter fails on a file I did not write. What do I do?
3. Coverage on new code is 62 percent against an 80 percent threshold. Does the merge block? Who set the threshold?
4. A test covers the routing code but sets the approver directly. Coverage is 100 percent. What is wrong, and which lesson explains it?
5. The SonarQube quality gate fails on a new bug-type issue. Where is it shown on the pull request, and how is a false positive recorded?
6. A dependency scan reports a vulnerable library. What blocks, what is triaged, and what goes into Jira?
7. Which CI results are required for merge and which are informational?

**Prove**

8. Where do test cases for AC-01 live, and how do I show that every criterion has a passing run on this candidate?
9. QA finds a defect. What goes in the bug, how is it linked to CC-123, and what status does each issue have?
10. Who decides severity and who decides priority?
11. The fix is merged. Which tests are rerun, on which digest, and what happens to the earlier QA pass?
12. A defect is found after QA passed but before the UAT decision. What is held and what is recorded?
13. UAT rejects because of a mapping error. How is that different from a code defect?

**Release and learn**

14. What is CC-123's Jira status at each of the seven map steps, and who moved it?
15. What is the difference between the Jira fix version, the Git tag and the GitHub release?
16. Who can approve a production deployment, and where is that enforced?
17. Someone edits the production routing table next week. What review and test does that change get?
18. Production assigns a request to the wrong approver. Which signal detects it if no request is left unassigned?
19. A production defect needs a code change today. What is the hotfix path and what qualification can be reduced?
20. The CSV shows 40 of 100 decided. Walk me from the file to the product decision on CC-100.

**Search probes** (each must return at least one topic): unit test, lint, coverage, SonarQube, quality gate, bug, severity, regression, test case, Jira status, hotfix, rollback, feature flag, median.

---

## 11. Gate report format

Post this at every gate, in this order, and nothing else.

1. **Phase and status.** One line.
2. **What changed.** Files and lesson IDs, with the pull request link.
3. **Check results.** The command output summary lines. Failures stated plainly.
4. **Depth standard.** A table: lesson ID against the twelve items in section 5, with any gap named.
5. **Acceptance questions answered so far.** Number and page.
6. **Reviews.** Who reviewed, in what context, findings, and what was fixed.
7. **Sources checked this phase.** Title, URL, date opened.
8. **Open decisions for the owner.** Each as a question with your recommendation.
9. **What I could not verify.**

---

## 12. Rules that apply throughout

- **Stop at gates.** Do not continue past a gate without the owner's reply.
- **Verify tool behavior against primary documentation in this session.** Do not write a product claim from memory. If you cannot open a source, say so in the report and mark the claim.
- **Do not invent a source title.** Use the page's own title.
- **Keep samples consistent.** Every ID, number and timestamp comes from `content/dataset.json`.
- **Mark the stack.** Every stack-dependent sample says it is illustrative.
- **Keep overview lessons short.** Move detail into deep dives; do not grow the 53 existing lessons beyond a "Go deeper" section and the figures in 6.7.
- **Write for the mixed audience.** A business analyst should be able to read the first two sections of any deep dive. Code samples need a one-sentence plain-language explanation.
- **Keep the site accessible.** Tables have headers. Figures have alt text and a text equivalent. New pages work by keyboard and at 390px width.
- **Stay public.** No internal links, customer data or company detail.
- **No direct pushes to `main`, no tags and no deployment** until Gate 4.
- **Report failure honestly.** A failing check or a skipped review is stated in the gate report, not worked around.

---

## 13. Prompts for the owner to paste

**Kickoff**

```text
You are the maintainer of the repository vishalkhondre/sdlc-delivery-map.
Read project/DEPTH-PLAN.md in full, then README.md, CLAUDE.md and everything in project/.
Follow the plan exactly. Where the plan conflicts with CLAUDE.md, GROUND-RULES.md or
APPROACH.md, the plan wins, and section 4.5 tells you to update those files.

Start Phase 0 only. Change no files. Run the checks listed in section 9 and post the
gate report in the format of section 11. Then stop and wait for my reply.

Tell me at the start whether you can run shell commands and open pull requests in this
session, and whether you can start separate agents or fresh contexts for the reviewers.
```

**Gate 0 reply**

```text
Baseline confirmed. Do Phase 1 (corrections C1 to C6) as one pull request, then Phase 2.
Stop at Gate 1 with the inventory and the four owner questions.
```

**Gate 1 reply**

```text
Inventory approved with these changes: <list or "none">.
Decisions: stack = <...>, test tool = <...>, static analysis = <...>, map revision = <...>.
(Or: use the defaults.)
Do Phase 3: the content model and the CI pilot only. Stop at Gate 2.
```

**Gate 2 reply**

```text
Pilot depth is <right / too shallow / too detailed>. Specific changes: <list>.
Update the depth standard in the template if needed, fix the pilot, then start Phase 4
with the Define section. Stop after each section with the gate report.
```

**Gate 3 reply (each section)**

```text
Continue with the next section.
(Or: before continuing, change <list>.)
```

**Gate 4 reply**

```text
Approved. Bind the review, update the version and changelog, and open the release pull
request. Do not merge or tag; I will do that.
```

## Amendments after Gate 0

Owner decisions of 21 November 2026 take precedence over the earlier instructions.

- Start from a clean clone of main at c8993e1. The workflow-only PR to main precedes the corrections. It runs the release-binding check for PRs to main and for Pages deployment. Source, unit, generation, link and browser checks remain required on every PR. Link each PR's successful GitHub Actions browser run at its gate.
- Phase 1 ships C1–C6 as edition 1.0.2 under the existing publication rules. Bump the edition and changelog, perform all three independent reviews, record them, then bind. Open the PR to main for the owner to merge. This is the only exception to the pre-Gate-4 publication restriction.
- From Phase 2, target edition/1.1.0 until Gate 4. The owner handles main merges. Bring the owner-merged corrections forward before pilot authoring.
- C1. Preserve the 24 eligible requests in the corrected pilot and the later 100-submission outcome cohort. The pilot met its two-minute window. The later 92 correct assignments took 3 to 19 minutes, so none met that window. The other eight rows show no correct assignment by 24 hours. The Service Owner investigates and reconciles them. They are separate from the eight pilot requests reconciled in INC-7. Correct the “now happens promptly” assertion in feedback.
- C4. Fix all nine ISTQB citations, including both original link labels.
- C6. For retirement add the contextual link from feedback. Other existing routes already reach retirement. Retain the card-return and Section-filter corrections.
- Section 4.2. Update the four numbered lesson readers together: site/generate.py, scripts/validate.py, scripts/check_browser.py and scripts/field_guide_pdf.py. Exclude dataset.json and hotspots.json from lesson discovery.
- Sections 4.4 and 10. At the six-lesson CI pilot, require unit test, lint, coverage, SonarQube and quality gate. At integration require all fourteen probes, adding bug, severity, regression, test case, Jira status, hotfix, rollback, feature flag and median. Preserve the established correction search checks throughout.
- The inventory contains 40 deep dives and six cross-cutting flows, in addition to the existing 53 overviews. The four technology and map decisions remain open until Gate 1.

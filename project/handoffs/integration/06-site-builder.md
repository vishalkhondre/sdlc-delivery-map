# Section 6.7 and Phase 5 site integration

From the merged Learn base I generated the site, validated the lesson structure and complete local link graph, and ran the unit suite. The build contains 53 overviews, 40 deep dives and six flows, with 139 map regions and four navigation pages. All 11 unit tests passed. A regression case now rejects duplicate and unrelated links inside a parent’s Go deeper section.

| Discovery path | Check and result |
|---|---|
| Go deeper on overviews | The validator compares each overview’s rendered card links to the lesson records. Every one of the 23 parents links to exactly its children. |
| Guided tour | All 40 distinct deep dives appear under Go deeper, including Build lessons reached through their map parents. Five dives are also useful links at the reliability stop. The Flows list contains all six flows in reading order. |
| Topic index | The Deep dive and Flow sections contain exactly the 40 and six expected records. The hosted browser suite selects each Section filter and compares the visible links with those records. |
| Six overview additions | The four figure routes render their intended source, alt text and text disclosure. The policy and environments routes render captioned four-column tables with three and four data rows respectively. Each reference section has a mobile Contents link. |
| Search | The required workflow now runs both static and browser checks with full integration probes enabled. Static validation matched all 15 queries below to their specified topics. The browser opens a visible result for each query. |

| Plan §10 query | Expected result |
|---|---|
| unit test | ci-unit-tests |
| lint | ci-lint-format |
| coverage | ci-coverage |
| SonarQube | ci-static-analysis |
| quality gate | ci-static-analysis |
| bug | defect-report |
| severity | defect-lifecycle |
| regression | regression-scope |
| test case | test-case-design |
| Jira status | flow-jira-status |
| hotfix | hotfix-flow |
| rollback | recover |
| feature flag | rollout |
| median | measure |

The additional edition 1.0.2 correction probe, security, targets qa-tests.

The integration browser suite checks the 53 overview pages and the four navigation pages at 390 pixels, alongside the existing 390-pixel tests for every deep dive and flow. On each of the six reference routes it opens mobile Contents, follows the section link by keyboard and tabs to the reference control. It opens the figure text or checks the focusable table region, including horizontal keyboard scrolling where the table is wider than the region. The suite also checks rendered label bounds on every instructional SVG at desktop and phone widths.

The local Chromium process could not open its startup socket. The hosted validation run linked from the pull request supplies the browser result. On a pull request the same workflow builds the unbound field guide and uploads it as the field-guide-preview artifact outside the Pages site. Its build and inspection are recorded in the separate PDF handoff.

The PR navigation step sets SDLC_INTEGRATION_PREVIEW=1. The browser check expects an unbound integration label and the checked-out commit on that build. The deploy and release callers use the ordinary edition label and the same commit check. A local check of both builds found all 103 HTML footers correctly labeled in each mode.

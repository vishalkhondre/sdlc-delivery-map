# Integration figure inspection

Two new figures bring the edition to fourteen distinct instructional figures. The evidence record reuses the PR-to-production trace. Hold release reuses the code-versus-configuration requalification decision. Measure and Handoffs each get an editable SVG with a caption, short alternative and expandable text route.

The cohort graphic reads the published one-day CSV. All four bars use the same 100 submissions and full 24-hour observation period. The decision bar ends at 40, short of the 50% reference. Sixty requests remain open. Correct assignment by one day covers 92 requests, all of which took 3–19 minutes. The printed totals and the two-minute result remain readable with the colors removed.

The arrow samples match the four meanings in the legend of the 2048 × 1735 reference map. I traced the same-lane branch-to-PR arrow, the PR-to-CI handoff, the failed-QA path to Hold release and the UAT-to-Confluence evidence link. Each example states its start and destination and names its stroke pattern. The output chip appears separately in the original legend.

I regenerated each SVG from a separate copy of its Python source and compared the output byte for byte to the checked-in asset. I rendered all fourteen at natural size and at 365 pixels wide in Inkscape, inspected both views and compared each route with its text equivalent. I measured each boxed line against its enclosing rectangle. The last column gives the smallest distance from the rendered ink to a box edge in natural SVG units.

| Figure | Natural dimensions | Boxes | Boxed lines | Minimum inset |
|---|---:|---:|---:|---:|
| build-evidence | 664 × 526 | 6 | 17 | 11.7 |
| ci-pipeline | 640 × 514 | 8 | 16 | 9.9 |
| cohort-at-one-day | 468 × 389 | 1 | 2 | 10.5 |
| data-change-coordination | 468 × 985 | 8 | 27 | 10.5 |
| defect-lifecycle | 620 × 654 | 7 | 14 | 11.5 |
| flow-bug-ci | 440 × 544 | 5 | 13 | 10.5 |
| flow-bug-prod | 456 × 905 | 8 | 39 | 10.5 |
| flow-bug-qa | 510 × 833 | 11 | 47 | 10.5 |
| flow-bug-uat | 456 × 636 | 6 | 26 | 10.5 |
| flow-traceability | 452 × 851 | 6 | 19 | 10.5 |
| hotfix-flow | 474 × 1276 | 11 | 42 | 10.5 |
| jira-workflow | 680 × 545 | 14 | 14 | 8.6 |
| map-arrow-legend | 462 × 425 | 4 | 12 | 8.5 |
| regression-scope | 650 × 720 | 6 | 24 | 14.0 |

All 312 measured lines fit within their 101 cards. The closest inset was 8.5 units, in the new legend. Free captions and connector labels cleared the dividers, and the split/join routes retained their directions. The 365-pixel render makes the dense older figures smaller, especially the Jira state labels. Their text descriptions preserve the route at normal reading size.

I also inspected the fixed map at full resolution in four quadrants and at a 365-pixel fit. Full size shows the labels and individual arrowheads. The fit view shows the overall layout and requires zoom or the text route for the fine print.

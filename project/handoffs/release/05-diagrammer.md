# Release figure inspection

The new instructional figure in `data-change-coordination` follows a hypothetical change to the stored routing group. A mixed deployment keeps the old read path and writes both fields. Before switching reads, the team backfills old rows, drains writers that update only the old field, catches up, and checks open requests, ownership and decision history. Dual writes continue through the rollback window. The last comparison between old and new field values takes place under dual writes. After new-only writes begin, verify current assignments against the authoritative business record and approved rule. Retirement also requires that readers, writers and eligible rollback versions can operate without the old field. The two branches give explicit actions for passing and holding. The lesson author and diagrammer agreed on this order and the text equivalent. The SVG and matching Python source are in `site/assets/figures`.

I regenerated all eleven SVGs from copied editable sources, compared each result byte for byte with the edition, and rendered the originals with Inkscape at their natural dimensions and at 365 pixels wide. I read the label baselines, box insets, headings, branch destinations, junctions and free captions on both renders. I also compared each route with its lesson text equivalent.

| Figure | Natural width × height | Smallest painted label inset (SVG units) |
| --- | --- | ---: |
| build-evidence | 664 × 526 | 11.7 |
| ci-pipeline | 640 × 514 | 9.9 |
| data-change-coordination | 468 × 985 | 10.5 |
| defect-lifecycle | 620 × 654 | 11.5 |
| flow-bug-ci | 440 × 544 | 10.5 |
| flow-bug-prod | 456 × 905 | 10.5 |
| flow-bug-qa | 510 × 833 | 10.5 |
| flow-bug-uat | 456 × 636 | 10.5 |
| flow-traceability | 452 × 851 | 10.5 |
| jira-workflow | 680 × 545 | 8.6 |
| regression-scope | 650 × 720 | 14.0 |

All 256 grouped labels in 85 boxes cleared their box edges. The migration figure contains 27 labels in eight boxes. Its fork has two labelled destinations and no arrowhead on the dividing line. The approved regression figure still has one downward arrow into Business handoff. No visual defect needed correction in the ten existing SVGs. In the new illustration I made the old-writer drain and catch-up explicit. On editorial recheck I separated the two verification steps so a stale old field cannot block retirement. I regenerated the final artwork byte for byte, measured all eleven figures again and inspected the revised illustration at natural and phone sizes.

I inspected the original 2048 × 1735 map in four full-resolution quadrants and fitted it to a 365-pixel screen. The fit view shows the stage and tool layout; reading its card copy on a phone requires zoom or the text navigation. The map and its clickable regions use the approved coordinates. Inkscape supplies the local measurements above. The repository's browser validator independently checks rendered SVG bounds on the built edition in the pull request run.

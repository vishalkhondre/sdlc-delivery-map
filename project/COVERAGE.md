# Coverage and handoffs

The inventory is executable. Run `python scripts/validate.py source` to count canonical lessons and visible map regions, validate their destinations and detect rectangles outside the approved image. Run the link checker after building to validate topic routes, evidence links and each in-page anchor. The catalog is the public text equivalent for navigation.

| Lifecycle question | What the reader can inspect |
| --- | --- |
| Why build this? | The fictional objective, expected value, acceptance criteria and baseline. |
| What changed? | Branch and review, CI, integrated candidate build, image digest and registry. |
| Was it verified? | Technical evidence, business acceptance, rejected candidates and requalification. |
| What reached users? | Release records, configuration, promotion authorization, runtime checks and recovery. |
| Did it help? | Alert handling, comparable-request cohorts, incomplete outcomes, user feedback and follow-up work. |

For extensions, add an inventory row for the new target and note where its inputs come from and where its outputs go. Keep repeated evidence labels connected to their canonical topic.

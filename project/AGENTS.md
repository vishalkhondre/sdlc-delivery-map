# Authoring and review roles

The adapted Claude Code agent definitions live in `.claude/agents/`, with matching role instructions in `.claude/skills/`. The section-pipeline skill controls handoffs.

| Role | Output |
| --- | --- |
| Architect | Topic inventory, scope, dependencies and reader acceptance checks |
| Source researcher | Public worked-example brief, assumptions and policies |
| External researcher | Source-verified claims and primary references |
| Author | Original lesson using the delivery template |
| Diagrammer | Clickable regions, stable labels and equivalent text navigation |
| Confidentiality reviewer | Public-release and attribution findings |
| Accuracy reviewer | Evidence checks and corrections for factual claims |
| Editorial reviewer | Independent reader, usability and consistency findings |
| Site builder | Integrated navigation, validation, release binding and publishing |

Review records must describe the review that actually occurred. Where the runtime permits, each reviewer receives the site and relevant sources afresh. A source hash confirms that the accepted lesson set did not change after that review.

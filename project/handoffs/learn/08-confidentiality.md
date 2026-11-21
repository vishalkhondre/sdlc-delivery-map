# Independent public-release review of Learn

**21 November 2026 · Accept for Gate 3.** I followed the learning stop through instrumentation, alert design, incident lifecycle, hotfix flow, outcome analysis and feedback to backlog. I inspected the rendered lessons, page metadata, link and asset destinations, samples and figure descriptions against the numbered lesson source, fictional dataset and two published downloads.

| Material | Finding |
| --- | --- |
| Routing event history | The JSONL rehearsal uses an opaque training request, generic actor and group labels, and an explicitly fabricated trace ID. It identifies the invented event times. Revision and settings match the fictional deployment attempt. The lesson directs request-level identifiers, recipient details and traces into restricted evidence and uses aggregate outcomes for shared metrics. |
| Rules and notification | The example gives role-based receiver aliases. The on-call page identifies a controlled mismatch, the fictional deployment and settings, its owner and the immediate action. It contains no request ID, person's name, purchase text, account address or private evidence URL. The lesson explains who can enrich the page and tells the responder to use a private evidence lookup. |
| Incident and subsequent work | The qualification record labels its identifiers and measurements fictional. Its eight affected purchases have aggregate dispositions. The 100 synthetic CSV rows have sequential EX keys, elapsed times and open status. The eight later missing assignments have their own investigation. The example incident ledger directs record-level details to restricted access. The public backlog example uses aggregate findings and roles. |
| Hotfix illustration | I inspected the alternate text, text equivalent, SVG title, description and elements, editable drawing script and shared helper. They describe a hypothetical code repair. The SVG contains text and vector geometry. The historical INC-7 record describes a mapping correction. |
| References and credits | The six pages link to 20 distinct public publisher references and the project's public source repository. Their file destinations resolve locally. The Sources page credits the adapted AI SDLC Map by Vishal Khondre. The distributed licences cover original educational material under CC BY 4.0, site tooling under MIT, and both bundled font families under the SIL Open Font License. |

**Final recheck.** The revised rehearsal adds generic event keys and per-request sequence values. Record links describe relationship types without exposing any private target. The new pre-expansion decision in the hotfix figure names the QA and Service Owner roles and refers to the same hypothetical repair. The final direct-entry definitions explain eligibility and the purpose of the fictional Jira epic CC-100. Neither introduces an internal eligibility rule, organization or record URL. I rechecked the page notification, log samples, revised figure and public links, then repeated the independent build on this final source.

**Independent build.** In a temporary output directory I regenerated the site from the reviewed source, carrying over the displayed edition stamp. The six lessons, source index, topic index and guided tour matched the supplied build byte for byte. The two example downloads, hotfix SVG, its Python source, shared drawing helper and distributed licence files also matched their counterparts in the project.

| Reviewed source | SHA-256 |
| --- | --- |
| `content/09-deep-release.json` | `341750aa059f42e4cc6661dce346af37305c539b68410a54bdf00f8c066b72cb` |
| `site/assets/figures/hotfix-flow.svg` | `30ccbec8b8c62ae69e7cfa6aa98a9ad4412d2890c4a0168f541d264b40474293` |
| `site/assets/figures/hotfix-flow.py` | `ffb6ec7f0606b7a7f005a53ea3f52b5a5e7249bdd3a29143d5e9e3c5420fadca` |

I found no public-disclosure issue requiring a correction. This decision covers the supplied teaching material. Live logging permissions, pager routes and work-item access were outside the review.

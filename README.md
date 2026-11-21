# The SDLC Delivery Map

Follow one fictional software feature from its business objective to a running production revision and the next product decision. The interactive swimlane opens practical lessons on delivery activities, roles, environments, evidence and recovery. The guided tour introduces the sequence, and the topic catalog supports direct lookup.

**[Open the interactive map](https://vishalkhondre.github.io/sdlc-delivery-map/)** · [Guided tour](https://vishalkhondre.github.io/sdlc-delivery-map/tour.html) · [Topic catalog](https://vishalkhondre.github.io/sdlc-delivery-map/topics.html)

## Run locally

Use Python 3.10 or later. Static generation is separate from the browser and PDF tooling.

```sh
python -m pip install -r scripts/requirements.txt
python -m playwright install chromium
python scripts/validate.py source
python site/generate.py
python scripts/validate.py links
python -m unittest discover -s scripts/tests -v
python scripts/check_browser.py
python scripts/check_release.py check
python -m http.server --directory dist 8000
```

Open `http://localhost:8000/`. On a machine with Chromium already installed, set `PLAYWRIGHT_CHROMIUM_EXECUTABLE` to its absolute executable path for browser checks and PDF rendering.

## Maintain a lesson

- `content/0*.json` holds the canonical lesson records, including their owners, inputs, steps, evidence, examples, failure paths, measures and references.
- `content/hotspots.json` connects rectangles on the 2048 × 1735 illustration to lesson IDs. Several regions may teach different uses of one lesson.
- `site/` contains the generator, styles, interactions and original map illustration. `dist/` is the generated, self-contained static site.
- `project/`, `templates/`, `.claude/` and `.github/prompts/` preserve the authoring and review handoff.
- `content/reviews/` records the three reviews and binds their conclusion to the exact edition. Run `python scripts/check_release.py bind` only after reviewing the current lesson set and site.

Start with [the publishing approach](project/APPROACH.md), [the agent roles](project/AGENTS.md) and [the lesson template](templates/pages/lesson.md).

## Publish

On GitHub, set the repository's Pages source to **GitHub Actions**. Pull requests run the complete validation workflow. A push to `main` reuses validation and deploys the resulting `dist/` artifact to the protected `github-pages` environment. All navigation is relative to the project's path.

After a successful main build, the publishing workflow also creates a GitHub Release and printable field guide for a new reviewed edition. An existing release is preserved.

For a tagged edition, update `content/VERSION`, `content/CHANGELOG.md` and `release/sections.yml`, collect the review and bind it. A matching `vMAJOR.MINOR.PATCH` tag on a commit reachable from `main` creates a GitHub Release with notes and a section PDF. Maintainers may also dispatch the release workflow on `main`. Check a snapshot locally with:

```sh
python scripts/release_snapshot.py notes v1.0.0
python scripts/release_snapshot.py pdf v1.0.0 build/sdlc-delivery-map-v1.0.0.pdf
```

A second PDF layout can be generated on machines without a browser. Run `python scripts/field_guide_pdf.py v1.0.0 build/sdlc-delivery-field-guide.pdf` to produce a printable guide from the same lesson inventory, with a linked index, bookmarks and the full-size map scaled to the page.

## Credits and license

The site's static documentation design, agent roles, review discipline, Pages workflows and tagged snapshot mechanism adapt Vishal Khondre’s [AI SDLC Map](https://github.com/vishalkhondre/ai-sdlc-map/tree/60e0864f54b727eb582332ce1a4932ad89378266). The SDLC Delivery Map presents its own fictional feature and delivery lessons. The original educational material uses CC BY 4.0 and the tooling uses MIT. See [LICENSE](LICENSE).

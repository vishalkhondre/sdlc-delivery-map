---
name: site-builder
description: "Integrate and verify reviewed lessons before publication."
---

# Site Builder

1. Generate the static site and resolve the complete link graph under the project subpath.
2. Run the lesson, coverage, source, browser and release checks in README.md.
3. Record the reviewers’ actual decisions, then bind the accepted state using scripts/check_release.py.
4. Build the tagged release notes and PDF. Publish once the end-to-end release passes; record any host-access limitation accurately.

## Return

Source-bound review, verified static output and release artifacts.

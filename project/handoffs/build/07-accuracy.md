# Independent accuracy review · ACCEPT · 21 November 2026

A fresh reviewer inspected the six new rendered Build pages against the vendor sources, course dataset and qualification record. The Dockerfile initially copied a different directory from the source path reviewed in CODEOWNERS and lint. The corrected image copies src/routing/. Both the developer's shell and the supplemental test job now put src on Python's import path. The test explains how a unique increasing sequence per request identifies the first persisted event. The Testcontainers transfer note correctly starts a separate container from the test, using driver=None for a Psycopg-compatible URL. The image workflow and illustrative push receipt use Docker Hub, as on the map.

The reviewer reopened the rendered changes and accepted all six lessons. The PR head remains unknown, and the integrated commit and digest match build-418/qa-204. The queue, approval and platform-manifest cases were checked against published mechanisms. This was a static review of examples; no external application or registry was exercised.

## GitHub Action release audit for PR #7

I checked all 12 Build lessons, including the six inherited CI pilot lessons. Five lessons contain workflow samples with `uses:` references. Their 12 invocations match the rendered lesson pages and use seven distinct action/major pairs.

| Action reference in the sample | Lesson IDs | Invocations | Published release verified | Published on (UTC) |
| --- | --- | ---: | --- | --- |
| `actions/checkout@v4` | `ci-pipeline-anatomy`, `ci-static-analysis`, `ci-security-checks`, `ci-integration-tests`, `image-build` | 5 | [v4.2.2](https://github.com/actions/checkout/releases/tag/v4.2.2) | 2024-10-23 |
| `actions/setup-python@v5` | `ci-pipeline-anatomy`, `ci-integration-tests` | 2 | [v5.6.0](https://github.com/actions/setup-python/releases/tag/v5.6.0) | 2025-04-24 |
| `actions/upload-artifact@v4` | `ci-pipeline-anatomy` | 1 | [v4.6.2](https://github.com/actions/upload-artifact/releases/tag/v4.6.2) | 2025-03-19 |
| `actions/dependency-review-action@v4` | `ci-security-checks` | 1 | [v4.7.0](https://github.com/actions/dependency-review-action/releases/tag/v4.7.0) | 2025-05-08 |
| `docker/setup-buildx-action@v3` | `image-build` | 1 | [v3.10.0](https://github.com/docker/setup-buildx-action/releases/tag/v3.10.0) | 2025-02-26 |
| `docker/login-action@v4` | `image-build` | 1 | [v4.0.0](https://github.com/docker/login-action/releases/tag/v4.0.0) | 2026-03-04 |
| `docker/build-push-action@v6` | `image-build` | 1 | [v6.18.0](https://github.com/docker/build-push-action/releases/tag/v6.18.0) | 2025-05-27 |

For each row I opened the publisher’s GitHub release record, confirmed its publication time and stable status, and inspected its versioned `action.yml` for the sample’s inputs and outputs. All seven major references also resolve. The dependency review action publishes the moving `v4` reference as a branch. The other six use major-version tags. The linked releases establish that each major existed by the fictional build-418 date of 9 March 2026. An exact patch or commit used by that fictional job is unspecified.

**Verdict: pass.** Every sampled major has a published release. The samples require no action-version corrections.

# V4 Publication and Cleanup

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | V4 publication, archived evidence and branch cleanup |

## Publication

The public V4 pull request was merged into the portfolio's `main` on October 2. The private blueprint V4 was independently merged into its own `main`. Public and private Git histories remain separate; the public tree does not contain the private companion.

## Archived and removed

Four July commissioning records and the older troubleshooting knowledge base were moved to `archive/commissioning-2026-07/`. The live troubleshooting guide now describes current boundary checks. All affected links were updated. The duplicate inventory summary and unused V3 audit wrapper were removed.

Original decisions and reusable templates remain useful and were retained. No credentials, private logs, working configuration or household data were transferred or deleted.

## Branch lifecycle

`main` is the live branch in each repository. A one-time workflow preserves each named old branch tip as a tag under `archive/`, verifies it is an ancestor of main, and only then deletes that exact branch using an expected-head lease. It rejects moved heads, unmerged commits and conflicting existing archive tags.

The workflow is removed after successful remote verification. Archive tags preserve historical lookup without keeping additional live branches. Git history itself is retained.

## Validation

The public and private-aware V4 audits check links, metadata, text/SVG privacy patterns, asset structure and whitespace. Remote GitHub Actions results and branch/tag inventories must be verified after cleanup; archive presence is not a runtime homelab test.

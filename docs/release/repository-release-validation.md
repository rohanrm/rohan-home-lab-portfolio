# Repository Release Validation

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Repository Release Validation |



## V4 scope

The V4 reconciliation covers every one of the 48 source files shared by private V3 and public main. Technical claims derive from dated project evidence, not a new homelab audit. The source file disposition is recorded in [document audit](v4-document-audit.md).

## Validation record

| Check | Result / limit |
|---|---|
| Source inventory | Both source trees have the same 48 file paths and content blobs |
| Current documentation | Flat-LAN, deferred-switch/DNS migration and absent-Jellyfin claims corrected in active records |
| Historical evidence | Original July commissioning retained with explicit historical labels |
| Local structure and links | Checked with the V4 audit before commit |
| Public content patterns | Public addresses/identifiers/secret patterns scanned across text and SVG files |
| SVG assets | Self-contained, parsed and visually inspected before commit |
| Shared/private separation | Only the private blueprint contains the companion operational directory |
| Remote publish | Check branch contents after commit; commit SHAs are Git metadata |
| GitHub Actions | Must be checked after push; local validation alone is not a remote pass |
| Live lab / full history | Not re-tested or exhaustively scanned in this documentation update |

## V3 historical release

The July record documented a clean-history employer-facing publication. That history remains separate from the private development repository. V4 uses the portfolio's own existing ancestry rather than importing private history.

## Acceptance limits

Fresh backup ages are not restoration proof. Host GPU availability is not transcoding proof. A short storage check is not long-term stability proof. Snapshot import is not continuous collection. See [V4 evidence](../validation/v4-baseline.md) for runtime observations and open checks.

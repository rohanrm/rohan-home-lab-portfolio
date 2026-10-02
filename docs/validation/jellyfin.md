# Jellyfin Validation

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Jellyfin Validation |
| Validation status | Passed with Exception |


## Recorded results

| Check | Evidence | Status |
|---|---|---|
| Runtime | Healthy Jellyfin service recorded on Docker VM | Passed |
| Public proxy path | External media endpoint validated through Caddy | Passed |
| Media boundary | NAS consumer read access, rejected writes and excluded photos established during storage validation | Passed for recorded storage tests |
| All playback profiles | Complete dated codec/client matrix unavailable | Not established |
| Container recreation / VM restart | Complete dated persistence result unavailable for V4 | Not established |
| GPU transcoding | Host GPU capability observed; actual transcode evidence unavailable | Not established |
| Restore | Fresh VM backup exists; restoration result unavailable | Not established |

Jellyfin is operational according to the later service records. This table does not retrospectively mark every July planned validation step passed.

## Checks after a change

From the active Compose directory, inspect service state and logs. Confirm the media path is an actual CIFS mount and that the container sees the intended libraries. Test authenticated internal and external access, representative playback, read-only permissions, and exclusion of photos. Restart/recreate only in a planned maintenance window with recovery material available.

For acceleration, validate host device, VM presentation, container mapping, Jellyfin configuration, and an actual hardware transcode. For restoration, recover configuration to an isolated instance, supply secrets securely, and prove usable service access. Backup archive presence alone is insufficient.

See [implementation](../implementation/jellyfin.md), [service](../services/jellyfin.md), and [V4 evidence](v4-baseline.md).

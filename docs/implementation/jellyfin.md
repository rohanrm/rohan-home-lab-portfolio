# Jellyfin Implementation

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Jellyfin Implementation |
| System status | Operational |


## Change from V3

V3 recorded preparation only. Later project records confirm a healthy Jellyfin deployment inside the Docker VM and externally validated access through Caddy. This update removes the obsolete no-container claim while retaining strict limits on unsupported test results.

## Deployment structure

| Layer | Implementation role |
|---|---|
| Application VM | Ubuntu, Docker Engine and Compose; server network |
| Definition | Active service-specific Compose file, inspected before changes |
| Application state | Persistent configuration/database and separate cache |
| Media | CIFS systemd automount from NAS; separate read-only libraries |
| External access | HTTPS at Caddy in DMZ; permitted application upstream |
| Administration | Approved internal access; secrets outside Git |

## Repeatable change method

1. Confirm the correct Compose directory and retain the previous definition/image reference.
2. Verify the NAS source is mounted and the real service identity has the intended access.
3. Validate the definition locally; keep secret-bearing rendered output private.
4. Apply the reviewed definition during maintenance and inspect service health/logs.
5. Test authentication, libraries, representative playback, and persistent configuration.
6. Test the external proxy path independently of the local path.
7. Record dated results and exceptions in the validation document.

Do not reconstruct the production Compose file from memory. Hardware mapping and image versions require inspection of the active deployment.

## Rollback

Stop the affected project, preserve diagnostic logs privately, restore the prior definition and compatible configuration, confirm the NAS mount, and restart the known-good version. Do not delete media, configuration, or named volumes as a shortcut.

## Separate optimization work

GPU availability on Proxmox does not prove VM passthrough or a working container transcode. Hardware acceleration and restore validation remain separate acceptance gates.

See [service](../services/jellyfin.md), [validation](../validation/jellyfin.md), and [proxy implementation](caddy-dmz.md).

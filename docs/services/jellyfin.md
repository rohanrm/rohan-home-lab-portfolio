# Jellyfin

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Jellyfin |
| Service status | Operational |


## Current state

Jellyfin is running in Docker on the Ubuntu application VM. The July record of prepared directories with no running container has been superseded. Media access uses the NAS automount; configuration and cache persist separately from the container image. External HTTPS access is provided through Caddy in the DMZ.

## Access and data

| Data | Permission / treatment |
|---|---|
| Movies, television, music | Read-only source libraries |
| Photos | Excluded from Jellyfin |
| Configuration, database, metadata | Persistent writable application state; back up |
| Cache and downloaded image | Re-creatable; distinct from source media |

Only required media paths should be exposed to the container. Application authentication remains necessary behind TLS. Do not publish viewing histories, client identities, administrator URLs, or tokens.

## Routine inspection

From the verified active Compose directory:

```bash
docker compose ps
docker compose logs --tail=100 jellyfin
findmnt <media-mount-point>
```

Before updates, preserve configuration and the previous image reference. Validate storage, application startup, authenticated access, and representative playback after a change. Do not delete persistent volumes as a troubleshooting shortcut.

## Evidence limits

Running-container health and external access are recorded. Intel graphics exist on the host, but V4 does not claim successful hardware transcoding. Container recreation, complete playback coverage, and restoration are not promoted to passed without dated results. See [validation](../validation/jellyfin.md).

See [implementation](../implementation/jellyfin.md), [Caddy](caddy.md), and [Samba](samba.md).

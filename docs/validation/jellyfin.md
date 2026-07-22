# Jellyfin Validation

| Field | Value |
|---|---|
| Document status | Current |
| System status | In Progress |
| Validation status | Not Started |
| Visibility | Public |
| Last reviewed | 2026-07-21 |
| Source of truth for | Jellyfin readiness, deployment checks, and promotion criteria |

## Purpose

This document defines the checks required before Jellyfin can be marked:

```text
Implemented → Validated → Operational
```

The Docker platform and storage prerequisites have been validated, but the Jellyfin application itself has not yet been deployed.

This record intentionally distinguishes completed preparation from application validation.

## Current State

Completed prerequisites:

| Prerequisite | Result |
|---|---|
| Docker VM running | Passed |
| Docker Engine active | Passed |
| Docker Compose available | Passed |
| Persistent configuration directory exists | Passed |
| Persistent cache directory exists | Passed |
| NAS media automount operational | Passed |
| Movies readable and non-writable | Passed |
| Television readable and non-writable | Passed |
| Music readable and non-writable | Passed |
| Photos inaccessible | Passed |

Incomplete application items:

| Requirement | Current result |
|---|---|
| Final Compose file in active Jellyfin directory | Not Started |
| Compose configuration renders successfully | Not Started |
| Jellyfin container running | Not Started |
| Browser setup page reachable | Not Started |
| Media libraries added | Not Started |
| Playback tested | Not Started |
| Restart persistence tested | Not Started |
| Container recreation tested | Not Started |
| Hardware acceleration tested | Not Started |

## Validation Criteria

| ID | Check | Expected result | Status |
|---|---|---|---|
| JF-01 | Compose file exists | One approved Compose file exists in the active directory | Not Started |
| JF-02 | Compose syntax | `docker compose config` succeeds | Not Started |
| JF-03 | Service definition | Jellyfin appears in the rendered service list | Not Started |
| JF-04 | Image retrieval | Approved image pulls successfully | Not Started |
| JF-05 | Container startup | Container starts without restart loop | Not Started |
| JF-06 | Container health | Service remains stable after initial startup | Not Started |
| JF-07 | Web access | Setup interface reachable from trusted LAN | Not Started |
| JF-08 | Configuration persistence | Settings survive restart | Not Started |
| JF-09 | Container recreation | Configuration survives container replacement | Not Started |
| JF-10 | Movies library | Files can be scanned and played | Not Started |
| JF-11 | Television library | Files can be scanned and played | Not Started |
| JF-12 | Music library | Files can be scanned and played | Not Started |
| JF-13 | Write protection | Jellyfin cannot modify source media | Not Started |
| JF-14 | Photo isolation | Photo library remains inaccessible | Not Started |
| JF-15 | Reboot recovery | Service returns after Docker VM reboot | Not Started |
| JF-16 | Logs | No unresolved permission, mount, or database errors | Not Started |
| JF-17 | Hardware acceleration | Capability tested separately if enabled | Not Started |
| JF-18 | Backup boundary | Required configuration backup identified | Not Started |

## Planned Validation Procedure

### JF-01 — Compose File Exists

From the active Jellyfin directory:

```bash
find . -maxdepth 1 -type f \
  \( -name 'compose.yaml' \
  -o -name 'compose.yml' \
  -o -name 'docker-compose.yaml' \
  -o -name 'docker-compose.yml' \) \
  -print
```

Expected result:

- Exactly one approved Compose file
- No obsolete test file used accidentally

Status: `Not Started`

### JF-02 — Compose Syntax

```bash
docker compose config
```

Expected result:

- Configuration renders without syntax errors
- No unresolved environment variables
- Mounts and ports appear as intended
- No secrets are printed or committed

Status: `Not Started`

### JF-03 — Service Definition

```bash
docker compose config --services
```

Expected result:

```text
jellyfin
```

Status: `Not Started`

### JF-04 — Image Retrieval

```bash
docker compose pull
```

Expected result:

- Approved Jellyfin image downloads successfully
- No authentication or registry error
- Image source matches the documented deployment

Status: `Not Started`

### JF-05 — Container Startup

```bash
docker compose up -d
docker compose ps
```

Expected result:

- Jellyfin container starts
- Container does not enter a restart loop
- Expected service state remains stable

Status: `Not Started`

### JF-06 — Logs and Initial Health

```bash
docker compose logs --tail=200 jellyfin
```

Expected result:

- Application initializes normally
- Configuration and cache paths are writable by the container
- Media paths are readable
- No repeated fatal errors
- No database corruption or permission failure

Status: `Not Started`

### JF-07 — Trusted-LAN Web Access

Expected result:

- Jellyfin setup page is reachable from an approved client on the trusted LAN
- Administrative interface is not intentionally exposed to the public internet
- Initial administrator account can be created securely

The exact private URL is retained outside the public repository.

Status: `Not Started`

### JF-08 — Configuration Persistence

Procedure:

1. Complete minimal setup.
2. Create a harmless test preference.
3. Restart the container.
4. Sign in again.
5. Confirm the preference remains.

Commands:

```bash
docker compose restart jellyfin
docker compose ps
```

Expected result:

- Service returns normally
- Configuration survives restart

Status: `Not Started`

### JF-09 — Container Recreation

Procedure:

```bash
docker compose down
docker compose up -d
```

Expected result:

- Container is recreated
- Configuration remains intact
- Libraries remain defined
- Persistent directories contain application state
- No source media is stored inside the disposable container layer

Status: `Not Started`

### JF-10 — Movies Library

Expected result:

- Movies directory can be added
- Library scan completes
- Representative file metadata appears
- Representative file plays
- Source file remains unchanged

Status: `Not Started`

### JF-11 — Television Library

Expected result:

- Television directory can be added
- Series and episode structure is detected
- Representative episode plays
- Source files remain unchanged

Status: `Not Started`

### JF-12 — Music Library

Expected result:

- Music directory can be added
- Representative album or track is detected
- Representative track plays
- Source files remain unchanged

Status: `Not Started`

### JF-13 — Write Protection

The container must not receive write access to the source-media mount.

Validation should confirm:

- Application can read approved media.
- Attempted creation or modification in the media source is rejected.
- Deletion of source media is not possible from the service account.

Status: `Not Started`

### JF-14 — Photo Isolation

Expected result:

- Photo directory is not mounted into the container, or access is rejected.
- Jellyfin cannot scan or traverse the photo library.
- Immich planning remains independent.

Status: `Not Started`

### JF-15 — Reboot Recovery

Procedure:

1. Confirm no manual mounts are required.
2. Reboot the Docker VM during an approved maintenance window.
3. Confirm Docker starts.
4. Trigger the media automount.
5. Confirm Jellyfin returns.
6. Test representative playback.

Expected result:

- Docker service active
- NAS media available
- Jellyfin running
- Configuration intact
- Playback successful

Status: `Not Started`

### JF-16 — Log Review

Commands:

```bash
docker compose logs --since=30m jellyfin
journalctl -u docker --since "30 minutes ago"
```

Expected result:

- No unresolved mount failures
- No repeated permission errors
- No database corruption messages
- No continuous restart behaviour

Status: `Not Started`

### JF-17 — Hardware Acceleration

Hardware acceleration is a separate optional validation area.

It must not be marked passed merely because the host has Intel integrated graphics.

If enabled, validate:

- Device presented to the Docker VM
- Device presented to the container
- Jellyfin configured for the correct acceleration method
- A real transcode uses hardware acceleration
- CPU utilization is reasonable
- Direct-play behaviour remains correct
- Restart and upgrade do not break device access

Status: `Not Started`

### JF-18 — Backup Boundary

Before operational promotion, identify:

- Configuration directory
- Database and metadata location
- Compose definition
- Any environment file containing non-secret configuration
- Secret-storage method
- Restore order

Cache does not normally require backup because it can be recreated.

Status: `Not Started`

## Promotion Gates

### In Progress to Implemented

Required:

- Final Compose file exists.
- `docker compose config` succeeds.
- Jellyfin container starts.
- Web interface is reachable.
- Persistent paths are mounted correctly.

### Implemented to Validated

Required:

- All mandatory checks JF-01 through JF-16 pass.
- JF-18 backup boundary is documented.
- Any failed or skipped check has a documented exception.
- Hardware acceleration may remain not applicable when it has not been enabled.

### Validated to Operational

Required:

- Service is actively used.
- Restart and reboot behaviour remain stable.
- Logs show no unresolved critical errors.
- Documentation reflects the real deployment.
- Service catalogue status is updated.
- Changelog records the milestone.

## Current Exceptions

| Item | Current condition | Effect |
|---|---|---|
| Compose definition | Missing from active deployment directory | Application cannot be implemented |
| Running container | None | Web access and playback cannot be tested |
| Hardware acceleration | Not configured | Performance capability remains unknown |
| Backup restore | Not tested | Recovery readiness remains incomplete |

## Conclusion

Jellyfin validation has not started because there is no active Jellyfin Compose deployment.

The underlying Docker, storage, automount, and permission prerequisites have passed.

The current lifecycle status remains:

```text
In Progress
```

No document should describe Jellyfin as validated or operational until the required checks pass.

## Related Documentation

- [Infrastructure Baseline](infrastructure-baseline.md)
- [Docker VM Validation](docker-vm.md)
- [NAS LXC Validation](nas-lxc.md)
- [Jellyfin Implementation](../implementation/jellyfin.md)
- [Jellyfin Service](../services/jellyfin.md)
- [Roadmap](../planning/roadmap.md)
- [Service Architecture](../architecture/service-architecture.md)

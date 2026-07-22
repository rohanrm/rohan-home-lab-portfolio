# Jellyfin Implementation

| Field | Value |
|---|---|
| Document status | Current |
| System status | In Progress |
| Visibility | Public |
| Last reviewed | 2026-07-21 |
| Last validated | Not yet validated |
| Source of truth for | Current Jellyfin preparation state and remaining deployment work |

## Purpose

This document records the Jellyfin implementation as it actually exists.

Jellyfin is not yet a running or validated service.

The current state is:

- Docker VM operational
- Docker Engine and Compose operational
- NAS media automount operational
- Jellyfin configuration directory prepared
- Jellyfin cache directory prepared
- Final Compose definition absent from the active Jellyfin directory
- Jellyfin container not running

This document will be updated as implementation progresses.

## Intended Outcome

The approved outcome is an internally accessible Jellyfin service that:

- Runs through Docker Compose
- Stores configuration persistently
- Stores cache separately from configuration
- Reads approved NAS media categories
- Cannot modify source media
- Restarts predictably
- Survives container recreation
- Can later be evaluated for hardware acceleration

## Starting State

The application host was prepared before Jellyfin deployment:

- Ubuntu Docker VM operational
- Docker Engine enabled and active
- Docker Compose available
- Permanent NAS media automount completed
- Movies, television, and music readable
- Media writes rejected
- Photo access intentionally denied

## Current Directory State

The active service directory is:

```text
/opt/docker/jellyfin/
```

The validated contents are:

```text
/opt/docker/jellyfin/
├── cache/
└── config/
```

At the Stage 1 snapshot, no file named any of the following existed in that directory:

```text
compose.yaml
compose.yml
docker-compose.yaml
docker-compose.yml
```

Therefore, the persistent directories are prepared, but the application has not been deployed.

## Obsolete Test Compose File

A Compose file was found under an unrelated test directory beneath `/opt/docker`.

It is not the Jellyfin deployment definition and must not be used as evidence that Jellyfin is installed or running.

The obsolete test directory should be reviewed and removed separately after confirming it contains no required configuration.

## Planned Deployment Model

| Item | Planned design |
|---|---|
| Platform | Docker VM |
| Runtime | Docker Engine |
| Definition | Docker Compose |
| Configuration | `/opt/docker/jellyfin/config` |
| Cache | `/opt/docker/jellyfin/cache` |
| Media source | `/mnt/nas/media` |
| Media access | Read-only |
| Network exposure | Trusted LAN only |
| Restart behaviour | Defined in Compose and validated after reboot |
| Hardware acceleration | Separate later implementation and validation |

## Prerequisites

Before creating the Compose definition, confirm:

```bash
docker --version
docker compose version
systemctl is-active docker
findmnt /mnt/nas/media
```

Confirm the media access model:

```bash
test -r /mnt/nas/media/movies
test -r /mnt/nas/media/tv
test -r /mnt/nas/media/music
```

Confirm writes remain rejected.

Do not deploy Jellyfin if the media path is merely an unmounted empty local directory.

## Compose Design Requirements

The final Compose definition must declare:

- A deliberately selected Jellyfin image and version policy
- A stable container name or Compose service name
- Persistent configuration mount
- Persistent cache mount
- Read-only media mounts
- Required internal port exposure
- Restart policy
- Timezone handling if required
- Appropriate user or group mapping
- Optional device mapping only after hardware-acceleration design is approved

The final production Compose file must be generated during the active Jellyfin deployment stage rather than guessed in advance.

## Example Directory Preparation

The existing directories can be recreated with:

```bash
sudo install -d -m 2770 -o <admin-user> -g docker \
  /opt/docker/jellyfin \
  /opt/docker/jellyfin/config \
  /opt/docker/jellyfin/cache
```

The actual owner is recorded privately where personal usernames are involved.

## Media Mount Design

The container should receive separate read-only media paths rather than broad write access.

A conceptual mapping is:

```text
Docker VM path                Container path
/mnt/nas/media/movies      →  /media/movies
/mnt/nas/media/tv          →  /media/tv
/mnt/nas/media/music       →  /media/music
```

Photos are intentionally excluded from Jellyfin.

The final Compose syntax will be documented after it is created and tested.

## User and Permission Design

The container must run with an identity that can:

- Read Jellyfin configuration
- Write Jellyfin cache
- Read and traverse approved media directories
- Not write to source media
- Not access the photo directory

Before selecting user and group mappings, confirm:

- The effective container identity
- The UID and GID expected by the image
- The CIFS mount ownership presentation
- Whether supplemental groups are required

Do not solve access problems by granting world-writable permissions.

## Network Design

The initial service is intended for trusted LAN access only.

The final deployment should publish only the required Jellyfin port or use an approved reverse-proxy design later.

The current project does not approve:

- Direct router port forwarding
- Public exposure of the Jellyfin administration interface
- Unauthenticated remote access
- Arbitrary host networking without a documented reason

## Hardware Acceleration Boundary

The Beelink platform may support Intel Quick Sync, but hardware acceleration is not part of the initial deployment claim.

It requires separate work covering:

- Proxmox device availability
- VM device passthrough or virtual GPU design
- Docker device mapping
- Jellyfin configuration
- Supported codec testing
- CPU and GPU utilisation verification
- Fallback behaviour

Jellyfin should first become operational with software playback and direct streaming before this optimization is attempted.

## Planned Implementation Procedure

### 1. Confirm dependencies

Validate Docker, Compose, NAS mount, and permissions.

### 2. Select the image policy

Choose a trusted Jellyfin image source and decide whether to pin a version or use a controlled update channel.

Record the decision in the final Compose file and service documentation.

### 3. Create `compose.yaml`

Create the production definition only in:

```text
/opt/docker/jellyfin/compose.yaml
```

Do not use the obsolete test Compose file.

### 4. Validate the definition

```bash
cd /opt/docker/jellyfin
docker compose config
docker compose config --services
```

### 5. Start the service

```bash
docker compose up -d
```

### 6. Inspect status and logs

```bash
docker compose ps
docker compose logs --tail=100
```

### 7. Complete first-run configuration

Use the internal web interface to:

- Create the administrator account
- Set language and metadata preferences
- Add only approved media libraries
- Confirm the correct container paths
- Avoid enabling unreviewed external-access features

Credentials are stored outside Git.

### 8. Validate media access

Confirm that:

- Movies are visible
- Television libraries are visible
- Music is visible
- Photos are not visible
- Source files cannot be changed or deleted

### 9. Validate persistence

Restart the container and VM, then confirm:

- Jellyfin returns automatically as designed
- Configuration remains present
- Libraries remain configured
- The NAS mount is the actual CIFS source
- No data was written into an unmounted local directory

### 10. Update documentation status

The lifecycle should progress only when criteria are met:

```text
In Progress
  → Implemented
  → Validated
  → Operational
```

## Current Completion Checklist

- [x] Docker VM operational
- [x] Docker Engine operational
- [x] Docker Compose operational
- [x] Persistent configuration directory created
- [x] Persistent cache directory created
- [x] NAS media automount operational
- [x] Approved media readable
- [x] Media writes rejected
- [x] Photos excluded
- [ ] Final image policy selected
- [ ] Production `compose.yaml` created
- [ ] Compose definition validated
- [ ] Jellyfin container started
- [ ] First-run configuration completed
- [ ] Media libraries added
- [ ] Restart persistence tested
- [ ] Container recreation tested
- [ ] Validation document passed
- [ ] Service marked Operational

## Validation Requirements

The service must not be marked operational until the following pass:

| Check | Expected result |
|---|---|
| Compose syntax | Valid |
| Container state | Running and stable |
| Web access | Available on trusted LAN |
| Configuration persistence | Survives restart and recreation |
| Movies | Readable |
| Television | Readable |
| Music | Readable |
| Photos | Not accessible |
| Source media writes | Rejected |
| NAS source | Confirmed as CIFS mount |
| Logs | No unresolved critical errors |
| Reboot behaviour | Service returns as designed |

See [Jellyfin Validation](../validation/jellyfin.md).

## Backup Requirements

Before Jellyfin becomes operational, define backup coverage for:

- `config/`
- Any database stored within the configuration directory
- Custom metadata or artwork
- The Compose definition
- Non-secret environment templates

The cache directory normally does not require backup.

Source media backup is a separate NAS responsibility.

## Rollback

For a failed initial deployment:

1. Capture sanitized logs.
2. Stop the Compose project.
3. Preserve the rejected Compose definition for diagnosis.
4. Confirm the NAS mount remains correct.
5. Restore configuration if a migration changed it.
6. Remove only disposable containers and images.
7. Do not delete persistent configuration or source media.

Representative stop command:

```bash
cd /opt/docker/jellyfin
docker compose down
```

Do not add `-v` unless volume deletion is explicitly intended and backed up.

## Security Considerations

- Jellyfin is limited to trusted LAN access during the initial deployment.
- Source media remains read-only.
- Photos are excluded.
- Administrator credentials are not stored in Git.
- Container configuration is separated from media.
- Hardware devices are not mapped until justified.
- The container should receive no broader host access than required.
- Public documentation must not include session tokens, API keys, or exact administrative URLs.

## Known Limitations

- No active Compose definition exists yet.
- No Jellyfin container is running.
- Hardware acceleration is not configured.
- Backup and restore have not been validated.
- Remote access is not approved.
- Application monitoring is not yet implemented.

## Lessons Learned

- Creating persistent directories is preparation, not deployment.
- A Compose file in a test directory is not the active service definition.
- Storage access should be proven before starting the application.
- Read-only media access should be enforced at more than one layer.
- Status wording must reflect observed state rather than intended state.

## Related Documentation

- [Docker VM Implementation](docker-vm.md)
- [Samba systemd Automount Implementation](samba-systemd-automount.md)
- [Service Architecture](../architecture/service-architecture.md)
- [Jellyfin Service](../services/jellyfin.md)
- [Jellyfin Validation](../validation/jellyfin.md)
- [Roadmap](../planning/roadmap.md)

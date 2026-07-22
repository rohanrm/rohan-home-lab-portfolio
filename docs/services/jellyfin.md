# Jellyfin

| Field | Value |
|---|---|
| Document status | Current |
| Service status | In Progress |
| Visibility | Public |
| Platform | Docker VM |
| Last validated | Application validation not started |
| Source of truth for | Jellyfin role, current state, dependencies, and operational target |

## Purpose

Jellyfin is the selected media-service project for browsing and streaming approved movie, television, and music libraries.

The service is intended to demonstrate:

- Docker Compose deployment
- Persistent application configuration
- Separation of application and media storage
- Read-only access to source media
- Service validation
- Potential Intel hardware acceleration

## Current State

Completed preparation:

- Docker VM operational
- Docker Engine active
- Docker Compose available
- Jellyfin application directory created
- Persistent configuration directory created
- Persistent cache directory created
- NAS media automount operational
- Movies readable and non-writable
- Television readable and non-writable
- Music readable and non-writable
- Photos inaccessible

Not completed:

- Final Compose definition
- Jellyfin container startup
- Web setup
- Library creation
- Playback tests
- Restart persistence
- Container recreation
- Hardware-acceleration testing
- Backup and restore testing

The service must not be described as implemented, validated, or operational.

## Deployment Model

| Item | Intended value |
|---|---|
| Host type | Docker container inside Ubuntu VM |
| Orchestration | Docker Compose |
| Configuration | Persistent bind-mounted directory |
| Cache | Persistent but re-creatable directory |
| Media | Read-only NAS-backed mount |
| Client scope | Trusted LAN |
| Public exposure | Not approved |
| Hardware acceleration | Optional future validation |

## Dependencies

| Dependency | Purpose | Required state |
|---|---|---|
| Proxmox host | Runs Docker VM and NAS LXC | Operational |
| NAS LXC | Presents persistent media through Samba | Operational |
| Samba | Provides approved media access | Operational |
| Docker VM | Hosts Docker runtime | Operational |
| Docker Engine | Runs Jellyfin container | Operational |
| Docker Compose | Defines Jellyfin service | Operational |
| Systemd automount | Makes media available on access | Operational |
| Jellyfin Compose definition | Declares service | Not Started |

## Network Role

Trusted clients will connect to Jellyfin over the internal LAN.

The public repository does not publish the exact private URL or port mapping.

No current design approves:

- Direct public internet exposure
- Router port forwarding
- Anonymous administrator access
- Publishing private authentication details

A future remote-access requirement must receive a separate security design.

## Storage

| Data | Location class | Persistence | Backup priority |
|---|---|---|---|
| Compose definition | Docker application directory | Persistent | High |
| Configuration and database | Jellyfin configuration directory | Persistent | High |
| Cache | Jellyfin cache directory | Re-creatable | Low |
| Movies | NAS media share | Persistent source data | High |
| Television | NAS media share | Persistent source data | High |
| Music | NAS media share | Persistent source data | High |
| Photos | Not exposed to Jellyfin | Separate private data | Not applicable to Jellyfin |

## Access and Permissions

The intended media boundary is:

| Library | Read | Traverse | Write |
|---|---|---|---|
| Movies | Allowed | Allowed | Rejected |
| Television | Allowed | Allowed | Rejected |
| Music | Allowed | Allowed | Rejected |
| Photos | Rejected | Rejected | Rejected |

The container should receive only the paths needed for the approved libraries.

Configuration and cache must be writable by the Jellyfin process.

Source media must remain read-only.

## Planned Operations

These commands become authoritative only after the Compose file exists.

### Render configuration

```bash
docker compose config
```

### Pull image

```bash
docker compose pull
```

### Start

```bash
docker compose up -d
```

### Stop

```bash
docker compose down
```

### Restart

```bash
docker compose restart jellyfin
```

### Status

```bash
docker compose ps
```

### Logs

```bash
docker compose logs --tail=200 jellyfin
```

Commands should be run from the active Jellyfin Compose directory.

## Updates

The intended update workflow is:

1. Review Jellyfin release notes.
2. Confirm configuration backup.
3. Record current image reference.
4. Pull the approved image.
5. Recreate the container.
6. Review logs.
7. Test web access.
8. Test representative playback.
9. Confirm media remains read-only.
10. Record meaningful changes.

Do not automatically track an unreviewed image tag in a way that makes rollback difficult.

## Backup and Recovery

Required backup scope:

- Compose definition
- Non-secret environment configuration
- Jellyfin configuration
- Database and metadata
- Plugin configuration
- Private record of exact service address and mount dependencies

Cache generally does not require backup.

Secrets must remain outside Git.

Recovery must prove that a recreated container can use the restored configuration and reconnect to the existing media libraries.

## Monitoring

After deployment, monitor:

- Container state
- Restart count
- Application logs
- Configuration-disk usage
- Cache growth
- Media mount availability
- Library-scan failures
- Permission errors
- Transcoding load
- Client playback errors

## Security Considerations

- Keep access internal during the initial deployment.
- Use a strong Jellyfin administrator password.
- Do not publish user lists or viewing history.
- Keep source media read-only.
- Keep photos outside Jellyfin.
- Review plugins before installation.
- Keep the container image updated through a controlled process.
- Avoid privileged container mode unless a separately justified requirement exists.
- Validate hardware-device passthrough before enabling it.

## Hardware Acceleration

The Beelink host provides Intel integrated graphics with potential Quick Sync support.

This capability is not yet implemented or validated for Jellyfin.

A valid hardware-acceleration result requires:

- Device availability on the Proxmox host
- Correct presentation to the Docker VM
- Correct presentation to the container
- Jellyfin configuration for the selected acceleration method
- A real transcode showing hardware use
- Stable direct play and restart behaviour

Hardware capability alone is not proof of a working configuration.

## Known Limitations

- No final Compose definition exists.
- No Jellyfin container is running.
- No web setup has been completed.
- No playback has been tested.
- No hardware acceleration has been tested.
- No restore has been tested.
- No approved remote-access design exists.

## Promotion Criteria

### To Implemented

- Final Compose definition exists.
- Configuration renders successfully.
- Container starts.
- Web setup is reachable.
- Persistent paths are correct.

### To Validated

- Mandatory checks in the validation record pass.
- Libraries scan and play.
- Restart and recreation preserve configuration.
- Source media remains read-only.
- Logs contain no unresolved critical errors.

### To Operational

- Service is actively used.
- Reboot recovery is stable.
- Backup scope is documented.
- Service catalogue and changelog are updated.

## Validation

See [Jellyfin Validation](../validation/jellyfin.md).

Current validation status:

```text
Not Started
```

## Related Documentation

- [Service Catalogue](README.md)
- [Jellyfin Implementation](../implementation/jellyfin.md)
- [Jellyfin Validation](../validation/jellyfin.md)
- [Docker VM Validation](../validation/docker-vm.md)
- [NAS LXC Validation](../validation/nas-lxc.md)
- [Service Architecture](../architecture/service-architecture.md)
- [Roadmap](../planning/roadmap.md)
- [Troubleshooting Guide](../operations/troubleshooting.md)

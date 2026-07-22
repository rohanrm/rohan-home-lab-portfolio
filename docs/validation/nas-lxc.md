# NAS LXC Validation

| Field | Value |
|---|---|
| Document status | Current |
| Validation status | Passed |
| Validation date | 2026-07-20 |
| Visibility | Public |
| Source of truth for | NAS LXC, storage presentation, Samba, and media-access validation |

## Purpose

This document records the tests used to confirm that the NAS LXC is operational and that its storage, permissions, and Samba services behave as designed.

The validation focuses on:

- Container state
- Unprivileged-container configuration
- Host bind mounts
- Filesystem availability
- Samba service state
- Media-library permissions
- Read-only access for the media-service account
- Isolation of the photo library

Exact addresses, guest identifiers, MAC addresses, raw configuration, and complete terminal output remain private.

## Environment

| Item | Validated state |
|---|---|
| Guest type | Unprivileged LXC |
| Operating-system family | Debian |
| CPU allocation | 2 virtual cores |
| Memory allocation | 1 GB |
| Swap allocation | 512 MB |
| Root disk | 16 GB |
| Startup | Enabled |
| Primary service | Samba |
| Persistent data source | Host-mounted external storage |

## Validation Criteria

| ID | Check | Expected result | Status |
|---|---|---|---|
| NAS-01 | Container state | NAS LXC is running | Passed |
| NAS-02 | Isolation mode | Container is unprivileged | Passed |
| NAS-03 | Bind mounts | Approved host directories appear inside the LXC | Passed |
| NAS-04 | Filesystem structure | Media, documents, downloads, and shared areas exist | Passed |
| NAS-05 | Samba service | Service is enabled and active | Passed |
| NAS-06 | Sharing-group model | Approved users receive intended access | Passed |
| NAS-07 | Media read access | Movies, television, and music are readable and traversable | Passed |
| NAS-08 | Media write protection | Media-service account cannot write to approved libraries | Passed |
| NAS-09 | Photo isolation | Media-service account cannot read, traverse, or write photos | Passed |
| NAS-10 | Startup persistence | Container and mounts return after host startup | Passed |

## Validation Procedure

### NAS-01 — Container State

From the Proxmox host:

```bash
pct list
```

Observed result:

- NAS guest listed
- Status reported as running

Exact guest ID is retained privately.

Status: `Passed`

### NAS-02 — Isolation Mode

From the Proxmox host:

```bash
pct config <nas-vmid>
```

Observed result:

- Container type reported as Debian
- Unprivileged mode enabled
- Automatic startup enabled
- Resource allocation matched the approved design

Status: `Passed`

### NAS-03 — Bind Mounts

From inside the NAS LXC:

```bash
findmnt
```

Observed result:

- Media area available
- Documents area available
- Downloads area available
- Shared area available
- Each area backed by the host's persistent ext4 filesystem

The public document omits exact host paths and mount identifiers.

Status: `Passed`

### NAS-04 — Filesystem Structure

Command:

```bash
find /srv -maxdepth 2 -type d -print
```

Observed structure included:

- Media
  - Movies
  - Television
  - Music
  - Photos
- Documents
- Downloads
- Shared files

Status: `Passed`

### NAS-05 — Samba Service

Commands:

```bash
systemctl is-enabled smbd
systemctl is-active smbd
systemctl --no-pager --full status smbd
```

Observed result:

```text
enabled
active
```

The service reported that it was ready to serve connections.

Status: `Passed`

### NAS-06 — Sharing-Group Model

Example checks:

```bash
getent group <sharing-group>
id <approved-user>
getfacl <shared-directory>
```

Observed result:

- Shared directories used the approved sharing group.
- Setgid inheritance was present where required.
- Access control lists preserved intended inheritance.
- Unauthorized users did not receive broad write access.

Exact usernames and group identifiers are retained privately.

Status: `Passed`

### NAS-07 — Media Read Access

The media-service account was tested against the approved libraries.

Observed result:

| Library | Readable | Traversable |
|---|---|---|
| Movies | Yes | Yes |
| Television | Yes | Yes |
| Music | Yes | Yes |

Status: `Passed`

### NAS-08 — Media Write Protection

Write tests were performed using the media-service account.

Observed result:

| Library | Writable |
|---|---|
| Movies | No |
| Television | No |
| Music | No |

This confirmed that the media service can consume the library without changing or deleting source media.

Status: `Passed`

### NAS-09 — Photo Isolation

The same account was tested against the photo library.

Observed result:

| Capability | Result |
|---|---|
| Read | Rejected |
| Traverse | Rejected |
| Write | Rejected |

This prevents the media service from receiving access to private photo content before a dedicated photo-management design is approved.

Status: `Passed`

### NAS-10 — Startup Persistence

The Proxmox guest configuration and Stage 1 snapshot confirmed:

- NAS LXC configured to start automatically
- Host storage mounted
- Bind-mounted directories present
- Samba active after startup

Status: `Passed`

## Samba Client Boundary

The Docker VM uses a separate Samba client account and root-protected credentials file.

The validation confirmed that:

- Authentication succeeds.
- Approved media is readable.
- Writes are rejected.
- Credentials are not embedded directly in the public documentation or `/etc/fstab`.

Status: `Passed`

## Exceptions

| Item | Exception | Impact |
|---|---|---|
| Photos | Intentionally unavailable to the media-service account | Supports least privilege |
| Media writes | Intentionally rejected | Prevents application-side modification of source media |
| Storage redundancy | One shared-data disk | Disk or enclosure failure can interrupt service |
| Restore validation | Not yet complete | Recovery work remains planned |

The first two items are intentional controls, not failed checks.

## Conclusion

The NAS LXC passed validation and is operational.

It successfully:

- Receives persistent host storage
- Presents approved directories
- Runs Samba at startup
- Applies controlled sharing-group permissions
- Allows read-only media consumption
- Isolates the photo library
- Preserves a clear boundary between physical storage ownership and application access

## Revalidation Triggers

Repeat relevant checks after:

- LXC configuration change
- Bind-mount change
- Disk or filesystem replacement
- Samba upgrade
- Share-definition change
- User or group redesign
- ACL change
- Docker media-account change
- Introduction of Immich or another photo service
- Restore from backup

## Related Documentation

- [Infrastructure Baseline](infrastructure-baseline.md)
- [NAS LXC Implementation](../implementation/nas-lxc.md)
- [Docker VM Validation](docker-vm.md)
- [Service Architecture](../architecture/service-architecture.md)
- [Samba Service](../services/samba.md)

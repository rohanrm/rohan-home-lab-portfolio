# Infrastructure Baseline Validation

| Field | Value |
|---|---|
| Document status | Current |
| Validation status | Passed |
| Validation date | 2026-07-20 |
| Visibility | Public |
| Source of truth for | Sanitized Stage 1 infrastructure baseline |

## Purpose

This document records the validated infrastructure state at the close of Stage 1 of the Version 3 documentation redesign.

It establishes a trustworthy point-in-time baseline before legacy documents are rewritten or removed.

The complete raw terminal output, exact addresses, guest identifiers, hardware identifiers, filesystem UUIDs, and other operational details are retained in the private repository.

## Validation Scope

The snapshot covered:

- Proxmox host identity and software versions
- Running virtual-machine and LXC inventory
- Internal and external storage
- NAS LXC configuration
- Samba service state
- Docker VM operating system and container tooling
- Persistent NAS access from the Docker VM
- Jellyfin preparation state
- Current project boundaries and approved service status

## Baseline Summary

| Component | Validated state | Lifecycle status |
|---|---|---|
| Proxmox host | Current platform and kernel confirmed; host operational | Operational |
| NAS LXC | Running, unprivileged, storage bind mounts present | Operational |
| Samba | Enabled, active, and serving configured shares | Operational |
| Docker VM | Running Ubuntu with Docker Engine and Compose active | Operational |
| NAS automount | Persistent systemd automount completed and tested | Operational |
| Pi-hole | Remains on its existing bare-metal host | Operational |
| Jellyfin | Persistent directories prepared; no active Compose deployment | In Progress |
| Immich | Approved after Jellyfin deployment | Planned |

## Software Baseline

| Platform | Validated version |
|---|---|
| Proxmox VE package | 9.2.0 |
| Proxmox Manager | 9.2.4 |
| Proxmox kernel | 7.0.14-4-pve |
| Proxmox host operating system | Debian GNU/Linux 13 |
| Docker VM operating system | Ubuntu 24.04.4 LTS |
| Docker Engine | 29.6.2 |
| Docker Compose | v5.3.1 |

Versions are intentionally recorded here because they define the validated baseline. They should not be copied into every architecture or service document.

## Compute Baseline

### NAS LXC

The NAS guest was validated with:

- Two virtual CPU cores
- 1 GB memory
- 512 MB swap
- 16 GB root disk
- Unprivileged-container mode
- Automatic startup
- Host storage presented through selected bind mounts

### Docker VM

The Docker guest was validated with:

- 4 GB memory
- 80 GB primary virtual disk
- Automatic startup through the Proxmox guest configuration
- Docker Engine enabled and active
- Docker Compose available

Exact guest IDs and network assignments remain private operational data.

## Storage Baseline

### Internal storage

The Proxmox host uses a 1 TB NVMe SSD for:

- Host operating system
- Swap
- LVM-backed guest storage
- NAS LXC root disk
- Docker VM disks

### Shared-data storage

A 4 TB Seagate IronWolf disk in an external enclosure was validated as:

- Detected by the Proxmox host
- Formatted with ext4
- Mounted by the host
- Presented to the NAS LXC through selected bind mounts
- Available through Samba
- Accessible from the Docker VM through the persistent automount

The public record describes capacity and responsibility without publishing the filesystem UUID or exact device identifiers.

## NAS Filesystem Baseline

The NAS LXC received selected storage areas for:

- Media
- Documents
- Downloads
- Shared files

The media area contained separate directories for:

- Movies
- Television
- Music
- Photos

The media-service access model was validated as follows:

| Library | Read | Traverse | Write |
|---|---|---|---|
| Movies | Allowed | Allowed | Rejected |
| Television | Allowed | Allowed | Rejected |
| Music | Allowed | Allowed | Rejected |
| Photos | Rejected | Rejected | Rejected |

This proves that the media-service account can consume approved libraries without receiving unnecessary write access or access to the photo library.

## Service Baseline

### Samba

Samba was validated as:

- Installed
- Enabled
- Active
- Ready to serve configured connections
- Backed by host-mounted persistent storage

### Docker

Docker was validated as:

- Installed
- Enabled at boot
- Active
- Usable by the approved administrative account
- Ready for Compose-managed applications

### Pi-hole

Pi-hole remains operational on its existing Raspberry Pi.

Migration is paused until Jellyfin and Immich have been deployed.

## Jellyfin Baseline

The active Jellyfin application directory contained:

- Persistent configuration directory
- Persistent cache directory

It did not contain:

- A final `compose.yaml`
- A final `compose.yml`
- A final `docker-compose.yaml`
- A final `docker-compose.yml`

No Jellyfin container was running from the active deployment directory.

Therefore, the correct lifecycle status was and remains:

```text
In Progress
```

The obsolete test Compose file found elsewhere under the Docker service root is not part of the Jellyfin deployment.

## Public and Private Evidence Boundary

The public validation record includes:

- Test purpose
- Commands that are safe to reuse
- Sanitized observed results
- Pass or fail conclusions

The private evidence record retains:

- Exact IP addresses
- Guest IDs
- MAC addresses
- Serial numbers
- Disk UUIDs
- Raw command output
- Detailed mount configuration
- Administrative identifiers

Secrets are stored outside both Git repositories.

## Exceptions

| Item | Exception | Impact |
|---|---|---|
| Jellyfin | Application deployment not complete | Jellyfin cannot be marked Implemented, Validated, or Operational |
| Pi-hole migration | Intentionally paused | Existing bare-metal Pi-hole remains the active DNS service |
| Network segmentation | Deferred | Current environment remains a single trusted LAN |
| Backup restoration | Not yet validated | Backup work remains planned |

These are documented project states rather than failed Stage 1 infrastructure checks.

## Conclusion

The Stage 1 baseline passed.

The Proxmox host, NAS LXC, Samba service, Docker VM, Docker tooling, and persistent NAS automount were confirmed operational.

Jellyfin preparation was accurately separated from a completed application deployment.

This baseline is the foundation for all Version 3 implementation, validation, service, operations, and reference documents.

## Revalidation Triggers

Repeat the baseline after:

- Major Proxmox upgrade
- Host replacement
- Guest migration
- Storage-device replacement
- Filesystem or mount redesign
- Network readdressing
- Samba permission redesign
- Docker host replacement
- Pi-hole migration
- Completion of the Jellyfin deployment

## Related Documentation

- [Proxmox Host Validation](proxmox-host.md)
- [NAS LXC Validation](nas-lxc.md)
- [Docker VM Validation](docker-vm.md)
- [Jellyfin Validation](jellyfin.md)
- [Service Architecture](../architecture/service-architecture.md)
- [Public and Private Information Boundary](../standards/public-private-boundary.md)

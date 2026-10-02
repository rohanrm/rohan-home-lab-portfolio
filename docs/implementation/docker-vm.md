# Docker VM Implementation

| Field | Value |
|---|---|
| Document status | Current |
| System status | Operational |
| Visibility | Public |
| Original commissioning | 2026-07-20 |
| Last reviewed | 2026-10-02 |
| Source of truth for | Sanitized Docker VM implementation record |

## Purpose

This document records the implementation of the dedicated Ubuntu VM used for Docker and Compose workloads.

The VM provides a conventional container platform while keeping Docker away from the Proxmox host and separate from the NAS service.

Exact internal addresses, guest identifiers, MAC addresses, and credentials are maintained privately.

## Starting State

Before the Docker VM was created:

- Proxmox was operational.
- The NAS LXC and Samba service were available.
- Persistent shared storage existed on the NAS.
- No dedicated application host had been deployed.

The required outcome was a stable VM capable of hosting Jellyfin, Immich, and later approved containerized services.

## Design Summary

The application platform uses an Ubuntu VM rather than Docker directly on the Proxmox host or nested inside the NAS LXC.

| Design choice | Reason |
|---|---|
| Full VM | Provides kernel isolation from Proxmox and LXC workloads |
| Ubuntu LTS | Familiar, well-documented Docker platform |
| Docker Engine | Standard container runtime |
| Docker Compose | Declarative multi-container service definitions |
| Local application directories | Separates configuration and cache from disposable containers |
| Samba automount | Gives applications controlled access to NAS media |

## Guest Resources

The validated guest allocation is:

| Resource | Allocation |
|---|---|
| Memory | 4 GB |
| Boot disk | 80 GB |
| Operating system | Ubuntu 24.04 LTS |
| Startup | Enabled through Proxmox guest configuration |

The VM's CPU allocation and exact guest identifier are recorded privately.

## Operating System

The Stage 1 snapshot confirmed:

| Item | Validated state |
|---|---|
| Distribution | Ubuntu |
| Release | 24.04.4 LTS |
| Codename | Noble |
| Architecture | x86-64 |

The VM uses a predictable address in the server zone and the approved Pi-hole resolvers for DNS.

The exact address is not published.

## Base System Preparation

The VM was prepared with:

- Current package updates
- Administrative user access
- Time synchronization
- Network connectivity
- Required CIFS client support
- Docker Engine
- Docker Compose

Representative verification commands are:

```bash
hostname
ip -br addr
lsb_release -a 2>/dev/null || cat /etc/os-release
```

## Docker Installation State

The Stage 1 snapshot confirmed:

| Component | Validated state |
|---|---|
| Docker Engine | 29.6.2 |
| Docker Compose | v5.3.1 |
| Docker service enabled | Yes |
| Docker service active | Yes |

Verify the current installation with:

```bash
docker --version
docker compose version
systemctl is-enabled docker
systemctl is-active docker
```

Versions will change over time and should be updated in the validation record after upgrades.

## Docker Access Model

The administrative user is permitted to manage Docker through the local Docker group.

This is operationally convenient but security-sensitive because access to the Docker daemon is effectively privileged access to the VM.

Group membership should therefore be limited to trusted administrators.

Inspect membership with:

```bash
getent group docker
```

Do not grant Docker access to ordinary service accounts unless a documented requirement exists.

## Application Directory Standard

Persistent configuration remains under a service-specific directory separate from source media and disposable containers. Jellyfin is now deployed; the July prepared-directory/no-container state is historical. The exact active Compose definition must be inspected before updates. See [Jellyfin implementation](jellyfin.md).

## Ownership and Permissions

Application directories are owned by the trusted administrative user and the Docker administration group.

The directory design uses group inheritance so new files remain manageable by the intended administrators.

A representative directory mode is:

```text
drwxrws---
```

This avoids broad world-readable or world-writable access.

## Compose File Standard

Each deployed service should use one clearly named Compose file in its own directory:

```text
/opt/docker/<service>/compose.yaml
```

The service directory should contain only files relevant to that deployment, such as:

```text
compose.yaml
.env.example
config/
cache/
```

Real `.env` files containing secrets must not be committed to Git.

Before deployment, validate a Compose definition with:

```bash
docker compose config
```

List declared services with:

```bash
docker compose config --services
```

## NAS Media Access

The Docker VM accesses NAS media through a persistent Samba systemd automount.

The mounted media path is:

```text
/mnt/nas/media
```

This path is consumed by container bind mounts after the remote share is available.

The VM does not receive the physical disk directly.

See [Samba systemd Automount Implementation](samba-systemd-automount.md).

## Container Storage Principles

The implementation distinguishes three data types:

| Data type | Location | Persistence requirement |
|---|---|---|
| Container image | Docker image store | Re-downloadable |
| Application configuration | Service directory under `/opt/docker` | Must persist and be backed up |
| Cache | Service cache directory | Usually re-creatable |
| Media and user data | NAS-backed storage | Must persist and be protected |
| Secrets | Root-restricted files or secrets system | Must persist outside Git |

Deleting and recreating a container should not delete application configuration or source media.

## Network Exposure Principles

The VM is in the server zone. Jellyfin accepts approved internal access and the Caddy upstream path from the DMZ. Public HTTPS terminates at the proxy rather than exposing Docker administration. Administrative SSH uses keys with password login disabled; QEMU Guest Agent and unattended updates were installed. Exact guest firewall and router policy remain private.

## Service Lifecycle

Common Docker operations are:

```bash
docker ps
docker compose ps
docker compose logs
docker compose up -d
docker compose down
```

These commands must be run from the correct service directory or with an explicit Compose file.

Do not use `docker compose down -v` casually because it may remove named volumes.

## Startup Behaviour

Docker is enabled at boot.

Application containers should use an appropriate restart policy, but restart policy does not replace dependency validation.

A container may start while NAS storage is unavailable. Application validation must therefore confirm:

- The remote mount is available when accessed.
- The expected media path is visible inside the container.
- Failure does not cause the application to write into an unintended empty local directory.

## Security Boundaries

- Docker runs inside a VM rather than on the Proxmox host.
- Docker administration is limited to trusted users.
- Application directories are not world-accessible.
- Remote media access uses a root-restricted credentials file.
- Source media is read-only for Jellyfin.
- Secrets are excluded from Git.
- Application ports are limited to approved internal and reverse-proxy paths.
- The VM receives only the storage paths required by its workloads.

## Backup Requirements

The VM can be rebuilt, but the following must be preserved:

- Compose definitions
- Application configuration
- Required environment templates
- Documentation of secret locations
- Service-specific databases
- Backup and restore procedures

Cache and container images normally do not require backup.

VM-level backup is useful but does not replace application-aware backup and restore validation.

## Rollback

For a failed application deployment:

1. Stop the affected Compose project.
2. Preserve logs and the rejected configuration.
3. Restore the previous Compose definition and configuration backup.
4. Confirm the NAS mount is correct.
5. Start the previous version.
6. Run the service validation checks.

For a Docker platform problem, avoid deleting `/var/lib/docker` or service directories until recovery impact is understood.

## Operational Notes

- Run Compose commands from the correct service directory.
- Use `docker compose config` before deployment.
- Pin versions deliberately when service stability matters.
- Review images before updating production services.
- Confirm storage mounts before application troubleshooting.
- Protect the Docker group as privileged access.
- Keep service configuration separate from source media.

## Lessons Learned

- A running Docker daemon does not mean an application has been deployed.
- Persistent directories alone are preparation, not a completed service.
- Compose files are the rebuild instructions for the application layer.
- Docker inside a VM uses more memory than Docker inside an LXC but provides a simpler and stronger isolation boundary for this lab.
- A test Compose file elsewhere on the host must not be mistaken for the active application definition.

## Validation

See [Docker VM Validation](../validation/docker-vm.md).

## Related Documentation

- [Proxmox Host Implementation](proxmox-host.md)
- [NAS LXC Implementation](nas-lxc.md)
- [Samba systemd Automount Implementation](samba-systemd-automount.md)
- [Jellyfin Implementation](jellyfin.md)
- [Service Architecture](../architecture/service-architecture.md)
- [Docker VM Validation](../validation/docker-vm.md)


## V4 reconciliation

The original build methods above remain useful. Network placement and service inventory have changed since commissioning. Shared storage remains host-owned; source media remains read-only to the application consumer. Guest backups do not by themselves prove coverage of bind-mounted user data. The October 2 storage check was healthy after a USB port move, with continued observation required. See [V4 evidence](../validation/v4-baseline.md).

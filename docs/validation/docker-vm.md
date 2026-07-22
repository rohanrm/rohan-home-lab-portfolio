# Docker VM Validation

| Field | Value |
|---|---|
| Document status | Current |
| Validation status | Passed |
| Validation date | 2026-07-20 |
| Visibility | Public |
| Source of truth for | Docker VM platform, tooling, persistence, and NAS-access validation |

## Purpose

This document records the tests used to confirm that the Docker VM is ready to host Compose-managed applications.

The validation covers:

- Virtual-machine state
- Operating system
- Docker Engine
- Docker Compose
- Docker service startup
- Administrative access
- Persistent application directories
- NAS media automount
- Read-only media access
- Jellyfin readiness boundary

Exact addresses, guest identifiers, credentials, and raw command output remain private.

## Environment

| Item | Validated state |
|---|---|
| Guest type | Virtual machine |
| Operating system | Ubuntu 24.04.4 LTS |
| Memory allocation | 4 GB |
| Primary virtual disk | 80 GB |
| Container runtime | Docker Engine 29.6.2 |
| Compose tooling | Docker Compose v5.3.1 |
| Intended role | Containerized application host |

## Validation Criteria

| ID | Check | Expected result | Status |
|---|---|---|---|
| DKR-01 | VM state | Docker VM is running | Passed |
| DKR-02 | Operating system | Approved Ubuntu LTS release detected | Passed |
| DKR-03 | Docker Engine | Installed and reports expected version | Passed |
| DKR-04 | Docker Compose | Installed and reports expected version | Passed |
| DKR-05 | Docker service | Enabled and active | Passed |
| DKR-06 | Administrative access | Approved user can run Docker commands | Passed |
| DKR-07 | Persistent application root | Controlled application directory exists | Passed |
| DKR-08 | NAS automount | Media share mounts through systemd automount | Passed |
| DKR-09 | Media access | Approved libraries readable and writes rejected | Passed |
| DKR-10 | Jellyfin persistence directories | Configuration and cache directories exist | Passed |
| DKR-11 | Jellyfin deployment | Final Compose service exists and runs | Not Started |

## Validation Procedure

### DKR-01 — VM State

From the Proxmox host:

```bash
qm list
```

Observed result:

- Docker VM listed
- Status reported as running
- Resource allocation matched the approved design

Exact guest ID is retained privately.

Status: `Passed`

### DKR-02 — Operating System

Command:

```bash
lsb_release -a 2>/dev/null || cat /etc/os-release
```

Observed result:

```text
Ubuntu 24.04.4 LTS
Codename: noble
```

Status: `Passed`

### DKR-03 — Docker Engine

Command:

```bash
docker --version
```

Observed result:

```text
Docker version 29.6.2
```

Status: `Passed`

### DKR-04 — Docker Compose

Command:

```bash
docker compose version
```

Observed result:

```text
Docker Compose version v5.3.1
```

Status: `Passed`

### DKR-05 — Docker Service

Commands:

```bash
systemctl is-enabled docker
systemctl is-active docker
```

Observed result:

```text
enabled
active
```

Status: `Passed`

### DKR-06 — Administrative Access

Example checks:

```bash
id
docker info
docker ps
```

Observed result:

- Approved administrative account belonged to the Docker management group.
- Docker commands completed without requiring direct root login.
- No unauthorized broad filesystem permissions were introduced.

Status: `Passed`

### DKR-07 — Persistent Application Root

Example check:

```bash
find /opt/docker -maxdepth 2 -type d -print
```

Observed result:

- Controlled Docker application root existed.
- Jellyfin configuration directory existed.
- Jellyfin cache directory existed.
- Directories used the approved administrative ownership model.

Status: `Passed`

### DKR-08 — NAS Automount

Example checks:

```bash
findmnt <media-mount-point>
systemctl status <media-automount-unit>
```

Observed result:

- systemd automount configuration present
- Remote media share mounted on access
- Mount persisted across reboot testing
- Samba password not embedded directly in `/etc/fstab`

Status: `Passed`

### DKR-09 — Media Access

The Docker-side media account was tested against approved libraries.

Observed result:

| Library | Read | Traverse | Write |
|---|---|---|---|
| Movies | Allowed | Allowed | Rejected |
| Television | Allowed | Allowed | Rejected |
| Music | Allowed | Allowed | Rejected |
| Photos | Rejected | Rejected | Rejected |

Status: `Passed`

### DKR-10 — Jellyfin Persistence Directories

Commands:

```bash
ls -ld /opt/docker/jellyfin
ls -ld /opt/docker/jellyfin/config
ls -ld /opt/docker/jellyfin/cache
```

Observed result:

- Application directory existed.
- Configuration directory existed.
- Cache directory existed.
- Directory group ownership supported the approved Docker administration model.

Status: `Passed`

### DKR-11 — Jellyfin Deployment Boundary

Checks:

```bash
find /opt/docker/jellyfin -maxdepth 1 -type f \
  \( -name 'compose.yaml' \
  -o -name 'compose.yml' \
  -o -name 'docker-compose.yaml' \
  -o -name 'docker-compose.yml' \) \
  -print
```

Observed result:

- No final Compose file existed in the active Jellyfin directory.
- No Jellyfin container was running from that directory.
- A test Compose file found elsewhere was not part of the active deployment.

Status: `Not Started`

This result does not fail the Docker VM validation. It defines the boundary between an operational container host and an application that has not yet been deployed.

## Startup and Dependency Validation

The current dependency chain was confirmed:

```text
Proxmox host
  → NAS LXC
  → Samba
  → Docker VM
  → systemd automount on media access
  → future application containers
```

The Docker service and NAS automount were available after startup testing.

Status: `Passed`

## Security Validation

The platform review confirmed:

- Docker runs inside a VM rather than directly on the Proxmox host.
- Samba credentials are stored in a root-restricted file.
- Application data uses persistent host directories.
- Media access is read-only.
- Photos are unavailable to the Jellyfin service account.
- Exact administrative details are excluded from the public repository.

Status: `Passed`

## Exceptions

| Item | Exception | Impact |
|---|---|---|
| Jellyfin | No active Compose deployment | Application remains In Progress |
| Application backup | Restore testing not complete | Recovery work remains planned |
| Hardware acceleration | Not configured or validated | Transcoding performance remains unproven |
| External access | No approved design | Services remain intended for trusted local access |

## Conclusion

The Docker VM passed platform validation and is operational.

It provides:

- Supported Ubuntu LTS environment
- Active Docker Engine
- Available Docker Compose
- Persistent application directories
- Controlled administrative access
- Persistent, credential-protected NAS automount
- Read-only media access

Jellyfin remains a separate incomplete application deployment.

## Revalidation Triggers

Repeat relevant checks after:

- Ubuntu major upgrade
- Docker Engine major upgrade
- Compose major upgrade
- VM resource change
- Docker data-root change
- Samba credential change
- Automount redesign
- NAS path or permission change
- VM restore or migration
- Introduction of hardware passthrough

## Related Documentation

- [Infrastructure Baseline](infrastructure-baseline.md)
- [Docker VM Implementation](../implementation/docker-vm.md)
- [NAS LXC Validation](nas-lxc.md)
- [Jellyfin Validation](jellyfin.md)
- [Samba Systemd Automount Implementation](../implementation/samba-systemd-automount.md)
- [Service Architecture](../architecture/service-architecture.md)

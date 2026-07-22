# Rohan Home Lab Blueprint

A staged home-lab project focused on Linux administration, virtualization, network services, containerized applications, storage, validation, and maintainable technical documentation.

> **Repository status:** The Version 3 documentation and release-hardening structure are complete. The current technical focus is completing and validating the Jellyfin deployment. Clean-history employer-facing publication remains planned.

## Project Goals

This project demonstrates practical experience with:

- Linux system administration
- Proxmox virtualization
- LXC and virtual-machine design
- Docker Engine and Docker Compose
- Network-attached storage
- Samba file sharing
- DNS filtering
- Service deployment and validation
- Architecture Decision Records
- Operational troubleshooting
- Security-conscious documentation
- Automated documentation quality checks
- Clean-history release preparation

## Current Environment

| Component | Role | Status |
|---|---|---|
| Proxmox host | Virtualization platform | Operational |
| NAS LXC | Storage presentation and Samba services | Operational |
| Docker VM | Container host | Operational |
| Samba automount | Controlled media access from Docker VM | Operational |
| Bare-metal Pi-hole | Network DNS filtering | Operational |
| Jellyfin | Media-service deployment | In Progress |
| Immich | Planned photo-management service | Planned |

Exact internal addresses, hardware identifiers, household-device details, raw command output, and security-sensitive configuration are intentionally maintained outside this public repository.

## Architecture Summary

The environment separates responsibilities across several layers:

1. **Network layer** — routing, DHCP, DNS, and wireless access.
2. **Virtualization layer** — Proxmox hosts the NAS LXC and Docker VM.
3. **Storage layer** — persistent storage is mounted by the Proxmox host.
4. **File-service layer** — the NAS LXC presents approved data through Samba.
5. **Application layer** — the Docker VM runs Compose-managed services.
6. **Documentation layer** — architecture, implementation, validation, operations, and decisions are maintained separately.
7. **Release layer** — automated audits and publication procedures protect the employer-facing repository.

Primary architecture documents:

- [Network Architecture](docs/architecture/network-architecture.md)
- [Physical Topology](docs/architecture/physical-topology.md)
- [Service Architecture](docs/architecture/service-architecture.md)

## Current Technical Baseline

The following infrastructure has been validated:

- Proxmox VE host
- Hardware virtualization and IOMMU
- Internal NVMe storage
- External shared-data storage
- Unprivileged NAS LXC
- Persistent storage bind mounts
- Samba service
- Docker VM
- Docker Engine and Compose
- Root-protected Samba credentials
- Persistent systemd automount
- Read-only media access
- Photo-library isolation

See [Infrastructure Baseline Validation](docs/validation/infrastructure-baseline.md).

## Current Focus

The next technical milestone is completing Jellyfin.

Current preparation includes:

- Operational Docker VM
- Persistent Jellyfin configuration and cache directories
- Operational NAS media automount
- Read access to movies, television, and music
- Write rejection for source media
- No access to the photo library

Remaining work includes:

- Final Compose definition
- Container startup
- Web setup
- Library creation
- Playback testing
- Restart and recreation testing
- Optional hardware-acceleration validation
- Backup-boundary documentation

See:

- [Jellyfin Service](docs/services/jellyfin.md)
- [Jellyfin Implementation](docs/implementation/jellyfin.md)
- [Jellyfin Validation](docs/validation/jellyfin.md)

## Documentation

The complete index is available in [`docs/README.md`](docs/README.md).

| Area | Purpose |
|---|---|
| [`architecture/`](docs/architecture/) | How the environment is designed |
| [`decisions/`](docs/decisions/) | Why significant choices were made |
| [`implementation/`](docs/implementation/) | How components were built |
| [`validation/`](docs/validation/) | How completed work was proven |
| [`services/`](docs/services/) | Service roles, dependencies, and operations |
| [`operations/`](docs/operations/) | Routine administration and troubleshooting |
| [`reference/`](docs/reference/) | Stable hardware, inventory, and policy references |
| [`planning/`](docs/planning/) | Approved work and future exploration |
| [`history/`](docs/history/) | Meaningful project milestones |
| [`standards/`](docs/standards/) | Documentation rules, privacy boundary, and templates |
| [`release/`](docs/release/) | Clean-history publication and release validation |

## Quality and Release Controls

The repository includes:

- [Contributing Guide](CONTRIBUTING.md)
- [Security Policy](SECURITY.md)
- [Permanent Documentation Audit](tools/audit-v3.py)
- [GitHub Actions Audit Workflow](.github/workflows/documentation-audit.yml)
- [Publication Checklist](docs/release/publication-checklist.md)
- [Clean-History Publication Procedure](docs/release/clean-history-publication.md)
- [Repository Release Validation](docs/release/repository-release-validation.md)

Run the local audit with:

```bash
python3 tools/audit-v3.py .
```

## Documentation Principles

This repository follows several core rules:

- Each important fact has one primary source of truth.
- Current and planned states are documented separately.
- Implementation steps and validation evidence are separate.
- Significant design choices are recorded as ADRs.
- Git replaces revision-history tables inside individual documents.
- Public documentation explains technical skill without exposing unnecessary operational detail.
- Secrets are stored outside Git.
- A service is not marked operational until its validation requirements pass.

See:

- [Documentation Standard](docs/standards/documentation-standard.md)
- [Public and Private Information Boundary](docs/standards/public-private-boundary.md)

## Lifecycle Vocabulary

Infrastructure and services use:

```text
Idea
  → Planned
  → In Progress
  → Implemented
  → Validated
  → Operational
```

Additional states are:

- Paused
- Blocked
- Retired
- Rejected

The written status term is authoritative.

## Public and Private Repositories

The public repository contains:

- Sanitized architecture
- Technical reasoning
- Reusable procedures
- Validation methodology
- Operational lessons
- Project planning
- Release controls

A separate private repository contains:

- Exact IP allocations
- MAC addresses
- Serial numbers
- Disk UUIDs
- Client-device records
- Physical port and cable maps
- Raw command output
- Recovery notes
- Detailed security configuration

Passwords, keys, tokens, credential files, and other secrets belong in neither Git repository.

## Publication History Notice

The current Version 3 working tree is sanitized and contains no legacy Version 2 files.

Earlier commits in the development repository may still contain operational details that were later removed. Deleting a file from the current branch does not erase it from Git history.

The employer-facing publication must therefore be created through the documented [Clean-History Publication](docs/release/clean-history-publication.md) process.

## Project Roadmap

See the [Roadmap](docs/planning/roadmap.md) for approved work and [Future Exploration](docs/planning/future-exploration.md) for unapproved ideas.

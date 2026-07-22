# Proxmox Host Implementation

| Field | Value |
|---|---|
| Document status | Current |
| System status | Operational |
| Visibility | Public |
| Last validated | 2026-07-20 |
| Source of truth for | Sanitized Proxmox host implementation record |

## Purpose

This document records how the dedicated virtualization host was prepared for the home lab.

It focuses on the final, reproducible design rather than preserving the original exploratory terminal transcript.

Exact internal addresses, interface identifiers, disk UUIDs, serial numbers, and administrative credentials are maintained privately.

## Starting State

The selected Beelink EQ14 was a new dedicated mini PC intended to become the always-on infrastructure platform.

The required outcome was a stable Proxmox host capable of running:

- An unprivileged NAS LXC
- An Ubuntu Docker VM
- Host-mounted persistent storage
- Future staged services without installing applications directly on the hypervisor

## Design Summary

The final host design uses:

| Layer | Implementation |
|---|---|
| Bare-metal operating environment | Proxmox VE on Debian |
| Host role | Hypervisor, guest lifecycle, storage mounting, and hardware monitoring |
| Guest storage | LVM-backed local storage on the internal NVMe SSD |
| Shared-data storage | External ext4 filesystem mounted by the host |
| DNS | Existing Pi-hole service on the trusted LAN |
| Application hosting | Dedicated Ubuntu VM rather than the Proxmox host |

The host is intentionally kept narrow in scope. Normal self-hosted applications belong inside guests.

## Installation Method

Proxmox VE was installed from bootable installation media created with Ventoy.

The text-based installer was selected after the graphical installer encountered compatibility problems with the Intel N-series display environment.

The installation established:

- The Proxmox system filesystem
- Swap
- LVM-backed guest storage
- A management interface on the trusted LAN
- A stable hostname
- Administrative access to the Proxmox interface

The exact management address and hardware identifiers are recorded privately.

## Initial Repository Configuration

The host was configured to use the appropriate Proxmox no-subscription repository for this non-enterprise home lab.

Enterprise repositories requiring a subscription were disabled to prevent authorization errors during package updates.

The resulting repository policy is:

- Debian repositories enabled
- Proxmox no-subscription repository enabled
- Proxmox enterprise repository disabled
- Enterprise Ceph repository disabled unless a future design explicitly requires Ceph

Repository configuration should be revalidated after a major Proxmox upgrade.

## DNS Configuration

The host was configured to use the operational Pi-hole service for DNS resolution.

Validation confirmed that the host could:

- Resolve package repositories
- Reach the default gateway
- Reach the internet
- Complete package updates

The exact DNS address is retained in the private network record.

## Host Update Procedure

After repository and DNS correction, the host package index and installed packages were updated.

Representative maintenance commands are:

```bash
apt update
apt full-upgrade
```

A reboot should be performed when a new kernel or other host-critical package requires it.

After reboot, confirm the running kernel:

```bash
uname -r
```

## Current Validated Platform

The Stage 1 snapshot confirmed:

| Item | Validated state |
|---|---|
| Proxmox VE package | 9.2 series |
| Proxmox Manager | 9.2.4 |
| Host operating system | Debian GNU/Linux 13 |
| Running kernel | 7.0.14-4-pve |
| Architecture | x86-64 |
| Hardware virtualization | Available |
| IOMMU | Available |

Versions belong in validation records because they will change over time. Architecture documents should not repeat them unnecessarily.

## Internal Storage Layout

The internal 1 TB NVMe SSD contains:

- EFI boot storage
- Proxmox root filesystem
- Swap
- LVM thin storage for guests
- NAS LXC root disk
- Docker VM disks

The public repository documents the role and capacity of this storage without publishing logical-volume identifiers or filesystem UUIDs.

Inspect the current layout with:

```bash
lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINTS,MODEL
pvesm status
```

## External Storage Mount

The shared-data disk uses an ext4 filesystem and is mounted by the Proxmox host.

The host, rather than a guest, owns the physical mount. Selected directories are then bind-mounted into the NAS LXC.

A sanitized persistent mount pattern is:

```fstab
UUID=<private-storage-uuid> <host-storage-mount> ext4 defaults,nofail 0 2
```

The exact UUID and host path are recorded privately.

Validate the mount with:

```bash
findmnt <host-storage-mount>
lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINTS,MODEL
```

## Guest Design

### NAS LXC

The NAS workload runs in an unprivileged LXC because it benefits from:

- Low overhead
- Direct bind mounts
- Fast startup
- A dedicated userspace for Samba and permissions

### Docker VM

Docker runs inside an Ubuntu VM because this provides:

- A conventional Docker environment
- VM-level kernel isolation
- Separation from the Proxmox host
- Separation from the NAS service
- Easier use of standard Docker tooling

The Docker daemon is not installed directly on the Proxmox host.

## Startup Design

The intended startup sequence is:

1. Proxmox host starts.
2. External storage is mounted.
3. NAS LXC starts.
4. Samba becomes available.
5. Docker VM starts.
6. Remote media is mounted on demand.
7. Application containers start or are started after dependencies are available.

Guest startup settings should preserve storage availability before dependent applications attempt access.

## Hardware Validation

The host was checked for:

- CPU virtualization support
- IOMMU availability
- Internal NVMe detection
- External storage detection
- SMART capability
- Ethernet-controller detection
- USB-controller and port behaviour

Exact hardware identifiers and physical port mapping are retained privately.

## Security Boundaries

The implementation follows these controls:

- Proxmox is used only for host and virtualization responsibilities.
- Applications run inside guests.
- The NAS LXC is unprivileged.
- Docker runs inside a VM.
- Administrative interfaces are intended for trusted internal access.
- Exact management details are excluded from the public repository.
- Credentials and private keys are stored outside Git.

## Rollback and Recovery Principles

A full host recovery requires:

1. Reinstalling a compatible Proxmox version.
2. Restoring repository and network configuration.
3. Re-establishing the external storage mount.
4. Restoring guest definitions or backups.
5. Revalidating bind mounts and service dependencies.
6. Restoring application configuration and data according to their own recovery records.

Detailed identifiers and recovery sequencing belong in the private repository.

## Operational Notes

- Update the host separately from application guests.
- Confirm storage before starting dependent services after maintenance.
- Do not disconnect the external disk while mounted.
- Review SMART health and available storage regularly.
- Revalidate repositories after major platform upgrades.
- Avoid installing convenience applications directly on the hypervisor.

## Lessons Learned

- A text-based installer can avoid graphics compatibility issues on newer low-power Intel hardware.
- Repository authorization errors do not necessarily mean the whole installation is broken; they may indicate an enterprise repository is enabled without a subscription.
- DNS must be validated before interpreting package-update failures.
- Host, NAS, and application responsibilities are easier to recover when they are separated deliberately.

## Validation

See [Proxmox Host Validation](../validation/proxmox-host.md).

## Related Documentation

- [ADR-0002 — Select the Beelink EQ14](../decisions/adr-0002-select-beelink-eq14.md)
- [Hardware Profile](../reference/hardware-profile.md)
- [Physical Topology](../architecture/physical-topology.md)
- [Service Architecture](../architecture/service-architecture.md)
- [NAS LXC Implementation](nas-lxc.md)
- [Docker VM Implementation](docker-vm.md)

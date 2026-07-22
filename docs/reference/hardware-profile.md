# Hardware Profile

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-07-21 |
| Source of truth for | Sanitized hardware capabilities and verified platform characteristics |

## Purpose

This document records the hardware capabilities that shape the home-lab architecture.

It intentionally excludes serial numbers, product UUIDs, disk UUIDs, MAC addresses, exact physical port assignments, warranty identifiers, and administrative access details. Those values are retained in the private operational repository when they remain useful.

## Hardware Summary

| Component | Hardware | Role | Status |
|---|---|---|---|
| Virtualization host | Beelink EQ14 mini PC | Runs Proxmox VE and infrastructure guests | Operational |
| System storage | 1 TB NVMe SSD | Proxmox host, guest disks, and local application data | Operational |
| Shared-data storage | 4 TB Seagate IronWolf HDD | Persistent media and shared data | Operational |
| Storage enclosure | UGREEN external enclosure | Connects shared storage to the Proxmox host | Operational |
| Router | GL.iNet Flint 2 | Routing, DHCP, firewall, and current wired aggregation | Operational |
| Wireless access point | UniFi U6-LR | Ethernet-backhauled wireless coverage | Operational |
| DNS host | Raspberry Pi | Bare-metal Pi-hole service | Operational |

## Virtualization Host

### Platform

The Beelink EQ14 is the dedicated, always-on virtualization host.

Its responsibilities are limited to:

- Proxmox VE
- Host-level storage mounting
- Virtual-machine and LXC lifecycle
- Hardware monitoring
- Required host networking

Normal application services are not installed directly on the Proxmox host.

### Processor

The host uses an Intel N-series processor.

Verified characteristics relevant to the lab include:

- x86-64 architecture
- Hardware virtualization support
- IOMMU support
- Integrated graphics
- Intel media-acceleration potential
- Low-power operation suitable for an always-on mini PC

Integrated graphics capability may support Jellyfin hardware acceleration, but this remains a separate implementation and validation task.

### Memory

Installed memory supports the current staged allocation:

| Workload | Current role |
|---|---|
| Proxmox host | Hypervisor and host services |
| NAS LXC | Lightweight storage and Samba services |
| Docker VM | Docker Engine, Compose, and application workloads |
| Remaining capacity | Host overhead and controlled future growth |

Memory is finite. New services should be evaluated before increasing guest allocations or creating additional VMs.

### Internal Storage

The host contains a 1 TB NVMe SSD.

The NVMe device currently supports:

- Proxmox system storage
- Swap
- LVM-backed guest storage
- NAS LXC root disk
- Docker VM disks
- Local Docker application configuration and cache

The public profile documents capacity and role rather than exact logical-volume identifiers or filesystem UUIDs.

### Expansion

The platform provides a path for additional internal storage expansion.

Any future drive should receive:

- A defined purpose
- A backup strategy
- SMART validation
- Mount and ownership documentation
- A decision about host, guest, or application responsibility

## Shared-Data Storage

### Disk

The shared-data disk is a 4 TB Seagate IronWolf HDD.

Its current role includes persistent directories for:

- Media
- Documents
- Downloads
- Shared files

Usable capacity is lower than the manufacturer's decimal capacity because operating systems report capacity differently and filesystems reserve space for metadata.

### Enclosure

The disk is installed in a UGREEN external enclosure connected to the Proxmox host through high-speed USB.

The enclosure creates several design considerations:

- USB connection stability matters.
- The cable must remain secure and unstressed.
- The disk should not be disconnected while mounted.
- The host must mount the filesystem before dependent services use it.
- Enclosure and disk health are separate failure domains.

### Filesystem Ownership

The Proxmox host mounts the physical filesystem.

Selected directories are bind-mounted into the NAS LXC.

The Docker VM does not receive direct ownership of the physical disk.

See [Service Architecture](../architecture/service-architecture.md).

## Networking Hardware

### Flint 2 Router

The GL.iNet Flint 2 currently provides:

- Default-gateway functions
- DHCP
- Network address translation
- Perimeter firewalling
- Wired LAN connections
- Local wireless coverage
- Uplink to the additional access point
- Connectivity for the Proxmox host and Pi-hole host

The router is sufficient for the current single-LAN design.

A managed switch becomes more relevant when the lab requires additional wired ports, VLAN trunking, PoE aggregation, or improved switch-level visibility.

### UniFi U6-LR

The UniFi U6-LR provides additional wireless coverage.

Verified design characteristics include:

- Ethernet backhaul
- Shared LAN access
- Compatibility with future VLAN-based wireless segmentation
- Independent access-point management

The exact device address, MAC address, mounting location, and physical port assignment remain private.

### Ethernet Interfaces

The Beelink EQ14 provides two 2.5 GbE interfaces.

The current design does not require both interfaces simultaneously, but the second interface preserves options for:

- Future segmentation
- Dedicated service paths
- Network experiments
- Recovery from a single interface problem
- Migration toward managed-switch infrastructure

Interface names and physical-port mapping are retained privately.

## USB Capability

The host provides both high-speed and lower-speed USB interfaces.

High-speed USB was verified for the external storage path.

Exact front and rear port mapping is operational information and remains in the private physical-port record.

## Firmware and Platform Validation

The host has been validated for:

- Proxmox installation
- Current booted kernel
- Hardware virtualization
- IOMMU
- NVMe detection
- External storage detection
- Network-interface detection
- USB-interface identification
- SMART monitoring

Exact firmware identifiers, product UUIDs, and serial numbers are excluded from the public repository.

## Current Hardware Constraints

| Constraint | Architectural effect |
|---|---|
| Single virtualization host | NAS and Docker workloads share one hardware failure domain |
| Finite memory | Services must be staged and resource allocations reviewed |
| One primary shared-data disk | Data availability depends on one disk and enclosure |
| USB-attached shared storage | Cable and enclosure reliability matter |
| No managed switch | Segmentation and wired expansion remain limited |
| No dedicated backup appliance | Backup implementation remains future work |
| No UPS documented | Power-loss resilience remains an improvement opportunity |

## Upgrade Principles

Hardware should be added only when a documented need exists.

Before an upgrade:

1. Define the problem.
2. Confirm the current platform cannot solve it safely.
3. Record cost, power, complexity, and recovery impact.
4. Decide whether an ADR is required.
5. Update architecture and inventory documents.
6. Validate the new hardware before placing it into operational use.

## Candidate Future Hardware

The following are possibilities, not installed equipment:

- Managed switch
- Additional NVMe storage
- Dedicated backup storage
- Uninterruptible power supply
- Secondary DNS host
- Additional access point
- Replacement or expansion server

Approved work belongs in the roadmap. Unapproved possibilities belong in future exploration.

## Related Documentation

- [Physical Topology](../architecture/physical-topology.md)
- [Service Architecture](../architecture/service-architecture.md)
- [Inventory Summary](inventory-summary.md)
- [Proxmox Host Validation](../validation/proxmox-host.md)
- [ADR-0002 — Select the Beelink EQ14](../decisions/adr-0002-select-beelink-eq14.md)
- [Public and Private Information Boundary](../standards/public-private-boundary.md)

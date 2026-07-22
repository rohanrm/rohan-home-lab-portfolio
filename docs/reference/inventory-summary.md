# Inventory Summary

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-07-21 |
| Source of truth for | Sanitized infrastructure inventory and lifecycle state |

## Purpose

This document provides an employer-facing inventory of the home-lab infrastructure.

It records component type, role, platform, lifecycle status, and high-level dependency.

It does not publish exact internal addresses, MAC addresses, serial numbers, disk UUIDs, household-member names, phone names, complete client-device lists, or detailed security infrastructure. The complete operational inventory is maintained in the private repository.

## Inventory Scope

### Included

- Core network equipment
- Virtualization platform
- Storage platform
- Infrastructure guests
- Current services
- Approved planned services
- Relevant lifecycle status

### Excluded

- Personal clients
- Smart-home device inventory
- Unknown-device identifiers
- Exact hardware identifiers
- Physical cable and port mapping
- Secrets and access credentials

## Core Infrastructure

| Asset | Platform | Role | Status |
|---|---|---|---|
| ISP gateway | Provider equipment | Provider handoff operating in bridge mode | Operational |
| Router | GL.iNet Flint 2 | Routing, DHCP, firewall, and current wired aggregation | Operational |
| Wireless access point | UniFi U6-LR | Ethernet-backhauled wireless coverage | Operational |
| DNS filtering host | Raspberry Pi | Bare-metal Pi-hole | Operational |
| Virtualization host | Beelink EQ14 | Proxmox VE host | Operational |
| Shared-data storage | Seagate IronWolf HDD in external enclosure | Persistent media and shared data | Operational |

## Virtualization Inventory

| Guest | Type | Role | Status |
|---|---|---|---|
| NAS | Unprivileged LXC | Storage presentation, Linux permissions, and Samba | Operational |
| Docker host | Ubuntu VM | Docker Engine and Compose workloads | Operational |

The public inventory uses role names rather than exact guest identifiers and internal addresses.

## Service Inventory

| Service | Platform | Role | Status |
|---|---|---|---|
| Proxmox VE | Virtualization host | Guest and storage lifecycle | Operational |
| Samba | NAS LXC | Controlled network file sharing | Operational |
| Docker Engine | Docker VM | Container runtime | Operational |
| Docker Compose | Docker VM | Declarative application deployment | Operational |
| Samba systemd automount | Docker VM | Persistent, credential-protected access to NAS media | Operational |
| Pi-hole | Raspberry Pi | DNS filtering | Operational |
| Jellyfin | Docker VM | Media streaming | In Progress |
| Immich | Docker VM | Photo management | Planned |

## Storage Inventory

| Storage | Role | Ownership model | Status |
|---|---|---|---|
| Internal NVMe SSD | Host OS, guest disks, and local application persistence | Proxmox host | Operational |
| External IronWolf HDD | Media, documents, downloads, and shared data | Mounted by Proxmox and presented through the NAS LXC | Operational |
| Jellyfin configuration directory | Application configuration | Docker VM | Prepared |
| Jellyfin cache directory | Re-creatable application cache | Docker VM | Prepared |
| NAS media share | Media access for application workloads | Samba-controlled | Operational |

Exact mount identifiers, filesystem UUIDs, and detailed operational paths are maintained privately where appropriate.

## Current Service Boundary

### Operational

- Routing and DHCP
- Wireless access
- Pi-hole DNS filtering
- Proxmox virtualization
- NAS LXC
- Samba
- Docker VM
- Docker Engine
- Docker Compose
- Persistent Samba automount

### In Progress

- Jellyfin deployment
- Version 3 documentation migration

### Planned

- Immich deployment
- Backup implementation and validation
- Monitoring improvements

### Paused

- Pi-hole migration
- Network segmentation and managed-switch work

### Ideas

- Plex
- Home Assistant
- Additional Proxmox capacity
- Secondary active DNS service
- Dedicated backup appliance
- UPS integration

## Client Inventory Boundary

The public repository does not include a client-by-client asset list.

Private client records may include:

- Primary workstation
- Mobile clients
- Media clients
- Smart-home devices
- Unknown or unclassified clients
- Reservation status
- Owner or household association
- MAC and address information

Only information required for public architecture explanation is published here.

## Lifecycle Vocabulary

| Status | Meaning |
|---|---|
| `Idea` | Worth recording but not approved |
| `Planned` | Approved but not started |
| `In Progress` | Active work is underway |
| `Implemented` | Configuration complete; validation pending |
| `Validated` | Required tests passed |
| `Operational` | Validated and actively used |
| `Paused` | Intentionally deferred |
| `Blocked` | Waiting on an unresolved dependency |
| `Retired` | Removed from active use |
| `Rejected` | Considered and not selected |

## Inventory Maintenance

Update this document when:

- A core asset is added or retired.
- A service changes platform.
- A planned service becomes operational.
- A component's public role changes.
- A new failure dependency becomes architecturally important.

Do not update this public summary merely because a private address, MAC, or serial changes.

## Private Source Records

The private repository is the source of truth for:

- Asset register
- Client devices
- Hardware identifiers
- Exact IP allocations
- MAC addresses
- Physical port map
- Cable map
- Raw infrastructure records

## Related Documentation

- [Hardware Profile](hardware-profile.md)
- [Network Addressing Policy](network-addressing-policy.md)
- [Network Architecture](../architecture/network-architecture.md)
- [Service Architecture](../architecture/service-architecture.md)
- [Service Catalogue](../services/README.md)
- [Public and Private Information Boundary](../standards/public-private-boundary.md)

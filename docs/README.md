# Documentation Index

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Documentation Index |


## Read first

[Network architecture](architecture/network-architecture.md) → [service catalogue](services/README.md) → [dated V4 evidence](validation/v4-baseline.md). The roadmap separates active work, future work, and verification gaps.

V4 retains historical decisions and July commissioning results with explicit labels. Shared documentation is safe for public review; exact private operational notes are excluded from the portfolio.

## Architecture

- [Network Architecture](architecture/network-architecture.md)
- [Physical Topology](architecture/physical-topology.md)
- [Service Architecture](architecture/service-architecture.md)

## Decisions

- [Architecture Decision Records](decisions/README.md)
- [ADR-0001 — Defer Investigation of Unknown Wireless Devices](decisions/adr-0001-defer-unknown-wireless-devices.md)
- [ADR-0002 — Select the Beelink EQ14 as the Proxmox Host](decisions/adr-0002-select-beelink-eq14.md)
- [ADR-0003 — Segment the Network](decisions/adr-0003-segment-network.md)
- [ADR-0004 — Always-On Controller and Independent DNS](decisions/adr-0004-always-on-controller-and-independent-dns.md)

## History

- [Changelog](history/changelog.md)

## Implementation

- [Caddy DMZ Implementation](implementation/caddy-dmz.md)
- [Docker VM Implementation](implementation/docker-vm.md)
- [Guest DNS Analytics Implementation](implementation/guest-dns-analytics.md)
- [Jellyfin Implementation](implementation/jellyfin.md)
- [NAS LXC Implementation](implementation/nas-lxc.md)
- [Network Segmentation Implementation](implementation/network-segmentation.md)
- [Pi-hole Migration](implementation/pihole-migration.md)
- [Proxmox Host Implementation](implementation/proxmox-host.md)
- [Samba systemd Automount Implementation](implementation/samba-systemd-automount.md)
- [UniFi Controller Migration](implementation/unifi-controller.md)

## Operations

- [Operations Guide](operations/operations-guide.md)
- [Troubleshooting Guide](operations/troubleshooting.md)

## Planning

- [Future Exploration](planning/future-exploration.md)
- [Roadmap](planning/roadmap.md)

## Reference

- [Hardware Profile](reference/hardware-profile.md)
- [Inventory Summary](reference/inventory-summary.md)
- [Network Addressing Policy](reference/network-addressing-policy.md)

## Release

- [Release Documentation](release/README.md)
- [Separated-History Publication](release/clean-history-publication.md)
- [Pruning Recommendations](release/pruning-recommendations.md)
- [Publication Checklist](release/publication-checklist.md)
- [Repository Release Validation](release/repository-release-validation.md)

## Services

- [Service Catalogue](services/README.md)
- [Caddy Reverse Proxy](services/caddy.md)
- [Guest DNS Analytics](services/guest-dns-analytics.md)
- [Jellyfin](services/jellyfin.md)
- [Monitoring and Backup Visibility](services/monitoring.md)
- [Pi-hole](services/pihole.md)
- [Samba](services/samba.md)
- [UniFi Controller](services/unifi-controller.md)

## Standards

- [Documentation Standard](standards/documentation-standard.md)
- [Public and Private Information Boundary](standards/public-private-boundary.md)
- [Architecture Title](standards/templates/architecture-template.md)
- [ADR-0000 — Decision Title](standards/templates/decision-template.md)
- [Component Implementation](standards/templates/implementation-template.md)
- [Service Name](standards/templates/service-template.md)
- [Component Validation](standards/templates/validation-template.md)

## Validation

- [Docker VM Validation](validation/docker-vm.md) — historical commissioning record
- [Infrastructure Baseline Validation](validation/infrastructure-baseline.md) — historical commissioning record
- [Jellyfin Validation](validation/jellyfin.md)
- [NAS LXC Validation](validation/nas-lxc.md) — historical commissioning record
- [Proxmox Host Validation](validation/proxmox-host.md) — historical commissioning record
- [V4 Evidence Baseline](validation/v4-baseline.md)

## Release review

- [File-by-file V3 audit](release/v4-document-audit.md)
- [Pruning recommendations](release/pruning-recommendations.md)

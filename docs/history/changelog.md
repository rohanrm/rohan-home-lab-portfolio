# Changelog

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Changelog |



## 2026-10-02 — V4 architecture reconciliation

Reconciled private V3 and public portfolio documents with the segmented network, primary DNS LXC/physical secondary, running Jellyfin, DMZ proxy, always-on controller, and monitoring. Added dated evidence limits, refreshed all architecture illustrations, a new portfolio landing page, a file-by-file audit, pruning recommendations, and a public/private-aware V4 checker.

The same day's project evidence confirmed six-workload backup presence and a healthy storage check after a USB port move. Storage observation and restore validation remain open.

## September 2026 — Segmentation, controller and observability

Phase 10 established managed switching, VLAN roles, host/AP trunks and required service paths. Caddy operated in the DMZ with externally validated media access. September 20–21 controller records established cutover to a dedicated VM and a verified final backup. Monitoring and the guest DNS archive/enrichment project expanded.

## July 2026 — Infrastructure and documentation foundation

Proxmox, NAS permissions, Docker, and persistent Samba automount were commissioned. The original media-service preparation record preceded the later running deployment. Primary Pi-hole was migrated using a verified configuration export and clean LXC installation.

The V3 documentation system and separate employer-facing history were published in July. Original editorial batch details remain available in Git rather than duplicated in the landing-page narrative.

See [V4 baseline](../validation/v4-baseline.md), [decisions](../decisions/README.md), and [roadmap](../planning/roadmap.md).

# V4 Document Audit

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | V3 file disposition and cross-reference review |

## Source inventory

The private blueprint `docs-v3-redesign` and public portfolio `main` each contained **48 files with matching paths and blob content**. Every source file is accounted for below. There were no Version 2 legacy paths or existing bitmap assets in either source tree.

The review compared architecture, placement, inventory, service status, implementation, dated evidence, roadmap, decisions, publication standards and automation against project records through October 2. Obsolete active claims about a flat LAN, deferred VLAN/DNS work, and an absent Jellyfin container were corrected. July tests remain dated historical evidence rather than retrospectively updated passes.

## File-by-file disposition

| Source path | Disposition | V4 treatment |
|---|---|---|
| `.github/pull_request_template.md` | Updated | Updated V4 workflow references and maintained privacy/security requirements |
| `.github/workflows/documentation-audit.yml` | Updated | Updated branch trigger and separate public/private validation modes |
| `.gitignore` | Updated | Removed obsolete test entry; excluded caches and secret-bearing environment files |
| `.markdownlint.json` | Retained | Retained valid Markdown configuration; no architecture facts present |
| `CONTRIBUTING.md` | Updated | Updated V4 workflow references and maintained privacy/security requirements |
| `README.md` | Updated | Rebuilt employer-facing landing page with visual architecture, skills, outcomes and evidence limits |
| `SECURITY.md` | Updated | Updated V4 workflow references and maintained privacy/security requirements |
| `docs/README.md` | Updated | Reconciled with the V4 architecture and evidence boundary |
| `docs/architecture/network-architecture.md` | Updated | Reconciled with the V4 architecture and evidence boundary |
| `docs/architecture/physical-topology.md` | Updated | Reconciled with the V4 architecture and evidence boundary |
| `docs/architecture/service-architecture.md` | Updated | Reconciled with the V4 architecture and evidence boundary |
| `docs/decisions/README.md` | Updated | Reconciled with the V4 architecture and evidence boundary |
| `docs/decisions/adr-0001-defer-unknown-wireless-devices.md` | Updated | Preserved original decision reasoning; linked later architectural decisions |
| `docs/decisions/adr-0002-select-beelink-eq14.md` | Updated | Preserved original decision reasoning; linked later architectural decisions |
| `docs/history/changelog.md` | Updated | Reconciled with the V4 architecture and evidence boundary |
| `docs/implementation/docker-vm.md` | Updated | Preserved implementation methods; updated routed placement, service state and recovery limits |
| `docs/implementation/jellyfin.md` | Updated | Reconciled with the V4 architecture and evidence boundary |
| `docs/implementation/nas-lxc.md` | Updated | Preserved implementation methods; updated routed placement, service state and recovery limits |
| `docs/implementation/proxmox-host.md` | Updated | Preserved implementation methods; updated routed placement, service state and recovery limits |
| `docs/implementation/samba-systemd-automount.md` | Updated | Preserved implementation methods; updated routed placement, service state and recovery limits |
| `docs/operations/operations-guide.md` | Updated | Reconciled with the V4 architecture and evidence boundary |
| `docs/operations/troubleshooting.md` | Updated | Preserved commissioning knowledge base, dated obsolete examples, added current incident lessons |
| `docs/planning/future-exploration.md` | Updated | Reconciled with the V4 architecture and evidence boundary |
| `docs/planning/roadmap.md` | Updated | Reconciled with the V4 architecture and evidence boundary |
| `docs/reference/hardware-profile.md` | Updated | Reconciled with the V4 architecture and evidence boundary |
| `docs/reference/inventory-summary.md` | Updated | Reconciled with the V4 architecture and evidence boundary |
| `docs/reference/network-addressing-policy.md` | Updated | Reconciled with the V4 architecture and evidence boundary |
| `docs/release/README.md` | Updated | Reconciled with the V4 architecture and evidence boundary |
| `docs/release/clean-history-publication.md` | Updated | Reconciled with the V4 architecture and evidence boundary |
| `docs/release/publication-checklist.md` | Updated | Reconciled with the V4 architecture and evidence boundary |
| `docs/release/repository-release-validation.md` | Updated | Reconciled with the V4 architecture and evidence boundary |
| `docs/services/README.md` | Updated | Reconciled with the V4 architecture and evidence boundary |
| `docs/services/jellyfin.md` | Updated | Reconciled with the V4 architecture and evidence boundary |
| `docs/services/pihole.md` | Updated | Reconciled with the V4 architecture and evidence boundary |
| `docs/services/samba.md` | Updated | Reconciled with the V4 architecture and evidence boundary |
| `docs/standards/documentation-standard.md` | Updated | Updated V4 workflow references and maintained privacy/security requirements |
| `docs/standards/public-private-boundary.md` | Updated | Updated V4 workflow references and maintained privacy/security requirements |
| `docs/standards/templates/architecture-template.md` | Updated | Reviewed reusable template; added evidence and visual guidance |
| `docs/standards/templates/decision-template.md` | Updated | Reviewed reusable template; added evidence and visual guidance |
| `docs/standards/templates/implementation-template.md` | Updated | Reviewed reusable template; added evidence and visual guidance |
| `docs/standards/templates/service-template.md` | Updated | Reviewed reusable template; added evidence and visual guidance |
| `docs/standards/templates/validation-template.md` | Updated | Reviewed reusable template; added evidence and visual guidance |
| `docs/validation/docker-vm.md` | Updated | Retained dated July evidence; marked historical and linked to V4 results |
| `docs/validation/infrastructure-baseline.md` | Updated | Retained dated July evidence; marked historical and linked to V4 results |
| `docs/validation/jellyfin.md` | Updated | Reconciled with the V4 architecture and evidence boundary |
| `docs/validation/nas-lxc.md` | Updated | Retained dated July evidence; marked historical and linked to V4 results |
| `docs/validation/proxmox-host.md` | Updated | Retained dated July evidence; marked historical and linked to V4 results |
| `tools/audit-v3.py` | Updated | Converted frozen V3 checker into a compatibility wrapper for V4 |

## New coverage

- Implementation records: network segmentation, primary DNS migration, UniFi migration, Caddy DMZ, guest DNS analytics.
- Service records: Caddy, UniFi, monitoring/backup visibility, guest DNS analytics.
- Evidence: dated V4 baseline and explicitly limited Jellyfin result matrix.
- Decisions: retrospective records for segmentation and always-on controller/independent DNS.
- Release review: this audit, pruning recommendations and public/private-aware V4 automation.
- Visual assets: seven self-contained SVG illustrations with accessible text alternatives.

## Diagram reconciliation

All seven original Mermaid blocks were replaced with the shared SVG visual system. Network, DNS, physical, service placement, monitoring, analytics and the README hero now have distinct illustrations. The previous planned Immich target diagram was removed from current architecture because it was not an installed service.

## Limits

This reconciles the source tree and project records. It does not claim a new live system audit, forensic scan of all Git history, final analytics counters, a full restore, completed GPU transcoding, or long-term USB stability. The separate existing private operations repository was not modified.

See [V4 baseline](../validation/v4-baseline.md), [pruning](pruning-recommendations.md), and [documentation index](../README.md).

## Post-publication cleanup

The table above records the initial V4 reconciliation. Later archive moves and removals are recorded in [publication cleanup](cleanup-record.md); it is not an inventory of current paths.

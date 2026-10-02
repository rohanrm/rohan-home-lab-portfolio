# V4 Evidence Baseline

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | V4 Evidence Baseline |



## Scope and evidence cutoff

This is a documentation reconciliation using dated project records through **2026-10-02**, not a new live audit. It updates the July baseline without inventing new runtime tests. The older commissioning records are retained and explicitly marked historical.

| Area | Recorded observation | Period | Conclusion and limits |
|---|---|---|---|
| Network | Managed switch persistence, VLAN routing, host tags, SSID separation and required service paths checked | Phase 10, September | Segmented architecture in service; public policy matrix intentionally omitted |
| DNS | Clean LXC installation, configuration restore and service checks; later dual-DNS routing | July migration / September network changes | Primary LXC and physical secondary established; synchronized failover not claimed |
| Jellyfin / DMZ | Healthy Docker service and externally validated proxy access | By September | July not-deployed wording superseded; GPU/restore outcomes not established |
| UniFi | AP connected to new controller after old-controller rules removed; final backup checksum verified | September 20–21 | Dedicated VM cutover established |
| Host metrics | Listener and permitted exporter scrape path corrected | September monitoring work | Host monitoring path established |
| Guest analytics | Guest-only snapshot import; repeated import added zero rows; later capture/enrichment and batch-4 report | September 28–October 2 | Snapshot analytics established; final counters, continuous ingestion and dashboard not asserted |
| Backup visibility | Successful fresh archives for six workloads, six age panels and 6 / 6 PRESENT; dashboard JSON export verified | October 2 | Archive presence and telemetry established; restoration not proved |
| Storage | SMART passed; post-port-move data/bind mounts and Samba active; 5 Gbit/s USB; no new errors at check | October 2 | Healthy point-in-time check; sustained stability still open |
| UPS | CyberPower unit present, USB preflight recorded | September | Hardware established; NUT shutdown/outage test unconfirmed |

## What remains unverified

No claim is made here for a complete restore exercise, coverage of NAS bind-mounted datasets by guest backups, hardware-accelerated Jellyfin transcoding, alert delivery, automated DNS synchronization, controlled resolver failover, continuous DNS collection, or completed analytics dashboard.

## Repeatable validation method

For each change, capture the current configuration privately; define both required access and denied access; change one layer; verify the original client-facing behavior; record commands, time, expected result, observed result, and exceptions. Sanitize evidence before public publication. A diagram depicts documented architecture, not a measured connectivity result.

Use separate checks for router/switch persistence, host networking, guest services, source filesystem, permissions, client experience, telemetry freshness, and restoration. Test as the real service identity rather than only as root. Store sensitive raw outputs and logs in protected evidence storage.

## Historical references

- [July infrastructure commissioning](../../archive/commissioning-2026-07/infrastructure-baseline.md)
- [Proxmox commissioning](../../archive/commissioning-2026-07/proxmox-host.md)
- [NAS commissioning](../../archive/commissioning-2026-07/nas-lxc.md)
- [Docker commissioning](../../archive/commissioning-2026-07/docker-vm.md)
- [Current Jellyfin validation limits](jellyfin.md)
- [Roadmap acceptance work](../planning/roadmap.md)

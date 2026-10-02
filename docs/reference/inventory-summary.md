# Inventory Summary

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Inventory Summary |



## Functional inventory

| Layer | Current components | State |
|---|---|---|
| Network edge | Bridged provider gateway, Flint 2 | Operational |
| Wired network | Managed M4100, VLAN trunks and access ports | Operational |
| Wireless | U6-LR, trusted/IoT/guest SSIDs | Operational |
| Compute | Proxmox on EQ14, six hosted workloads | Operational |
| Storage | NVMe system/guest storage, ext4 shared-data HDD | Operational; USB observation open |
| DNS | Pi-hole LXC plus physical secondary | Operational |
| Applications | Docker VM with Jellyfin | Operational |
| External service entry | Caddy DMZ proxy | Operational |
| Management | Dedicated UniFi controller VM | Operational |
| Observability | Grafana, Prometheus, host exporter, six-workload backup dashboard | Operational |
| Analytics | Guest-only SQLite DNS import and enrichment | In Progress |
| Power protection | CyberPower UPS | Installed; shutdown validation unconfirmed |

## Scope

This inventory lists roles rather than client identities. It does not expose guest IDs, addresses, household-device names, exact switch ports, or monitoring URLs. The service catalogue is authoritative for workload lifecycle; the private companion contains exact infrastructure assignments.

## Planned versus installed

Immich, new compute hardware, a larger data disk, router VPN egress refinements, and completion of DNS analytics remain future work. Do not treat a shopping comparison, prepared directory, or hardware capability as deployment evidence.

See [service catalogue](../services/README.md), [hardware profile](hardware-profile.md), and [roadmap](../planning/roadmap.md).

# Roadmap

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Roadmap |



## Completed architecture changes

| Workstream | State | Recorded outcome |
|---|---|---|
| Proxmox, NAS, Docker | Operational | Separated compute/storage/application roles |
| Jellyfin and Caddy | Operational | Container running; external proxy access validated |
| Segmentation | Operational | Managed switch, routed VLAN zones, tagged host/AP uplinks |
| Primary DNS migration | Operational | LXC resolver plus physical secondary |
| UniFi migration | Operational | Dedicated VM; AP connected after cutover |
| Monitoring | Operational | Grafana/Prometheus and host exporter path |
| Backup presence monitoring | Operational | All six hosted workloads displayed and fresh |

## Active work and verification gaps

| Item | Status | Next acceptance criterion |
|---|---|---|
| Guest DNS analytics | In Progress | Confirm final mapping counts, continuous collection and reporting separately |
| Storage USB stability | In Progress | Complete observation period without disconnect/reset/I/O errors |
| Backup restoration | Planned | Isolated restore yields usable data and working service |
| NAS user-data coverage | Needs verification | Confirm independent copies include host bind-mounted datasets |
| Jellyfin acceleration | Planned | Real transcode shows intended hardware path and stable fallback |
| Dual DNS resilience | Needs verification | Controlled resolver outage and configuration consistency checks |
| UPS/NUT shutdown | Needs verification | Record installed configuration and safe shutdown/recovery tests |
| Personal-device reservations | Planned | Verify stable device identity and free addresses, then reserve centrally |
| Router VPN egress / exceptions | Planned | Verify default and exception paths without disrupting workplace VPN |
| Immich | Planned | Approve storage/privacy/restore design before importing photos |

Needs verification is a task description, not a service lifecycle promotion. Unknown results remain unknown.

## Capacity evaluation

Additional compute, RAM, and a larger IronWolf remain evaluation topics. Purchases, clustering, RAID, and high availability are not implemented outcomes. Stabilize existing storage and define backup coverage before expanding irreplaceable data.

## Acceptance rule

Installation, successful backup jobs, and hardware capability each prove a limited result. Promote a service or test only after its defined checks pass. The dated [V4 baseline](../validation/v4-baseline.md) controls evidence claims; the [service catalogue](../services/README.md) controls lifecycle status.

See [future exploration](future-exploration.md) and [pruning recommendations](../release/pruning-recommendations.md).

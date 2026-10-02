# Service Architecture

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Service Architecture |



## Workload separation

Proxmox now hosts six infrastructure workloads. Samba, primary DNS, monitoring, and Caddy are separated into LXCs; Docker applications and UniFi run in VMs. A physical Pi-hole remains outside the hypervisor failure domain.

![Six Proxmox workloads grouped by infrastructure, application and edge roles, with physical secondary DNS outside the host](../../assets/diagrams/services.svg)

## Placement and dependencies

| Workload | Platform | Role | Important dependency |
|---|---|---|---|
| Caddy | DMZ LXC | TLS reverse proxy | DNS/certificate issuance and approved Jellyfin upstream |
| NAS / Samba | Unprivileged LXC | Controlled storage presentation | Host-mounted shared-data disk |
| Docker / Jellyfin | Ubuntu VM | Media application | Read-only NAS media and persistent local configuration |
| Primary Pi-hole | Debian LXC | DNS filtering | Network and upstream resolution |
| Monitoring | LXC | Prometheus, Grafana, backup visibility | Reachable exporters and fresh observations |
| UniFi controller | Debian VM | AP management | AP-to-controller routed connectivity |
| Secondary Pi-hole | Physical host | Independent DNS endpoint | Network and upstream resolution |

The [service catalogue](../services/README.md) owns lifecycle status. This diagram depicts placement, not broad network permission between workloads.

## Persistent data

The hypervisor mounts the shared disk. The NAS binds selected directories and serves them through Samba. The Docker VM uses a credential-protected systemd automount. Jellyfin receives movies, television, and music as read-only libraries; photos stay outside its access boundary.

Application configuration and databases persist independently of disposable containers. Raw DNS history and enrichment data live in a separate restricted collector area on the monitoring guest. They are private operational data and are excluded from public artifacts.

## Observability and backups

Prometheus and Grafana are operational. The host node-exporter listener and its permitted monitoring path were corrected. The Backup Status dashboard now displays six protected workloads, individual backup ages, and an overview. Fresh archives were confirmed for all six on October 2.

That proves backup presence and telemetry freshness, not successful restoration or inclusion of bind-mounted NAS user data. Shared-disk backups on the same physical disk also remain in the same failure domain. See [backup and monitoring](../services/monitoring.md).

## DNS analytics

Guest-only Pi-hole snapshots have been imported into a dedicated SQLite database with deduplication and domain classification. Exact-hostname and base-domain service rules allow related infrastructure names to be grouped. This is an active analytics project, not proof of continuous collection or a finished reporting dashboard. DNS queries show name-resolution activity, not confirmed page visits.

## Remaining constraints

Memory and a single hypervisor limit growth. GPU capability does not prove hardware transcoding is working. Restore testing, long-term USB stability, DNS configuration synchronization, and remaining analytics delivery are explicitly tracked in the [roadmap](../planning/roadmap.md).

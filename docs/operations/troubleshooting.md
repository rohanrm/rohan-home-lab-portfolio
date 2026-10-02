# Troubleshooting Guide

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Current dependency-aware troubleshooting |

## Diagnose the failed boundary

Read current state first. Record the symptom and time, identify the lowest failed dependency, change one layer, and re-test the original client behavior. Preserve identifying logs privately. Do not grant broad permissions or unrestricted inter-zone access to make a test pass.

| Symptom | Inspect first | Verify after correction |
|---|---|---|
| Routed service unreachable | Client zone, guest tag, switch membership, gateway and required policy | Intended access plus prohibited access from the actual client network |
| DNS fails | Both resolver endpoints, FTL, upstream path and DHCP settings | Direct lookup/filtering on each resolver and the client path |
| Controller/AP disconnected | Controller VM availability and AP communication | AP connected state plus wireless service on each SSID |
| NAS share empty/unavailable | Host data mount, USB errors, bind mounts and Samba | Real backing filesystem, expected content and account permissions |
| Media cannot play | CIFS mount, container paths, real service identity and logs | Representative playback, write rejection and photo exclusion |
| Proxy access fails | Internal upstream, Caddy validation, TLS and external route | Authenticated access from an external network |
| Exporter/metrics missing | Listener, routed scrape path and Prometheus target | Fresh series rather than a cached dashboard |
| Backup workload missing | Actual archives, collector inventory and dashboard queries | Correct per-workload age, overview and protected count |
| Analytics totals inflate | Snapshot provenance and unique event keys | Repeated import adds zero; new events remain distinguishable |

## Read-only diagnostics

Run each check on its appropriate system; substitute locally verified values:

```bash
pct list
qm list
findmnt <shared-data-mount>
systemctl is-active <service>
journalctl -u <service> --since "30 minutes ago"
```

From the active application directory inspect `docker compose ps` and logs. Inspect kernel USB/filesystem errors before restarting storage consumers. SMART health and transport stability are separate checks.

## Stop and investigate

Unexpected write access by a read-only account, lost mounts, repeated I/O errors, restarts, or credentials in Git require investigation before unrelated changes. Restore known-good configuration where appropriate and verify the complete dependency chain.

## Historical examples

Older installation and commissioning incidents are retained in [the historical troubleshooting archive](../../archive/commissioning-2026-07/troubleshooting.md). The old no-container Jellyfin example is not current service status.

See [operations](operations-guide.md), [V4 evidence](../validation/v4-baseline.md), and [service catalogue](../services/README.md).

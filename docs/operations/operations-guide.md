# Operations Guide

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Operations Guide |



## Dependency-aware maintenance

Start routing/switching and the physical DNS host before dependent network clients. Confirm host storage before NAS bind mounts; confirm Samba before media consumers. DNS, proxy, monitoring, and controller workloads each need their own checks. Stop application consumers before taking storage down.

## Read-only health checks

On Proxmox:

```bash
pveversion
pct list
qm list
pvesm status
free -h
findmnt <shared-data-mount>
```

On the appropriate service guest:

```bash
systemctl is-active smbd
systemctl is-active pihole-FTL
systemctl is-active caddy
systemctl is-active prometheus
systemctl is-active grafana-server
```

These are checks on different guests, not one combined command to run on every system. Inspect Docker state/logs from its active Compose directory. Test both DNS endpoints directly and inspect Prometheus targets, backup ages, controller/AP state, and required client behavior.

## Update workflow

Read current state, capture protected configuration and rollback material, change one layer, then verify required and denied behavior. Review release notes before selecting updates. Keep host changes separate from guest changes and update one DNS resolver at a time. Treat the Docker administration group as privileged access.

## Backup and restoration

Six guest backups and dashboard coverage are recorded. Confirm NAS bind-mounted user data has independently verified coverage and protected copies. Test restoration in an isolated environment, checking data, permissions, configuration, and usable service access. Do not equate green backup-age panels with restore readiness.

## Storage issue observation

After the October USB port change, retain the same configuration during the observation window. Inspect transport errors, data mount, bind mounts, and Samba before declaring success. Stop consumers and unmount safely before moving storage. A healthy SMART check does not establish a healthy cable/enclosure path.

## Documentation and privacy

Update implementation, dated validation, service lifecycle, architecture, and roadmap according to the facts that changed. Keep exact production allocations and useful diagnostics private; keep passwords, keys, tokens, credential files, and sensitive backups outside Git. Run the V4 audit before publication.

See [troubleshooting](troubleshooting.md), [service catalogue](../services/README.md), [V4 baseline](../validation/v4-baseline.md), and [release checklist](../release/publication-checklist.md).

# Future Exploration

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Future Exploration |



## Candidate ideas

| Idea | Reason to evaluate | Entry requirement |
|---|---|---|
| Additional compute / RAM | Capacity headroom | Measured workload pressure and maintenance budget |
| Larger storage | More persistent data | Data migration and independent backup plan |
| Home Assistant | Local automation | Concrete integration need and constrained network access |
| Alternate media platform | Client compatibility | Demonstrated Jellyfin limitation |
| Off-site / disconnected copies | Storage-loss resilience | Encryption, retention, and successful restore |
| Additional AP | Coverage improvements | Measurements showing a coverage gap |
| More documentation automation | Better release confidence | Useful checks that do not invent validation evidence |

These are ideas rather than installed systems. DNS migration, managed switching, VLANs, remote media access, and Grafana/Prometheus are no longer future ideas; they are documented in current architecture. Installed UPS hardware does not prove NUT automation.

Evaluate operational value, failure domains, permissions, data sensitivity, resources, backups, and rollback before promoting an idea. Approved work belongs in the [roadmap](roadmap.md); architectural decisions belong in the [ADR index](../decisions/README.md).

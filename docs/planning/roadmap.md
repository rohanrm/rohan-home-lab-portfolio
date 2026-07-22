# Roadmap

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-07-22 |
| Source of truth for | Approved project work, sequencing, and current focus |

## Purpose

This roadmap records approved work and its current lifecycle state.

It separates completed or operational outcomes, active implementation work, approved planned work, paused work, and unapproved ideas.

Unapproved possibilities belong in [Future Exploration](future-exploration.md).

## Current Focus

The immediate technical priority is:

> Complete the Jellyfin Compose deployment and validate startup, persistence, media access, playback, and recovery behaviour.

The immediate release priority is:

> Use the completed publication controls to create and validate a fresh clean-history employer-facing repository.

## Status Summary

| Workstream | Status | Current outcome |
|---|---|---|
| Network discovery and initial documentation | Operational | Core roles and architecture documented |
| Proxmox platform | Operational | Dedicated virtualization host in service |
| NAS LXC | Operational | Persistent storage presented through an unprivileged LXC |
| Samba | Operational | Controlled file sharing available |
| Docker VM | Operational | Docker Engine and Compose ready |
| Samba systemd automount | Operational | Docker VM can access approved NAS media |
| Version 3 public documentation | Operational | Sanitized structure and current records completed |
| Documentation release controls | Operational | Audit, workflow, policies, and release procedures completed |
| Clean-history employer publication | Planned | New public repository not yet created |
| Private operational documentation | In Progress | Exact values and recovery records maintained separately |
| Jellyfin | In Progress | Platform and storage prerequisites ready; application deployment incomplete |
| Immich | Planned | Begins after Jellyfin is stable |
| Backup implementation | Planned | Requires design, execution, and restore validation |
| Monitoring improvements | Planned | Follows core application deployment |
| Pi-hole migration | Paused | Bare-metal service remains operational |
| VLAN and managed-switch work | Paused | Deferred until core services are stable |

## Milestone 1 — Discovery and Documentation Foundation

**Status:** Operational

### Outcomes

- Core network roles identified
- Initial physical and logical topology documented
- Addressing philosophy established
- Major hardware recorded
- Early architecture decisions captured
- Project work organized into stages

## Milestone 2 — Proxmox Platform

**Status:** Operational

### Outcomes

- Dedicated Beelink host deployed
- Proxmox installed and updated
- Hardware virtualization verified
- IOMMU verified
- Internal storage validated
- Network interfaces validated
- External storage detected
- SMART monitoring established

## Milestone 3 — NAS and Samba

**Status:** Operational

### Outcomes

- Unprivileged NAS LXC deployed
- Persistent host directories bind-mounted
- Linux users, groups, and permissions configured
- Samba installed and enabled
- Approved media readable
- Source-media writes rejected
- Photo-library access rejected for the media-service account

## Milestone 4 — Docker Platform

**Status:** Operational

### Outcomes

- Ubuntu VM deployed
- Docker Engine installed
- Docker Compose installed
- Docker service enabled
- Persistent application directory structure created
- Samba credential file protected
- Persistent systemd automount completed
- NAS media access verified

## Milestone 5 — Version 3 Public Documentation

**Status:** Operational

### Outcomes

- Current-state snapshot validated
- Public/private information boundary approved
- Version 3 structure implemented
- Architecture and ADR records completed
- Implementation and validation records completed
- Service and operations records completed
- Reference and planning records completed
- Legacy Version 2 files removed from the current working tree
- README, index, roadmap, and changelog finalized

## Milestone 6 — Documentation Release Hardening

**Status:** Operational

### Outcomes

- Permanent repository audit tool added
- Read-only GitHub Actions audit workflow added
- Markdown configuration added
- Contribution workflow documented
- Security reporting and accidental-exposure response documented
- Pull-request review template added
- Publication checklist added
- Clean-history publication procedure added
- Release-validation record added

### Completion Criteria

- Local audit passes.
- Workflow configuration uses read-only permissions.
- Release process does not copy development Git history.
- Publication guidance keeps private repositories separate.
- New release documents are linked from the repository index.
- Release validation remains `Not Started` until a new public repository exists.

## Milestone 7 — Clean-History Employer Publication

**Status:** Planned

### Entry Conditions

- Public Batch 9 committed and pushed
- Development branch clean
- Local documentation audit passes
- GitHub Actions audit passes
- Publication checklist reviewed
- New empty public repository created

### Planned Outcomes

- Export tracked Version 3 files
- Audit the export
- Initialize a new Git repository
- Create one clean publication commit
- Push to the new employer-facing repository
- Confirm repository visibility
- Confirm remote workflow passes
- Complete the release-validation record

### Completion Criteria

- New public repository contains only sanitized Version 3 content.
- Commit history begins with the clean publication commit.
- No development commits appear.
- No private or legacy files appear.
- GitHub Actions audit passes.
- Repository release validation passes.

## Milestone 8 — Jellyfin

**Status:** In Progress

### Current State

- Docker host is operational.
- Persistent configuration and cache directories exist.
- NAS media automount is operational.
- Approved media is readable and non-writable.
- Photos are inaccessible.
- No final Compose definition exists in the active Jellyfin directory.
- No Jellyfin container is currently running.

### Next Actions

1. Create the final Compose definition.
2. Confirm service identity and permissions.
3. Render the Compose configuration.
4. Pull the approved image.
5. Start the container.
6. Review logs.
7. Complete browser setup.
8. Add media libraries.
9. Test representative playback.
10. Test restart and recreation persistence.
11. Evaluate hardware acceleration separately.
12. Define and test the backup boundary.
13. Update implementation, validation, service, roadmap, and changelog records.

### Completion Criteria

- Container health is stable.
- Media libraries are readable.
- Source media remains non-writable.
- Configuration survives restart and recreation.
- Mandatory validation checks pass.
- Service catalogue status becomes `Operational`.

## Milestone 9 — Immich

**Status:** Planned

### Entry Condition

Jellyfin must be operational and its deployment pattern must be documented.

### Planned Outcomes

- Define photo-storage architecture
- Separate database, application, and media persistence
- Establish backup requirements before importing irreplaceable photos
- Deploy with Docker Compose
- Validate restart and recovery
- Document privacy and access boundaries

## Milestone 10 — Backup and Recovery

**Status:** Planned

### Planned Work

- Identify irreplaceable data
- Define backup destinations
- Separate configuration backup from user-data backup
- Document retention
- Test restoration
- Record recovery dependencies privately
- Add public validation conclusions

### Completion Criteria

A backup job completing is insufficient. At least one restore test must succeed.

## Milestone 11 — Monitoring

**Status:** Planned

### Planned Work

- Host resource monitoring
- Storage-health monitoring
- Guest availability checks
- Service-health checks
- Backup-failure visibility
- Capacity thresholds
- Alert routing

## Paused Work

### Pi-hole Migration

The current Raspberry Pi remains the operational DNS filtering host.

Migration will be reconsidered after Jellyfin and Immich are deployed.

### Network Segmentation

Managed-switch and VLAN work remain paused.

Before resuming:

- Core services must be stable.
- The segmentation goal must be explicit.
- Firewall and rollback plans must exist.
- Required hardware must be selected.
- Validation criteria must be written.

## Guiding Principles

- Stabilize one layer before adding the next.
- Prefer documented, rebuildable services.
- Keep persistent data outside disposable containers.
- Validate outcomes rather than assuming success.
- Avoid new VMs when a justified container fits.
- Do not expose services publicly without an approved design.
- Protect exact operational details in the private repository.
- Add complexity only when it solves a real problem.
- Use a clean sanitized history for employer-facing publication.
- Keep automated workflow permissions read-only unless a reviewed requirement justifies more.

## Related Documentation

- [Future Exploration](future-exploration.md)
- [Service Architecture](../architecture/service-architecture.md)
- [Service Catalogue](../services/README.md)
- [Infrastructure Baseline](../validation/infrastructure-baseline.md)
- [Release Documentation](../release/README.md)
- [Publication Checklist](../release/publication-checklist.md)
- [Changelog](../history/changelog.md)

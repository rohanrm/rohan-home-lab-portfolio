# Changelog

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-07-22 |
| Source of truth for | Meaningful repository and infrastructure milestones |

## Purpose

This changelog records significant project milestones.

Git remains the source of truth for individual file edits, authorship, diffs, and commit history.

A changelog entry is appropriate for:

- Completion of a project stage
- Deployment of a major component
- A meaningful architecture change
- A documentation-system redesign
- A service becoming operational
- Retirement of an important component
- Public-release preparation

A changelog entry is not required for every wording, formatting, or link correction.

## Milestones

### 2026-07-22 — Public Batch 9: Release Hardening

**Status:** Completed

Added:

- `CONTRIBUTING.md`
- `SECURITY.md`
- Pull-request template
- Permanent corrected Version 3 audit tool
- Read-only GitHub Actions documentation audit
- Markdown lint configuration
- Release documentation index
- Publication checklist
- Clean-history publication procedure
- Repository release-validation record

Updated:

- Root README
- Documentation index
- Roadmap
- Changelog
- Local publication-artifact exclusions

The development branch is now prepared for clean-history export. The employer-facing public repository has not yet been created, so release validation remains `Not Started`.

### 2026-07-21 — Public Batch 8: Version 3 Public Repository Finalization

**Status:** Completed

Completed the Version 3 migration by:

- Finalizing the root README
- Finalizing the documentation index
- Updating the roadmap
- Updating the milestone changelog
- Auditing local Markdown links
- Auditing H1 heading counts
- Auditing controlled metadata statuses
- Auditing empty Markdown placeholders
- Reviewing public files for private-address and MAC patterns
- Removing obsolete Version 2 files from the current public working tree
- Preserving legacy documentation in the private operational repository
- Documenting the need for a clean public Git history

### 2026-07-21 — Public Batch 7: Service and Operations Documentation

**Status:** Completed

Added:

- Service catalogue
- Samba service record
- Pi-hole service record
- Jellyfin service record
- Operations guide
- Troubleshooting guide

### 2026-07-21 — Public Batch 6: Validation Records

**Status:** Completed

Added:

- Infrastructure baseline validation
- Proxmox host validation
- NAS LXC validation
- Docker VM validation
- Jellyfin validation plan

The records distinguish validated infrastructure from the Jellyfin application, whose validation remains not started.

### 2026-07-21 — Public Batch 5: Implementation Records

**Status:** Completed

Added:

- Proxmox host implementation
- NAS LXC implementation
- Docker VM implementation
- Samba systemd automount implementation
- Jellyfin implementation record

The Jellyfin implementation accurately records completed preparation without claiming that a container is running.

### 2026-07-21 — Public Batch 4: Reference and Planning Documentation

**Status:** Completed

Added:

- Hardware profile
- Sanitized inventory summary
- Network-addressing policy
- Roadmap
- Future exploration
- Version 3 changelog

### 2026-07-21 — Public Batch 3: Architecture Decisions

**Status:** Completed

Added:

- ADR index
- ADR maintenance rules
- ADR-0001 covering deferred unknown wireless-device investigation
- ADR-0002 covering selection of the Beelink EQ14

### 2026-07-21 — Public Batch 2: Architecture Documents

**Status:** Completed

Added:

- Network architecture
- Physical topology
- Service architecture

### 2026-07-21 — Public Batch 1: Navigation and Standards

**Status:** Completed

Added:

- Root repository README
- Documentation index
- Documentation standard
- Public/private information boundary
- Architecture template
- Implementation template
- Validation template
- Decision template
- Service template

Established `docs-v3-redesign` as the working branch for the migration.

### 2026-07-20 — Stage 1 Current-State Validation Completed

**Status:** Completed

Validated and recorded:

- Proxmox host
- NAS LXC
- Persistent storage
- Samba
- Docker VM
- Docker Engine and Compose
- Samba systemd automount
- Jellyfin preparation state
- Current service addresses and identifiers in the private record

### 2026-07-20 — Public/Private Repository Boundary Approved

**Status:** Completed

Decided that the employer-facing repository would exclude:

- Exact internal addresses
- MAC addresses
- Household and phone names
- Device serial numbers
- Disk UUIDs
- Detailed security infrastructure
- Raw identifying command output

Created a separate private repository for operational records.

### 2026-07-20 — Docker-to-NAS Automount Completed

**Status:** Completed

Completed the persistent systemd automount from the Docker VM to the NAS media share.

The design uses:

- A root-restricted credentials file
- A systemd-aware automount
- Controlled media access
- No password embedded directly in `/etc/fstab`

### 2026-07-20 — Docker Platform Validated

**Status:** Completed

Confirmed:

- Ubuntu Docker VM operational
- Docker Engine installed
- Docker Compose installed
- Docker enabled at boot
- Docker active
- Persistent Jellyfin directories prepared

Jellyfin remained `In Progress` because no active Compose definition or running container existed in the deployment directory.

### 2026-07-20 — NAS Platform Validated

**Status:** Completed

Confirmed:

- NAS LXC operational
- Persistent storage bind mounts present
- Media directory structure present
- Samba enabled and active
- Access controls aligned with the intended read/write model

### Earlier Project Work — Infrastructure Foundation

**Status:** Completed

Earlier work established:

- Network discovery
- Initial inventory
- Logical and physical architecture
- Addressing plan
- Beelink platform selection
- Proxmox installation
- Storage preparation
- NAS LXC deployment
- Docker VM deployment
- Initial operational and troubleshooting notes

The useful information has been migrated into Version 3. The original files no longer remain in the current public working tree.

## Entry Format

Use this structure for future entries:

```markdown
### YYYY-MM-DD — Milestone Title

**Status:** Completed

Summary of the meaningful outcome.

- Major result
- Major result
- Related decision or validation
```

## Changelog Rules

- Use ISO dates.
- Record outcomes rather than chat transcripts.
- Keep entries concise.
- Link to source documents when useful.
- Do not repeat every Git commit.
- Do not publish private identifiers.
- Do not claim a service is operational before validation passes.
- Correct factual errors, but do not rewrite project history to hide earlier decisions.

## Related Documentation

- [Documentation Index](../README.md)
- [Roadmap](../planning/roadmap.md)
- [Release Documentation](../release/README.md)
- [Decision Index](../decisions/README.md)
- [Documentation Standard](../standards/documentation-standard.md)

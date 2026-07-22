# Documentation Index

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-07-22 |
| Source of truth for | Repository documentation navigation |

## Purpose

This document is the navigation layer for the Version 3 documentation system.

It explains where each kind of information belongs and prevents the same fact from being maintained in several files.

## Version 3 Status

The public Version 3 documentation and release-hardening structure are complete.

The current repository includes:

- Architecture documents
- Individual architecture decisions
- Implementation records
- Validation records
- Service records
- Operations and troubleshooting guidance
- Sanitized reference material
- Roadmap and future-exploration documents
- Documentation standards and reusable templates
- Release and clean-history publication procedures
- A permanent repository audit tool
- A read-only GitHub Actions audit workflow
- Contribution and security policies
- A milestone-focused changelog

Legacy Version 2 Markdown files have been removed from the current public working tree after their useful content was migrated.

Historical development commits may still contain earlier operational details. Employer-facing publication must use a clean sanitized Git history.

## Start Here

| Need | Document |
|---|---|
| High-level project overview | [Repository README](../README.md) |
| Logical network design | [Network Architecture](architecture/network-architecture.md) |
| Physical equipment relationships | [Physical Topology](architecture/physical-topology.md) |
| VM, LXC, service, and storage relationships | [Service Architecture](architecture/service-architecture.md) |
| Current service status | [Service Catalogue](services/README.md) |
| Current approved work | [Roadmap](planning/roadmap.md) |
| Routine administration | [Operations Guide](operations/operations-guide.md) |
| Known issues and diagnostics | [Troubleshooting Guide](operations/troubleshooting.md) |
| Documentation rules | [Documentation Standard](standards/documentation-standard.md) |
| Publication and privacy rules | [Public and Private Information Boundary](standards/public-private-boundary.md) |
| Public release process | [Release Documentation](release/README.md) |
| Contribution workflow | [Contributing Guide](../CONTRIBUTING.md) |
| Security reporting | [Security Policy](../SECURITY.md) |

## Architecture

Architecture documents explain **how the system is designed**.

- [Network Architecture](architecture/network-architecture.md)
- [Physical Topology](architecture/physical-topology.md)
- [Service Architecture](architecture/service-architecture.md)

Architecture documents describe the current design first and separate future changes explicitly.

## Decisions

Architecture Decision Records explain **why a significant choice was made**.

- [Decision Index](decisions/README.md)
- [ADR-0001 — Defer Unknown Wireless Devices](decisions/adr-0001-defer-unknown-wireless-devices.md)
- [ADR-0002 — Select Beelink EQ14](decisions/adr-0002-select-beelink-eq14.md)

Accepted ADRs are historical records. A later change should normally create a new ADR rather than rewrite the earlier decision.

## Implementation

Implementation records explain **how a component was built or configured**.

- [Proxmox Host](implementation/proxmox-host.md)
- [NAS LXC](implementation/nas-lxc.md)
- [Docker VM](implementation/docker-vm.md)
- [Samba Systemd Automount](implementation/samba-systemd-automount.md)
- [Jellyfin](implementation/jellyfin.md)

Implementation records do not replace validation.

## Validation

Validation records explain **how a result was proven to work**.

- [Infrastructure Baseline](validation/infrastructure-baseline.md)
- [Proxmox Host](validation/proxmox-host.md)
- [NAS LXC](validation/nas-lxc.md)
- [Docker VM](validation/docker-vm.md)
- [Jellyfin](validation/jellyfin.md)

Raw identifying output belongs in the private operational repository. Public validation documents retain sanitized evidence and conclusions.

## Services

Service documents explain **what each service does, where it runs, what it depends on, and how it is operated**.

- [Service Catalogue](services/README.md)
- [Samba](services/samba.md)
- [Pi-hole](services/pihole.md)
- [Jellyfin](services/jellyfin.md)

Immich remains planned and is tracked in the roadmap until implementation begins.

## Operations

Operations documents explain **how the environment is maintained and repaired**.

- [Operations Guide](operations/operations-guide.md)
- [Troubleshooting Guide](operations/troubleshooting.md)

## Reference

Reference documents hold stable facts and policies that need to be looked up repeatedly.

- [Hardware Profile](reference/hardware-profile.md)
- [Inventory Summary](reference/inventory-summary.md)
- [Network Addressing Policy](reference/network-addressing-policy.md)

The public inventory is intentionally summarized. Exact allocations and identifiers remain private.

## Planning

Planning documents separate approved work from unapproved ideas.

- [Roadmap](planning/roadmap.md)
- [Future Exploration](planning/future-exploration.md)

Plex and Home Assistant remain ideas unless formally approved.

## History

- [Changelog](history/changelog.md)

The changelog records meaningful milestones. Git records individual line-by-line edits.

## Standards

- [Documentation Standard](standards/documentation-standard.md)
- [Public and Private Information Boundary](standards/public-private-boundary.md)

Templates:

- [Architecture Template](standards/templates/architecture-template.md)
- [Implementation Template](standards/templates/implementation-template.md)
- [Validation Template](standards/templates/validation-template.md)
- [Decision Template](standards/templates/decision-template.md)
- [Service Template](standards/templates/service-template.md)

## Release

Release documents govern the creation and validation of the employer-facing clean-history repository.

- [Release Documentation Index](release/README.md)
- [Publication Checklist](release/publication-checklist.md)
- [Clean-History Publication](release/clean-history-publication.md)
- [Repository Release Validation](release/repository-release-validation.md)

Supporting controls:

- [Contributing Guide](../CONTRIBUTING.md)
- [Security Policy](../SECURITY.md)
- [Permanent Audit Tool](../tools/audit-v3.py)
- [Documentation Audit Workflow](../.github/workflows/documentation-audit.yml)
- [Pull-Request Template](../.github/pull_request_template.md)

## Source-of-Truth Map

| Information | Primary location |
|---|---|
| Repository overview and demonstrated skills | Root `README.md` |
| Logical network design | `architecture/network-architecture.md` |
| Physical equipment relationships | `architecture/physical-topology.md` |
| Service placement and dependencies | `architecture/service-architecture.md` |
| Reason for a significant choice | Relevant ADR |
| Build procedure | Relevant implementation record |
| Test evidence | Relevant validation record |
| Service lifecycle status | `services/README.md` |
| Routine administrative workflow | `operations/operations-guide.md` |
| Reusable incident resolution | `operations/troubleshooting.md` |
| Approved future work | `planning/roadmap.md` |
| Unapproved possibilities | `planning/future-exploration.md` |
| Hardware capabilities | `reference/hardware-profile.md` |
| Public inventory | `reference/inventory-summary.md` |
| Addressing rules | `reference/network-addressing-policy.md` |
| Public release procedure | `release/clean-history-publication.md` |
| Release evidence | `release/repository-release-validation.md` |
| Exact IP, MAC, serial, UUID, and client data | Private repository |

## Document Quality Rule

A document is ready to be marked `Current` only when:

- Its purpose is clear.
- It uses the approved status vocabulary.
- Current and planned states are separated.
- Sensitive values are absent or safely generalized.
- Links resolve correctly.
- Commands do not include copied shell prompts.
- Validation claims are supported by a validation record.
- Duplicated facts have been replaced with links to the source of truth.
- It contains exactly one H1 heading.
- `python3 tools/audit-v3.py .` passes.
- `git diff --check` reports no whitespace errors.

## Publication Boundary

The current working tree is sanitized, but previous development commits may contain removed operational values.

Use the [Clean-History Publication](release/clean-history-publication.md) procedure for final public release.

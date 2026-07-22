# Architecture Decision Records

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-07-21 |
| Source of truth for | Architecture Decision Record index and maintenance rules |

## Purpose

This directory records significant technical and architectural decisions made during the home-lab project.

An Architecture Decision Record, or ADR, explains:

- What problem required a decision
- Which option was selected
- Why it was selected
- Which alternatives were considered
- What benefits, trade-offs, and risks followed
- Whether a later decision replaced it

ADR documents preserve the reasoning behind the current design. They are not implementation guides and should not contain secrets or unnecessary operational identifiers.

## Decision Index

| ADR | Decision | Status | Outcome |
|---|---|---|---|
| [ADR-0001](adr-0001-defer-unknown-wireless-devices.md) | Defer investigation of unknown wireless devices during initial documentation | Accepted | Project work continued without allowing incomplete client attribution to block infrastructure planning |
| [ADR-0002](adr-0002-select-beelink-eq14.md) | Select the Beelink EQ14 as the Proxmox host | Accepted | The EQ14 became the virtualization platform for the NAS LXC and Docker VM |

## When an ADR Is Required

Create an ADR when a choice has meaningful long-term consequences.

Examples include:

- Selecting a virtualization platform
- Choosing VM versus LXC
- Defining a storage-ownership model
- Approving network segmentation
- Replacing a major service
- Changing a trust boundary
- Selecting a backup architecture
- Rejecting a major alternative after evaluation
- Moving a critical service between hosts

An ADR is usually unnecessary for routine package updates, normal service restarts, temporary troubleshooting commands, or minor documentation corrections.

## ADR Status Vocabulary

| Status | Meaning |
|---|---|
| `Proposed` | The decision is under consideration |
| `Accepted` | The decision has been approved |
| `Rejected` | The option was considered but not selected |
| `Superseded` | A later ADR replaced this decision |
| `Deprecated` | The decision remains historically relevant but is no longer recommended |

## Numbering Convention

ADR identifiers are assigned sequentially:

```text
ADR-0001
ADR-0002
ADR-0003
```

Filenames use lowercase kebab-case:

```text
adr-0003-example-decision.md
```

Numbers are never reused, even when an ADR is rejected, deprecated, or superseded.

## Immutability Rule

An accepted ADR is a historical record.

Minor corrections may be made for spelling, broken links, formatting, or clarification that does not change the original meaning.

When the architecture changes:

1. Create a new ADR.
2. Explain why the earlier decision no longer fits.
3. Mark the earlier ADR as `Superseded`.
4. Link both records through their supersession fields.

## Required Structure

Each ADR should contain:

- Metadata
- Context
- Decision
- Rationale
- Alternatives considered
- Consequences
- Security and privacy impact
- Implementation impact
- Validation
- Related documentation
- Supersession information

Use the [decision template](../standards/templates/decision-template.md).

## Public and Private Boundary

Public ADRs may explain the selected platform, design constraints, technical reasoning, general security considerations, and high-level consequences.

Public ADRs must not expose exact internal addresses, MAC addresses, serial numbers, household-device names, credentials, private keys, detailed defensive configuration, recovery secrets, or raw configuration exports.

See [Public and Private Information Boundary](../standards/public-private-boundary.md).

## Candidate Future Decisions

The following topics may require ADRs when they become approved decisions:

- Docker VM resource changes
- Jellyfin hardware-transcoding design
- Immich deployment architecture
- Backup platform selection
- Pi-hole migration or redundancy
- Managed-switch selection
- VLAN and segmentation design
- External-access architecture
- Uninterruptible-power-supply strategy

Ideas should not receive accepted ADRs until they are genuinely evaluated and approved.

## Related Documentation

- [Documentation Standard](../standards/documentation-standard.md)
- [Public and Private Information Boundary](../standards/public-private-boundary.md)
- [Network Architecture](../architecture/network-architecture.md)
- [Service Architecture](../architecture/service-architecture.md)
- [Roadmap](../planning/roadmap.md)
- [Future Exploration](../planning/future-exploration.md)

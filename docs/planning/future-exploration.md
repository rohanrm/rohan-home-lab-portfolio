# Future Exploration

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-07-21 |
| Source of truth for | Unapproved ideas and evaluation questions |

## Purpose

This document records ideas that may be worth exploring but are not approved roadmap commitments.

An item in this file is not scheduled, budgeted, architecturally approved, installed, operational, or guaranteed to be implemented.

When an idea is approved, it should move to the roadmap and may require an ADR.

## Evaluation Principles

Before promoting an idea to `Planned`, determine:

1. What problem does it solve?
2. Is the problem already solved another way?
3. What hardware, memory, storage, and maintenance does it require?
4. What new security exposure does it introduce?
5. What data must be backed up?
6. How will it be validated?
7. What is the rollback path?
8. Is the learning value worth the complexity?

## Plex

**Status:** Idea

### Why It May Be Considered

Plex is a mature media-server alternative with a broad client ecosystem.

It may be worth revisiting if Jellyfin cannot meet an important requirement involving:

- Client compatibility
- Remote playback
- Media metadata
- Transcoding behaviour
- Household usability

### Why It Is Not Active Work

Jellyfin is the selected current media-service project.

Running both services prematurely would:

- Duplicate maintenance
- Consume more resources
- Complicate storage permissions
- Split testing effort
- Reduce clarity in the portfolio

### Promotion Criteria

Plex should move to the roadmap only when a specific Jellyfin limitation is demonstrated and the alternative is evaluated against that requirement.

## Home Assistant

**Status:** Idea

### Why It May Be Considered

Home Assistant could provide:

- Central smart-home control
- Local automation
- Device integration
- Improved visibility
- Reduced dependence on separate vendor applications

### Why It Is Not Active Work

The current project priority is infrastructure, storage, and core application deployment.

Home Assistant would introduce:

- A new service category
- Additional device integrations
- Broader network access
- More sensitive household data
- New backup and availability requirements

### Promotion Criteria

Before approval:

- Define the specific automation goal.
- Identify supported devices.
- Determine whether network segmentation is required.
- Define backup and recovery.
- Decide whether the service belongs in a VM, container, or dedicated appliance.
- Review the public/private documentation boundary.

## Secondary DNS Service

**Status:** Idea

A second DNS filtering instance could reduce dependency on one Pi-hole host.

Questions to resolve:

- Should both instances use the same configuration?
- How will configuration be synchronized?
- Which platform should host the second instance?
- How will clients receive both DNS addresses?
- Could a fallback bypass filtering?
- How will failure be tested?

This idea is separate from migrating the existing Pi-hole service.

## Pi-hole Migration

**Status:** Paused elsewhere in the roadmap

The existing Raspberry Pi is working and remains the active DNS host.

Possible future targets include:

- LXC
- VM
- Container
- Continued bare-metal operation

Migration should occur only when it improves maintainability or resilience without creating unnecessary dependency on the main Proxmox host.

## Managed Switch and VLANs

**Status:** Paused elsewhere in the roadmap

Possible benefits include:

- IoT isolation
- Guest separation
- Management network
- Controlled service access
- Better wired expansion
- VLAN-aware wireless networks

Questions to resolve:

- Which trust zones are actually needed?
- Does the router support the required design?
- How many managed ports are required?
- Is PoE needed?
- Which access rules should be allowed?
- How will lockout be prevented?
- What is the rollback plan?

## Uninterruptible Power Supply

**Status:** Idea

A UPS may reduce risk from brief outages and support controlled shutdown.

Evaluation should include:

- Router, Proxmox host, storage enclosure, and Pi-hole power draw
- Required runtime
- USB or network shutdown support
- Battery replacement cost
- Surge protection
- Safe shutdown ordering
- Recovery after power returns

## Dedicated Backup Storage

**Status:** Idea

A separate backup target may improve recovery from disk failure or accidental deletion.

Questions include:

- Local versus off-site
- Capacity
- Versioning
- Encryption
- Retention
- Restore speed
- Protection from ransomware or accidental overwrite
- Whether the backup remains connected continuously

## Additional Proxmox Node

**Status:** Idea

A second node could provide experimentation or future redundancy, but it would add hardware cost, power use, network complexity, cluster administration, and additional backup requirements.

It should not be approved merely to imitate an enterprise cluster.

## Remote Access

**Status:** Idea

Remote access to internal services may eventually be useful.

Any design must begin with security and threat modelling.

Possible approaches might include a VPN or identity-aware access solution. Directly exposing administrative interfaces or application ports is not an approved design.

Questions to resolve:

- Which service needs remote access?
- Who needs access?
- Is browser access sufficient?
- Is a VPN appropriate?
- How will multifactor authentication be enforced?
- How will certificates and keys be protected?
- How will access be revoked?
- How will logs be reviewed?

## Monitoring Platform

**Status:** Planned at a high level; product not selected

Monitoring is approved as a future capability, but the exact platform remains open.

Possible areas include:

- Host health
- Storage capacity
- SMART health
- Guest state
- Container health
- Service reachability
- Backup success
- Alerting

Tool selection should follow requirements rather than popularity.

## Documentation Automation

**Status:** Idea

Possible improvements include:

- Markdown linting
- Link checking
- Secret scanning
- Status vocabulary checks
- Mermaid rendering checks
- Automated repository-structure validation

Automation should support documentation quality without making ordinary updates difficult.

## Idea Promotion Workflow

To promote an item:

1. Define the problem.
2. Compare alternatives.
3. Identify resource and security impacts.
4. Decide whether an ADR is needed.
5. Add approved work to the roadmap.
6. Create implementation and validation documents.
7. Keep the item out of the current architecture until implemented.

## Related Documentation

- [Roadmap](roadmap.md)
- [Service Architecture](../architecture/service-architecture.md)
- [Decision Index](../decisions/README.md)
- [Public and Private Information Boundary](../standards/public-private-boundary.md)

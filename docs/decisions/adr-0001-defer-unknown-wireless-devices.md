# ADR-0001 — Defer Investigation of Unknown Wireless Devices

| Field | Value |
|---|---|
| Decision status | Accepted |
| Original decision period | Phase 1 — Network discovery and documentation |
| Record formalized | 2026-07-21 |
| Visibility | Public |
| Decision owner | Repository owner |
| Supersedes | None |
| Superseded by | None |

## Context

During the initial network-discovery phase, several wireless clients could not be confidently matched to a known household device.

Fully identifying every client would have required additional time and possibly disruptive testing, such as:

- Disconnecting devices one at a time
- Comparing changing DHCP leases
- Reviewing manufacturer identifiers
- Temporarily disabling wireless clients
- Inspecting device-specific applications
- Repeating the process as devices reconnected

The unknown clients did not prevent the core infrastructure from being documented or the Proxmox host from being planned.

The project needed to balance completeness against forward progress.

## Decision

Defer detailed investigation of unknown wireless clients during the initial documentation phase.

Record that the devices were not yet attributed, but do not allow the incomplete client inventory to block the next project stages.

Do not publish the unknown devices' exact addresses, MAC addresses, or identifying details in the employer-facing repository.

## Rationale

### Limited architectural impact

The unidentified clients did not change:

- The router role
- The DHCP design
- The DNS design
- The Proxmox deployment
- The storage architecture
- The planned service platform

### Better use of project time

The highest-value work at that stage was:

- Establishing the network baseline
- Documenting core infrastructure
- Selecting the virtualization host
- Defining the addressing policy
- Planning staged deployment

Client attribution could be revisited later without invalidating those decisions.

### Avoiding unnecessary disruption

Disconnecting or disabling devices could interrupt normal household services and create confusion without providing immediate architectural benefit.

### Public privacy boundary

A public portfolio does not need a complete household-device inventory.

Personal devices, smart-home names, exact addresses, and MAC addresses are operational details rather than evidence of technical skill.

## Alternatives Considered

### Identify every device before continuing

This would have produced a more complete client inventory.

It was not selected because:

- It would delay higher-priority infrastructure work.
- It might require disruptive testing.
- The result would not materially change the next deployment stage.
- Much of the resulting information would remain private anyway.

### Remove unknown devices from the network immediately

This would reduce uncertainty but could disconnect legitimate household or smart-home equipment.

It was not selected because there was no evidence that the devices were malicious, and the risk of interrupting legitimate services outweighed the immediate benefit.

### Publish the unknown-device list for completeness

This was rejected because exact client identifiers and household-device details are unnecessary in a public employer-facing repository.

## Consequences

### Positive

- Infrastructure planning continued without unnecessary delay.
- Household services were not disrupted for low-priority identification work.
- The public repository avoided collecting and exposing excessive personal-device detail.
- The project adopted a practical distinction between critical unknowns and non-blocking unknowns.

### Negative

- The private client inventory remained incomplete.
- A later review could still be required.
- Device attribution became less certain as DHCP leases and client states changed.

### Risks

#### Unauthorized device remains unnoticed

A genuinely unauthorized client could be mistaken for an unclassified legitimate device.

Mitigation:

- Keep router access protected.
- Review active clients periodically.
- Investigate unfamiliar clients when behaviour, traffic, or device count changes.
- Consider future network segmentation for untrusted or IoT devices.

#### Documentation becomes misleading

A reader could assume the inventory was complete.

Mitigation:

- Clearly label incomplete inventories.
- Keep the public inventory role-based and sanitized.
- Maintain exact operational details privately.

## Security and Privacy Impact

This decision accepted temporary uncertainty about some clients while reducing public exposure of household-device information.

It did not approve unknown clients as trusted indefinitely.

The decision can be revisited when:

- An unfamiliar client appears unexpectedly
- The number of unknown devices changes
- Suspicious network behaviour is observed
- Network segmentation is designed
- A formal asset-audit stage begins

## Implementation Impact

The decision affected documentation rather than core network configuration.

Required actions:

- Continue with infrastructure planning.
- Avoid presenting the client inventory as complete.
- Move detailed client records to the private repository.
- Keep only a sanitized infrastructure summary in the public repository.
- Revisit unidentified devices when operationally justified.

## Validation

The decision was considered successful when:

- Core network and infrastructure documentation could proceed.
- Proxmox planning was not blocked.
- No public document required publication of exact unknown-client identifiers.
- The limitation remained explicitly documented.

Future client-attribution work belongs in the private operational repository.

## Related Documentation

- [Network Architecture](../architecture/network-architecture.md)
- [Inventory Summary](../reference/inventory-summary.md)
- [Public and Private Information Boundary](../standards/public-private-boundary.md)
- [Roadmap](../planning/roadmap.md)

## Notes

This ADR preserves the original decision to defer investigation. It does not state that unknown clients should never be investigated.

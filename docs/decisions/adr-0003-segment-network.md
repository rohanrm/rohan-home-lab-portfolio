# ADR-0003 — Segment the Network

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | ADR-0003 — Segment the Network |
| Decision status | Accepted |
| Record type | Retrospective record of implemented design |


## Context

The initial flat network mixed administration, household clients, connected appliances, and server workloads. The expanded lab needed controlled service access and a clean place for public proxy ingress.

## Decision

Use Flint-routed VLAN zones, a managed M4100 switch, a VLAN-aware Proxmox bridge, and VLAN-backed UniFi SSIDs. Retain required native AP management. Place the proxy in the DMZ, infrastructure services in the server network, and administration in management.

This ADR is a retrospective V4 record of the already implemented Phase 10 architecture; it does not invent a historical approval date.

## Rationale and alternatives

A flat LAN was simpler but could not express the intended trust separation. Separate physical networks would require more hardware and cables. VLAN trunks preserve multiple zones over shared uplinks while routed policy controls cross-zone dependencies.

## Consequences

The network gains clearer boundaries and purposeful guest/IoT separation. It also adds switch membership, guest tags, routed policy, and management-lockout risk. Preserve a wired recovery path, save configuration, and verify both allowed and denied behavior.

## Validation

Phase 10 records establish persistence and required infrastructure access checks. Exact rule matrices and identities remain private. See [network architecture](../architecture/network-architecture.md), [implementation](../implementation/network-segmentation.md), and [V4 evidence](../validation/v4-baseline.md).

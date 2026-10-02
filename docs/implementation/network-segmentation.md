# Network Segmentation Implementation

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Network Segmentation Implementation |
| System status | Operational |


## Outcome

Phase 10 replaced the flat LAN with routed trust zones, a managed switch, a VLAN-aware Proxmox bridge, and VLAN-backed wireless networks. Network, DNS, NAS, administrative access, and DMZ paths were validated in the project records.

## Controlled migration method

1. Inventory current endpoints and preserve a working wired administrative path.
2. Define zone purposes and required service paths before changing membership.
3. Configure router VLAN gateways and scoped DHCP/DNS policy.
4. Build router/switch, switch/host, and switch/AP trunks with explicit tagged/native membership.
5. Enable VLAN-aware host networking and place management and guests in their intended zones.
6. Map trusted, IoT, and guest SSIDs; retain required AP native management.
7. Add only the routed paths required by service dependencies and administration.
8. Verify persistence, positive access, denied access, DNS, and services from actual client networks.

Exact port maps and rule exports remain private. A trunk can carry several zones while endpoints on access ports see one assigned zone.

## Critical invariants

Keep AP native management available, retain a known-good administrative path during cutover, and avoid treating tagged/untagged/PVID settings as interchangeable. Save switch configuration and verify it persists. A bridge tag must match the upstream trunk membership.

## Rollback

Use the retained wired path to restore saved router/switch and host-network settings. Reverse one change at a time, checking connectivity before continuing. Do not remove the recovery path before the replacement is proven.

See [network architecture](../architecture/network-architecture.md), [ADR](../decisions/adr-0003-segment-network.md), and [V4 evidence](../validation/v4-baseline.md).

# ADR-0004 — Always-On Controller and Independent DNS

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | ADR-0004 — Always-On Controller and Independent DNS |
| Decision status | Accepted |
| Record type | Retrospective record of implemented design |


## Context and decision

Workstation suspension made controller management dependent on a personal device. Moving all DNS onto the hypervisor would also increase the effects of host failure. The implemented design puts UniFi in a dedicated always-on VM, primary DNS in an LXC, and secondary DNS on separate physical hardware.

This is a retrospective V4 record of the deployed design, not a newly performed migration.

## Rationale

A dedicated VM avoids workstation sleep while preserving a conventional controller platform. A physical secondary resolver retains a DNS endpoint outside Proxmox. Running only one resolver or placing both on the same hypervisor would be simpler but retain that shared dependency.

## Trade-offs and verification

The controller consumes additional RAM, and dual DNS needs configuration consistency and direct testing. Independent placement reduces a failure dependency but does not establish strict client failover or high availability. AP connection and final controller backup were verified during migration; controlled resolver-loss and restoration tests remain separate.

See [controller migration](../implementation/unifi-controller.md), [DNS service](../services/pihole.md), and [V4 baseline](../validation/v4-baseline.md).

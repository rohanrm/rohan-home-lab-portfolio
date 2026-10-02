# UniFi Controller

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | UniFi Controller |
| Service status | Operational |


## Current state

UniFi now runs on a dedicated Debian VM in the server zone. The former controller depended on a workstation staying awake. The AP connected to the replacement inform endpoint; the recorded September check showed it remained connected after old-controller rules were removed.

## Migration controls

Export and verify a current controller backup, restore to the replacement, establish narrowly required AP communication, change inform settings, and verify adoption before retiring the old dependency. Retain native AP management on its switch uplink. The final September controller backup was checksum-verified.

## Operations

Review controller/AP connection state, SSID-to-network mappings, and configuration backups after updates. Validate wireless clients on each network as well as the controller UI. Loss of controller management does not automatically mean the AP has stopped forwarding client traffic.

The VM is included in the six-workload backup dashboard. Backups establish archive presence; restoration remains a separate test. Exact UI/inform endpoints and AP identity remain private.

See [migration implementation](../implementation/unifi-controller.md) and [V4 evidence](../validation/v4-baseline.md).

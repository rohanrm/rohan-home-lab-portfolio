# UniFi Controller Migration

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | UniFi Controller Migration |
| System status | Operational |


## Problem and outcome

The workstation-hosted controller could become unavailable when the workstation suspended. UniFi was moved to an always-on Debian VM in the server zone. The recorded September check showed the U6-LR connected to the replacement inform endpoint after old-controller rules were removed.

## Migration sequence

1. Export a fresh controller backup and verify the transferred copy.
2. Prepare the dedicated VM and replacement controller.
3. Restore the configuration and permit required AP/controller communication.
4. Move inform settings and inspect AP connected/adopted state.
5. Verify trusted, IoT, and guest wireless service.
6. Retire the old controller dependency after the replacement is proven.
7. Create and checksum-verify a final controller backup.

Keep the AP's native management network on its switch uplink. Replacing controller hosting does not require removing that network. Exact UI/inform addresses, backup locations, and firewall rules remain private.

## Recorded proof and limits

AP connection was recorded September 20, and a final controller backup was verified September 21. The VM now appears in the six-workload backup view. Backup presence does not substitute for an isolated controller restore test.

See [service](../services/unifi-controller.md), [architecture](../architecture/network-architecture.md), and [V4 baseline](../validation/v4-baseline.md).

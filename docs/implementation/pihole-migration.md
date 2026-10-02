# Pi-hole Migration

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Pi-hole Migration |
| System status | Operational |


## Implemented change

The primary Pi-hole moved from a physical host to a clean Debian LXC. The existing physical host remains as secondary DNS. The original migration preceded the later server-VLAN move.

## Method and validation

Export the supported configuration backup; verify it; take a pre-install guest snapshot; install cleanly; check DNS and web listeners; restore approved settings; confirm DHCP remains on Flint; inspect resolver/filtering behavior; and take a post-validation snapshot. Later update addressing and routed DNS paths for the segmented design.

Recorded checks confirmed service active/enabled, DNS/web listeners, restored upstream/local settings, and separate primary/secondary addresses. Exact local records and settings exports remain private because they can reveal household and access details.

## Recovery boundary

Retain protected configuration exports and a functioning physical DNS path during maintenance. Update one resolver at a time. Neither strict failover order nor automatic synchronization is established simply by distributing two DNS addresses.

See [Pi-hole service](../services/pihole.md), [network design](../architecture/network-architecture.md), and [V4 evidence](../validation/v4-baseline.md).

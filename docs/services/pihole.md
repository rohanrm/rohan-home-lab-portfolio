# Pi-hole

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Pi-hole |
| Service status | Operational |


## Current state

The primary resolver now runs in a Debian LXC. The former physical deployment remains as a secondary resolver outside Proxmox. Flint provides DHCP and advertises the approved DNS endpoints to applicable clients. Pi-hole DHCP is disabled.

The LXC migration used a configuration export, clean installation, restore, direct service checks, and pre/post snapshots. Later segmentation moved the resolver into the server network and added permitted DNS paths from client zones and WireGuard.

## Operating boundary

DNS filtering resolves names; it is not a traffic proxy and does not establish browsing intent. Client caching and alternate resolvers can affect observations. Keep both resolver configurations consistent through a documented process; automated synchronization is not established here.

## Read-only checks

Run on the relevant resolver and then on an authorized client, substituting local values:

```bash
pihole status
systemctl is-active pihole-FTL
dig @<dns-primary-address> example.com
dig @<dns-secondary-address> example.com
```

Check resolution and expected filtering on both endpoints. A working website can use cache and is insufficient proof of the DNS path. After updates, review FTL health and client results before updating the other resolver.

## Backup and privacy

Keep configuration exports in protected backup storage. Review local records and exported settings for private data and secrets before using excerpts in Git. Query databases and raw client histories remain private. Dual resolvers do not imply data replication or a tested failover event.

See [migration](../implementation/pihole-migration.md), [V4 evidence](../validation/v4-baseline.md), and [analytics](guest-dns-analytics.md).

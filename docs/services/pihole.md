# Pi-hole

| Field | Value |
|---|---|
| Document status | Current |
| Service status | Operational |
| Visibility | Public |
| Platform | Raspberry Pi bare metal |
| Last validated | 2026-07-20 |
| Source of truth for | Pi-hole role, dependency boundary, operations, and migration status |

## Purpose

Pi-hole provides DNS filtering for clients on the trusted LAN.

It reduces unwanted domain resolution while preserving the router's role as:

- DHCP server
- Default gateway
- Network address translation device
- Perimeter firewall

## Current State

Pi-hole currently runs on a dedicated Raspberry Pi.

The service remains operational in its existing location while the Proxmox-hosted application platform is completed.

Migration is intentionally paused until:

1. Jellyfin is deployed and operational.
2. Immich is deployed and operational.
3. The effect of moving DNS onto the main virtualization host is reassessed.

## Deployment Model

| Item | Value |
|---|---|
| Host type | Bare-metal Raspberry Pi |
| Service role | DNS filtering |
| Client scope | Trusted LAN |
| DHCP provider | Flint 2 router |
| Upstream resolution | Approved upstream DNS service |
| Current migration state | Paused |

## Dependencies

| Dependency | Purpose | Required state |
|---|---|---|
| Router | Advertises DNS configuration to clients | Operational |
| LAN connectivity | Allows clients to send DNS queries | Operational |
| Raspberry Pi host | Runs the Pi-hole service | Operational |
| Upstream DNS | Resolves allowed domains | Reachable |
| Correct time | Supports logs and certificate-related operations | Synchronized |
| Power | Keeps DNS filtering continuously available | Stable |

## Network Role

A normal client flow is:

```text
Client
  → DHCP configuration from router
  → DNS query to Pi-hole
  → Blocked response or upstream lookup
  → DNS result returned to client
```

Pi-hole does not replace the router as the default gateway.

## Addressing Boundary

The DNS host uses a predictable internal address so clients can reach it consistently.

The exact address, MAC address, reservation details, and administrative URL remain in the private repository.

Public documents refer to the service by role:

```text
dns-filter
```

## Operations

### Service state

Depending on the installed Pi-hole version and service layout, use the supported Pi-hole status command:

```bash
pihole status
```

Also inspect relevant systemd services:

```bash
systemctl --type=service --state=running | grep -Ei 'pihole|FTL' || true
```

### DNS response check

From an approved client:

```bash
getent hosts example.com
```

For a direct server test:

```bash
dig @<dns-filter-address> example.com
```

The exact production address belongs in the private record.

### Update check

Use the Pi-hole-supported update workflow after reviewing release notes and confirming a backup:

```bash
pihole -up
```

Do not run an update solely because a new version exists. Confirm compatibility and recovery requirements first.

### Logs

Use the Pi-hole interface and supported local logs to investigate:

- Query failures
- Blocked domains
- Upstream timeouts
- Client behaviour
- Database or FTL errors

Do not publish raw query logs because they may reveal household browsing activity and device identities.

### Restart

Use the Pi-hole-supported restart command or the relevant systemd service only during an approved maintenance window.

After restart, confirm:

- Service state
- Client resolution
- Upstream resolution
- Expected filtering
- Router-advertised DNS settings

## Backup and Recovery

Back up or record:

- Pi-hole configuration
- Allow and block lists
- Local DNS records
- Custom settings
- DHCP-related settings if ever enabled
- Administrative recovery procedure
- Exact host and network values in the private repository

Do not store administrator passwords or session tokens in Git.

## Monitoring

Monitor:

- DNS response success
- Upstream DNS availability
- Pi-hole service state
- Host storage
- Host memory
- System time
- Query volume changes
- Unexpected spikes in blocked or failed requests

A client reaching websites does not prove that Pi-hole is serving DNS; it may be using cached data or another resolver.

## Security Considerations

- Keep the administration interface on the trusted LAN.
- Do not publish query logs.
- Do not expose DNS service directly to the public internet.
- Protect administrative authentication.
- Keep the Raspberry Pi operating system updated.
- Review local DNS records for sensitive names before exporting configuration.
- Ensure fallback DNS choices do not silently bypass intended filtering.

## Current Limitations

| Limitation | Effect |
|---|---|
| Single active Pi-hole host | DNS filtering has one active service dependency |
| Bare-metal placement | Separate hardware must remain powered and maintained |
| No validated synchronized secondary | Redundancy remains an idea rather than an operational feature |
| Migration paused | DNS remains outside Proxmox during current project stages |

## Migration Decision Boundary

A future migration must compare:

- Continued bare-metal operation
- LXC
- VM
- Docker container
- Secondary-instance design

The evaluation must consider:

- Whether DNS should depend on the main Proxmox host
- Startup order
- Recovery during host failure
- Configuration migration
- Address continuity
- Redundancy
- Rollback
- Client DHCP changes
- Validation of filtering after migration

No migration target has been approved.

## Validation

The Stage 1 baseline confirmed that the existing Pi-hole service remained the active DNS-filtering platform.

A dedicated Version 3 Pi-hole validation document may be added when migration or redundancy work resumes.

## Related Documentation

- [Service Catalogue](README.md)
- [Network Architecture](../architecture/network-architecture.md)
- [Network Addressing Policy](../reference/network-addressing-policy.md)
- [Roadmap](../planning/roadmap.md)
- [Future Exploration](../planning/future-exploration.md)
- [Operations Guide](../operations/operations-guide.md)
- [Troubleshooting Guide](../operations/troubleshooting.md)

# Network Addressing Policy

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-07-21 |
| Source of truth for | Public network-addressing philosophy, reservation rules, and naming principles |

## Purpose

This document explains how network addresses are organized without publishing the exact production assignments.

The policy is designed to make the network predictable, easy to troubleshoot, easy to expand, consistent across documentation, and safer to publish.

Exact address ranges, reservations, MAC bindings, and host assignments are maintained in the private repository.

## Current Network Model

The home lab currently uses one private RFC 1918 LAN with a `/24` prefix.

The router provides:

- DHCP
- Default-gateway information
- DNS information
- Reservation management

The public repository does not publish the active subnet or exact address boundaries.

## Allocation Philosophy

Addresses are divided into functional bands.

The exact numerical boundaries are private, but the logical order is:

1. Default gateway
2. Core network infrastructure
3. Servers and virtualization hosts
4. Network equipment
5. Reserved client devices
6. Dynamic DHCP clients

This makes an address's role easier to infer during administration without requiring every value to be memorized.

## Address Categories

| Category | Intended use | Assignment method |
|---|---|---|
| Gateway | Primary router | Static device configuration |
| Core infrastructure | DNS, access points, and essential network services | Reservation or static assignment |
| Servers | Proxmox, NAS, Docker, and future server workloads | Reservation or static assignment |
| Network equipment | Switches, access points, and managed infrastructure | Reservation or static assignment |
| Reserved clients | Important workstations and predictable clients | DHCP reservation |
| Dynamic clients | Temporary, mobile, and ordinary client devices | DHCP pool |

## Reservation Policy

Use reservations for systems that need predictable reachability but do not require an address configured manually inside the operating system.

Reservations are preferred for:

- Access points
- Servers when supported by the design
- Administrative workstations
- Printers
- Infrastructure clients
- Devices referenced by monitoring or backup systems

Benefits include:

- Centralized address management
- Reduced risk of duplicate addresses
- Easier device replacement
- Clearer inventory
- More predictable troubleshooting

## Static Address Policy

A manually configured static address should be used only when the component must remain reachable even when DHCP is unavailable or when the platform design specifically requires it.

When a static address is used:

1. Keep it outside the dynamic pool.
2. Record it in the private allocation table.
3. Record the gateway and DNS configuration.
4. Confirm no DHCP reservation duplicates it.
5. Validate connectivity after changes.
6. Update recovery notes when the address is required for rebuilding.

## Dynamic DHCP Policy

The dynamic pool is reserved for devices that do not need a stable administrative identity.

Examples include:

- Guest devices
- Mobile devices
- Temporary test systems
- Consumer clients
- Devices that are not referenced by service configuration

A client should be promoted to a reservation when predictability becomes operationally valuable.

## DNS Policy

Pi-hole is the active DNS filtering service.

The DHCP configuration should advertise the approved DNS service to clients.

DNS responsibilities include:

- Filtering configured domains
- Forwarding allowed queries
- Caching responses
- Supporting consistent client resolution

The router remains responsible for DHCP and gateway services.

Pi-hole migration is paused until Jellyfin and Immich are deployed.

## Hostname Policy

Use short, descriptive, lowercase hostnames.

Preferred public examples:

```text
proxmox-host
nas
docker-host
dns-filter
media-service
```

Avoid public hostnames that expose:

- A person's name
- A household member
- A room
- A precise location
- A device owner's identity
- Security-sensitive function details

Existing operational hostnames may remain in the private record while public documents use neutral role names.

## Naming Conventions by Role

| Role | Pattern |
|---|---|
| Physical host | Function or platform role |
| VM | Primary workload role |
| LXC | Primary infrastructure role |
| Container | Application name |
| Network device | Device role |
| Client | Neutral functional label in public documentation |

Do not encode IP addresses into hostnames.

## Documentation Examples

Use placeholders in public commands:

```text
<proxmox-address>
<nas-address>
<docker-host-address>
<gateway-address>
```

When an example address is needed for teaching, use an address block reserved for documentation rather than a real production address.

Example:

```text
192.0.2.10
```

The documentation example must be clearly labelled as non-production.

## Change Control

Before changing the addressing policy:

1. Identify the reason.
2. Confirm whether the change affects DHCP, DNS, routing, firewalling, or service configuration.
3. Back up relevant private configuration.
4. Update the private allocation table.
5. Apply changes in a controlled order.
6. Validate local access, DNS, gateway reachability, and service access.
7. Update public architecture documents only when the policy itself changes.

A change to one device's private address does not normally require a public documentation change.

## Future Segmentation

VLANs and multiple subnets are not part of the current operational architecture.

If segmentation is approved, the design must define:

- Trust zones
- Address space per zone
- DHCP responsibility
- DNS policy
- Inter-zone firewall rules
- Management access
- Wireless SSID mapping
- Rollback plan
- Validation criteria

The future segmented plan should receive its own architecture decision record.

## Private Address Records

The private repository is the source of truth for:

- Active private subnet
- Exact category boundaries
- Static assignments
- DHCP reservations
- MAC-to-address mappings
- Guest identifiers
- Client ownership
- Historical address changes

## Review Triggers

Review this policy after:

- A router replacement
- VLAN approval
- Managed-switch deployment
- A second DNS service
- A new server category
- Exhaustion of the current dynamic pool
- A remote-access architecture change

## Related Documentation

- [Network Architecture](../architecture/network-architecture.md)
- [Inventory Summary](inventory-summary.md)
- [Public and Private Information Boundary](../standards/public-private-boundary.md)
- [Roadmap](../planning/roadmap.md)

# Network Addressing Policy

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Network Addressing Policy |



## Current policy

Addressing follows the segmented design. Each trust zone has its own routed subnet and gateway on the Flint 2. Network management, trusted clients, servers, IoT, guests, and the DMZ have separate roles. The access point retains a native management network; exact production allocations are private.

| Device class | Assignment approach | Reason |
|---|---|---|
| Gateways and infrastructure | Predictable documented infrastructure addresses | Stable routing and administration |
| Hosted services | Recorded server/DMZ assignments | Stable dependencies and monitoring targets |
| Personal management clients | Router-managed DHCP reservations after verification | Central management with minimal device configuration |
| Visitor clients | Dynamic guest leases | Avoid carrying personal infrastructure access into the guest zone |

Personal-device reservations are a policy preference, not a claim that every proposed reservation is already applied. Verify address availability and stable device identity before setting one; randomized wireless MACs require deliberate handling.

## DHCP and DNS

Flint is the DHCP authority. DHCP advertises the two approved Pi-hole resolvers where configured. Pi-hole DHCP remains disabled. Test each resolver directly as well as the client path; dual DNS configuration alone does not prove orderly failover or identical filtering configuration.

## Names and examples

Use neutral role names in public documents: `hypervisor`, `nas`, `docker-host`, `dns-primary`, and `controller`. Commands use placeholders such as `<server-address>`. Example addresses, when needed, must be explicitly identified as documentation values and must not impersonate production assignments.

## Change control

Before an address or VLAN change, record the current guest tag, switch membership, DHCP/DNS settings, and management recovery path privately. Change one boundary at a time. Validate gateway reachability, DNS, required service access, and prohibited access from the affected client zone. Preserve native AP management during trunk changes.

See [network architecture](../architecture/network-architecture.md), [segmentation implementation](../implementation/network-segmentation.md), and [publication boundary](../standards/public-private-boundary.md).

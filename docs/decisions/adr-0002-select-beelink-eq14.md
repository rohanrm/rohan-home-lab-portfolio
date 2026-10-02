# ADR-0002 — Select the Beelink EQ14 as the Proxmox Host

> Original decision preserved. Later architecture is documented in [ADR-0003](adr-0003-segment-network.md) and [ADR-0004](adr-0004-always-on-controller-and-independent-dns.md).

| Field | Value |
|---|---|
| Decision status | Accepted |
| Original decision period | Phase 1 — Platform selection |
| Record formalized | 2026-07-21 |
| Visibility | Public |
| Decision owner | Repository owner |
| Supersedes | None |
| Superseded by | None |

## Context

The home lab required a small, energy-efficient system capable of running Proxmox VE and supporting the initial service plan.

The platform needed to host:

- A lightweight NAS LXC
- An Ubuntu VM for Docker
- Media services
- Photo-management services
- Monitoring and backup tooling in later stages
- Possible future network services

The system also needed to fit within a home environment where power consumption, physical space, noise, memory, storage, and future media acceleration all mattered.

The Beelink EQ14 was compared with lower-cost or differently configured mini-PC alternatives, including the Beelink EQ12.

## Decision

Select the Beelink EQ14 as the primary Proxmox virtualization host.

Use it as the stable, always-on compute platform for the NAS LXC and Docker VM.

Do not place normal application services directly on the Proxmox host operating system.

## Rationale

### Dual 2.5 GbE interfaces

The EQ14 provides two 2.5 GbE interfaces.

The current architecture does not require both interfaces immediately, but the second interface provides future options for:

- Network segmentation
- Dedicated storage or service paths
- Testing routing or firewall designs
- Link-role separation
- Migration to a managed-switch architecture
- Recovery if one physical interface becomes unsuitable

### Intel integrated graphics and Quick Sync potential

The Intel platform provides integrated graphics that may support hardware-accelerated media transcoding.

This is relevant to Jellyfin because hardware acceleration can reduce CPU load during supported transcode workloads.

Hardware-transcoding support still requires separate implementation and validation. Platform capability alone does not prove that the application is configured correctly.

### Adequate virtualization resources

The system provides enough compute and storage capacity for the staged design:

- Proxmox host services
- NAS LXC
- Docker VM
- Initial containerized applications

The design deliberately avoids creating unnecessary VMs so the available memory remains focused on approved workloads.

### Compact and energy-conscious platform

A mini PC is appropriate for a continuously available home-lab host because it offers:

- Small physical footprint
- Low noise
- Lower power draw than many repurposed desktop systems
- Sufficient performance for the initial workload
- Straightforward placement near network equipment

### Storage expansion

The installed NVMe storage supports the Proxmox host and guest disks.

Additional internal expansion capability provides a path for later local-storage growth, while the primary shared-data disk remains external in the current design.

## Alternatives Considered

### Beelink EQ12

The EQ12 was considered as a lower-cost alternative.

It was not selected because the EQ14 provided a stronger overall fit for the planned lab, particularly around network-interface capacity, future flexibility, media-workload potential, and avoiding an early platform replacement.

### Repurpose the main workstation or laptop

This would reduce new hardware cost.

It was not selected because a personal workstation:

- Is not always powered on
- May sleep, reboot, or leave the home
- Mixes daily-use workloads with infrastructure services
- Provides a less predictable platform for NAS and container availability

The workstation remains appropriate for administration rather than hosting core services.

### Use a Raspberry Pi as the primary server

A Raspberry Pi offers low power consumption and is useful for dedicated services such as Pi-hole.

It was not selected as the main virtualization host because the intended x86 workloads, memory needs, storage expansion, and Proxmox learning goals fit the mini-PC platform better.

### Build or repurpose a full desktop server

A desktop could provide more expansion, memory, and drive bays.

It was not selected because it would occupy more space, generally use more power, and provide more capacity than the initial workload justified.

## Consequences

### Positive

- The home lab gained a dedicated always-on virtualization platform.
- Proxmox can separate NAS and Docker responsibilities.
- Dual 2.5 GbE interfaces preserve future network options.
- Intel integrated graphics may support later media acceleration.
- The compact platform fits the physical and power constraints of the environment.
- The host has sufficient capacity for the staged initial design.

### Negative

- Mini-PC expansion remains more limited than a tower server.
- Memory is finite and must be allocated carefully.
- The host is a single point of failure for both NAS and Docker guests.
- External storage depends on USB connectivity and enclosure reliability.
- The second network interface may remain unused until a later architecture justifies it.

### Risks

#### Resource exhaustion

Adding too many guests or services could consume available memory and storage.

Mitigation:

- Approve services through the roadmap.
- Prefer containers within the Docker VM where appropriate.
- Avoid creating a VM for every small service.
- Monitor guest and host resource use.
- Reassess allocations before major deployments.

#### Single-host dependency

A hardware failure would affect multiple services.

Mitigation:

- Maintain backups of important configurations and data.
- Document rebuild procedures.
- Keep services portable where possible.
- Add redundancy only when the operational value justifies the cost.

#### Hardware acceleration assumptions

Integrated graphics capability could be mistaken for a completed Jellyfin feature.

Mitigation:

- Keep Jellyfin hardware acceleration as an implementation and validation task.
- Do not mark it operational until real playback and transcode tests pass.

## Security and Privacy Impact

A dedicated host improves separation between personal-computing activity and infrastructure services.

The decision also introduces a management platform that must be protected through restricted administrative access, timely updates, strong authentication, minimal host-level services, and separation of public documentation from exact management details.

Serial numbers, exact interface identifiers, internal addresses, firmware identifiers, and disk UUIDs are retained privately.

## Implementation Impact

This decision established the following design:

- Proxmox VE runs directly on the Beelink EQ14.
- The NAS runs in an unprivileged LXC.
- Docker runs in an Ubuntu VM.
- Persistent application data is separated from disposable containers.
- The external storage device is mounted by the Proxmox host.
- The main workstation is used to administer the environment rather than host it.

## Validation

The platform selection was validated through checks confirming:

- Proxmox installation and updates
- Hardware virtualization support
- IOMMU availability
- Storage detection
- Network-interface detection
- USB interface mapping
- SMART monitoring capability
- Successful operation of the NAS LXC
- Successful operation of the Docker VM

See [Proxmox Host Validation](../validation/proxmox-host.md).

## Related Documentation

- [Physical Topology](../architecture/physical-topology.md)
- [Service Architecture](../architecture/service-architecture.md)
- [Hardware Profile](../reference/hardware-profile.md)
- [Proxmox Host Implementation](../implementation/proxmox-host.md)
- [Proxmox Host Validation](../validation/proxmox-host.md)
- [Roadmap](../planning/roadmap.md)

## Notes

This ADR records why the EQ14 was selected for the original staged design. A future hardware replacement should be documented through a new ADR rather than rewriting this record.

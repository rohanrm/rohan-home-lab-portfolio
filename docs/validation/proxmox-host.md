# Proxmox Host Validation

| Field | Value |
|---|---|
| Document status | Current |
| Validation status | Passed |
| Validation date | 2026-07-20 |
| Visibility | Public |
| Source of truth for | Proxmox host commissioning and current validated state |

## Purpose

This document records the tests used to confirm that the Proxmox host is suitable for its current operational role.

The validation covers:

- Host identity
- Platform and kernel versions
- Hardware virtualization
- IOMMU
- Internal and external storage
- Guest availability
- Network connectivity
- Package repositories and updates
- DNS
- Hardware-health monitoring

Raw identifying output is maintained privately.

## Environment

| Item | Validated state |
|---|---|
| Hardware platform | Beelink EQ14 |
| Hypervisor | Proxmox VE |
| Host operating system | Debian GNU/Linux 13 |
| Proxmox VE package | 9.2.0 |
| Proxmox Manager | 9.2.4 |
| Running kernel | 7.0.14-4-pve |
| Architecture | x86-64 |
| Intended role | Virtualization host and owner of the physical storage mount |

## Validation Criteria

| ID | Check | Expected result | Status |
|---|---|---|---|
| PVE-01 | Host identity and operating system | Correct dedicated host and supported OS detected | Passed |
| PVE-02 | Proxmox and kernel versions | Installed versions reported without conflict | Passed |
| PVE-03 | Hardware virtualization | CPU virtualization support available | Passed |
| PVE-04 | IOMMU | IOMMU initialized by the running kernel | Passed |
| PVE-05 | Internal storage | NVMe system storage and LVM layout detected | Passed |
| PVE-06 | External storage | Shared-data disk mounted by the host | Passed |
| PVE-07 | Guest inventory | NAS LXC and Docker VM present and running | Passed |
| PVE-08 | Network | Management interface and default route operational | Passed |
| PVE-09 | DNS | Host resolves package and internet names through approved DNS | Passed |
| PVE-10 | Package repositories | Unsupported subscription repositories disabled; approved repositories usable | Passed |
| PVE-11 | Updates | Host updates completed successfully | Passed |
| PVE-12 | SMART monitoring | Storage-health tooling detects supported devices | Passed |

## Validation Procedure

### PVE-01 — Host Identity

Commands:

```bash
hostnamectl
uname -m
```

Observed result:

- Dedicated Beelink host identified
- Debian GNU/Linux 13 reported
- x86-64 architecture reported

Status: `Passed`

### PVE-02 — Proxmox and Kernel Versions

Commands:

```bash
pveversion -v | head -n 10
uname -r
```

Observed result:

```text
Proxmox VE package: 9.2.0
Proxmox Manager: 9.2.4
Running kernel: 7.0.14-4-pve
```

The running kernel matched an installed Proxmox kernel package.

Status: `Passed`

### PVE-03 — Hardware Virtualization

Example check:

```bash
lscpu | grep -E 'Virtualization|Model name'
```

Previously completed validation confirmed Intel hardware-virtualization support.

Status: `Passed`

### PVE-04 — IOMMU

Example check:

```bash
dmesg | grep -Ei 'DMAR|IOMMU'
```

Observed result:

- Intel DMAR detected
- IOMMU initialized
- Queued invalidation available

Status: `Passed`

### PVE-05 — Internal Storage

Commands:

```bash
lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINTS,MODEL
pvs
vgs
lvs
```

Observed result:

- 1 TB NVMe device detected
- EFI system partition present
- Proxmox root and swap present
- LVM thin pool present
- NAS and Docker guest disks present

Exact logical-volume identifiers are retained privately.

Status: `Passed`

### PVE-06 — External Storage

Commands:

```bash
findmnt <shared-data-mount>
lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINTS,MODEL
```

Observed result:

- 4 TB IronWolf disk detected through the external enclosure
- ext4 filesystem mounted read-write by the Proxmox host
- Mount available for NAS bind-mount presentation

Status: `Passed`

### PVE-07 — Guest Inventory

Commands:

```bash
pct list
qm list
```

Observed result:

- NAS LXC running
- Docker VM running
- Guest resource allocations matched the approved design

Exact guest IDs remain private.

Status: `Passed`

### PVE-08 — Network

Example checks:

```bash
ip -br addr
ip route
ping -c 3 <gateway-address>
```

Observed result:

- Management interface active
- Expected default route present
- Gateway reachable
- Host available for normal administration

Exact interface and address details remain private.

Status: `Passed`

### PVE-09 — DNS

Example checks:

```bash
getent hosts debian.org
getent hosts download.proxmox.com
```

Observed result:

- DNS resolution succeeded through the approved internal DNS service
- Previous incorrect resolver configuration had been corrected

Status: `Passed`

### PVE-10 — Package Repositories

Example checks:

```bash
grep -RHE '^(deb|Types:|URIs:|Enabled:)' \
  /etc/apt/sources.list \
  /etc/apt/sources.list.d 2>/dev/null
```

Observed result:

- Proxmox no-subscription repository available
- Unsupported enterprise repositories disabled
- Enterprise Ceph subscription errors resolved

Status: `Passed`

### PVE-11 — Updates

Commands:

```bash
apt update
apt full-upgrade
```

Observed result:

- Package metadata refreshed successfully
- Approved updates completed
- Host rebooted into the current Proxmox kernel

Status: `Passed`

### PVE-12 — SMART Monitoring

Example check:

```bash
smartctl --scan-open
```

Observed result:

- NVMe health monitoring available
- Supported storage devices detected by SMART tooling
- No failing host-storage health state identified during commissioning

Status: `Passed`

## Guest Startup Validation

The approved guest sequence is:

1. NAS LXC starts after host storage is available.
2. Docker VM starts after the NAS startup window.
3. Docker applications use the NAS automount when media is first accessed.

The NAS and Docker guests were both running in the Stage 1 snapshot.

Status: `Passed`

## Security Validation

The commissioning review confirmed:

- Normal applications are not installed directly on the Proxmox host.
- NAS and Docker responsibilities are separated into guests.
- The NAS is an unprivileged LXC.
- Exact management details are not published.
- Subscription-only repositories are not left enabled without entitlement.
- Host administration uses the dedicated management interface.

Status: `Passed`

## Exceptions

| Item | Exception | Impact |
|---|---|---|
| Redundancy | Single Proxmox host | NAS and Docker share one host failure domain |
| Shared storage | One external disk and enclosure | Storage remains a single failure domain |
| UPS | Not yet documented or validated | Controlled shutdown during power loss remains future work |
| Backups | Restore validation not complete | Recovery maturity remains planned work |

These limitations do not invalidate the current commissioning result.

## Conclusion

The Proxmox host passed commissioning and remains operational.

The validated platform provides:

- A current Proxmox installation
- Correct running kernel
- Virtualization and IOMMU support
- Internal guest storage
- Mounted external shared storage
- Running NAS and Docker guests
- Working DNS and package management
- Hardware-health monitoring capability

## Revalidation Triggers

Repeat relevant checks after:

- Proxmox major-version upgrade
- Kernel replacement
- BIOS or firmware change
- Network-interface change
- Storage replacement
- Guest migration
- Repository redesign
- Host restore
- Hardware-acceleration passthrough changes

## Related Documentation

- [Infrastructure Baseline](infrastructure-baseline.md)
- [Proxmox Host Implementation](../implementation/proxmox-host.md)
- [NAS LXC Validation](nas-lxc.md)
- [Docker VM Validation](docker-vm.md)
- [Hardware Profile](../reference/hardware-profile.md)
- [ADR-0002 — Select the Beelink EQ14](../decisions/adr-0002-select-beelink-eq14.md)

# Hardware Profile

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Hardware Profile |



## Installed equipment

| Component | Model / capability | Architectural role |
|---|---|---|
| Compute | Beelink EQ14, Intel N-series, two 2.5GbE interfaces | Single Proxmox host |
| Internal storage | 1 TB NVMe | Host OS, guest disks, local application state |
| Shared-data storage | 4 TB Seagate IronWolf, ext4 | Host-owned persistent data |
| Enclosure | UGREEN external USB enclosure | Disk transport; stability under observation |
| Routing | GL.iNet Flint 2 / GL-MT6000 | OpenWrt routing, DHCP, VLAN gateways, VPN |
| Switching | Netgear M4100-26G | Managed VLAN trunks and access ports |
| Wireless | UniFi U6-LR | Ethernet backhaul and separated SSIDs |
| Secondary DNS | Raspberry Pi | Resolver independent of Proxmox |
| Manual backup target | WD Elements external drive | Separate copy destination when used |
| UPS | CyberPower CP1500AVRLCD3 | Installed power-protection hardware |

## Verified capability and limits

Virtualization and IOMMU were verified during commissioning. Intel graphics and a render device were present on the host; that alone does not establish guest passthrough or Jellyfin hardware transcoding. NVMe and HDD provide distinct system/data roles, but a single HDD is not RAID.

The October 2 disk check reported SMART health passed, with no reallocated, pending, or uncorrectable sectors. USB disconnects had nevertheless occurred. The replacement USB path negotiated 5 Gbit/s; sustained stability remains to be verified.

RAM headroom is a current planning constraint. A refurbished OptiPlex and a larger IronWolf are candidate upgrades, not current inventory. No claim of automated UPS shutdown is made without its implementation and test evidence.

## Reference boundary

Models, capacities, and useful capabilities are public. Serial numbers, MAC addresses, UUIDs, exact port assignments, firmware administration URLs, and load maps stay private. Software versions are historical observations, not a statement of the latest available release.

See [physical topology](../architecture/physical-topology.md), [inventory](inventory-summary.md), and [V4 evidence](../validation/v4-baseline.md).

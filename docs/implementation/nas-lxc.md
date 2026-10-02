# NAS LXC Implementation

| Field | Value |
|---|---|
| Document status | Current |
| System status | Operational |
| Visibility | Public |
| Original commissioning | 2026-07-20 |
| Last reviewed | 2026-10-02 |
| Source of truth for | Sanitized NAS LXC implementation record |

## Purpose

This document records the implementation of the NAS workload inside an unprivileged Proxmox LXC.

The NAS LXC provides:

- Linux ownership and permission management
- Samba file sharing
- Controlled presentation of persistent host storage
- A separation layer between the physical disk and application workloads

Exact guest identifiers, internal addresses, MAC addresses, and private user records are maintained outside the public repository.

## Starting State

Before the NAS guest was created:

- Proxmox was operational.
- The external ext4 filesystem was mounted by the Proxmox host.
- Persistent top-level directories existed for media, documents, downloads, and shared data.
- No dedicated guest yet owned Samba or network file-sharing responsibilities.

## Design Summary

The NAS uses an unprivileged Debian LXC rather than a full VM.

| Design choice | Reason |
|---|---|
| Unprivileged LXC | Reduces the impact of a container compromise |
| Host-owned physical mount | Keeps disk ownership and recovery at the hypervisor layer |
| Bind-mounted data directories | Gives the LXC access only to approved paths |
| Samba inside the LXC | Keeps file sharing and permissions out of the Proxmox host |
| Dedicated sharing group | Supports controlled multi-user access |
| Setgid and ACLs | Preserves group inheritance and directory-specific access |

## Guest Resources

The validated guest allocation is:

| Resource | Allocation |
|---|---|
| CPU | 2 virtual cores |
| Memory | 1 GB |
| Swap | 512 MB |
| Root disk | 16 GB |
| Container type | Unprivileged LXC |
| Startup | Enabled at host boot |

These resources are sufficient for the current Samba-focused role and should be reviewed if additional NAS applications are introduced.

## Network Configuration

The LXC uses a predictable address in the server zone and the router as its default gateway.

The approved Pi-hole resolvers provide DNS.

The exact address, guest identifier, and virtual-interface MAC are recorded privately.

Public documentation should use placeholders such as:

```text
<nas-address>
<gateway-address>
<dns-address>
```

## Bind-Mount Design

The Proxmox host passes selected directories into the LXC.

| Host data category | LXC mount point | Purpose |
|---|---|---|
| Media | `/srv/media` | Movies, television, music, and photos |
| Documents | `/srv/documents` | Document storage |
| Downloads | `/srv/downloads` | Download staging and transfer |
| Shared | `/srv/shared` | General shared storage |

A sanitized Proxmox configuration pattern is:

```text
mp0: <host-storage-mount>/media,mp=/srv/media
mp1: <host-storage-mount>/documents,mp=/srv/documents
mp2: <host-storage-mount>/downloads,mp=/srv/downloads
mp3: <host-storage-mount>/shared,mp=/srv/shared
```

The exact host path and guest identifier are maintained privately.

Inspect the active guest configuration from the Proxmox host with:

```bash
pct config <nas-ctid>
```

## Directory Structure

The media tree currently includes:

```text
/srv/media/
├── movies/
├── music/
├── photos/
└── tv/
```

Additional top-level storage is presented at:

```text
/srv/documents/
/srv/downloads/
/srv/shared/
```

## Users and Groups

A dedicated sharing group is used to manage access to shared data.

The public documentation refers to this group as:

```text
nas-share
```

Operational user accounts are recorded privately because some correspond to household members or personal devices.

Service accounts receive only the access required by their application role.

## Permission Model

Shared directories use a group-oriented permission model.

The general design is:

- Root owns the top-level data directories.
- The sharing group is assigned as the group owner.
- Setgid is applied so new content inherits the directory group.
- ACLs provide user- or service-specific exceptions where required.
- Media-service access is restricted to the appropriate library paths.
- Write permission is denied where an application only needs to read media.

A representative directory mode is:

```text
drwxrws---+
```

The trailing `+` indicates that ACL entries are present.

## Media-Service Boundary

The media service was validated against the intended access model:

| Media path | Readable | Traversable | Writable |
|---|---|---|---|
| Movies | Yes | Yes | No |
| Television | Yes | Yes | No |
| Music | Yes | Yes | No |
| Photos | No | No | No |

This prevents the media server from changing or deleting the source media library.

The photo library remains unavailable to Jellyfin because photo-management access will be designed separately for Immich.

## Samba Installation

Samba was installed inside the NAS LXC and enabled as a system service.

Representative package and service commands are:

```bash
apt update
apt install samba
systemctl enable --now smbd
```

Validate the service with:

```bash
systemctl --no-pager --full status smbd
```

The Stage 1 snapshot confirmed that `smbd` was enabled and active.

## Share Design

The NAS presents purpose-specific shares rather than exposing the entire filesystem.

The active model includes shares for:

- Media
- Documents
- Downloads
- Shared data

The public repository does not include the complete production `smb.conf` because it may reveal user mappings and access details.

A sanitized share pattern is:

```ini
[media]
    path = /srv/media
    browseable = yes
    read only = yes
    valid users = @nas-share
```

Actual read/write policy differs by share and user role. The private infrastructure record is authoritative for recovery.

## Samba Account Handling

Samba authentication is separated from ordinary Linux shell access.

Operational accounts may use a non-login shell when interactive access is not required.

Passwords are set through Samba tooling and are never stored in documentation:

```bash
smbpasswd -a <samba-user>
```

No Samba password belongs in Git.

## Configuration Validation

Before reloading Samba, validate the configuration:

```bash
testparm
```

Then reload without unnecessarily restarting active sessions:

```bash
systemctl reload smbd
```

Confirm readiness:

```bash
systemctl is-enabled smbd
systemctl is-active smbd
```

## Access Testing

Access was tested at both the Linux and Samba layers.

Linux-level checks used the target user identity rather than testing only as root:

```bash
runuser -u <service-user> -- test -r /srv/media/movies
runuser -u <service-user> -- test -x /srv/media/movies
runuser -u <service-user> -- test -w /srv/media/movies
```

Samba tests confirmed that approved clients could access their assigned shares while restricted access remained denied.

## Startup Behaviour

The LXC is configured to start automatically after the Proxmox host.

The external storage must already be mounted before the guest starts using its bind mounts.

The intended dependency sequence is:

```text
Proxmox host
  → External storage mount
  → NAS LXC
  → Samba
  → Remote clients and Docker VM
```

## Security Boundaries

- The container is unprivileged.
- Only approved host directories are bind-mounted.
- Samba shares expose selected paths rather than the guest root filesystem.
- Service accounts use least privilege.
- Jellyfin receives read-only access to approved media categories.
- Photos remain outside the Jellyfin access boundary.
- Passwords and exact user mappings are stored outside Git.
- Samba and administration use approved routed paths into the server network.

## Rollback

If a Samba or permission change causes problems:

1. Stop dependent application access.
2. Preserve the current configuration for comparison.
3. Restore the last known-good Samba configuration or ACL state.
4. Run `testparm`.
5. Reload Samba.
6. Retest access as the actual target users.
7. Confirm that write restrictions still hold.

Do not solve a permission problem by granting broad world-writable access.

## Operational Notes

- Test permissions as the actual account, not only as root.
- Review ACLs with `getfacl` when mode bits do not explain access.
- Use `setfacl` deliberately and document inherited defaults.
- Verify bind mounts after host or guest configuration changes.
- Validate Samba after package upgrades.
- Preserve share configuration and permission records as part of backup planning.

## Lessons Learned

- Linux filesystem permissions and Samba permissions are separate layers; both must allow access.
- Setgid preserves group ownership but does not replace a complete ACL design.
- An unprivileged LXC can use host bind mounts effectively when ownership and ID mapping are planned.
- Read-only application access reduces the impact of service mistakes or compromise.
- Public documentation can describe the permission model without publishing household account details.

## Validation

See [NAS LXC Validation](../validation/nas-lxc.md).

## Related Documentation

- [Proxmox Host Implementation](proxmox-host.md)
- [Docker VM Implementation](docker-vm.md)
- [Samba systemd Automount Implementation](samba-systemd-automount.md)
- [Service Architecture](../architecture/service-architecture.md)
- [Samba Service](../services/samba.md)
- [Inventory Summary](../reference/inventory-summary.md)


## V4 reconciliation

The original build methods above remain useful. Network placement and service inventory have changed since commissioning. Shared storage remains host-owned; source media remains read-only to the application consumer. Guest backups do not by themselves prove coverage of bind-mounted user data. The October 2 storage check was healthy after a USB port move, with continued observation required. See [V4 evidence](../validation/v4-baseline.md).

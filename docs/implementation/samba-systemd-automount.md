# Samba systemd Automount Implementation

| Field | Value |
|---|---|
| Document status | Current |
| System status | Operational |
| Visibility | Public |
| Original commissioning | 2026-07-20 |
| Last reviewed | 2026-10-02 |
| Source of truth for | Sanitized Docker-to-NAS Samba automount implementation |

## Purpose

This document records how the Docker VM receives persistent access to the NAS media share without placing a Samba password directly in `/etc/fstab`.

The implementation uses:

- `cifs-utils`
- A root-restricted credentials file
- A dedicated local mount point
- A CIFS entry managed by systemd automount
- Read-only media access for the application host

Exact addresses, usernames, credentials, and the authoritative production line are retained privately.

## Starting State

Before this work:

- The NAS LXC was operational.
- Samba was active.
- The media share was reachable from approved clients.
- The Docker VM had an empty local doorway for the remote media path.
- Docker Engine and Compose were operational.
- Jellyfin directories existed, but the media share was not yet persistently connected.

## Design Summary

The Docker VM does not mount or receive the physical storage disk.

Instead, access follows this path:

```text
Persistent disk
  → Proxmox host mount
  → NAS LXC bind mount
  → Samba media share
  → Docker VM systemd automount
  → Application container bind mount
```

This preserves clear responsibility boundaries and prevents application workloads from managing the physical filesystem directly.

## Prerequisites

The implementation requires:

- NAS LXC operational
- Samba media share available
- Dedicated Samba account for the application host
- Read and traversal permission on approved media paths
- Write permission denied
- Root or sudo access on the Docker VM
- Working DNS and network connectivity

## CIFS Client Installation

The Docker VM requires CIFS userspace tooling:

```bash
sudo apt update
sudo apt install cifs-utils
```

Confirm the helper is available:

```bash
command -v mount.cifs
```

## Local Mount Point

The approved local path is:

```text
/mnt/nas/media
```

Create the directory if it does not already exist:

```bash
sudo mkdir -p /mnt/nas/media
```

The mount point is only the local doorway. Its existence does not prove that the NAS share is mounted.

Validate the directory:

```bash
ls -ld /mnt/nas /mnt/nas/media
```

## Root-Restricted Credentials File

The Samba username and password are stored in a file readable only by root.

A sanitized example location is:

```text
/etc/samba/credentials/media
```

Create the parent directory:

```bash
sudo install -d -m 0700 /etc/samba/credentials
```

Create the credentials file without placing the password in shell history:

```bash
sudoedit /etc/samba/credentials/media
```

Expected format:

```ini
username=<samba-service-user>
password=<stored-secret>
```

Apply restrictive ownership and permissions:

```bash
sudo chown root:root /etc/samba/credentials/media
sudo chmod 0600 /etc/samba/credentials/media
```

Verify metadata without printing the secret:

```bash
sudo stat -c '%U %G %a %n' /etc/samba/credentials/media
```

Expected ownership and mode:

```text
root root 600 /etc/samba/credentials/media
```

Never run `cat` on the credentials file when capturing terminal output for documentation.

## Temporary Mount Test

Before making the mount persistent, test it manually.

A sanitized pattern is:

```bash
sudo mount -t cifs \
  //<nas-host>/media \
  /mnt/nas/media \
  -o credentials=/etc/samba/credentials/media,ro,vers=3.0
```

The exact NAS host value and any production-specific options are recorded privately.

Confirm the source and filesystem type:

```bash
findmnt /mnt/nas/media
```

## Read Test

Confirm the expected media categories are visible:

```bash
find /mnt/nas/media -maxdepth 2 -type d | head
```

A successful result should show the approved media directories without permission errors.

## Write-Rejection Test

The Docker VM is intended to consume the media library without modifying it.

Test that writes fail:

```bash
if touch /mnt/nas/media/.write-test 2>/dev/null; then
    echo 'Unexpected: write succeeded'
    rm -f /mnt/nas/media/.write-test
else
    echo 'Expected: write rejected'
fi
```

Do not proceed until the write attempt is rejected.

After the temporary validation, unmount the share:

```bash
sudo umount /mnt/nas/media
```

## Persistent systemd Automount

The persistent mount is defined through `/etc/fstab` using systemd-aware options.

A sanitized pattern is:

```fstab
//<nas-host>/media /mnt/nas/media cifs credentials=/etc/samba/credentials/media,ro,_netdev,nosuid,nodev,noexec,x-systemd.automount,x-systemd.idle-timeout=60 0 0
```

This is a public design example, not a substitute for the authoritative private production record.

### Important options

| Option | Purpose |
|---|---|
| `credentials=` | Reads the Samba username and password from a root-only file |
| `ro` | Prevents writes from the Docker VM |
| `_netdev` | Declares that the mount depends on the network |
| `nosuid` | Ignores set-user-ID and set-group-ID bits on the remote filesystem |
| `nodev` | Prevents device-node interpretation |
| `noexec` | Prevents direct execution from the media share |
| `x-systemd.automount` | Creates an on-demand systemd automount unit |
| `x-systemd.idle-timeout=` | Allows an idle mount to be released after the configured interval |

If a future application requires execution or write access, it must receive a separate documented design rather than weakening the media mount casually.

## Reload and Start

After editing `/etc/fstab`, reload systemd:

```bash
sudo systemctl daemon-reload
```

Validate the configuration without rebooting:

```bash
sudo mount -a
```

For an automount, access the directory to trigger the remote mount:

```bash
ls /mnt/nas/media >/dev/null
```

Then inspect it:

```bash
findmnt /mnt/nas/media
```

## Generated Unit Inspection

Systemd derives mount and automount unit names from the path.

Inspect the units with:

```bash
systemctl status mnt-nas-media.automount
systemctl status mnt-nas-media.mount
```

The automount unit may be active before the mount unit is active. The mount unit becomes active when the path is accessed.

## Reboot Validation

A persistent mount is not considered complete until it survives a reboot.

After reboot:

```bash
systemctl is-active mnt-nas-media.automount
findmnt /mnt/nas/media || true
```

Then trigger access:

```bash
ls /mnt/nas/media >/dev/null
findmnt /mnt/nas/media
```

Repeat the read and write-rejection tests.

The Stage 1 snapshot confirmed that the permanent automount had been completed.

## Failure Behaviour

If the NAS is temporarily unavailable:

- The Docker VM should still boot.
- The automount waits until the path is accessed.
- Access may pause or fail until the NAS becomes reachable.
- Applications must not silently write media into the empty local mount-point directory.

Before starting dependent containers, confirm the mount source:

```bash
findmnt -n -o FSTYPE,SOURCE /mnt/nas/media
```

The filesystem type should indicate CIFS and the source should be the expected NAS share.

## Security Boundaries

- The credentials file is owned by root and mode `0600`.
- The password is not embedded in `/etc/fstab`.
- The media mount is read-only.
- Device, set-ID, and execution behaviours are disabled for the media share.
- The Samba account has only the required NAS permissions.
- Exact credentials and addresses are excluded from Git.
- The mount is intended for trusted internal-network use.

## Rollback

To remove the automount safely:

1. Stop dependent containers.
2. Remove or comment out the relevant `/etc/fstab` entry.
3. Reload systemd.
4. Unmount the path if active.
5. Confirm the mount and automount units are inactive.
6. Remove the credentials file only after confirming it is no longer required.

Representative commands:

```bash
sudo systemctl daemon-reload
sudo umount /mnt/nas/media 2>/dev/null || true
systemctl status mnt-nas-media.automount
```

## Troubleshooting

### The directory exists but contains no NAS files

Check whether it is actually mounted:

```bash
findmnt /mnt/nas/media
```

An empty local directory is not proof of a successful remote mount.

### Permission denied

Check:

- Samba credentials
- Samba account status
- Share-level access
- Linux filesystem permissions in the NAS LXC
- ACLs on the media directories

### Write unexpectedly succeeds

Stop application deployment and review:

- The `ro` mount option
- Samba share write policy
- Linux permissions
- Whether the test is running against the real CIFS mount or an unmounted local directory

### Boot or mount timeout

Check:

```bash
journalctl -u mnt-nas-media.automount
journalctl -u mnt-nas-media.mount
```

Confirm network and NAS availability before changing timeouts.

## Operational Notes

- Validate `findmnt` before starting a media container.
- Do not print the credentials file during troubleshooting.
- Preserve the authoritative fstab line privately for recovery.
- Revalidate after changing Samba permissions, credentials, hostnames, or network addressing.
- A successful read test and rejected write test are both required.

## Lessons Learned

- A mount-point directory and an active remote mount are different things.
- Systemd automount reduces boot-time coupling to a network share.
- Keeping credentials outside `/etc/fstab` reduces accidental disclosure.
- Read-only mounting provides a second protection layer beyond Samba permissions.
- Write testing must confirm that the test is running against the actual CIFS mount.

## Validation

The automount is covered by [Docker VM Validation](../../archive/commissioning-2026-07/docker-vm.md) and the future service-specific checks for dependent applications.

## Related Documentation

- [NAS LXC Implementation](nas-lxc.md)
- [Docker VM Implementation](docker-vm.md)
- [Jellyfin Implementation](jellyfin.md)
- [Service Architecture](../architecture/service-architecture.md)
- [Samba Service](../services/samba.md)


## V4 reconciliation

The original build methods above remain useful. Network placement and service inventory have changed since commissioning. Shared storage remains host-owned; source media remains read-only to the application consumer. Guest backups do not by themselves prove coverage of bind-mounted user data. The October 2 storage check was healthy after a USB port move, with continued observation required. See [V4 evidence](../validation/v4-baseline.md).

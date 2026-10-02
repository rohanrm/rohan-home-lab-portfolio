# Samba

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Samba |
| Service status | Operational |


## Current state

Samba runs in the unprivileged NAS LXC in the server zone. Host-mounted data is presented through four selected bind mounts. Purpose-specific shares serve authorized clients; guest and public-internet access are not part of the intended design.

Linux ownership/ACLs and Samba permissions are separate enforcement layers. A dedicated sharing group and service identities grant required access. The media consumer can read and traverse movies, television, and music, cannot write source media, and cannot access photos.

## Routine inspection

Inside the NAS guest:

```bash
systemctl is-active smbd
systemctl is-enabled smbd
testparm -s
findmnt
```

Inspect sessions and logs privately when needed; they reveal usernames, client addresses, and share paths. Verify the host filesystem before restarting Samba. An apparently empty share may indicate missing storage rather than deleted data.

## Backup and recovery

Preserve share configuration, account/group mappings, ACLs, and the user-data files through appropriate protected backups. Host bind-mounted data must have explicitly verified coverage; guest root-disk archives alone are not evidence that the media/document dataset is backed up.

The October 2 post-USB-move check confirmed the data mount, all four bind mounts, and active Samba. Sustained USB stability is still under observation.

See [NAS implementation](../implementation/nas-lxc.md), [automount](../implementation/samba-systemd-automount.md), [operations](../operations/operations-guide.md), and [V4 evidence](../validation/v4-baseline.md).

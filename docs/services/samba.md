# Samba

| Field | Value |
|---|---|
| Document status | Current |
| Service status | Operational |
| Visibility | Public |
| Platform | NAS LXC |
| Last validated | 2026-07-20 |
| Source of truth for | Samba role, dependencies, access model, and routine operation |

## Purpose

Samba provides controlled network access to persistent storage managed by the NAS LXC.

Its current responsibilities include:

- Presenting approved storage areas to trusted clients
- Providing media access to the Docker VM
- Enforcing the intended read/write boundaries
- Keeping application hosts separate from direct ownership of the physical disk

## Current State

Samba is:

- Installed
- Enabled
- Active
- Serving configured shares
- Backed by persistent host-mounted storage
- Used by the Docker VM through a systemd automount
- Validated for read-only media consumption

## Deployment Model

| Item | Value |
|---|---|
| Host type | Unprivileged LXC |
| Operating-system family | Debian |
| Service manager | systemd |
| Primary daemon | `smbd` |
| Persistent data source | Host storage bind-mounted into the NAS LXC |
| Client boundary | Trusted LAN only |
| Credential storage | Stored privately on clients; never committed to Git |

## Dependencies

| Dependency | Purpose | Required state |
|---|---|---|
| Proxmox host | Runs the NAS LXC | Operational |
| Host shared-data mount | Supplies persistent files | Mounted |
| NAS bind mounts | Present approved directories inside the LXC | Available |
| Linux ownership and ACLs | Define local access | Correct |
| Network connectivity | Allows trusted clients to reach Samba | Operational |
| Client credentials | Authenticate approved access | Protected |

## Share Responsibilities

The NAS design includes storage areas for:

- Media
- Documents
- Downloads
- Shared files

Media contains separate library directories for:

- Movies
- Television
- Music
- Photos

The exact Samba share names and private paths are maintained in the operational repository.

## Access Model

### Approved media access

The Docker application host receives:

| Library | Read | Traverse | Write |
|---|---|---|---|
| Movies | Allowed | Allowed | Rejected |
| Television | Allowed | Allowed | Rejected |
| Music | Allowed | Allowed | Rejected |
| Photos | Rejected | Rejected | Rejected |

This supports least privilege:

- Jellyfin can consume approved media.
- Jellyfin cannot modify or delete source media.
- Jellyfin cannot access the private photo library.
- Immich can receive its own access design later.

### General sharing model

Linux permissions remain authoritative beneath Samba.

The design uses:

- Dedicated users
- A controlled sharing group
- Setgid directories where group inheritance is required
- Access control lists where default inheritance is required
- No broad world-writable directories

Samba does not replace correct Linux filesystem permissions.

## Network Role

Samba accepts connections only from the trusted internal network.

The current architecture does not approve:

- Public internet exposure
- Router port forwarding to Samba
- Guest-network access
- Anonymous write access
- Storage credentials in public documentation

## Storage

| Data | Persistence | Backup priority |
|---|---|---|
| Share configuration | Persistent | High |
| Linux user and group definitions | Persistent | High |
| Filesystem ownership and ACLs | Persistent | High |
| Media and shared data | Persistent user data | High |
| Samba logs | Operational history | Moderate |
| Temporary lock files | Re-creatable | Low |

## Operations

### Service state

```bash
systemctl is-enabled smbd
systemctl is-active smbd
```

Expected operational result:

```text
enabled
active
```

### Detailed status

```bash
systemctl --no-pager --full status smbd
```

### Configuration validation

```bash
testparm
```

The command should complete without fatal configuration errors.

### Restart

```bash
sudo systemctl restart smbd
```

Restart only after validating the configuration and considering active client sessions.

### Logs

```bash
journalctl -u smbd --since "30 minutes ago"
```

Additional Samba logs may exist under the distribution's configured log directory.

### Active sessions

```bash
sudo smbstatus
```

Do not publish output containing usernames, client addresses, or share names without sanitization.

## Client Automount

The Docker VM uses a systemd-aware CIFS automount.

The client design includes:

- `cifs-utils`
- A root-only credentials file
- No password embedded directly in `/etc/fstab`
- On-demand mounting
- Read-only media access
- Write rejection
- Reboot persistence

See [Samba Systemd Automount Implementation](../implementation/samba-systemd-automount.md).

## Updates

Before a Samba update:

1. Confirm recent backups of configuration and private operational records.
2. Validate current configuration with `testparm`.
3. Review active connections.
4. Apply approved package updates.
5. Confirm the service remains enabled and active.
6. Test a trusted client.
7. Re-run media read/write checks.

## Backup and Recovery

Back up or document:

- Samba configuration
- Linux users and groups required by the sharing model
- Filesystem ownership
- ACLs
- Share definitions
- Client-account mapping
- Exact mount dependencies in the private repository

Do not store plaintext Samba passwords in Git.

A successful configuration backup is not sufficient until restore procedures have been tested.

## Monitoring

Monitor:

- `smbd` service state
- Authentication failures
- Repeated disconnects
- Mount availability
- Storage capacity
- Filesystem errors
- Unexpected write attempts
- Disk and enclosure health

## Security Considerations

- Keep Samba internal to the trusted LAN.
- Use named accounts instead of anonymous write access.
- Protect client credential files with root-only permissions.
- Preserve read-only media access for Jellyfin.
- Do not expose exact share details publicly.
- Review inactive accounts and unnecessary group membership.
- Treat unexpected write success as a security and integrity failure.

## Known Limitations

- Samba depends on the NAS LXC and Proxmox host.
- The shared-data disk is a single storage failure domain.
- A single trusted LAN provides less isolation than a segmented design.
- Restore validation remains planned work.

## Validation

- [NAS LXC Validation](../validation/nas-lxc.md)
- [Docker VM Validation](../validation/docker-vm.md)
- [Infrastructure Baseline](../validation/infrastructure-baseline.md)

## Related Documentation

- [Service Catalogue](README.md)
- [NAS LXC Implementation](../implementation/nas-lxc.md)
- [Samba Systemd Automount](../implementation/samba-systemd-automount.md)
- [Service Architecture](../architecture/service-architecture.md)
- [Operations Guide](../operations/operations-guide.md)
- [Troubleshooting Guide](../operations/troubleshooting.md)

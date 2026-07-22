# Operations Guide

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-07-21 |
| Source of truth for | Routine administration, maintenance order, and operational checks |

## Purpose

This guide provides a safe, repeatable operating routine for the home lab.

It focuses on:

- Checking health
- Starting and stopping infrastructure
- Applying updates in a controlled order
- Reviewing storage and services
- Preserving the public/private information boundary
- Knowing when to stop and troubleshoot

Exact addresses, guest IDs, usernames, mount paths, credentials, and recovery values are maintained in the private repository.

## Operating Principles

1. Check current state before making changes.
2. Change one layer at a time.
3. Keep the Proxmox host focused on virtualization and host storage.
4. Start storage before applications.
5. Stop applications before storage.
6. Validate after every meaningful change.
7. Do not treat a successful command as proof that the full service works.
8. Keep secrets outside Git.
9. Record meaningful outcomes, not full chat transcripts.
10. Prefer a tested rollback over an improvised fix.

## Dependency Order

The principal service chain is:

```text
Router and trusted LAN
  → Proxmox host
  → Shared-data filesystem
  → NAS LXC
  → Samba
  → Docker VM
  → NAS systemd automount
  → Application containers
```

Pi-hole remains on a separate Raspberry Pi and depends on the router, LAN, upstream DNS, and power.

## Normal Startup Order

A normal startup should occur in this order:

1. Router and LAN become available.
2. Proxmox host boots.
3. Host mounts shared-data storage.
4. NAS LXC starts.
5. Samba becomes active.
6. Docker VM starts.
7. Docker Engine becomes active.
8. NAS media automount activates on first access.
9. Application containers start.

The systemd automount reduces boot-time coupling, but it does not remove the need for the NAS and Samba to be available when applications access media.

## Normal Shutdown Order

For planned maintenance:

1. Stop application containers.
2. Confirm no application is actively writing configuration or databases.
3. Shut down the Docker VM.
4. Confirm Samba clients have disconnected.
5. Stop the NAS LXC.
6. Confirm shared storage is no longer in use.
7. Shut down or reboot the Proxmox host.
8. Disconnect storage only after the filesystem is safely unmounted and the host is powered down.

Do not unplug the external storage enclosure while the filesystem is mounted.

## Quick Health Check

### Proxmox host

```bash
uptime
pveversion
free -h
df -h
findmnt
```

Review:

- Unexpected reboot
- Memory pressure
- Filesystem capacity
- Missing shared-data mount
- Package or kernel inconsistency

### Guest state

```bash
pct list
qm list
```

Expected:

- NAS LXC running
- Docker VM running

Exact guest IDs remain private.

### NAS LXC

From inside the NAS LXC:

```bash
findmnt
systemctl is-active smbd
systemctl is-enabled smbd
df -h
```

Expected:

- Approved bind mounts present
- Samba active
- Samba enabled
- Adequate storage capacity

### Docker VM

```bash
systemctl is-active docker
systemctl is-enabled docker
docker ps
findmnt <media-mount-point>
df -h
```

Expected:

- Docker active
- Docker enabled
- Expected containers listed
- Media mount available when accessed
- Adequate local and remote storage capacity

Until Jellyfin is deployed, no Jellyfin container is expected.

### Pi-hole

```bash
pihole status
```

From an approved client:

```bash
getent hosts example.com
```

Confirm that the response is using the intended internal DNS path rather than an unintended fallback.

## Daily Operations

Daily manual checks are not required when the environment is stable, but these checks are appropriate when using the lab:

- Confirm required service is reachable.
- Confirm no unexpected error banner appears.
- Confirm media or shared storage is available.
- Review any obvious performance degradation.
- Do not ignore repeated authentication or mount failures.

## Weekly Operations

### Review host resource use

On Proxmox:

```bash
free -h
df -h
pvesm status
```

Look for:

- Memory consistently near exhaustion
- Root filesystem growth
- Thin-pool pressure
- Missing storage
- Unexpected guest-disk growth

### Review guest states

```bash
pct list
qm list
```

Investigate guests that are unexpectedly stopped or repeatedly restarted.

### Review service logs

NAS LXC:

```bash
journalctl -u smbd --since "7 days ago" --priority=warning
```

Docker VM:

```bash
journalctl -u docker --since "7 days ago" --priority=warning
```

Pi-hole:

Use the supported local interface and logs without exporting household query history into the public repository.

### Review storage availability

On the Proxmox host:

```bash
findmnt <shared-data-mount>
df -h <shared-data-mount>
```

On the Docker VM:

```bash
findmnt <media-mount-point>
```

A mount being listed does not prove all permissions are correct. Test representative read access when a service has failed.

## Monthly Operations

### SMART health

On the host, use the supported device type for each storage device:

```bash
smartctl --scan-open
smartctl -a <device>
```

Review:

- Overall health
- Media errors
- Reallocated or pending sectors for HDDs
- NVMe critical warnings
- Temperature
- Unsafe shutdown count
- Percentage used for NVMe

Do not publish serial numbers from SMART output.

### Capacity review

```bash
df -h
du -xhd1 /opt/docker 2>/dev/null | sort -h
docker system df
```

Do not automatically run destructive Docker cleanup commands. Confirm what is safe to remove first.

### Package review

Check for available updates without immediately applying them:

Proxmox host and NAS LXC:

```bash
apt update
apt list --upgradable
```

Docker VM:

```bash
sudo apt update
apt list --upgradable
```

Review release notes for major platform changes.

### Documentation review

Confirm that:

- Lifecycle statuses still match reality.
- Newly operational services have validation records.
- Exact private values have not entered public documents.
- The private inventory remains current.
- Changelog contains only meaningful milestones.

## Controlled Update Procedure

## Proxmox Host Updates

Before updating:

1. Confirm NAS and Docker services are healthy.
2. Confirm important data and configuration are backed up.
3. Review available packages.
4. Note whether a kernel or Proxmox major update is included.
5. Plan a maintenance window when a reboot is required.

Commands:

```bash
apt update
apt full-upgrade
```

After updating:

```bash
pveversion -v
uname -r
pct list
qm list
findmnt
```

When rebooting, validate:

- Shared-data mount
- NAS LXC
- Samba
- Docker VM
- Docker Engine
- NAS automount
- Application services

## NAS LXC Updates

Before updating:

1. Confirm the host shared-data mount is healthy.
2. Validate Samba configuration.
3. Review active sessions.
4. Confirm configuration backup.

Commands:

```bash
apt update
apt full-upgrade
testparm
```

After updating:

```bash
systemctl is-active smbd
systemctl is-enabled smbd
testparm
```

Test a representative trusted client and the Docker-side media access.

## Docker VM Operating-System Updates

Before updating:

1. Review running containers.
2. Confirm application configuration backup.
3. Confirm the NAS is available.
4. Check whether Docker packages are included.

Commands:

```bash
sudo apt update
sudo apt full-upgrade
```

After updating:

```bash
systemctl is-active docker
docker version
docker compose version
docker ps
findmnt <media-mount-point>
```

Reboot when required and repeat the validation.

## Container Image Updates

From the application's Compose directory:

```bash
docker compose config
docker compose pull
docker compose up -d
docker compose ps
docker compose logs --tail=100
```

Before updating:

- Review application release notes.
- Record the current image reference.
- Confirm configuration backup.
- Confirm rollback method.
- Avoid changing multiple unrelated application stacks in one operation.

## Pi-hole Updates

Before updating:

- Confirm current DNS works.
- Export supported configuration backup.
- Review Pi-hole release notes.
- Record private recovery information.

Use the supported Pi-hole update command:

```bash
pihole -up
```

Afterward, test:

- Service status
- Direct DNS query
- Client query
- Expected blocking
- Upstream resolution

## Virtual-Machine Operations

### View state

```bash
qm list
```

### Start

```bash
qm start <vmid>
```

### Graceful shutdown

```bash
qm shutdown <vmid>
```

### Wait for shutdown

```bash
qm wait <vmid>
```

### Force stop

```bash
qm stop <vmid>
```

Use a forced stop only when a graceful shutdown has failed and the risk of data corruption is understood.

### Enter guest

Use SSH or the Proxmox console according to the private operational record.

## LXC Operations

### View state

```bash
pct list
```

### Start

```bash
pct start <ctid>
```

### Graceful shutdown

```bash
pct shutdown <ctid>
```

### Stop

```bash
pct stop <ctid>
```

### Enter container

```bash
pct enter <ctid>
```

Do not publish the production guest ID.

## Docker Operations

### List running containers

```bash
docker ps
```

### List all containers

```bash
docker ps -a
```

### Compose state

```bash
docker compose ps
```

### Logs

```bash
docker compose logs --tail=200
```

### Restart one service

```bash
docker compose restart <service>
```

### Stop a stack

```bash
docker compose down
```

### Start a stack

```bash
docker compose up -d
```

Avoid `docker system prune -a` as a routine operation. It can remove images and other objects needed for rollback or inactive stacks.

## Samba Operations

### Validate configuration

```bash
testparm
```

### Service state

```bash
systemctl is-active smbd
systemctl is-enabled smbd
```

### Sessions

```bash
sudo smbstatus
```

### Restart

```bash
sudo systemctl restart smbd
```

After restart, verify a client connection and the Docker media mount.

## NAS Automount Operations

### Inspect mount

```bash
findmnt <media-mount-point>
```

### Inspect automount unit

```bash
systemctl status <media-automount-unit>
```

### Trigger mount

```bash
ls <media-mount-point>
```

### Clear a failed unit

```bash
sudo systemctl reset-failed <media-mount-unit> <media-automount-unit>
```

Unit names and exact mount paths remain private.

Do not edit the root-only credentials file into public documentation.

## Backup Operations

Backup work remains a planned project area, so no backup system should be described as fully operational until restoration passes.

At minimum, protect:

- Proxmox guest configuration
- NAS LXC configuration
- Samba configuration
- Linux ownership and ACL information
- Docker Compose files
- Application configuration
- Jellyfin database and metadata after deployment
- Pi-hole supported configuration export
- Irreplaceable user data
- Private operational records
- Secrets through a separate secure system

## Restore Rule

A backup is not validated until a restoration test proves that:

- Data can be read.
- Configuration can be applied.
- Required permissions return.
- Services start.
- Clients can use the restored service.
- Secrets can be supplied securely.

## Incident Response

When a service fails:

1. Stop making unrelated changes.
2. Record the time and observed symptom.
3. Identify the lowest failed layer.
4. Check dependencies before restarting the application.
5. Preserve useful logs privately.
6. Apply one controlled change.
7. Re-test the original symptom.
8. Roll back when the change does not help.
9. Update troubleshooting documentation when the lesson is reusable.

## Public Documentation Update Workflow

After a meaningful infrastructure change:

1. Update the implementation record.
2. Run the validation checks.
3. Update the validation record.
4. Change the service status only after validation passes.
5. Update architecture only when design changed.
6. Add a changelog milestone when appropriate.
7. Update exact values in the private repository.
8. Run public-data and link checks before committing.

## Emergency Stop Conditions

Stop the current procedure and investigate when:

- Shared-data storage disappears.
- A filesystem becomes read-only unexpectedly.
- SMART reports a failing state.
- A write test unexpectedly succeeds for a read-only account.
- An application can access the photo library unexpectedly.
- Credentials appear in Git output.
- A guest enters a restart loop.
- Package management proposes removing critical Proxmox packages.
- DNS configuration changes unexpectedly.
- A public-facing port appears without an approved design.

## Related Documentation

- [Troubleshooting Guide](troubleshooting.md)
- [Service Catalogue](../services/README.md)
- [Samba](../services/samba.md)
- [Pi-hole](../services/pihole.md)
- [Jellyfin](../services/jellyfin.md)
- [Infrastructure Baseline](../validation/infrastructure-baseline.md)
- [Roadmap](../planning/roadmap.md)
- [Public and Private Information Boundary](../standards/public-private-boundary.md)

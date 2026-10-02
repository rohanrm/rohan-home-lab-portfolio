# Historical Troubleshooting Examples

| Field | Value |
|---|---|
| Document status | Archived |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Reusable diagnostic workflow and sanitized known-issue records |

> **V4 scope:** Earlier knowledge-base examples describe commissioning symptoms, not current service status. In particular, the July Jellyfin no-container case is historical; Jellyfin is now running. Check the [V4 evidence](../../docs/validation/v4-baseline.md) before applying an old symptom to the live design.

## Recorded incident patterns

| Symptom | Diagnostic distinction | Validation after correction |
|---|---|---|
| AP management disappears when workstation sleeps | Controller availability versus AP data forwarding | Dedicated controller connection and client service after cutover |
| Host exporter scrape fails | Listener binding versus routed firewall path | Exporter response and fresh Prometheus series |
| Backup panel missing a workload | Metrics inventory versus actual archive failure | Archive presence, per-workload age, overview and protected count |
| USB data disk disconnects despite healthy SMART | Disk health versus transport/enclosure path | Sustained error-free observation, correct mount/bind mounts and Samba |
| IoT application fails across client zones | Association, app permissions/discovery and routed reachability | Actual stream from the trusted client network |
| Analytics totals inflate | Repeated snapshot import versus new events | Unique event keys and repeat import adding zero |

Read state before changing it. Preserve identifying logs privately. Do not use broad permissions or unrestricted inter-zone access as a diagnostic fix.

## Purpose

This guide converts previously solved problems into reusable diagnostic procedures.

It is designed to help answer:

- What is the actual symptom?
- Which layer is failing?
- Which command provides evidence?
- What was the likely cause?
- What is the safest correction?
- How is the result verified?
- How can recurrence be prevented?

Exact addresses, guest IDs, usernames, hardware identifiers, credentials, raw configuration, and household details remain private.

## Safety Rules

Before troubleshooting:

1. Record the original symptom.
2. Do not change several layers at once.
3. Prefer read-only diagnostic commands first.
4. Preserve useful output privately.
5. Do not paste secrets into a terminal transcript.
6. Validate after each change.
7. Use graceful service stops before forced stops.
8. Do not delete configuration until a backup exists.
9. Do not use broad permissions such as `chmod 777` as a shortcut.
10. Stop when storage health or data integrity may be at risk.

## Troubleshooting Order

Use this bottom-up order:

1. **Power and physical connection**
2. **Host hardware and storage detection**
3. **Proxmox host**
4. **Guest state**
5. **Guest operating system**
6. **Filesystem and mounts**
7. **Network route and DNS**
8. **Service state**
9. **Application configuration**
10. **Client access**

An application restart cannot fix a missing disk, stopped guest, failed DNS service, or incorrect permission boundary.

## Quick Diagnostic Matrix

| Symptom | First checks |
|---|---|
| Proxmox interface unavailable | Host power, interface state, route, address, browser path |
| NAS share unavailable | Host mount, NAS LXC state, Samba state, client DNS and credentials |
| Docker application cannot see media | NAS, Samba, automount, permissions, container mount |
| Package update fails | DNS, route, repository configuration, system time |
| Jellyfin does not appear | Compose file location, rendered configuration, container state |
| DNS fails | Pi-hole state, direct query, router-advertised DNS, upstream reachability |
| Storage missing | USB connection, `lsblk`, `findmnt`, kernel log, SMART |
| Permission denied | Identity, groups, ownership, ACLs, mount options |
| Unexpected write succeeds | Stop application, inspect mount and share modes, re-run permission tests |
| Service repeatedly restarts | Service logs, dependency availability, configuration syntax |

## Knowledge Base Index

| ID | Issue |
|---|---|
| KB-001 | Proxmox web login returns 401 |
| KB-002 | Graphical Proxmox installer fails on Intel mini PC |
| KB-003 | Proxmox installed with the wrong management address |
| KB-004 | System boots back into the Ventoy installer |
| KB-005 | `apt update` fails because DNS resolution is broken |
| KB-006 | Proxmox enterprise or Ceph repository returns 401 |
| KB-007 | Confusion between `.list` and `.sources` repository files |
| KB-008 | Enterprise repository appears enabled after being disabled |
| KB-009 | Identifying physical USB ports |
| KB-010 | SMART output does not show an expected simple status |
| KB-011 | Verifying virtualization and IOMMU support |
| KB-012 | Samba service starts with locale warnings |
| KB-013 | Docker VM cannot mount the NAS media share |
| KB-014 | Media is readable but write protection must be proven |
| KB-015 | Docker Compose file exists in the wrong directory |
| KB-016 | Jellyfin directories exist but no container is running |
| KB-017 | systemd automount is configured but the share is not mounted |
| KB-018 | Git or documentation contains a sensitive operational value |

## KB-001 — Proxmox Web Login Returns 401

### Symptoms

- Proxmox web interface loads.
- Login attempt returns `401 Authentication failure`.
- Network connectivity to the host is otherwise working.

### Likely Causes

- Wrong username
- Wrong authentication realm
- Incorrect password
- Keyboard-layout mismatch during installation
- Attempting to use a normal Linux account that was not configured for Proxmox access
- Browser retaining incorrect session state

### Diagnosis

Confirm:

- The correct administrative account is being used.
- The realm selector matches the account type.
- Caps Lock and keyboard layout are correct.
- The password works from the host console when appropriate.

Avoid repeatedly guessing credentials, which can obscure the real issue.

### Resolution

Use the correct account and realm.

When the root password is genuinely unknown and the host is still in initial setup, reset it from a trusted local console or reinstall before placing data and workloads onto the system.

Do not publish the administrative username or password.

### Verification

- Login succeeds.
- Datacenter and node views load.
- No authentication error appears.
- The session can be closed and re-established.

### Prevention

- Record the authentication realm privately.
- Confirm keyboard layout during installation.
- Store credentials in a password manager.
- Test login before deploying guests.

## KB-002 — Graphical Proxmox Installer Fails on Intel Mini PC

### Symptoms

- Graphical installer freezes, displays incorrectly, or fails to progress.
- Hardware appears powered and the installer media is readable.
- Problem occurs before normal Proxmox installation completes.

### Likely Cause

Graphics compatibility between the installer environment and the mini-PC display hardware.

### Resolution

Use the text-based or terminal user-interface installer option from the Proxmox installer menu.

This changes only the installer interface; it does not result in a lesser Proxmox installation.

### Verification

- Installer proceeds through disk, network, locale, and password configuration.
- System reboots into Proxmox.
- Web management interface becomes reachable.

### Prevention

Document the TUI installer as the preferred method for this hardware platform.

## KB-003 — Proxmox Installed with the Wrong Management Address

### Symptoms

- Web interface is reachable at an unexpected address.
- Host address conflicts with the planned allocation policy.
- DNS or gateway settings may also be incorrect.

### Diagnosis

```bash
ip -br addr
ip route
cat /etc/network/interfaces
```

Review the private addressing record before editing.

### Resolution

Correct the host network configuration from a trusted local console.

Ensure:

- Address belongs to the approved server allocation
- Prefix length is correct
- Default gateway is correct
- Bridge configuration remains valid
- DNS configuration points to the approved resolver

Apply changes carefully. A network mistake can lock out remote administration.

### Verification

```bash
ip -br addr
ip route
ping -c 3 <gateway-address>
getent hosts debian.org
```

Then confirm the Proxmox web interface at the corrected private address.

### Prevention

Prepare the address, prefix, gateway, and DNS values before installation.

## KB-004 — System Boots Back Into the Ventoy Installer

### Symptoms

- Installation completes.
- On reboot, the system returns to Ventoy or the Proxmox installer.
- Installed system does not appear to start.

### Root Cause

USB installation media remains first in the boot order or is selected again during reboot.

### Resolution

- Remove the installation USB after the installer completes, or
- Select the internal NVMe device from the firmware boot menu.

### Verification

- System boots from internal storage.
- Proxmox console login appears.
- Web management interface becomes reachable.

### Prevention

Remove installation media during the first reboot unless it is still required.

## KB-005 — `apt update` Fails Because DNS Resolution Is Broken

### Symptoms

Errors include:

```text
Temporary failure resolving
Could not resolve
Name or service not known
```

The default gateway may still be reachable by IP.

### Diagnosis

Test in order:

```bash
ip route
ping -c 3 <gateway-address>
getent hosts debian.org
cat /etc/resolv.conf
```

Interpretation:

- Gateway fails: investigate routing or interface configuration.
- Gateway works but name lookup fails: investigate DNS.
- DNS configuration points to an old client address: correct the resolver source.

### Resolution

Configure the approved internal DNS service.

Do not fix the problem by permanently adding arbitrary public resolvers without considering the Pi-hole design and filtering boundary.

### Verification

```bash
getent hosts debian.org
apt update
```

Both should succeed.

### Prevention

- Keep DNS assignments in the private addressing record.
- Validate DNS after host or router changes.
- Avoid copying temporary installer addresses into permanent configuration.

## KB-006 — Enterprise or Ceph Repository Returns 401

### Symptoms

`apt update` reports:

```text
401 Unauthorized
```

The failing source references a Proxmox enterprise or enterprise Ceph repository.

### Root Cause

Subscription-only repositories are enabled without a corresponding subscription entitlement.

### Diagnosis

Inspect all APT source definitions:

```bash
grep -RHE '^(deb|Types:|URIs:|Suites:|Components:|Enabled:)' \
  /etc/apt/sources.list \
  /etc/apt/sources.list.d 2>/dev/null
```

### Resolution

- Disable subscription-only repositories that are not entitled.
- Enable the approved no-subscription repository.
- Do not delete unrelated Debian sources.
- Do not add duplicate entries.

The exact source format depends on the installed Proxmox and Debian release.

### Verification

```bash
apt update
```

Expected:

- No enterprise 401 error
- Debian sources load
- Approved Proxmox source loads

### Prevention

Review repository configuration immediately after installation.

## KB-007 — Confusion Between `.list` and `.sources` Files

### Symptoms

- A repository appears enabled even though a `.list` file was edited.
- Commands search only `/etc/apt/sources.list`.
- Duplicate sources or conflicting formats appear.

### Root Cause

Modern Debian systems may use Deb822-style `.sources` files in addition to traditional `.list` files.

### Diagnosis

```bash
find /etc/apt/sources.list.d -maxdepth 1 \
  -type f \( -name '*.list' -o -name '*.sources' \) \
  -print
```

Inspect both formats.

### Resolution

Edit the file that actually defines the active repository.

For Deb822 files, an entry may be disabled with:

```text
Enabled: no
```

Do not assume renaming one file disables every repository definition.

### Verification

```bash
apt update
```

Review the source URLs shown in the output.

### Prevention

Use repository-audit commands that inspect both `.list` and `.sources` formats.

## KB-008 — Enterprise Repository Appears Enabled After Being Disabled

### Symptoms

- Proxmox interface still shows a repository warning.
- `apt update` appears to reference an enterprise source.
- A previously edited file looks disabled.

### Likely Causes

- A second source file defines the same repository.
- A Deb822 `.sources` entry remains enabled.
- Browser view is stale.
- A Ceph enterprise source remains enabled separately.

### Diagnosis

Search all source files:

```bash
grep -RniE 'enterprise|ceph|proxmox' \
  /etc/apt/sources.list \
  /etc/apt/sources.list.d 2>/dev/null
```

### Resolution

Disable every unsupported enterprise definition while preserving approved Debian and Proxmox sources.

Refresh the web interface after `apt update` succeeds.

### Verification

- `apt update` completes without 401.
- Repository view reflects the intended state.
- No duplicate approved source exists.

## KB-009 — Identifying Physical USB Ports

### Symptoms

- System reports several USB buses.
- It is unclear which physical connector maps to which Linux device.
- High-speed and lower-speed ports must be distinguished.

### Diagnosis

Use a connect-and-observe method.

Before connecting a test device:

```bash
lsusb -t
```

Connect one known device to one physical port and run:

```bash
lsusb -t
dmesg | tail -n 30
```

Repeat one port at a time.

### Resolution

Record:

- Physical position
- USB bus and port path
- Negotiated speed
- Device type used for testing

Keep the exact physical port map private.

### Verification

A high-speed storage device should negotiate on the expected high-speed controller path rather than a full-speed path.

### Prevention

Label the approved storage port physically and in the private port map.

## KB-010 — SMART Output Does Not Show a Simple Expected Status

### Symptoms

- `smartctl` output differs between NVMe, SATA, and USB-attached disks.
- A command returns limited data.
- A USB enclosure requires an explicit device type.
- The user expects one universal `PASSED` line.

### Root Cause

SMART reporting depends on:

- Device protocol
- USB bridge
- `smartctl` device type
- Drive firmware
- Tool version

### Diagnosis

```bash
smartctl --scan-open
```

Then use the recommended device path and type.

Examples:

```bash
smartctl -a <nvme-device>
smartctl -a -d sat <usb-sata-device>
```

### Resolution

Use the correct command for the device.

Review multiple indicators rather than one line:

- Overall health
- Critical warnings
- Media errors
- Reallocated or pending sectors
- Temperature
- Percentage used
- Unsafe shutdowns

### Verification

The device returns meaningful health data and no failing health condition is present.

### Prevention

Record the correct SMART command per device privately.

## KB-011 — Verifying Virtualization and IOMMU Support

### Symptoms

- It is unclear whether hardware virtualization is enabled.
- Planned passthrough or nested workloads may require IOMMU.
- Proxmox installed successfully, but capability has not been proven.

### Diagnosis

Virtualization:

```bash
lscpu | grep -E 'Virtualization|Flags'
```

IOMMU:

```bash
dmesg | grep -Ei 'DMAR|IOMMU'
```

### Expected Result

- Intel virtualization support reported
- Intel DMAR detected
- IOMMU initialized

### Resolution

When missing:

- Check firmware settings.
- Enable Intel virtualization and VT-d where available.
- Review kernel command-line requirements.
- Reboot and re-test.

Do not change passthrough settings without a specific implementation need.

### Verification

The running kernel reports active IOMMU support.

## KB-012 — Samba Starts with Locale Warnings

### Symptoms

During package or service commands:

```text
perl: warning: Setting locale failed
```

Samba may still enable and start successfully.

### Root Cause

The configured locale is missing, incomplete, or not generated in the container.

### Impact

Locale warnings are usually separate from Samba service function, but they should be corrected to prevent script and package-management inconsistencies.

### Diagnosis

```bash
locale
locale -a
cat /etc/default/locale
```

### Resolution

Install or generate the intended locale through the distribution-supported configuration tool.

Example:

```bash
dpkg-reconfigure locales
```

Select only the locale actually intended for the system.

### Verification

```bash
locale
systemctl is-active smbd
```

The warning should disappear and Samba should remain active.

## KB-013 — Docker VM Cannot Mount the NAS Media Share

### Symptoms

- Mount command fails.
- `findmnt` shows no media mount.
- Application reports missing media.
- Authentication or permission error appears.

### Diagnostic Order

1. Confirm NAS LXC is running.
2. Confirm host bind mounts exist.
3. Confirm Samba is active.
4. Confirm Docker VM can resolve or reach the NAS.
5. Confirm the credentials file exists and is root-only.
6. Confirm client package is installed.
7. Confirm share and mount options match the private record.

Example checks:

```bash
systemctl is-active smbd
getent hosts <nas-hostname>
test -r <credentials-file>
stat -c '%a %U %G' <credentials-file>
findmnt <media-mount-point>
```

### Resolution

Correct only the failed layer.

Common corrections:

- Start NAS LXC.
- Start Samba.
- Restore the host mount.
- Correct name resolution.
- Correct root-only credentials-file permissions.
- Correct share or mount definition privately.
- Reset a failed systemd mount unit.

### Verification

```bash
ls <media-mount-point>
findmnt <media-mount-point>
```

Then re-run read and write-rejection tests.

## KB-014 — Proving Media Write Protection

### Symptoms

- Media is visible, but it is unclear whether the application can alter it.
- Directory permissions appear restrictive, but no real write test was performed.

### Diagnosis

Test as the exact service identity, not as root.

Example logic:

```bash
sudo -u <service-user> test -r <library>
sudo -u <service-user> test -x <library>
sudo -u <service-user> test -w <library>
```

A controlled file-creation attempt may be used only in an approved test location.

### Expected Result

| Library | Read | Traverse | Write |
|---|---|---|---|
| Approved media | Yes | Yes | No |
| Photos | No | No | No |

### Resolution

When write unexpectedly succeeds, stop the dependent application and inspect:

- Samba share mode
- CIFS mount options
- Linux ownership
- Group membership
- ACLs
- Container bind-mount mode

Do not hide the problem with additional permissions.

### Verification

Repeat the test as the service identity after correction.

## KB-015 — Docker Compose File Exists in the Wrong Directory

### Symptoms

- `docker compose` reports no configuration file.
- A test Compose file exists elsewhere.
- The intended application directory contains only persistent subdirectories.
- It is unclear which file is authoritative.

### Diagnosis

From the application directory:

```bash
find . -maxdepth 1 -type f \
  \( -name 'compose.yaml' \
  -o -name 'compose.yml' \
  -o -name 'docker-compose.yaml' \
  -o -name 'docker-compose.yml' \) \
  -print
```

Search the broader service root only to find misplaced files:

```bash
find /opt/docker -type f \
  \( -name 'compose.yaml' \
  -o -name 'compose.yml' \
  -o -name 'docker-compose.yaml' \
  -o -name 'docker-compose.yml' \) \
  -print
```

### Resolution

Do not treat an obsolete test file as the production definition.

Create the approved Compose file in the intended application directory after reviewing its contents.

Remove obsolete test files only after confirming they are not used.

### Verification

From the active directory:

```bash
docker compose config
docker compose config --services
```

## KB-016 — Jellyfin Directories Exist but No Container Is Running

### Symptoms

- Configuration and cache directories exist.
- `docker ps` shows no Jellyfin container.
- Browser access fails.
- Documentation may incorrectly imply that Jellyfin is installed.

### Root Cause

Directory preparation is not application deployment.

Without a Compose definition and container startup, Jellyfin is not implemented.

### Diagnosis

```bash
find /opt/docker/jellyfin -maxdepth 1 -type f \
  \( -name 'compose.yaml' \
  -o -name 'compose.yml' \
  -o -name 'docker-compose.yaml' \
  -o -name 'docker-compose.yml' \) \
  -print

docker ps -a --filter name=jellyfin
```

### Resolution

Complete the controlled Jellyfin implementation:

1. Create the Compose definition.
2. Render it.
3. Pull the image.
4. Start the container.
5. Review logs.
6. Complete validation.

### Verification

Use the checks in [Jellyfin Validation](../../docs/validation/jellyfin.md).

Until they pass, status remains `In Progress`.

## KB-017 — Systemd Automount Exists but Share Is Not Mounted

### Symptoms

- Mount point looks empty.
- `findmnt` does not show the CIFS mount.
- Automount unit is loaded.
- Access may pause or fail.

### Important Distinction

An automount is designed to mount on first access.

The share may correctly remain unmounted until something accesses the directory.

### Diagnosis

```bash
systemctl status <media-automount-unit>
ls <media-mount-point>
findmnt <media-mount-point>
```

If access fails:

```bash
systemctl status <media-mount-unit>
journalctl -u <media-mount-unit> --since "15 minutes ago"
```

### Resolution

Depending on the evidence:

- Confirm NAS and Samba are available.
- Confirm client name resolution.
- Confirm root-only credentials file.
- Correct the private mount definition.
- Reset failed units.
- Trigger the automount again.

```bash
sudo systemctl reset-failed \
  <media-mount-unit> \
  <media-automount-unit>
```

### Verification

- Directory access succeeds.
- `findmnt` shows the CIFS mount after access.
- Read succeeds.
- Write is rejected.
- Reboot test succeeds.

## KB-018 — Git Contains a Sensitive Operational Value

### Symptoms

A staged or committed public document contains:

- Exact internal IP address
- MAC address
- Serial number
- Disk UUID
- Household-device name
- Credential
- Token
- Private key
- Administrative URL

### Immediate Response

When the value is a secret:

1. Treat it as compromised.
2. Rotate or revoke it.
3. Remove it from the current file.
4. Assess Git history, forks, logs, and artifacts.
5. Do not copy it into an incident report.

When it is private but not secret:

1. Remove it from the public document.
2. Preserve it only in the private repository when useful.
3. Assess whether a clean public history is required.

### Diagnosis

Review staged content:

```bash
git diff --cached
```

Search for common indicators:

```bash
git grep -nEi \
  'password|passwd|api[_ -]?key|access[_ -]?token|secret|private[_ -]?key|BEGIN [A-Z ]*PRIVATE KEY|credentials' \
  -- '*.md' || true
```

Search for address patterns:

```bash
git grep -nE \
  '([0-9]{1,3}\.){3}[0-9]{1,3}|([[:xdigit:]]{2}:){5}[[:xdigit:]]{2}' \
  -- '*.md' || true
```

### Prevention

- Use the public/private boundary checklist.
- Review staged changes before every public commit.
- Keep raw command output private.
- Use placeholders in public examples.
- Publish reviewed content through a separate sanitized history.

## Escalation Template

When a problem is not resolved, record privately:

```text
Time observed:
Affected component:
Expected result:
Actual result:
Last known working state:
Recent changes:
Commands run:
Sanitized error:
Dependencies checked:
Rollback attempted:
Current risk to data:
```

Do not include passwords, tokens, keys, or unredacted credential files.

## Adding a New Knowledge-Base Entry

Use:

```markdown
## KB-XXX — Issue Title

### Symptoms

### Likely Cause

### Diagnosis

### Resolution

### Verification

### Prevention
```

A reusable entry should describe evidence and reasoning rather than one unexplained command.

## Related Documentation

- [Operations Guide](../../docs/operations/operations-guide.md)
- [Service Catalogue](../../docs/services/README.md)
- [Samba](../../docs/services/samba.md)
- [Pi-hole](../../docs/services/pihole.md)
- [Jellyfin](../../docs/services/jellyfin.md)
- [Infrastructure Baseline](infrastructure-baseline.md)
- [Public and Private Information Boundary](../../docs/standards/public-private-boundary.md)

# Public and Private Information Boundary

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-07-21 |
| Source of truth for | Publication, privacy, and redaction rules |

## Purpose

This document defines what belongs in the employer-facing public repository, what belongs in the separate private operational repository, and what must never be stored in Git.

The goal is to preserve useful technical evidence without publishing unnecessary information about the home, household, devices, access methods, or defensive configuration.

## Repository Roles

### Public repository

The public repository demonstrates:

- Architecture
- Technical reasoning
- Linux and virtualization skills
- Implementation methods
- Validation methods
- Troubleshooting lessons
- Documentation quality
- Project planning
- Security awareness

It should answer:

> What was designed, why was it designed that way, how was it implemented, and how was it validated?

### Private repository

The private repository supports actual administration of the environment.

It may contain:

- Exact internal address assignments
- Device identifiers
- Private asset records
- Raw validation output
- Detailed port and cable mapping
- Recovery procedures
- Security configuration notes
- Operational details that are useful to the owner but unnecessary for a portfolio reader

### Secrets system

Passwords and secrets do not belong in either repository.

They belong in a password manager or another dedicated secrets-management system.

## Classification Model

Use one of these classifications when deciding where information belongs:

| Classification | Meaning | Destination |
|---|---|---|
| Public | Safe and useful for an external reader | Public repository |
| Private Operational | Useful for administration but unnecessarily revealing | Private repository |
| Secret | Grants access, decrypts data, or enables impersonation | Password manager or secrets system |
| Temporary Sensitive | Needed briefly for troubleshooting or transfer | Secure temporary storage, then delete |

## Appropriate Public Content

The public repository may include:

- Sanitized architecture diagrams
- General hardware models and capabilities
- Platform roles
- Reasons for choosing Proxmox, LXC, VMs, or Docker
- General network addressing philosophy
- Generic Linux and Docker commands
- Sanitized implementation procedures
- Test criteria and conclusions
- High-level permission models
- Service lifecycle states
- Lessons learned
- Approved future work
- Architecture Decision Records
- Non-sensitive known issues and resolutions

Example:

```text
The Docker VM receives a reserved address from the server allocation range.
```

This communicates the design without publishing the exact address.

## Private Operational Content

The following should normally remain private:

- Exact internal IP allocations
- MAC addresses
- Device serial numbers
- Disk UUIDs
- Hardware warranty identifiers
- Personal usernames when not technically necessary
- Phone names
- Household-member names
- Smart-home device names
- Complete client-device inventories
- Exact room-by-room placement
- Detailed cable routes
- Exact physical router or switch port assignments
- Raw configuration files
- Raw terminal output containing identifiers
- Detailed firewall and security-control layouts
- Backup destinations and recovery sequencing
- Administrative URLs
- Internal hostnames when they reveal personal or security information

Public documentation may use neutral role names such as:

- `proxmox-host`
- `nas`
- `docker-host`
- `dns-filter`
- `wireless-access-point`

## Information That Must Never Be Stored in Git

Do not commit any of the following, even to a private repository:

- Passwords
- Password hashes intended for authentication
- Samba credential files
- Private SSH keys
- API keys
- Access tokens
- Refresh tokens
- Recovery codes
- Session cookies
- Application secrets
- Encryption keys
- VPN private keys
- Unredacted `.env` files
- Cloud credentials
- Database passwords
- Complete configuration backups containing credentials

Examples of forbidden content include:

```text
password=...
api_key=...
-----BEGIN OPENSSH PRIVATE KEY-----
```

A filename such as `credentials-example.txt` is not safe merely because the repository is private.

## Public Redaction Rules

### IP addresses

Replace exact addresses with:

- A role description
- A sanitized example range reserved for documentation
- A category such as `server reservation range`

Do not invent false production addresses and present them as real.

### MAC addresses

Remove them entirely from public documents unless a masked example is required for teaching:

```text
XX:XX:XX:XX:XX:XX
```

### Serial numbers and UUIDs

Replace exact values with a statement such as:

```text
The identifier is recorded in the private hardware register.
```

### User and device names

Replace personal names with functional labels:

```text
primary-workstation
mobile-client
media-client
```

### Command output

Retain only the lines needed to prove the documented point.

Replace identifying values with clear markers:

```text
IPv4 address: <private-server-address>
Disk UUID: <recorded privately>
```

Do not alter output in a way that changes its technical meaning.

### Configuration examples

Use placeholders:

```ini
username=<samba-user>
password=<stored-outside-git>
```

Never use real credentials in an example.

## Raw Command Output

Raw command output may be valuable for future troubleshooting, but it commonly contains private identifiers.

Use this pattern:

1. Store the complete output in the private repository when operationally useful.
2. Record the date, source system, and purpose.
3. Remove passwords, tokens, private keys, and credentials before committing.
4. Publish only a concise sanitized result in the public validation document.
5. Link conceptually to the private evidence without exposing its location or contents.

Public example:

```text
Result: Passed. The NAS mount was present after reboot and remained non-writable to the media-service account.
```

## Private Repository Structure

The private repository is organized around operational lookup:

```text
inventory/
network/
infrastructure/
operations/
security/
```

Its purpose is not to duplicate every public explanation. It should retain the exact values and raw evidence that the public repository intentionally omits.

## Public Repository History

Deleting a sensitive line in a later commit does not automatically remove it from earlier Git history.

Before public release:

1. Review the full repository for sensitive material.
2. Do not rely only on the latest branch state.
3. Prefer publishing the sanitized Version 3 tree in a fresh repository history.
4. Preserve the historical development repository privately if needed.
5. Do not make the historical repository public merely because current files are sanitized.

## Accidental Exposure Procedure

When a secret is committed:

1. Treat the secret as compromised.
2. Revoke or rotate it immediately.
3. Remove it from the current files.
4. Assess whether Git history must be rewritten.
5. Check forks, clones, CI logs, and published artifacts.
6. Record the incident privately without copying the secret again.

Removing the text is not a substitute for rotating the credential.

When private but non-secret infrastructure data is committed:

1. Remove it from the current public documentation.
2. Move the useful value to the private record.
3. Determine whether the public repository requires a clean history.
4. Review nearby files for similar exposure.

## Pre-Commit Checks

Before every public documentation commit, review staged changes:

```bash
git diff --cached
```

Search tracked Markdown files for common secret indicators:

```bash
git grep -nEi   'password|passwd|api[_ -]?key|access[_ -]?token|secret|private[_ -]?key|BEGIN [A-Z ]*PRIVATE KEY|credentials'   -- '*.md' || true
```

This search can produce harmless matches. Every result must be reviewed rather than automatically deleted.

Review for address and hardware identifiers:

```bash
git grep -nE   '([0-9]{1,3}\.){3}[0-9]{1,3}|([[:xdigit:]]{2}:){5}[[:xdigit:]]{2}'   -- '*.md' || true
```

A match is a review trigger, not automatic proof of a problem. Documentation-only example addresses may be acceptable when clearly labeled.

## Publication Checklist

Before publishing or merging a Version 3 batch:

- [ ] No passwords, tokens, keys, or recovery codes are present.
- [ ] Exact internal addresses have been removed unless explicitly approved.
- [ ] MAC addresses are absent.
- [ ] Serial numbers and disk UUIDs are absent.
- [ ] Household-member and personal-device names are absent.
- [ ] Raw outputs are sanitized.
- [ ] Administrative URLs and recovery details are absent.
- [ ] Security controls are described at an appropriate level.
- [ ] Private operational details have a destination in the private repository.
- [ ] The public document still provides enough technical evidence to be useful.
- [ ] Git history implications have been considered.

## Guiding Test

Before publishing a detail, ask:

> Does an external reader need this exact value to understand my technical skill or the system design?

When the answer is no, keep the exact value private and publish only the technical meaning.

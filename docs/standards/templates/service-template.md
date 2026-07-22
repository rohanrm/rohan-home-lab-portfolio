# Service Name

| Field | Value |
|---|---|
| Document status | Draft |
| Service status | Planned |
| Visibility | Public |
| Platform | Platform name |
| Last validated | Not yet validated |
| Source of truth for | Service role and operations |

## Purpose

Explain what the service provides and why it exists in the environment.

## Current State

Describe only what exists now.

Examples:

- Installed but not deployed
- Running and validated
- Paused pending a dependency
- Planned but not started

## Deployment Model

| Item | Value |
|---|---|
| Host type | VM, LXC, container, or bare metal |
| Runtime | Runtime |
| Startup method | Method |
| Configuration source | Sanitized path or repository |
| Service owner | Account or role |

## Dependencies

| Dependency | Purpose | Required status |
|---|---|---|
| Dependency | Purpose | Operational |

## Network Role

Describe:

- Who connects to the service
- Which general protocol is used
- Whether access is internal only
- Which upstream or downstream services are required

Do not publish exact internal addresses or unnecessary firewall details.

## Storage

| Data | Purpose | Persistence | Backup requirement |
|---|---|---|---|
| Configuration | Service configuration | Persistent | Required |
| Cache | Re-creatable data | Temporary or persistent | Usually not required |
| Application data | User or service data | Persistent | Required |

## Access and Permissions

Describe:

- Service account
- Required groups
- Read/write boundaries
- Least-privilege controls
- Credential storage method

Do not include credentials.

## Operations

### Start

```bash
command
```

### Stop

```bash
command
```

### Restart

```bash
command
```

### Status

```bash
command
```

### Logs

```bash
command
```

## Updates

Describe the approved update process and any required pre-update checks.

## Backup and Recovery

Document:

- What must be backed up
- What can be recreated
- Restore dependencies
- Where the detailed private recovery procedure is maintained

## Monitoring

Describe:

- Health checks
- Important logs
- Resource indicators
- Failure symptoms
- Validation cadence

## Security Considerations

Record relevant controls such as:

- Internal-only exposure
- Least privilege
- Read-only storage access
- Credential separation
- Update responsibility
- Public/private documentation boundary

## Validation

- [Service validation](../validation/service.md)

## Known Limitations

- Limitation
- Accepted trade-off

## Planned Changes

List only approved changes. Keep unapproved ideas in `planning/future-exploration.md`.

## Related Documentation

- [Implementation](../implementation/service.md)
- [Architecture](../architecture/service-architecture.md)
- [Decision record](../decisions/README.md)
- [Operations guide](../operations/operations-guide.md)

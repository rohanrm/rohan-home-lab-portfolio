# Component Implementation

| Field | Value |
|---|---|
| Document status | Draft |
| System status | Planned |
| Visibility | Public |
| Last validated | Not yet validated |
| Source of truth for | Component implementation |

## Purpose

State the outcome this implementation is intended to achieve.

## Starting State

Describe what existed before the work began.

Include only facts needed to understand the change.

## Prerequisites

- Required access
- Required package or platform
- Required storage or networking dependency
- Relevant accepted ADR

## Design Summary

Explain the selected implementation and why it fits the environment.

Link to the corresponding architecture and ADR documents rather than repeating them.

## Implementation Procedure

### 1. Prepare the environment

Explain the step.

```bash
command
```

### 2. Apply the configuration

Explain the step.

```bash
command
```

### 3. Enable startup or persistence

Explain the step.

```bash
command
```

Do not include shell prompts, passwords, tokens, private keys, exact private identifiers, or unredacted credential files.

## Configuration Changes

| Location | Change | Reason |
|---|---|---|
| File, directory, or setting | Sanitized summary | Reason |

## Permissions and Ownership

Describe:

- Service account
- Required group membership
- Read/write boundary
- Ownership model
- Why the permissions are appropriate

## Validation

Validation is documented separately:

- [Component validation](../validation/component.md)

Summarize only the final implementation state here.

## Rollback

Describe how to reverse the change safely.

1. Stop or disable the component.
2. Restore the prior configuration.
3. Confirm dependent services remain safe.
4. Run the relevant validation checks.

## Operational Notes

Document routine considerations such as:

- Startup order
- Update method
- Log location
- Dependency availability
- Backup requirement

## Lessons Learned

Record reusable lessons instead of copying the exploratory session transcript.

## Related Documentation

- [Architecture](../architecture/example.md)
- [Decision record](../decisions/adr-0000-example.md)
- [Validation](../validation/component.md)
- [Service record](../services/component.md)

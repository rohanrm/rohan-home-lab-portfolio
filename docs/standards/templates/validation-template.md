# Component Validation

| Field | Value |
|---|---|
| Document status | Draft |
| Validation status | Not Started |
| Visibility | Public |
| Validation date | Not yet validated |
| Source of truth for | Component validation |

## Purpose

Explain what this validation is intended to prove.

## Environment

| Item | Value |
|---|---|
| Component | Component name |
| Platform | Platform |
| Relevant version | Version or `Recorded privately` |
| Validation scope | Scope |

Do not publish exact identifiers unless they are necessary and approved.

## Validation Criteria

| ID | Check | Expected result | Status |
|---|---|---|---|
| VAL-01 | Check description | Expected result | Not Started |
| VAL-02 | Check description | Expected result | Not Started |

## Validation Procedure

### VAL-01 — Check name

Command:

```bash
command
```

Expected result:

```text
Sanitized expected output
```

Observed result:

```text
Sanitized observed output
```

Status: `Passed`

### VAL-02 — Check name

Command:

```bash
command
```

Expected result:

```text
Sanitized expected output
```

Observed result:

```text
Sanitized observed output
```

Status: `Passed`

## Exceptions

Document failed, blocked, skipped, or partially satisfied checks.

| Check | Exception | Impact | Follow-up |
|---|---|---|---|
| None | None | None | None |

## Evidence Summary

Summarize the evidence supporting the conclusion.

Store complete identifying output in the private operational repository when it remains useful.

## Conclusion

State whether the component is:

- Not Started
- In Progress
- Validated
- Validated with a documented exception
- Not validated

Do not mark a component operational solely because installation completed.

## Revalidation Triggers

Re-run relevant checks after:

- Major version upgrade
- Storage change
- Network change
- Permission-model change
- Configuration replacement
- Host migration
- Restore from backup

## Related Documentation

- [Implementation](../implementation/component.md)
- [Architecture](../architecture/example.md)
- [Service record](../services/component.md)

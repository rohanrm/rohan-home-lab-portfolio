# Architecture Title

| Field | Value |
|---|---|
| Document status | Draft |
| Visibility | Public |
| Last reviewed | YYYY-MM-DD |
| Source of truth for | Architectural area |

## Purpose

Explain what this architecture document covers and why it exists.

## Scope

### Included

- Component, flow, or responsibility

### Excluded

- Detailed implementation procedure
- Raw validation output
- Private operational identifiers

## Context

Describe the requirement, environment, constraints, and problem being solved.

## Current Architecture

Describe the architecture as it exists now.

Do not mix planned components into this section.

## Components and Responsibilities

| Component | Responsibility | Platform | Status |
|---|---|---|---|
| Component | Responsibility | Platform | Operational |

## Data or Traffic Flow

Describe important flows in numbered sequence.

1. A client initiates a request.
2. The request reaches the appropriate network or service component.
3. Dependencies process the request.
4. The result returns to the client.

## Storage and Dependencies

| Dependency | Purpose | Failure impact |
|---|---|---|
| Dependency | Purpose | Impact |

## Security and Trust Boundaries

Describe:

- Where trust changes
- Which components accept inbound connections
- How least privilege is applied
- Which details are intentionally maintained privately

Do not publish secrets or unnecessarily detailed defensive configuration.

## Constraints

- Hardware constraint
- Software constraint
- Operational constraint
- Learning or budget constraint

## Planned Architecture

Describe approved future changes.

Use `Idea` or `Planned` precisely. Do not present an idea as an approved target.

## Alternatives

Summarize alternatives only when useful. Significant choices should link to ADRs.

## Related Decisions

- [ADR-0000 — Decision title](../decisions/adr-0000-example.md)

## Validation References

- [Validation document](../validation/example.md)

## Related Documentation

- [Implementation document](../implementation/example.md)
- [Service document](../services/example.md)
- [Reference document](../reference/example.md)

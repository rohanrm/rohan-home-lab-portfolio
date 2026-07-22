# Documentation Standard

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-07-21 |
| Source of truth for | Version 3 documentation rules |

## Purpose

This standard defines how documentation in the public home-lab repository is organized, written, reviewed, and maintained.

Its goals are to make the repository:

- Accurate
- Easy to navigate
- Useful as an operational learning record
- Suitable for an employer-facing portfolio
- Safe to publish
- Maintainable as the lab grows

## Core Principles

### One source of truth

Each important fact should have one primary home. Other documents should link to it instead of repeating it.

Examples:

| Fact | Source of truth |
|---|---|
| Hardware capability | `reference/hardware-profile.md` |
| Logical network design | `architecture/network-architecture.md` |
| Build steps | Relevant file in `implementation/` |
| Test evidence | Relevant file in `validation/` |
| Service status | `services/README.md` |
| Approved future work | `planning/roadmap.md` |

### Current state before future state

Documents must describe what exists now before discussing planned changes.

Use separate headings:

```markdown
## Current State
```

```markdown
## Planned State
```

Do not describe a planned service as deployed or operational.

### Implementation is not validation

An implementation record explains what was changed.

A validation record proves whether the resulting system meets defined checks.

A command appearing in an implementation guide does not, by itself, prove that the component works.

### Public explanation, private operation

The public repository demonstrates architecture, reasoning, procedures, and learning.

Exact operational identifiers and sensitive infrastructure details belong in the separate private repository.

Secrets belong in neither Git repository.

### Git is the revision history

Do not add revision-history tables to individual documents.

Git already records:

- Authors
- Dates
- Commits
- Changed lines
- Previous versions

The repository changelog should contain only meaningful milestones.

## Directory Responsibilities

| Directory | Responsibility |
|---|---|
| `architecture/` | Current and target system design |
| `decisions/` | Significant architectural decisions |
| `implementation/` | Build and configuration procedures |
| `validation/` | Test criteria, evidence, and conclusions |
| `services/` | Service role, dependencies, lifecycle, and operations |
| `operations/` | Routine administration and troubleshooting |
| `reference/` | Stable facts and policies |
| `planning/` | Approved work and future exploration |
| `history/` | Meaningful milestones |
| `standards/` | Documentation governance and templates |

Project phase numbers should not be used as directory names. Phases change; document purposes are more stable.

## File Naming

Use lowercase kebab-case for normal Markdown files:

```text
network-architecture.md
samba-systemd-automount.md
network-addressing-policy.md
```

Use uppercase `README.md` for repository and directory indexes.

Use stable numeric identifiers for record series:

```text
adr-0001-defer-unknown-wireless-devices.md
adr-0002-select-beelink-eq14.md
```

Avoid:

- Spaces
- Underscores
- Ambiguous abbreviations
- Dates in normal document filenames
- Names such as `new`, `final`, `latest`, or `v2-final`

Dates are appropriate for timestamped evidence records, exports, and raw snapshots.

## Heading Rules

Each Markdown file must have exactly one H1 heading:

```markdown
# Document Title
```

Use H2 headings for major sections:

```markdown
## Purpose
## Current State
## Validation
```

Use H3 headings for subsections:

```markdown
### Storage
### Networking
```

Do not use additional H1 headings inside the same document.

## Document Metadata

Substantive documents should begin with a metadata table after the H1 heading.

Example:

```markdown
| Field | Value |
|---|---|
| Document status | Current |
| System status | Operational |
| Visibility | Public |
| Last validated | 2026-07-20 |
| Source of truth for | Component implementation |
```

Use only fields that apply to that document.

## Controlled Status Vocabulary

### Infrastructure and service lifecycle

| Status | Meaning |
|---|---|
| `Idea` | Worth recording but not approved |
| `Planned` | Approved but not started |
| `In Progress` | Active work is underway |
| `Implemented` | Configuration is complete, but validation is outstanding |
| `Validated` | Defined tests passed |
| `Operational` | Validated and actively used |
| `Paused` | Intentionally stopped with an intention to resume |
| `Blocked` | Cannot proceed because of an unresolved dependency |
| `Retired` | Removed from active use |
| `Rejected` | Considered and explicitly not selected |

### Document lifecycle

| Status | Meaning |
|---|---|
| `Draft` | Incomplete and not authoritative |
| `Current` | Reviewed and authoritative |
| `Needs Review` | Possibly stale or awaiting verification |
| `Superseded` | Replaced by an identified document |
| `Archived` | Preserved only for historical reasons |

### Validation lifecycle

| Status | Meaning |
|---|---|
| `Not Started` | No validation has been performed |
| `In Progress` | Validation is underway |
| `Passed` | The check met its expected result |
| `Failed` | The check did not meet its expected result |
| `Blocked` | The check cannot currently be performed |
| `Not Applicable` | The check does not apply |
| `Passed with Exception` | Core requirement passed with a documented limitation |

### ADR lifecycle

| Status | Meaning |
|---|---|
| `Proposed` | Under consideration |
| `Accepted` | Approved |
| `Rejected` | Considered but not selected |
| `Superseded` | Replaced by a later ADR |
| `Deprecated` | Retained historically but no longer recommended |

Do not replace the written status with an emoji. Emojis may be decorative, but the controlled term is authoritative.

## Dates

Use ISO 8601 format:

```text
2026-07-20
```

Avoid ambiguous forms such as:

```text
07/20/26
20/07/26
```

## Links

Use relative Markdown links for files in the same repository:

```markdown
[Service architecture](../architecture/service-architecture.md)
```

Do not use full GitHub URLs for internal documents.

Link to the primary source instead of copying large sections into multiple files.

## Commands and Output

Do not include the shell prompt in reusable commands.

Use:

```bash
docker compose ps
```

Not:

```text
rohan@docker:/opt/docker/jellyfin$ docker compose ps
```

Place observed output in a separate text block:

```text
NAME        STATUS
jellyfin    Up
```

Public output must be sanitized when it contains:

- Exact internal addresses
- MAC addresses
- Serial numbers
- UUIDs
- Usernames that add no technical value
- Household-device names
- Security-sensitive configuration
- Secrets

## Architecture Documents

Architecture documents should normally include:

- Purpose
- Scope
- Context
- Current architecture
- Components and responsibilities
- Important data or traffic flows
- Storage and dependencies
- Security and trust boundaries
- Constraints
- Planned architecture
- Related ADRs
- Validation references

Architecture documents explain design rather than providing a complete command transcript.

## Implementation Documents

Implementation documents should normally include:

- Purpose
- Starting state
- Prerequisites
- Design summary
- Implementation procedure
- Configuration changes
- Validation link
- Rollback
- Operational notes
- Lessons learned

Implementation records should transform exploratory work into a clear, repeatable procedure.

## Validation Documents

Validation documents should normally include:

- Purpose
- Environment
- Criteria
- Commands
- Expected results
- Sanitized observed results
- Status for each check
- Exceptions
- Evidence summary
- Conclusion
- Revalidation triggers

Raw identifying evidence should be preserved privately when it is operationally useful.

## Decision Records

Each significant decision receives its own ADR.

An accepted ADR should not be rewritten to make history appear different. A later decision should create a new ADR and mark the earlier one as superseded when appropriate.

Appropriate ADR topics include:

- Selecting a platform
- Choosing VM versus LXC
- Changing storage design
- Approving a new security boundary
- Replacing a major service
- Rejecting a significant alternative

Routine package updates do not normally require ADRs.

## Service Documents

A service document explains:

- What the service provides
- Where it runs
- Its lifecycle status
- Dependencies
- Storage
- Access model
- Routine operations
- Backup and recovery needs
- Monitoring
- Security considerations
- Known limitations

The service document is not a duplicate of its implementation guide.

## Changelog Rules

The changelog should record meaningful milestones such as:

- Completion of a project stage
- Deployment of a major service
- A significant architectural change
- A public/private documentation redesign
- Retirement of an important component

Do not create a changelog entry for every spelling fix or link correction.

## Writing Style

Use clear, direct language.

Prefer:

- Short paragraphs
- Descriptive headings
- Tables for structured comparisons
- Lists for steps and checks
- Explanations of why a decision matters

Avoid:

- Unexplained jargon
- Marketing language
- Repeated introductory text
- Claims that are not supported by validation
- Large unedited terminal transcripts
- Information copied into several documents

## Review Checklist

Before marking a document `Current`, verify:

- [ ] The file is in the correct directory.
- [ ] The filename follows the naming standard.
- [ ] The file has exactly one H1.
- [ ] Metadata is present and accurate.
- [ ] Current and future states are separated.
- [ ] Status terms use the controlled vocabulary.
- [ ] Sensitive values are absent or generalized.
- [ ] Claims of success link to validation evidence.
- [ ] Internal links are relative and resolve correctly.
- [ ] Commands do not contain shell prompts.
- [ ] The document does not duplicate another source of truth.
- [ ] `git diff --check` reports no whitespace errors.

## Change Workflow

For a documentation batch:

1. Work on a dedicated branch.
2. Confirm the working tree is clean.
3. Apply or create the batch.
4. Review `git diff --stat`.
5. Review `git diff`.
6. Run `git diff --check`.
7. Check links and headings.
8. Commit the batch with a focused message.
9. Merge only after review.

Recommended commit style:

```text
docs: add Version 3 documentation standards
```

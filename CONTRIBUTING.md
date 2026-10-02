# Contributing

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Documentation contribution and review workflow |

## Purpose

This repository is primarily a personal home-lab portfolio, but changes should still follow a consistent review process.

The contribution workflow is designed to protect:

- Technical accuracy
- Documentation consistency
- The public/private information boundary
- Validation evidence
- Clean Git history
- The current architecture and lifecycle vocabulary

## Before Making a Change

Confirm:

1. The change belongs in the public repository.
2. Exact operational values belong in the private repository instead.
3. A secret is not required in Git.
4. The current source-of-truth document has been identified.
5. The working tree is clean.
6. The change is being made on an appropriate branch.

Recommended check:

```bash
git status --short
git branch --show-current
```

## Documentation Placement

| Change type | Primary location |
|---|---|
| Architecture design | `docs/architecture/` |
| Significant decision | `docs/decisions/` |
| Build procedure | `docs/implementation/` |
| Test evidence | `docs/validation/` |
| Service role and lifecycle | `docs/services/` |
| Routine administration | `docs/operations/` |
| Stable facts and policy | `docs/reference/` |
| Approved future work | `docs/planning/roadmap.md` |
| Unapproved idea | `docs/planning/future-exploration.md` |
| Meaningful milestone | `docs/history/changelog.md` |
| Release and publication process | `docs/release/` |

Do not create a new file when an existing source-of-truth document should be updated.

## Writing Rules

Follow the [Documentation Standard](docs/standards/documentation-standard.md).

Key rules:

- Use one H1 heading per Markdown file.
- Use lowercase kebab-case filenames except `README.md`.
- Use ISO dates.
- Keep current and planned states separate.
- Use controlled lifecycle terms.
- Do not include copied shell prompts in reusable commands.
- Keep implementation and validation separate.
- Replace duplicated facts with links.
- Do not add per-file revision-history tables.

## Public and Private Information

Follow the [Public and Private Information Boundary](docs/standards/public-private-boundary.md).

Do not commit:

- Passwords
- Tokens
- Private keys
- Credential files
- Exact internal IP allocations
- MAC addresses
- Serial numbers
- Disk UUIDs
- Household-device names
- Raw identifying output
- Detailed recovery secrets

When exact operational data is necessary, update the private repository separately.

## Branch Workflow

Use a focused branch for meaningful changes.

Example:

```bash
git switch -c docs/update-jellyfin-validation
```

Keep one branch focused on one coherent outcome.

## Local Validation

Run the permanent audit tool:

```bash
python3 tools/audit-v4.py .
```

Validate JSON configuration:

```bash
python3 -m json.tool .markdownlint.json >/dev/null
```

Check whitespace:

```bash
git diff --check
```

Review the full change:

```bash
git diff --stat
git diff
```

## Staging Review

Stage only the intended files:

```bash
git add <paths>
```

Then review:

```bash
git status --short
git diff --cached --check
git diff --cached --stat
git diff --cached
```

Use `git add -A` only when deletions are intentionally part of the change.

## Commit Messages

Use a concise prefix and outcome.

Examples:

```text
docs: validate Jellyfin deployment
docs: update service architecture
docs: add backup decision record
ci: add documentation audit
fix: correct broken documentation links
```

Avoid vague messages such as:

```text
update files
changes
final version
```

## Pull Request Review

A pull request should explain:

- What changed
- Why it changed
- Which lifecycle statuses changed
- Which validation evidence supports the change
- Whether private operational records were updated
- Whether the public audit passed

Use the repository pull-request template.

## Status Changes

A status change requires evidence.

Examples:

- `In Progress` to `Implemented`: configuration is complete.
- `Implemented` to `Validated`: defined tests passed.
- `Validated` to `Operational`: the service is actively used and stable.
- `Planned` to `In Progress`: work has actually begun.
- `Idea` to `Planned`: the work has been approved.

Do not promote a service merely because a package was installed.

## Architecture Decisions

Create a new ADR when a meaningful design choice has long-term consequences.

Do not rewrite an accepted ADR to make history appear different.

Use the [Decision Template](docs/standards/templates/decision-template.md).

## Release Changes

Changes affecting public publication must update, when relevant:

- `README.md`
- `docs/README.md`
- `docs/release/`
- `docs/planning/roadmap.md`
- `docs/history/changelog.md`
- `tools/audit-v4.py`

Run the [Publication Checklist](docs/release/publication-checklist.md) before creating a clean-history public release.

## Related Documentation

- [Documentation Standard](docs/standards/documentation-standard.md)
- [Public and Private Information Boundary](docs/standards/public-private-boundary.md)
- [Documentation Index](docs/README.md)
- [Publication Checklist](docs/release/publication-checklist.md)

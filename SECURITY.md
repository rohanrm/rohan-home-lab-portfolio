# Security Policy

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-07-22 |
| Source of truth for | Security reporting and accidental-exposure response |

## Purpose

This policy explains how to report a security concern involving the public home-lab documentation repository.

The repository is a documentation portfolio. It does not intentionally publish live credentials, private keys, access tokens, exact internal addressing, or detailed recovery information.

## Supported Scope

Security reports are relevant when they involve:

- A credential or secret committed to the repository
- Exact private infrastructure data exposed unintentionally
- A workflow that could disclose repository secrets
- A malicious or unsafe contribution path
- A public document that exposes unnecessary household information
- A release archive containing excluded operational data

General infrastructure support questions belong in normal project documentation rather than a security report.

## How to Report a Concern

Do not open a public issue containing the sensitive value.

Use a private GitHub security-reporting method when available.

When private reporting is unavailable, contact the repository owner through the GitHub profile without copying the secret or sensitive value into a public message.

Include:

- Affected file and line
- Commit or release where the issue appears
- Classification: secret, private operational data, or workflow risk
- Whether the value appears in Git history
- Whether the value is still active
- Suggested immediate containment

Do not include:

- Full passwords
- Complete access tokens
- Private keys
- Recovery codes
- Session cookies
- Complete credential files

A short masked excerpt is sufficient to identify the issue.

## Response Priorities

### Exposed secret

When a secret is committed:

1. Treat it as compromised.
2. Revoke or rotate it immediately.
3. Remove it from the current working tree.
4. Assess earlier commits, pull requests, workflow logs, forks, and release archives.
5. Decide whether history must be replaced or rewritten.
6. Verify that the replacement secret is not committed.
7. Record the incident privately.

Deleting the line does not make the original secret safe again.

### Exposed private operational data

When a non-secret private value is published:

1. Remove it from the public document.
2. Preserve it privately only when operationally useful.
3. Review nearby content for related exposure.
4. Assess whether the public release should be replaced.
5. Update the audit rules when the pattern can be detected reliably.

Examples include:

- Exact private IP assignments
- MAC addresses
- Disk UUIDs
- Serial numbers
- Household-device names
- Administrative URLs
- Detailed cable or port maps

### Unsafe workflow change

When a workflow introduces unnecessary permissions or untrusted code execution:

1. Disable or revert the workflow.
2. Review workflow-run logs.
3. Review token and secret access.
4. Reduce permissions to the minimum required.
5. Re-run validation in a controlled branch.
6. Document the corrected trust boundary.

## Repository Security Controls

The public repository uses:

- A documented public/private information boundary
- A permanent repository audit tool
- A read-only GitHub Actions workflow
- Controlled lifecycle statuses
- A release checklist
- Clean-history publication guidance
- Manual staged-diff review

The automated audit supplements human review. It cannot prove that every sensitive value is absent.

## GitHub Actions Boundary

The documentation-audit workflow:

- Runs on pushes and pull requests
- Uses read-only repository permissions
- Does not require repository secrets
- Does not use `pull_request_target`
- Does not push changes
- Runs the repository's local audit script

A future workflow requiring write access or secrets must receive a separate security review.

## Disclosure Expectations

Reasonable effort will be made to:

- Acknowledge a valid report
- Contain active exposure quickly
- Correct the current repository state
- Replace unsafe public release artifacts
- Document reusable lessons without republishing the sensitive value

No guaranteed response-time service level is provided for this personal project.

## Related Documentation

- [Public and Private Information Boundary](docs/standards/public-private-boundary.md)
- [Publication Checklist](docs/release/publication-checklist.md)
- [Clean-History Publication](docs/release/clean-history-publication.md)
- [Troubleshooting Guide](docs/operations/troubleshooting.md)

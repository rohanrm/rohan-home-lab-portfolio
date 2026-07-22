# Release Documentation

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-07-22 |
| Source of truth for | Public-release preparation and validation navigation |

## Purpose

This directory contains the procedures required to publish the sanitized Version 3 documentation through a fresh Git history.

The development repository and the employer-facing publication have different responsibilities:

- The development repository preserves the working history.
- The employer-facing repository contains only the sanitized Version 3 state and later public-safe changes.

## Release Documents

| Document | Purpose |
|---|---|
| [Publication Checklist](publication-checklist.md) | Confirms the source tree is safe and complete before export |
| [Clean-History Publication](clean-history-publication.md) | Creates a new repository without carrying old commits forward |
| [Repository Release Validation](repository-release-validation.md) | Proves that the published repository contains the intended files and controls |

## Release Sequence

```text
Validate source branch
  → Export tracked Version 3 tree
  → Inspect export
  → Initialize fresh Git repository
  → Create clean first commit
  → Push to new public repository
  → Validate remote publication
```

## Security Boundary

Do not:

- Make the development repository public solely because its current tree is sanitized.
- Copy its `.git` directory into the release.
- Force-push sanitized content over an existing history without a separately reviewed plan.
- Copy files from the private operational repository.
- Include local baseline exports or temporary ZIP packages.
- Include credentials or exact infrastructure identifiers.

## Related Documentation

- [Security Policy](../../SECURITY.md)
- [Contributing](../../CONTRIBUTING.md)
- [Public and Private Information Boundary](../standards/public-private-boundary.md)
- [Roadmap](../planning/roadmap.md)
- [Changelog](../history/changelog.md)

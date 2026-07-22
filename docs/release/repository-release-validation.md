# Repository Release Validation

| Field | Value |
|---|---|
| Document status | Current |
| Validation status | Passed |
| Visibility | Public |
| Last reviewed | 2026-07-22 |
| Source of truth for | Evidence that the clean-history public repository was published correctly |

## Purpose

This document records the validation of the clean-history employer-facing repository.

## Release Identification

| Item | Value |
|---|---|
| Source development branch | `docs-v3-redesign` |
| Source development commit | `340bf88295c25d47df3161bf1f430b94311cf95e` |
| Release repository | `https://github.com/rohanrm/rohan-home-lab-portfolio` |
| Release first commit | `98e84dad9dd5ecc9cbefc9a9855641e17ec180b8` |
| Release date | 2026-07-22 |
| Repository visibility | Public |

No credential, private URL, or operational infrastructure identifier is recorded here.

## Validation Summary

| ID | Check | Expected result | Status |
|---|---|---|---|
| REL-01 | Clean commit history | Public repository starts with the sanitized publication commit | Passed |
| REL-02 | Required structure | All expected Version 3 files exist | Passed |
| REL-03 | Legacy removal | No Version 2 files exist | Passed |
| REL-04 | Local link audit | All local Markdown links resolve | Passed |
| REL-05 | Metadata audit | Controlled statuses are valid | Passed |
| REL-06 | Privacy audit | No exact private IP or MAC patterns detected | Passed |
| REL-07 | Secret review | No credentials, keys, or tokens present | Passed |
| REL-08 | README rendering | Root README renders correctly | Passed |
| REL-09 | Mermaid rendering | Architecture diagrams render | Passed |
| REL-10 | GitHub Actions | Documentation audit workflow passes | Passed |
| REL-11 | Security files | Security and contribution guidance appear | Passed |
| REL-12 | Repository visibility | Intended public visibility confirmed | Passed |

## Automated Evidence

The release passed:

```bash
python3 tools/audit-v3.py .
python3 -m json.tool .markdownlint.json
```

The validation confirmed:

- Expected Version 3 structure
- Exactly one real H1 per Markdown document
- Controlled metadata statuses
- Valid local Markdown links
- No legacy Version 2 files
- No detected production private-address or MAC patterns
- No complete private-key block
- No copied development Git history

## Remote Evidence

The public repository was reviewed after publication.

Confirmed:

- Local `main` matched remote `main`.
- The initial public commit was the sanitized publication commit.
- The root README rendered correctly.
- Mermaid diagrams rendered correctly.
- The documentation-audit workflow passed.
- Repository visibility displayed as public.
- Development and private repositories remained separate.

## Validation Conclusion

```text
Passed
```

The clean-history employer-facing publication is operational.

## Revalidation Triggers

Repeat relevant checks after:

- Repository rename or transfer
- GitHub Actions change
- Security-policy change
- New documentation category
- Major architecture update
- New service becoming operational
- Accidental exposure incident
- Replacement of the public repository

## Related Documentation

- [Publication Checklist](publication-checklist.md)
- [Clean-History Publication](clean-history-publication.md)
- [Security Policy](../../SECURITY.md)
- [Documentation Audit Workflow](../../.github/workflows/documentation-audit.yml)

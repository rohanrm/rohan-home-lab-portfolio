# Repository Release Validation

| Field | Value |
|---|---|
| Document status | Current |
| Validation status | Not Started |
| Visibility | Public |
| Last reviewed | 2026-07-22 |
| Source of truth for | Evidence that the clean-history public repository was published correctly |

## Purpose

This document records the tests required after creating the fresh employer-facing repository.

It should be updated with sanitized observed results after publication.

## Release Identification

| Item | Value |
|---|---|
| Source development branch | `docs-v3-redesign` |
| Source development commit | Not yet recorded |
| Release repository | Not yet created |
| Release first commit | Not yet recorded |
| Release date | Not yet published |
| Repository visibility | Not yet validated |

Do not record access tokens, private URLs, or operational infrastructure identifiers.

## Validation Criteria

| ID | Check | Expected result | Status |
|---|---|---|---|
| REL-01 | Clean commit history | Public repository starts with the sanitized publication commit | Not Started |
| REL-02 | Required structure | All expected Version 3 files exist | Not Started |
| REL-03 | Legacy removal | No Version 2 files exist | Not Started |
| REL-04 | Local link audit | All local Markdown links resolve | Not Started |
| REL-05 | Metadata audit | Controlled statuses are valid | Not Started |
| REL-06 | Privacy audit | No exact private IP or MAC patterns detected | Not Started |
| REL-07 | Secret review | No credentials, keys, or tokens present | Not Started |
| REL-08 | README rendering | Root README renders correctly | Not Started |
| REL-09 | Mermaid rendering | Architecture diagrams render | Not Started |
| REL-10 | GitHub Actions | Documentation audit workflow passes | Not Started |
| REL-11 | Security files | `SECURITY.md` and contribution guidance appear | Not Started |
| REL-12 | Repository visibility | Intended public visibility confirmed | Not Started |

## REL-01 — Clean Commit History

Local command in the release clone:

```bash
git log --oneline --decorate
```

Expected:

- First public commit is the sanitized publication commit.
- No development-repository commits appear.
- No merge from the development repository appears.

Observed result:

```text
Not yet validated
```

Status: `Not Started`

## REL-02 — Required Structure

Run:

```bash
python3 tools/audit-v3.py .
```

Expected:

```text
Errors: 0
Audit passed.
```

Observed result:

```text
Not yet validated
```

Status: `Not Started`

## REL-03 — Legacy Removal

Run:

```bash
find docs -maxdepth 1 -type f -name '*.md' -print
```

Expected:

```text
docs/README.md
```

Also confirm that the old misspelled troubleshooting filename and combined Version 2 files are absent.

Status: `Not Started`

## REL-04 — Local Link Audit

The repository-local audit tool must report no broken local links.

Status: `Not Started`

## REL-05 — Metadata Audit

The repository-local audit must accept all opening metadata-table status values.

Status: `Not Started`

## REL-06 — Privacy Audit

Run the repository-local audit and review additional search results:

```bash
git grep -nE \
  '([0-9]{1,3}\.){3}[0-9]{1,3}|([[:xdigit:]]{2}:){5}[[:xdigit:]]{2}' \
  -- '*.md' '*.yml' '*.yaml' '*.json' '*.py' || true
```

Expected:

- No production private address
- No MAC address
- Documentation-only public examples reviewed and approved

Status: `Not Started`

## REL-07 — Secret Review

Run:

```bash
git grep -nEi \
  'password|passwd|api[_ -]?key|access[_ -]?token|secret|private[_ -]?key|credentials' \
  -- '*.md' '*.yml' '*.yaml' '*.json' '*.py' || true
```

Every match must be reviewed.

Expected:

- Explanatory security text only
- No actual credential value
- No private-key block
- No secret file

Status: `Not Started`

## REL-08 — README Rendering

On GitHub, verify:

- Project summary is readable.
- Current service statuses are accurate.
- Documentation links work.
- Publication-history warning is present.
- No private value appears.

Status: `Not Started`

## REL-09 — Mermaid Rendering

Open:

- Network architecture
- Physical topology
- Service architecture
- Service catalogue

Expected:

- Diagrams render without syntax errors.
- Labels remain sanitized.
- Current and planned components are distinguishable.

Status: `Not Started`

## REL-10 — GitHub Actions

Open the documentation-audit workflow run.

Expected:

- Checkout succeeds.
- Repository audit passes.
- JSON configuration check passes.
- Trailing-whitespace check passes.
- Workflow uses no secrets.

Status: `Not Started`

## REL-11 — Security and Contribution Files

Verify the repository displays:

- `CONTRIBUTING.md`
- `SECURITY.md`
- Pull-request template
- Release documentation
- Permanent audit tool

Status: `Not Started`

## REL-12 — Repository Visibility

Confirm:

- Repository is intentionally public.
- Development repository remains private.
- Private operational repository remains private.
- New public remote is not accidentally attached to either private working repository.

Status: `Not Started`

## Validation Conclusion

Current conclusion:

```text
Not yet published
```

The release must not be marked validated until all mandatory checks pass.

## Revalidation Triggers

Repeat relevant checks after:

- First public publication
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

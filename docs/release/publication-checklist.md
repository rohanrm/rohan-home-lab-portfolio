# Publication Checklist

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Publication Checklist |



## Required checks

- [ ] Every source document has a recorded disposition in the V4 audit.
- [ ] Current architecture agrees across README, architecture, service catalogue and roadmap.
- [ ] Dated results remain distinct from newly performed tests.
- [ ] Private addresses, MACs, UUIDs, household identities and access endpoints are absent publicly.
- [ ] Detailed rule/port maps and raw DNS/client history remain excluded publicly.
- [ ] Passwords, keys, tokens, credential files and sensitive backups are absent from both Git trees.
- [ ] Images and SVG metadata have been reviewed as well as prose.
- [ ] Local links and fragments resolve, SVGs parse, and Markdown structure checks pass.
- [ ] The public branch has public-only commit ancestry.
- [ ] The private companion does not appear in the public tree.
- [ ] Remote files and GitHub Actions results are verified after push.

## Commands

```bash
python3 tools/audit-v4.py .
python3 -m json.tool .markdownlint.json
git diff --check
```

Use `--private` only inside the private blueprint. It permits non-secret operational identifiers solely in `private/`; the shared documentation remains subject to public checks. Automation supplements content review rather than certifying that no secret can exist.

See [release validation](repository-release-validation.md) and [pruning recommendations](pruning-recommendations.md).

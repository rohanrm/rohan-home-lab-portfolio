# Pull Request

## Summary

Describe the documentation or automation change.

## Reason

Explain why the change is needed and which source-of-truth document is affected.

## Lifecycle Changes

List any status transition:

```text
No lifecycle change
```

## Validation

- [ ] `python3 tools/audit-v4.py .` passes.
- [ ] `python3 -m json.tool .markdownlint.json` passes.
- [ ] `git diff --check` passes.
- [ ] Local Markdown links resolve.
- [ ] Current and planned states remain separate.
- [ ] Validation claims are supported by evidence.

## Public and Private Boundary

- [ ] No password, token, key, credential file, or recovery code is included.
- [ ] No exact private IP allocation is included.
- [ ] No MAC address, serial number, or disk UUID is included.
- [ ] No household-device or personal-client name is included.
- [ ] Required exact operational values were updated privately instead.

## Documentation Impact

- [ ] Relevant implementation record updated.
- [ ] Relevant validation record updated.
- [ ] Service catalogue updated when status changed.
- [ ] Architecture updated only when design changed.
- [ ] Roadmap updated when approved work changed.
- [ ] Changelog updated for a meaningful milestone.

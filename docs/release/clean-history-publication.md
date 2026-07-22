# Clean-History Publication

| Field | Value |
|---|---|
| Document status | Current |
| System status | Planned |
| Visibility | Public |
| Last reviewed | 2026-07-22 |
| Source of truth for | Creating a fresh employer-facing Git repository |

## Purpose

This procedure creates a new public repository from the sanitized Version 3 tree without carrying the development repository's earlier commits into the release.

Deleting a sensitive file from the current branch does not remove it from previous commits.

The release must therefore be created from tracked files only and initialized as a new Git repository.

## Preconditions

Before starting:

- Public Batch 9 is committed.
- The Version 3 audit passes.
- The development working tree is clean.
- The source commit is recorded.
- The publication checklist has been reviewed.
- A new empty GitHub repository is available.
- The private operational repository is not used as a source.

## Variables

Choose temporary paths outside the development repository:

```bash
SOURCE_REPO=/workspaces/rohan-home-lab-blueprint
SOURCE_BRANCH=docs-v3-redesign
EXPORT_TAR=/tmp/rohan-home-lab-public.tar
RELEASE_DIR=/tmp/rohan-home-lab-public
```

Choose the new remote only after creating the empty GitHub repository:

```bash
NEW_PUBLIC_REMOTE=<new-public-repository-url>
```

Do not put credentials into the URL.

## Step 1 — Validate the Source

```bash
git -C "$SOURCE_REPO" branch --show-current
git -C "$SOURCE_REPO" status --short
git -C "$SOURCE_REPO" log -1 --oneline
python3 "$SOURCE_REPO/tools/audit-v3.py" "$SOURCE_REPO"
```

Expected:

- Correct Version 3 branch
- Clean working tree
- Audit passes

Record the source commit privately or in the release-validation record.

## Step 2 — Create a Tracked-File Export

Remove previous temporary output:

```bash
rm -rf "$RELEASE_DIR" "$EXPORT_TAR"
```

Create the archive directly from Git:

```bash
git -C "$SOURCE_REPO" archive \
  --format=tar \
  --output="$EXPORT_TAR" \
  "$SOURCE_BRANCH"
```

Create the release directory and extract:

```bash
mkdir -p "$RELEASE_DIR"
tar -xf "$EXPORT_TAR" -C "$RELEASE_DIR"
```

Using `git archive` ensures that untracked local files and the original `.git` directory are not copied.

## Step 3 — Inspect the Export

List top-level content:

```bash
find "$RELEASE_DIR" -maxdepth 2 -type f | sort
```

Confirm no Git history exists:

```bash
test ! -e "$RELEASE_DIR/.git" &&
    echo "No Git history copied"
```

Confirm no local batch artifacts exist:

```bash
find "$RELEASE_DIR" \
  -type f \
  \( -name 'public-batch-*.zip' \
  -o -name '*baseline*.txt' \
  -o -name '*baseline*.tar.gz' \) \
  -print
```

Expected: no output.

## Step 4 — Audit the Export

```bash
python3 "$RELEASE_DIR/tools/audit-v3.py" "$RELEASE_DIR"
python3 -m json.tool "$RELEASE_DIR/.markdownlint.json" >/dev/null
```

Expected:

```text
Errors: 0
Audit passed.
```

Review all files:

```bash
find "$RELEASE_DIR" -type f | sort
```

## Step 5 — Initialize Fresh Git History

```bash
git -C "$RELEASE_DIR" init -b main
git -C "$RELEASE_DIR" add -A
git -C "$RELEASE_DIR" status --short
```

Review the first commit:

```bash
git -C "$RELEASE_DIR" diff --cached --stat
git -C "$RELEASE_DIR" diff --cached --check
```

Create the clean first commit:

```bash
git -C "$RELEASE_DIR" commit \
  -m "docs: publish sanitized home lab blueprint"
```

Confirm that only one commit exists:

```bash
git -C "$RELEASE_DIR" log --oneline --decorate
```

## Step 6 — Add the New Public Remote

Verify the value before using it:

```bash
printf '%s\n' "$NEW_PUBLIC_REMOTE"
```

Add the new remote:

```bash
git -C "$RELEASE_DIR" remote add origin "$NEW_PUBLIC_REMOTE"
```

Verify:

```bash
git -C "$RELEASE_DIR" remote -v
```

The remote must point to the new empty employer-facing repository, not the development or private repository.

## Step 7 — Push the Clean History

```bash
git -C "$RELEASE_DIR" push -u origin main
```

No force push should be required because the destination repository is empty.

## Step 8 — Validate the Remote Publication

On GitHub, confirm:

- Root README renders.
- Documentation links work.
- Mermaid diagrams render.
- Actions workflow starts.
- Documentation audit passes.
- Commit history begins with the clean publication commit.
- No development commits appear.
- No legacy files appear.
- Repository visibility is correct.

Update [Repository Release Validation](repository-release-validation.md) with the observed results in the development repository.

## Step 9 — Clean Temporary Files

After the remote publication is validated:

```bash
rm -rf "$RELEASE_DIR" "$EXPORT_TAR"
```

Do not remove the development repository or the private operational repository.

## Ongoing Public Development

After publication, future public-safe work can occur in the new repository.

Operational changes should continue to update:

- The private operational repository
- The public portfolio repository when the change is safe and meaningful
- Implementation and validation records
- Service lifecycle status
- Changelog milestones

Do not merge the old development history into the new public repository.

## Rollback

When the first public push is wrong:

1. Change the new repository visibility to private when necessary.
2. Remove or replace the affected public repository.
3. Correct the sanitized source branch.
4. Repeat the export from tracked files.
5. Create another new clean-history repository or approved replacement.
6. Rotate any secret that was exposed.

Do not assume that deleting a public repository immediately removes every clone or cached copy.

## Related Documentation

- [Publication Checklist](publication-checklist.md)
- [Repository Release Validation](repository-release-validation.md)
- [Security Policy](../../SECURITY.md)
- [Public and Private Information Boundary](../standards/public-private-boundary.md)

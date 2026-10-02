#!/usr/bin/env bash
set -euo pipefail
# Arguments: exact branch, expected commit and archive tag separated by '='.
if [[ $# -eq 0 ]]; then
  echo 'No archive targets supplied.' >&2
  exit 1
fi

git fetch --no-tags origin refs/heads/main:refs/remotes/origin/main
leases=()
changes=()
for target in "$@"; do
  IFS='=' read -r branch expected tag <<< "$target"
  [[ "$branch" == 'docs-v3-redesign' || "$branch" == 'docs-v4-redesign' ]] || exit 1
  [[ "$expected" =~ ^[0-9a-f]{40}$ && "$tag" == "archive/${branch}-2026-10-02" ]] || exit 1
  remote_head=$(git ls-remote origin "refs/heads/$branch" | cut -f1)
  [[ "$remote_head" == "$expected" ]] || { echo "Head moved or missing: $branch" >&2; exit 1; }
  git fetch --no-tags origin "refs/heads/$branch:refs/remotes/origin/$branch"
  [[ "$(git rev-parse "refs/remotes/origin/$branch")" == "$expected" ]] || exit 1
  git merge-base --is-ancestor "$expected" refs/remotes/origin/main || { echo "Unmerged branch: $branch" >&2; exit 1; }
  remote_tag=$(git ls-remote origin "refs/tags/$tag" | cut -f1)
  [[ -z "$remote_tag" || "$remote_tag" == "$expected" ]] || { echo "Conflicting archive tag: $tag" >&2; exit 1; }
  if [[ -z "$remote_tag" ]]; then
    git tag "$tag" "$expected"
    changes+=("refs/tags/$tag:refs/tags/$tag")
  fi
  leases+=("--force-with-lease=refs/heads/$branch:$expected")
  changes+=(":refs/heads/$branch")
done
# Tag creation and explicitly leased branch deletion are a single transaction.
git push --atomic origin "${leases[@]}" "${changes[@]}"
echo 'Archive tags saved and verified merged branches removed.'

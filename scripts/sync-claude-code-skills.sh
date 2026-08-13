#!/usr/bin/env bash
# Sync canonical GPT/Codex skills into the Claude Code project skills layout.
#
# Source of truth : skills/<name>/{SKILL.md,references/}
# Generated copy  : .claude/skills/<name>/{SKILL.md,references/}
#
# This script never touches skills/, canonical/, agents/, or assets/. It only
# writes under .claude/skills/. Re-run it any time skills/<name>/SKILL.md or
# skills/<name>/references/ change, to propagate the update to the Claude
# Code copy without hand-editing two places.
#
# Usage:
#   scripts/sync-claude-code-skills.sh          # sync + report what changed
#   scripts/sync-claude-code-skills.sh --check  # exit 1 if out of sync, no writes

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# The 8 Claude Code skills this repo distributes. articulate-marketing-problem
# exists in skills/ (Marketing Compass 00) but is intentionally NOT part of
# the Claude Code conversion scope and is left untouched here.
SKILLS=(
  diagnose-marketing-structure
  design-marketing-measurement
  evaluate-ad-investment
  design-btob-growth
  assess-ma-crm-ltv
  design-marketing-communications
  audit-marketing-reasoning
  thinking-staircase
)

CHECK_ONLY=0
if [[ "${1:-}" == "--check" ]]; then
  CHECK_ONLY=1
fi

CHANGED=0

for name in "${SKILLS[@]}"; do
  src="skills/$name"
  dst=".claude/skills/$name"

  if [[ ! -f "$src/SKILL.md" ]]; then
    echo "ERROR: missing source $src/SKILL.md" >&2
    exit 1
  fi

  if [[ "$CHECK_ONLY" -eq 1 ]]; then
    if [[ ! -f "$dst/SKILL.md" ]] || ! diff -q "$src/SKILL.md" "$dst/SKILL.md" >/dev/null 2>&1; then
      echo "OUT OF SYNC: $dst/SKILL.md"
      CHANGED=1
    fi
    if [[ -d "$src/references" ]]; then
      while IFS= read -r -d '' f; do
        rel="${f#"$src/references/"}"
        if [[ ! -f "$dst/references/$rel" ]] || ! diff -q "$f" "$dst/references/$rel" >/dev/null 2>&1; then
          echo "OUT OF SYNC: $dst/references/$rel"
          CHANGED=1
        fi
      done < <(find "$src/references" -type f -name '*.md' -print0)
    fi
    continue
  fi

  mkdir -p "$dst"
  if [[ ! -f "$dst/SKILL.md" ]] || ! diff -q "$src/SKILL.md" "$dst/SKILL.md" >/dev/null 2>&1; then
    cp "$src/SKILL.md" "$dst/SKILL.md"
    echo "updated: $dst/SKILL.md"
    CHANGED=1
  fi

  if [[ -d "$src/references" ]]; then
    mkdir -p "$dst/references"
    while IFS= read -r -d '' f; do
      rel="${f#"$src/references/"}"
      if [[ ! -f "$dst/references/$rel" ]] || ! diff -q "$f" "$dst/references/$rel" >/dev/null 2>&1; then
        cp "$f" "$dst/references/$rel"
        echo "updated: $dst/references/$rel"
        CHANGED=1
      fi
    done < <(find "$src/references" -type f -name '*.md' -print0)

    # Remove any generated reference file that no longer exists in the source,
    # so the Claude Code copy never drifts ahead of the canonical corpus.
    if [[ -d "$dst/references" ]]; then
      while IFS= read -r -d '' f; do
        rel="${f#"$dst/references/"}"
        if [[ ! -f "$src/references/$rel" ]]; then
          rm "$f"
          echo "removed (no longer in source): $dst/references/$rel"
          CHANGED=1
        fi
      done < <(find "$dst/references" -type f -name '*.md' -print0)
    fi
  fi
done

if [[ "$CHECK_ONLY" -eq 1 ]]; then
  if [[ "$CHANGED" -eq 1 ]]; then
    echo "Claude Code skill copies are out of sync with skills/. Run scripts/sync-claude-code-skills.sh to update." >&2
    exit 1
  fi
  echo "Claude Code skill copies are in sync with skills/."
  exit 0
fi

if [[ "$CHANGED" -eq 0 ]]; then
  echo "Already in sync. No files changed."
fi

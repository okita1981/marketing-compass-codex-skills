#!/usr/bin/env bash
# Shared logic for propagating the canonical skills/<name>/ corpus into any
# Claude Code-shaped copy (project skills at .claude/skills/, or a plugin's
# skills/ directory at plugin/skills/). Sourced by
# scripts/sync-claude-code-skills.sh and scripts/sync-claude-code-plugin.sh
# so both targets share one skill list and one copy/removal algorithm — no
# risk of the two destinations drifting apart when a skill is added, renamed,
# or removed.
#
# Not meant to be run directly.

# The 9 Claude Code skills this repo distributes: Marketing Compass 00-07
# (articulate-marketing-problem is the entry-point skill, 00) plus the
# related thinking-staircase skill. This is the single source of truth for
# "which skills go into every Claude Code-shaped copy" — add or remove a
# skill here once, and both sync targets pick up the change.
CLAUDE_CODE_SKILLS=(
  articulate-marketing-problem
  diagnose-marketing-structure
  design-marketing-measurement
  evaluate-ad-investment
  design-btob-growth
  assess-ma-crm-ltv
  design-marketing-communications
  audit-marketing-reasoning
  thinking-staircase
)

# sync_skills_to <dest-root-relative-to-repo-root> <check-only: 0|1>
#
# dest-root example: ".claude/skills" or "plugin/skills"
sync_skills_to() {
  local dest_root="$1"
  local check_only="$2"
  local changed=0
  local name src dst f rel

  for name in "${CLAUDE_CODE_SKILLS[@]}"; do
    src="skills/$name"
    dst="$dest_root/$name"

    if [[ ! -f "$src/SKILL.md" ]]; then
      echo "ERROR: missing source $src/SKILL.md" >&2
      exit 1
    fi

    if [[ "$check_only" -eq 1 ]]; then
      if [[ ! -f "$dst/SKILL.md" ]] || ! diff -q "$src/SKILL.md" "$dst/SKILL.md" >/dev/null 2>&1; then
        echo "OUT OF SYNC: $dst/SKILL.md"
        changed=1
      fi
      if [[ -d "$src/references" ]]; then
        while IFS= read -r -d '' f; do
          rel="${f#"$src/references/"}"
          if [[ ! -f "$dst/references/$rel" ]] || ! diff -q "$f" "$dst/references/$rel" >/dev/null 2>&1; then
            echo "OUT OF SYNC: $dst/references/$rel"
            changed=1
          fi
        done < <(find "$src/references" -type f -name '*.md' -print0)
      fi
      continue
    fi

    mkdir -p "$dst"
    if [[ ! -f "$dst/SKILL.md" ]] || ! diff -q "$src/SKILL.md" "$dst/SKILL.md" >/dev/null 2>&1; then
      cp "$src/SKILL.md" "$dst/SKILL.md"
      echo "updated: $dst/SKILL.md"
      changed=1
    fi

    if [[ -d "$src/references" ]]; then
      mkdir -p "$dst/references"
      while IFS= read -r -d '' f; do
        rel="${f#"$src/references/"}"
        if [[ ! -f "$dst/references/$rel" ]] || ! diff -q "$f" "$dst/references/$rel" >/dev/null 2>&1; then
          cp "$f" "$dst/references/$rel"
          echo "updated: $dst/references/$rel"
          changed=1
        fi
      done < <(find "$src/references" -type f -name '*.md' -print0)

      # Remove any generated reference file that no longer exists in the
      # source, so the copy never drifts ahead of the canonical corpus.
      if [[ -d "$dst/references" ]]; then
        while IFS= read -r -d '' f; do
          rel="${f#"$dst/references/"}"
          if [[ ! -f "$src/references/$rel" ]]; then
            rm "$f"
            echo "removed (no longer in source): $dst/references/$rel"
            changed=1
          fi
        done < <(find "$dst/references" -type f -name '*.md' -print0)
      fi
    fi
  done

  return "$changed"
}

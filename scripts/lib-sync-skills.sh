#!/usr/bin/env bash
# Shared logic for propagating the canonical skills/<name>/ corpus into any
# Claude Code-shaped copy (project skills at .claude/skills/, or a plugin's
# skills/ directory). Sourced by scripts/sync-claude-code-skills.sh and
# scripts/sync-claude-code-plugin.sh so all targets share one copy/removal
# algorithm — no risk of the destinations drifting apart from skills/.

# Not meant to be run directly.

# The 9 Claude Code skills this repo distributes: Marketing Compass 00-07
# (articulate-marketing-problem is the entry-point skill, 00) plus the
# related thinking-staircase skill. This is the single source of truth for
# ".claude/skills/" (project skills, all 9) and for the Codex plugin's skill
# list (scripts/_skills_list.py mirrors this for Python consumers). It is
# NOT the list used by an individual Claude Code *plugin* package — see
# MARKETING_COMPASS_PLUGIN_SKILLS / THINKING_STAIRCASE_PLUGIN_SKILLS below.
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

# As of 2026-08-25, the Claude Code plugin packaging is split into two
# plugins: marketing-compass (the 8 Marketing Compass skills) and
# thinking-staircase (the general-purpose skill, shipped separately because
# it is not marketing-specific). .claude/skills/ and the Codex plugin are
# unaffected by this split and still cover all 9 skills via
# CLAUDE_CODE_SKILLS above. Keep these two lists' union equal to
# CLAUDE_CODE_SKILLS if a skill is ever added or removed.
MARKETING_COMPASS_PLUGIN_SKILLS=(
  articulate-marketing-problem
  diagnose-marketing-structure
  design-marketing-measurement
  evaluate-ad-investment
  design-btob-growth
  assess-ma-crm-ltv
  design-marketing-communications
  audit-marketing-reasoning
)
THINKING_STAIRCASE_PLUGIN_SKILLS=(
  thinking-staircase
)

# sync_skills_to <dest-root-relative-to-repo-root> <check-only: 0|1> <skill-names...>
#
# dest-root example: ".claude/skills" or "plugin/marketing-compass/skills"
# skill-names: one or more skill directory names to sync, e.g.
#   sync_skills_to ".claude/skills" 0 "${CLAUDE_CODE_SKILLS[@]}"
sync_skills_to() {
  local dest_root="$1"
  local check_only="$2"
  shift 2
  local changed=0
  local name src dst f rel

  for name in "$@"; do
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

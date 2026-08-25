#!/usr/bin/env bash
# Sync canonical GPT/Codex skills into the two installable Claude Code
# plugin packages, for distribution via a plugin marketplace (e.g. the
# claude-community marketplace):
#
#   plugin/marketing-compass/skills/  <- the 8 Marketing Compass skills
#   plugin/thinking-staircase/skills/ <- the general-purpose thinking-staircase skill
#
# They are two separate plugins (not one plugin with two skill groups)
# because thinking-staircase is not Marketing Compass-specific; see
# plugin/thinking-staircase/README.md for why.
#
# Source of truth : skills/<name>/{SKILL.md,references/}
# Generated copy  : plugin/<plugin-name>/skills/<name>/{SKILL.md,references/}
#
# This script never touches skills/, canonical/, agents/, or assets/, and
# never touches either plugin's .claude-plugin/plugin.json. It only writes
# under plugin/*/skills/. Re-run it any time skills/<name>/SKILL.md or
# skills/<name>/references/ change.
#
# The copy algorithm lives in scripts/lib-sync-skills.sh, shared with
# scripts/sync-claude-code-skills.sh (which targets .claude/skills/ instead,
# unsplit, covering all 9 skills).
#
# Usage:
#   scripts/sync-claude-code-plugin.sh          # sync + report what changed
#   scripts/sync-claude-code-plugin.sh --check  # exit 1 if out of sync, no writes

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"
# shellcheck source=lib-sync-skills.sh
source "$REPO_ROOT/scripts/lib-sync-skills.sh"

CHECK_ONLY=0
if [[ "${1:-}" == "--check" ]]; then
  CHECK_ONLY=1
fi

CHANGED=0

if sync_skills_to "plugin/marketing-compass/skills" "$CHECK_ONLY" "${MARKETING_COMPASS_PLUGIN_SKILLS[@]}"; then
  :
else
  CHANGED=1
fi

if sync_skills_to "plugin/thinking-staircase/skills" "$CHECK_ONLY" "${THINKING_STAIRCASE_PLUGIN_SKILLS[@]}"; then
  :
else
  CHANGED=1
fi

if [[ "$CHECK_ONLY" -eq 1 ]]; then
  if [[ "$CHANGED" -eq 1 ]]; then
    echo "Claude Code plugin skill copies (plugin/marketing-compass/, plugin/thinking-staircase/) are out of sync with skills/. Run scripts/sync-claude-code-plugin.sh to update." >&2
    exit 1
  fi
  echo "Claude Code plugin skill copies (plugin/marketing-compass/, plugin/thinking-staircase/) are in sync with skills/."
  exit 0
fi

if [[ "$CHANGED" -eq 0 ]]; then
  echo "Already in sync. No files changed."
fi

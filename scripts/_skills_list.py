"""Single source of truth for the skills this repository distributes.

Shared by the Codex and Claude Code sync/verification scripts.

Mirrors the CLAUDE_CODE_SKILLS array in scripts/lib-sync-skills.sh, which is
the equivalent source of truth for the two bash sync scripts. If you add,
rename, or remove a skill, update both this file and lib-sync-skills.sh.
"""

SKILLS = [
    "articulate-marketing-problem",
    "diagnose-marketing-structure",
    "design-marketing-measurement",
    "evaluate-ad-investment",
    "design-btob-growth",
    "assess-ma-crm-ltv",
    "design-marketing-communications",
    "audit-marketing-reasoning",
    "thinking-staircase",
]

# As of 2026-08-25, the Claude Code plugin packaging (plugin/) is split into
# two plugins: marketing-compass (the 8 Marketing Compass skills) and
# thinking-staircase (the general-purpose skill, shipped separately because
# it is not marketing-specific — see plugin/thinking-staircase/README.md).
# .claude/skills/ and the Codex plugin (plugins/marketing-compass/) are
# unaffected by this split and still cover all 9 skills via SKILLS above.
MARKETING_COMPASS_PLUGIN_SKILLS = [s for s in SKILLS if s != "thinking-staircase"]
THINKING_STAIRCASE_PLUGIN_SKILLS = [s for s in SKILLS if s == "thinking-staircase"]

"""Single source of truth for the list of Claude Code skills this repo
distributes, shared by scripts/verify-claude-code-skills.py (checks
.claude/skills/) and scripts/verify-claude-code-plugin.py (checks plugin/).

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

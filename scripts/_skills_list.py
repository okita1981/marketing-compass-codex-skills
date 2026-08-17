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

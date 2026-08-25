# .claude/skills/ — generated, do not hand-edit

Everything under this directory is a **generated, byte-identical copy** of [`../../skills/`](../../skills) in the repository root, produced by [`scripts/sync-claude-code-skills.sh`](../../scripts/sync-claude-code-skills.sh). It is what Claude Code loads as [project skills](https://code.claude.com/docs/en/skills) when you open this repository.

**Do not edit files under `.claude/skills/<name>/` directly.** Any change made here will be silently overwritten (or flagged as drift) the next time the sync script runs. To change a skill:

1. Edit the source at `skills/<name>/SKILL.md` or `skills/<name>/references/`.
2. Run `bash scripts/sync-claude-code-skills.sh` to propagate the change here (and `bash scripts/sync-claude-code-plugin.sh` / `python3 scripts/sync-codex-plugin.py` to propagate it to the Claude Code plugin packages and the Codex plugin package too).
3. Run `python3 scripts/verify-claude-code-skills.py` to confirm everything is still in sync and structurally valid.

See the parent repo's [README](../../README.md#claude-code) for the full explanation of the GPT/Codex ↔ Claude Code relationship and sync policy.

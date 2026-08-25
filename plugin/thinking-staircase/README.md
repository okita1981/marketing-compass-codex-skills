# Thinking Staircase (Claude Code plugin)

This directory is a self-contained [Claude Code plugin](https://code.claude.com/docs/en/plugins) package for the Thinking Staircase skill. It ships as its own plugin, separate from [`../marketing-compass/`](../marketing-compass), because it is a general-purpose thinking-navigation skill — not a Marketing Compass-specific one. Bundling it inside a plugin named `marketing-compass` would misrepresent it as marketing-specific and could cause it to activate outside marketing contexts as an unexpected side effect of installing a marketing tool.

This is **not the source of truth**. The canonical skill definition lives at [`skills/thinking-staircase/`](../../skills/thinking-staircase) in the repository root; everything in this directory is a generated, byte-identical copy kept in sync by [`scripts/sync-claude-code-plugin.sh`](../../scripts/sync-claude-code-plugin.sh). See the parent repo's [README](../../README.md#claude-code) for the full explanation of the GPT/Codex ↔ Claude Code relationship and sync policy.

## Skill in this plugin

| Skill (this plugin)                | Project skill (`.claude/skills/`) |
| :----------------------------------- | :---------------------------------- |
| `/thinking-staircase:thinking-staircase` | `/thinking-staircase`           |

The two forms don't conflict — Claude Code namespaces plugin skills, so installing this plugin alongside the project-skill copy leaves both `/thinking-staircase` and `/thinking-staircase:thinking-staircase` available.

## Test locally

```bash
git clone https://github.com/okita1981/marketing-compass-codex-skills.git
cd marketing-compass-codex-skills
claude --plugin-dir ./plugin/thinking-staircase
```

Then try, for example:

```text
/thinking-staircase:thinking-staircase を使って、この会議が噛み合わない原因と、いま必要な判断を整理してください。
```

## Validate before submitting changes

```bash
claude plugin validate ./plugin/thinking-staircase --strict
```

## Marketplace status

Not yet submitted to any marketplace. There is no application process for the `claude-plugins-official` marketplace — it is curated entirely at Anthropic's discretion, with no public submission channel. Submitting to `claude-community` requires the plugin author's own login at one of:

- [claude.ai/admin-settings/directory/submissions/plugins/new](https://claude.ai/admin-settings/directory/submissions/plugins/new) (requires a Team/Enterprise organization)
- [platform.claude.com/plugins/submit](https://platform.claude.com/plugins/submit) (individual authors)

Until (and unless) that submission happens and is approved, this plugin is installable only via `--plugin-dir` (above).

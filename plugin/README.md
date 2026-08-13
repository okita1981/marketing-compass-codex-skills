# Marketing Compass (Claude Code plugin)

This directory is a self-contained [Claude Code plugin](https://code.claude.com/docs/en/plugins) package for [Marketing Compass](https://github.com/okita1981/marketing-compass-codex-skills). It bundles the same 9 skills that live at [`.claude/skills/`](../.claude/skills) in the parent repository, packaged so they can be distributed through a plugin marketplace instead of only as project skills.

This is **not the source of truth**. The canonical skill definitions live at [`skills/<name>/`](../skills) in the repository root; everything in this directory is a generated, byte-identical copy kept in sync by [`scripts/sync-claude-code-plugin.sh`](../scripts/sync-claude-code-plugin.sh). See the parent repo's [README](../README.md#claude-code) for the full explanation of the GPT/Codex ↔ Claude Code relationship and sync policy.

## Skills in this plugin

Because plugin skills are namespaced by the plugin's `name` (`marketing-compass`), invocation differs from the project-skill copy at `.claude/skills/`:

| Skill (this plugin)                             | Project skill (`.claude/skills/`)     |
| :----------------------------------------------- | :------------------------------------- |
| `/marketing-compass:articulate-marketing-problem` | `/articulate-marketing-problem`        |
| `/marketing-compass:diagnose-marketing-structure` | `/diagnose-marketing-structure`        |
| `/marketing-compass:design-marketing-measurement` | `/design-marketing-measurement`        |
| `/marketing-compass:evaluate-ad-investment`       | `/evaluate-ad-investment`              |
| `/marketing-compass:design-btob-growth`           | `/design-btob-growth`                  |
| `/marketing-compass:assess-ma-crm-ltv`            | `/assess-ma-crm-ltv`                   |
| `/marketing-compass:design-marketing-communications` | `/design-marketing-communications`  |
| `/marketing-compass:audit-marketing-reasoning`    | `/audit-marketing-reasoning`           |
| `/marketing-compass:thinking-staircase`           | `/thinking-staircase`                  |

The two forms don't conflict — Claude Code namespaces plugin skills, so installing this plugin alongside the project-skill copy leaves both `/diagnose-marketing-structure` and `/marketing-compass:diagnose-marketing-structure` available.

## Test locally

```bash
git clone https://github.com/okita1981/marketing-compass-codex-skills.git
cd marketing-compass-codex-skills
claude --plugin-dir ./plugin
```

Then try, for example:

```text
/marketing-compass:diagnose-marketing-structure を使って、売上が伸びない原因を施策提案の前に構造分解してください。
```

## Validate before submitting changes

```bash
claude plugin validate ./plugin --strict
```

## Status: not yet listed on any marketplace

As of this writing, this plugin has **not** been submitted to Anthropic's `claude-community` marketplace. There is no application process for the `claude-plugins-official` marketplace — it is curated entirely at Anthropic's discretion, with no public submission channel. Submitting to `claude-community` requires the plugin author's own login at one of:

- [claude.ai/admin-settings/directory/submissions/plugins/new](https://claude.ai/admin-settings/directory/submissions/plugins/new) (requires a Team/Enterprise organization)
- [platform.claude.com/plugins/submit](https://platform.claude.com/plugins/submit) (individual authors)

Until (and unless) that submission happens and is approved, this plugin is installable only via `--plugin-dir` (above). This repository does not currently publish its own `marketplace.json`, so `/plugin marketplace add` against this repository will not yet find this plugin; see [Create and distribute a plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces) if that changes in the future.

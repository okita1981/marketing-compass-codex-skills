# Changelog

All notable changes to the `marketing-compass` Claude Code plugin are documented here. Versions follow [Semantic Versioning](https://semver.org).

## 2.0.0 — 2026-08-25

**Breaking.** `marketing-compass:thinking-staircase` is removed from this plugin. Thinking Staircase is a general-purpose thinking-navigation skill, not specific to Marketing Compass, and now ships as its own plugin at [`../thinking-staircase/`](../thinking-staircase) (`thinking-staircase:thinking-staircase`). Users who need it should install that plugin as well; there is no automatic migration. This directory also moved from `plugin/` to `plugin/marketing-compass/` as part of the same change — update any `--plugin-dir` or marketplace-submission path accordingly.

This plugin now bundles exactly the 8 Marketing Compass skills (00–07).

## 1.0.0 — 2026-08-13

Initial release. Bundles all 9 skills from the [Marketing Compass GPT / Codex Skills](https://github.com/okita1981/marketing-compass-codex-skills) repository as Claude Code plugin skills, namespaced under `marketing-compass:`:

- `marketing-compass:articulate-marketing-problem`
- `marketing-compass:diagnose-marketing-structure`
- `marketing-compass:design-marketing-measurement`
- `marketing-compass:evaluate-ad-investment`
- `marketing-compass:design-btob-growth`
- `marketing-compass:assess-ma-crm-ltv`
- `marketing-compass:design-marketing-communications`
- `marketing-compass:audit-marketing-reasoning`
- `marketing-compass:thinking-staircase`

Each skill's `SKILL.md` and `references/` are byte-identical copies of the canonical source at `skills/<name>/` in the parent repository. No judgment logic, definitions, decision branches, Guardrails, or output contracts differ from the GPT/Codex version.

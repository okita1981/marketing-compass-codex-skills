# Changelog

All notable changes to the `marketing-compass` Codex plugin are documented here. Versions follow [Semantic Versioning](https://semver.org).

## 2.0.0 — 2026-08-25

**Breaking.** `thinking-staircase` is removed from this plugin. Thinking Staircase is a general-purpose thinking-navigation skill, not specific to Marketing Compass, and now ships as its own plugin at [`../thinking-staircase/`](../thinking-staircase). Users who need it should install that plugin as well; there is no automatic migration. `.agents/plugins/marketplace.json` now lists `thinking-staircase` as a separate entry alongside `marketing-compass`.

This plugin now bundles exactly the 8 Marketing Compass skills (00–07). This mirrors the same split already done for the Claude Code plugin (see [`plugin/marketing-compass/CHANGELOG.md`](../../plugin/marketing-compass/CHANGELOG.md)).

## 1.0.0 — 2026-08-17

Initial release. Bundles all 9 skills from the canonical [`skills/`](../../skills) source in this repository:

- `articulate-marketing-problem`
- `diagnose-marketing-structure`
- `design-marketing-measurement`
- `evaluate-ad-investment`
- `design-btob-growth`
- `assess-ma-crm-ltv`
- `design-marketing-communications`
- `audit-marketing-reasoning`
- `thinking-staircase`

Each skill's `SKILL.md`, `references/`, and `agents/openai.yaml` are copies of the canonical source at `skills/<name>/` in the repository root, kept in sync by `scripts/sync-codex-plugin.py`. No judgment logic, definitions, decision branches, Guardrails, or output contracts differ from the source.

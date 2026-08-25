# Thinking Staircase (Codex plugin)

This directory is a self-contained Codex plugin package for the Thinking Staircase skill. It ships as its own plugin, separate from [`../marketing-compass/`](../marketing-compass), because it is a general-purpose thinking-navigation skill — not a Marketing Compass-specific one. Bundling it inside a plugin named `marketing-compass` would misrepresent it as marketing-specific and could cause it to activate outside marketing contexts as an unexpected side effect of installing a marketing tool. This mirrors the equivalent split on the Claude Code side: [`plugin/thinking-staircase/`](../../plugin/thinking-staircase) and [`plugin/marketing-compass/`](../../plugin/marketing-compass).

This is **not the source of truth**. The canonical skill definition lives at [`skills/thinking-staircase/`](../../skills/thinking-staircase) in the repository root; everything in this directory is a generated copy kept in sync by [`scripts/sync-codex-plugin.py`](../../scripts/sync-codex-plugin.py). See the parent repo's [README](../../README.md) for the full explanation of the canonical-source ↔ generated-copy relationship and sync policy.

## Skill in this plugin

- `thinking-staircase`

For how to invoke a skill once installed, see the parent repo's [README §Codex / ChatGPT](../../README.md#codex--chatgpt).

## Install locally

```bash
git clone https://github.com/okita1981/marketing-compass-codex-skills.git
cd marketing-compass-codex-skills
codex plugin marketplace add .
codex plugin add thinking-staircase@marketing-compass
```

## Verify before submitting changes

```bash
python3 scripts/sync-codex-plugin.py --check
python3 scripts/verify-codex-plugin.py
```

Codex公式のプラグイン検証ツールが利用できる環境では、`validate_plugin.py plugins/thinking-staircase`も実行してください。

## Marketplace status

This repository publishes its own marketplace definition at [`.agents/plugins/marketplace.json`](../../.agents/plugins/marketplace.json), listing this plugin and `marketing-compass` as two separate local entries. There is no separate submission/review step for this Codex marketplace — anyone who runs `codex plugin marketplace add .` against this repository gets both plugins immediately. This is a different distribution model from the Claude Code plugin, which has not yet been submitted to any marketplace (see [`plugin/thinking-staircase/README.md`](../../plugin/thinking-staircase/README.md#marketplace-status)).

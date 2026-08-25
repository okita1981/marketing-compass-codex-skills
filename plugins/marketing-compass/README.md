# Marketing Compass (Codex plugin)

This directory is a self-contained Codex plugin package for the 8 Marketing Compass skills (00–07). It is one of two Codex plugins in this repository — see [`../thinking-staircase/`](../thinking-staircase) for the related general-purpose Thinking Staircase skill, which ships as its own plugin because it is explicitly not Marketing Compass-specific. This mirrors the equivalent split on the Claude Code side: [`plugin/marketing-compass/`](../../plugin/marketing-compass) and [`plugin/thinking-staircase/`](../../plugin/thinking-staircase).

This is **not the source of truth**. The canonical skill definitions live at [`skills/<name>/`](../../skills) in the repository root; everything in this directory is a generated copy kept in sync by [`scripts/sync-codex-plugin.py`](../../scripts/sync-codex-plugin.py). See the parent repo's [README](../../README.md) for the full explanation of the canonical-source ↔ generated-copy relationship and sync policy.

## Skills in this plugin

- `articulate-marketing-problem`
- `diagnose-marketing-structure`
- `design-marketing-measurement`
- `evaluate-ad-investment`
- `design-btob-growth`
- `assess-ma-crm-ltv`
- `design-marketing-communications`
- `audit-marketing-reasoning`

For how to invoke a skill once installed, see the parent repo's [README §Codex / ChatGPT](../../README.md#codex--chatgpt).

## Install locally

```bash
git clone https://github.com/okita1981/marketing-compass-codex-skills.git
cd marketing-compass-codex-skills
codex plugin marketplace add .
codex plugin add marketing-compass@marketing-compass
```

## Verify before submitting changes

```bash
python3 scripts/sync-codex-plugin.py --check
python3 scripts/verify-codex-plugin.py
```

Codex公式のプラグイン検証ツールが利用できる環境では、`validate_plugin.py plugins/marketing-compass`も実行してください。

## Marketplace status

This repository publishes its own marketplace definition at [`.agents/plugins/marketplace.json`](../../.agents/plugins/marketplace.json), listing this plugin and `thinking-staircase` as two separate local entries. There is no separate submission/review step for this Codex marketplace — anyone who runs `codex plugin marketplace add .` against this repository gets both plugins immediately. This is a different distribution model from the Claude Code plugin, which is submitted for review to Anthropic's hosted `claude-community` marketplace (see [`plugin/marketing-compass/README.md`](../../plugin/marketing-compass/README.md#marketplace-status)).

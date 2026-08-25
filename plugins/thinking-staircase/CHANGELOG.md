# Changelog

All notable changes to the `thinking-staircase` Codex plugin are documented here. Versions follow [Semantic Versioning](https://semver.org).

## 1.0.0 — 2026-08-25

Initial release. Split out from the `marketing-compass` Codex plugin (previously bundled there since its own 1.0.0 release on 2026-08-17) into its own package, since Thinking Staircase is a general-purpose thinking-navigation skill and not specific to Marketing Compass. This mirrors the same split already done for the Claude Code plugin (see [`plugin/thinking-staircase/CHANGELOG.md`](../../plugin/thinking-staircase/CHANGELOG.md)). Bundles:

- `thinking-staircase`

The skill's `SKILL.md`, `references/`, and `agents/openai.yaml` are copies of the canonical source at [`skills/thinking-staircase/`](../../skills/thinking-staircase) in the repository root, kept in sync by `scripts/sync-codex-plugin.py`. No judgment logic, definitions, or Guardrails differ from the source.

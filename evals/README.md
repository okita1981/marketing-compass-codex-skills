# Eval fixtures

This directory holds regression-test **fixtures** (input scenarios + checkable assertions) for the 9 skills in this repository. It exists so a prompt revision to any skill can be checked against a fixed set of realistic inputs instead of relying on memory of how the skill used to behave.

## Scope: data only, no automated grading runner (yet)

**This directory is fixtures, not a test harness.** There is no script here that sends these inputs to a model and grades the response — that would require choosing a model, provisioning API access, and deciding how a non-deterministic response gets pass/fail-judged, which is a separate decision this repository hasn't made yet. Wiring these fixtures into an actual automated eval run (locally or in CI) is future work, not claimed as done by this directory's existence.

What this directory gives you today:

- A fixed, versioned set of realistic input scenarios per skill.
- For each scenario, a list of concrete, checkable assertions derived directly from that skill's own `references/output-contract.md` "Quality checks" section (or, for `thinking-staircase`, its `Guardrails`) — not invented criteria.
- A manual regression-check procedure (below) any contributor or reviewer can run today with no tooling.

## Files

```text
evals/
├── README.md
└── <skill-name>/
    └── cases.json
```

Each `cases.json`:

```json
{
  "skill": "<skill-name>",
  "cases": [
    {
      "id": "<skill-name>-01",
      "language": "ja | en",
      "input": "the user message to paste into the skill",
      "assertions": [
        "a concrete, checkable statement about what a correct response must or must not do"
      ]
    }
  ]
}
```

Each skill has 3 cases (27 total across the 9 skills), mixing Japanese and English inputs so the [output-language policy](../README.md#claude-code) has direct regression coverage, not just the marketing judgment logic itself.

## Manual regression-check procedure

Until an automated runner exists, check a skill this way after changing its `SKILL.md` or `references/`:

1. Open `evals/<skill-name>/cases.json`.
2. For each case, invoke the skill (`/`\<skill-name\> in Claude Code, `$`\<skill-name\> in Codex/ChatGPT) with the `input` text.
3. Check the response against every listed `assertions` entry.
4. If a case that previously passed now fails, that's a regression from the prompt change — fix it before merging.

## What these assertions are not

- Not exact-match string comparisons. Marketing Compass judgments are not single-correct-answer questions; "the response names exactly one primary bottleneck" is checkable, "the bottleneck the model names" is not something these fixtures grade as right or wrong.
- Not a substitute for the skill's own `references/output-contract.md` Quality checks section, which remains the authoritative list — these fixtures operationalize it against concrete inputs, they don't replace or extend it with new criteria.

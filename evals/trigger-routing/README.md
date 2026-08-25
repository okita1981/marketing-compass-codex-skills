# Trigger routing fixtures

This directory checks a different thing than [`evals/<skill-name>/cases.json`](../README.md). Those fixtures check **output quality**: once a skill is running, does its response meet its own `references/output-contract.md` checklist? This directory checks **entry-point routing**: given a short input, which skill should a human or an implicit-invocation router reach first, and which skills should it *not* reach first?

## Files

```text
evals/trigger-routing/
├── README.md
└── cases.json
```

`cases.json`:

```json
{
  "scope": "trigger-routing",
  "cases": [
    {
      "id": "tr-01",
      "prompt": "the short input a user might actually type",
      "primary_skill": "the skill this input should reach first",
      "allowed_secondary_skills": ["skills that are also a legitimate first stop, depending on unstated context"],
      "must_not_route_first": ["skills that would be a routing mistake if reached before primary_skill or allowed_secondary_skills"],
      "category": "a short label grouping related cases (see below)",
      "contrast_group": "id shared by a same-vocabulary-different-context pair/set, or null",
      "rationale": "why, grounded in the skill's own description/body/canonical, not invented"
    }
  ]
}
```

22 cases: the 18 required by the review this fixture set responds to, plus 4 additional contrast entries (`contrast_group: "cpa"` — a 3-way split of \"CPA\" prompts across `diagnose-marketing-structure` / `design-marketing-measurement` / `evaluate-ad-investment`; `contrast_group: "awareness"` — a 2-way split of \"raise awareness\" prompts across `articulate-marketing-problem` and `design-marketing-communications`). One case (`tr-05`) is a **negative control**: a general meeting-misalignment prompt that should still reach `thinking-staircase`, not get pulled into Marketing Compass by the newly broadened `articulate-marketing-problem` description.

## No single correct answer

These are not exact-match routing tests. Marketing Compass's own entry-point philosophy is conditional (00 vs. 01 vs. a specialist skill depends on whether the problem is already bounded), so most cases have one `primary_skill` plus one or more `allowed_secondary_skills` that would also be a defensible first stop given information the short prompt doesn't state. `must_not_route_first` is the one thing each case actually asserts hard: these specific skills would be a *routing mistake* if reached before the problem is bounded or the decision is otherwise established.

## Two kinds of check — do not conflate them

**STATIC_METADATA_REVIEW** — a review of the frontmatter `description` text itself: does it plausibly cover the prompt's intent, does it avoid claiming territory that contradicts `must_not_route_first`, is the routing boundary stated explicitly enough that a reader (human or model) would not need to guess. This is what a contributor or reviewer can check today by reading `skills/<name>/SKILL.md` frontmatter against this file. **It is not evidence that any actual ChatGPT, Codex, or Claude Code implicit-invocation router would in fact select `primary_skill` for a given prompt.**

**LIVE_TRIGGER_TEST** — actually pasting each `prompt` into a live ChatGPT / Codex / Claude Code session with implicit invocation enabled, observing which skill (if any) fires, and recording whether it matches `primary_skill` or an `allowed_secondary_skills` entry, repeated across multiple runs to see whether the result is stable. This is the only kind of check that can support a claim like "trigger routing improved."

**Report results under these two labels explicitly, and never write "PASS" for a case that only received a STATIC_METADATA_REVIEW.** If a live test was not run for this pass, say `LIVE_TRIGGER_TEST_NOT_EXECUTED` — do not omit the distinction, and do not describe a static review as if it were a live test. Even where a live test is possible, a single run by one person is not enough to claim a stable probability of firing; report it as one observed run, not a settled result.

## Manual STATIC_METADATA_REVIEW procedure (usable today)

1. Open `cases.json`.
2. For each case, read `skills/<primary_skill>/SKILL.md` frontmatter `description` (and, for the negative control, `skills/thinking-staircase/SKILL.md`) against `prompt`.
3. Confirm the description's own wording would plausibly cover this prompt's intent, and that nothing in the description for any skill listed in `must_not_route_first` claims this prompt's territory without the routing-boundary qualifier the review requires.
4. Record the result as `STATIC_METADATA_REVIEW: <PASS|FAIL> — <one-line reason>` per case, not a bare PASS.

## Manual LIVE_TRIGGER_TEST procedure (when a live environment is available)

1. Open a fresh conversation in the target environment (ChatGPT/Codex with these skills installed and implicit invocation enabled, or Claude Code with this repository's `.claude/skills/` loaded).
2. Paste `prompt` verbatim, with no other context, and do not name the skill explicitly.
3. Record which skill (if any) actually ran.
4. Repeat at least 3 times per case before drawing any conclusion about stability; a single run is one data point, not a trend.
5. Record the result as `LIVE_TRIGGER_TEST: <fired skill(s) per run> — matches primary_skill in N/M runs`.

## Structural verification

[`scripts/verify-trigger-routing.py`](../../scripts/verify-trigger-routing.py) checks this file is structurally well-formed (valid JSON, every case has all required fields, `id`s are unique, every skill name referenced is a real skill from `scripts/_skills_list.py`, a skill is never listed as both allowed and forbidden for the same case, and the 18 prompts required by the review this fixture responds to are all present). It does **not** run or grade a live trigger test — see the scope note above.

```bash
python3 scripts/verify-trigger-routing.py
```

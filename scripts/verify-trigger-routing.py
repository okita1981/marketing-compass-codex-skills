#!/usr/bin/env python3
"""Structural verification for evals/trigger-routing/cases.json.

This checks the fixture DATA is well-formed. It does NOT run or grade a live
trigger test against ChatGPT, Codex, or Claude Code — see
evals/trigger-routing/README.md for why that distinction (STATIC_METADATA_REVIEW
vs. LIVE_TRIGGER_TEST) matters and is never collapsed into a bare "PASS" here.

Checks:
  1. evals/trigger-routing/cases.json exists and is valid JSON with a
     non-empty `cases` array.
  2. Each case has: id, prompt, primary_skill, allowed_secondary_skills,
     must_not_route_first, rationale, category. `contrast_group` is optional
     (may be omitted or null).
  3. `id` is unique across all cases.
  4. `prompt` and `rationale` are non-empty strings.
  5. `primary_skill`, and every entry in `allowed_secondary_skills` and
     `must_not_route_first`, is a real skill name from
     scripts/_skills_list.py (SKILLS) — including thinking-staircase, since
     it is a legitimate routing target for the negative-control case.
  6. `primary_skill` does not also appear in that same case's
     `allowed_secondary_skills` (redundant) or `must_not_route_first`
     (self-contradictory).
  7. `allowed_secondary_skills` and `must_not_route_first` do not share a
     skill for the same case (a skill cannot be simultaneously allowed and
     forbidden as a first stop).
  8. The 18 prompts required by the trigger-routing review this fixture set
     responds to are all present, verbatim.

Exit code 0 = all checks passed. Non-zero = at least one failure, printed.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

# Fixture prompts and rationale in this file are Japanese. On Windows
# consoles, stdout defaults to the system codepage (e.g. cp932), which
# can't encode arbitrary Japanese text and would crash a plain print() if a
# failure message ever echoes fixture content back. Fall back to
# replacement characters instead of crashing (same pattern as
# verify-claude-code-plugin.py).
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
from _skills_list import SKILLS  # noqa: E402 (see scripts/_skills_list.py)

CASES_PATH = REPO_ROOT / "evals" / "trigger-routing" / "cases.json"
VALID_SKILLS = set(SKILLS)

REQUIRED_FIELDS = [
    "id",
    "prompt",
    "primary_skill",
    "allowed_secondary_skills",
    "must_not_route_first",
    "category",
    "rationale",
]

# The 18 inputs the trigger-routing review required this fixture set to
# cover, verbatim. This list is intentionally hardcoded (not derived from
# cases.json) so a case being silently dropped or reworded is caught rather
# than trusted.
REQUIRED_PROMPTS = [
    "うちの商品、良いのに売れない",
    "SEOとリスティング、どっちが先？",
    "インスタ強化した方がいい？",
    "代理店からこの提案来た、どう思う？",
    "この会議、話が噛み合わない",
    "解約率が高い",
    "LTVを上げるには？",
    "MA入れた方がいい？",
    "リードは増えてるのに売上が伸びない",
    "展示会で名刺1000枚、商談にならない",
    "TVCM打ちたい、効果測定できる？",
    "予算どこに寄せる？",
    "来期予算3億の配分",
    "マーケ部の評価指標どうする？",
    "ブランディングって意味ある？",
    "CPAが上がってきた",
    "認知度を上げたい",
    "競合が値下げしてきた",
]

failures: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)


if not CASES_PATH.is_file():
    fail(f"missing {CASES_PATH.relative_to(REPO_ROOT)}")
    print("FAILURES (1):\n  - " + failures[0])
    sys.exit(1)

try:
    data = json.loads(CASES_PATH.read_text(encoding="utf-8"))
except json.JSONDecodeError as exc:
    print(f"FAILURES (1):\n  - cases.json is not valid JSON: {exc}")
    sys.exit(1)

cases = data.get("cases")
if not isinstance(cases, list) or not cases:
    fail("cases.json has no non-empty `cases` array")
    print(f"FAILURES (1):\n  - {failures[0]}")
    sys.exit(1)

seen_ids: set[str] = set()
seen_prompts: set[str] = set()

for i, case in enumerate(cases):
    label = case.get("id", f"<case {i}>")

    for field in REQUIRED_FIELDS:
        if field not in case:
            fail(f"[{label}] missing required field `{field}`")

    case_id = case.get("id")
    if not case_id:
        fail(f"[case {i}] missing `id`")
    elif case_id in seen_ids:
        fail(f"[{label}] duplicate case id")
    else:
        seen_ids.add(case_id)

    prompt = case.get("prompt")
    if not isinstance(prompt, str) or not prompt.strip():
        fail(f"[{label}] `prompt` is empty or not a string")
    else:
        seen_prompts.add(prompt)

    if not isinstance(case.get("rationale"), str) or not case.get("rationale", "").strip():
        fail(f"[{label}] `rationale` is empty or not a string")

    if not isinstance(case.get("category"), str) or not case.get("category", "").strip():
        fail(f"[{label}] `category` is empty or not a string")

    primary = case.get("primary_skill")
    if not primary:
        fail(f"[{label}] missing `primary_skill`")
    elif primary not in VALID_SKILLS:
        fail(f"[{label}] primary_skill '{primary}' is not a known skill (see scripts/_skills_list.py)")

    secondary = case.get("allowed_secondary_skills")
    if not isinstance(secondary, list):
        fail(f"[{label}] `allowed_secondary_skills` must be a list (use [] for none)")
        secondary = []
    else:
        for s in secondary:
            if s not in VALID_SKILLS:
                fail(f"[{label}] allowed_secondary_skills entry '{s}' is not a known skill")

    forbidden = case.get("must_not_route_first")
    if not isinstance(forbidden, list):
        fail(f"[{label}] `must_not_route_first` must be a list (use [] for none)")
        forbidden = []
    else:
        for s in forbidden:
            if s not in VALID_SKILLS:
                fail(f"[{label}] must_not_route_first entry '{s}' is not a known skill")

    if primary and primary in secondary:
        fail(f"[{label}] primary_skill '{primary}' is redundantly repeated in allowed_secondary_skills")
    if primary and primary in forbidden:
        fail(f"[{label}] primary_skill '{primary}' contradictorily appears in must_not_route_first")

    overlap = set(secondary) & set(forbidden)
    if overlap:
        fail(f"[{label}] skill(s) {sorted(overlap)} appear in both allowed_secondary_skills and must_not_route_first")

    # contrast_group is optional; if present it must be a string or null.
    if "contrast_group" in case and case["contrast_group"] is not None:
        if not isinstance(case["contrast_group"], str) or not case["contrast_group"].strip():
            fail(f"[{label}] `contrast_group`, when present, must be a non-empty string or null")


missing_required = [p for p in REQUIRED_PROMPTS if p not in seen_prompts]
for p in missing_required:
    fail(f"required prompt not found in any case: {p!r}")


# --- report ---
print(f"Checked evals/trigger-routing/cases.json: {len(cases)} cases, "
      f"{len(REQUIRED_PROMPTS) - len(missing_required)}/{len(REQUIRED_PROMPTS)} required prompts present\n")

print(
    "NOTE: this is STATIC structural verification only (schema, unique ids, "
    "valid skill references, required prompts present). It does not run or "
    "grade a live trigger test -- see evals/trigger-routing/README.md."
)

if failures:
    print(f"\nFAILURES ({len(failures)}):")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)

print("\nAll trigger-routing fixture structural checks PASSED.")
sys.exit(0)

#!/usr/bin/env python3
"""Structural verification for evals/ fixtures.

This does NOT run the eval cases against a model — see evals/README.md for
why that's out of scope for now. It only checks the fixture data itself is
well-formed:

  1. evals/<name>/cases.json exists for exactly the 9 skills in
     scripts/_skills_list.py (SKILLS) — no missing skill, no stray extra
     directory for a skill that doesn't exist.
  2. Each cases.json is valid JSON with a `skill` field matching its
     directory name and a non-empty `cases` array.
  3. Each case has a unique `id` (unique within its file), a `language` of
     either "ja" or "en", a non-empty `input`, and at least 3 `assertions`.
  4. Every skill has exactly 3 cases (the scale agreed for this pass).

Exit code 0 = all checks passed. Non-zero = at least one failure, printed.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
from _skills_list import SKILLS  # noqa: E402 (see scripts/_skills_list.py)

EVALS_ROOT = REPO_ROOT / "evals"
EXPECTED_CASES_PER_SKILL = 3

failures: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)


actual_dirs = {p.name for p in EVALS_ROOT.iterdir() if p.is_dir()} if EVALS_ROOT.is_dir() else set()
expected_dirs = set(SKILLS)

for missing in sorted(expected_dirs - actual_dirs):
    fail(f"missing evals/{missing}/ (every skill in scripts/_skills_list.py needs a fixture directory)")
for extra in sorted(actual_dirs - expected_dirs):
    fail(f"evals/{extra}/ does not correspond to any skill in scripts/_skills_list.py")

total_cases = 0

for name in sorted(expected_dirs & actual_dirs):
    cases_path = EVALS_ROOT / name / "cases.json"
    if not cases_path.is_file():
        fail(f"[{name}] missing evals/{name}/cases.json")
        continue

    try:
        data = json.loads(cases_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"[{name}] cases.json is not valid JSON: {exc}")
        continue

    if data.get("skill") != name:
        fail(f"[{name}] cases.json `skill` field is '{data.get('skill')}', expected '{name}'")

    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        fail(f"[{name}] cases.json has no non-empty `cases` array")
        continue

    if len(cases) != EXPECTED_CASES_PER_SKILL:
        fail(f"[{name}] has {len(cases)} case(s), expected {EXPECTED_CASES_PER_SKILL}")

    seen_ids: set[str] = set()
    for i, case in enumerate(cases):
        label = case.get("id", f"<case {i}>")

        case_id = case.get("id")
        if not case_id:
            fail(f"[{name}] case {i} missing `id`")
        elif case_id in seen_ids:
            fail(f"[{name}/{label}] duplicate case id within this file")
        else:
            seen_ids.add(case_id)

        if case.get("language") not in ("ja", "en"):
            fail(f"[{name}/{label}] `language` must be 'ja' or 'en', got {case.get('language')!r}")

        if not str(case.get("input", "")).strip():
            fail(f"[{name}/{label}] `input` is empty")

        assertions = case.get("assertions")
        if not isinstance(assertions, list) or len(assertions) < 3:
            fail(f"[{name}/{label}] needs at least 3 `assertions`, has {len(assertions) if isinstance(assertions, list) else 0}")
        elif any(not str(a).strip() for a in assertions):
            fail(f"[{name}/{label}] has an empty assertion entry")

    total_cases += len(cases)


print(f"Checked evals/ fixtures for {len(SKILLS)} skills ({total_cases} cases found)\n")

if failures:
    print(f"FAILURES ({len(failures)}):")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)

print("All eval fixture structural checks PASSED.")
sys.exit(0)

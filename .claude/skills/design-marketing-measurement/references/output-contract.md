# Measurement Output Contract

## Contents

1. Missing-input behavior
2. Compact design
3. Full specification
4. Decision table
5. Quality checks
6. Output language

## 1. Missing-input behavior

Ask at most three questions that can materially change the design:

- What decision will this measurement change, and by when?
- What single customer or business return should the intervention create?
- What variation, comparison group, survey, or historical data is actually available?

If the user cannot answer, provide a provisional design with explicit unknowns. Do not invent baselines or thresholds.

## 2. Compact design

```text
Decision:
Primary R:
KGI:
KPI:
Evidence method:
Can conclude:
Cannot conclude:
Next measurement step:
```

## 3. Full specification

```text
Decision owner and deadline:
Intervention, population, and period:
Primary R:

Business KGI:
Intervention KGI:
KPI:
Operational metrics:

Metric definitions:
- Name:
- Definition and equation type:
- Numerator / denominator:
- Population / cohort:
- Data source:
- Cadence and owner:

Causal chain:
Evidence method:
Confounders and biases:
Evidence level:
Can conclude:
Cannot conclude:

Baseline:
Desired Signal:
Counter-signal:
Guardrail:
Review window:
Action if crossed:

Minimum next step:
What not to measure or optimize:
Uncertainty and exceptions:
```

## 4. Decision table

Use when measurement controls continuation or investment:

| State | Evidence pattern | Action |
|---|---|---|
| Expand | Desired signal with no guardrail breach and adequate evidence | Increase cautiously and re-estimate |
| Continue | Direction is acceptable but certainty or lag is incomplete | Maintain through review window |
| Hold | Measurement integrity or prerequisite is missing | Fix design before changing investment |
| Reduce | Counter-signal strengthens or expected value falls | Contain exposure while preserving learning |
| Stop/restore | Guardrail breach or wrong causal mechanism | Stop, reverse, or restore the prior state |

## 5. Quality checks

- The design begins with a decision and one primary `R`.
- Business and intervention responsibility are separated.
- KPI connects to KGI through an explicit hypothesis.
- The method matches the claim required.
- The specification states what cannot be concluded.
- No proxy, attributed return, or MMM coefficient is called causal truth.
- Baseline, signal, counter-signal, guardrail, review window, and action are defined or labeled unknown.
- Complexity is proportional to the decision's value and risk.

## 6. Output language

Respond in the language of the user's most recent message. When replying in Japanese, translate the field labels above using the table below; keep the field structure and order unchanged. `Signal`, `Counter-signal`, `Guardrail`, and `Baseline` are used as-is in Japanese (the established Marketing Compass convention — see `canonical/marketing-compass-canonical-v1.0.md` §7.5, §14), not translated. `KGI`/`KPI` are also used as-is.

| English label | 日本語ラベル |
|---|---|
| Decision | 判断 |
| Primary R | 主要R |
| Evidence method | 検証方法 |
| Can conclude | 言えること |
| Cannot conclude | 言えないこと |
| Next measurement step | 次の測定ステップ |
| Decision owner and deadline | 決定権者と期限 |
| Intervention, population, and period | 介入・対象母集団・期間 |
| Business KGI | 事業KGI |
| Intervention KGI | 介入KGI |
| Operational metrics | 運用指標 |
| Metric definitions | 指標定義 |
| Name | 名称 |
| Definition and equation type | 定義と式の種別 |
| Numerator / denominator | 分子／分母 |
| Population / cohort | 母集団／コホート |
| Data source | データソース |
| Cadence and owner | 測定頻度と担当者 |
| Causal chain | 因果連鎖 |
| Confounders and biases | 交絡とバイアス |
| Evidence level | 証拠レベル |
| Desired Signal | 期待するSignal |
| Review window | 見直し期間 |
| Action if crossed | 超過時の行動 |
| Minimum next step | 最小限の次の一手 |
| What not to measure or optimize | 測定・最適化しないこと |
| Uncertainty and exceptions | 不確実性と例外 |

Decision table (§4) columns and state values:

| English | 日本語 |
|---|---|
| State | 状態 |
| Evidence pattern | 証拠パターン |
| Action | 行動 |
| Expand | 拡大 |
| Continue | 継続 |
| Hold | 保留 |
| Reduce | 縮小 |
| Stop/restore | 撤退／原状回復 |

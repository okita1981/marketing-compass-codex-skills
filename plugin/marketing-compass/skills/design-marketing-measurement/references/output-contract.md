# Measurement Output Contract

## Contents

1. Missing-input behavior
2. Compact design
3. Full specification
4. Decision table
5. Quality checks

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

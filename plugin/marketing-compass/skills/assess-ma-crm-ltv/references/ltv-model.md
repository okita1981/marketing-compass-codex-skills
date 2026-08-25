# LTV Model

## Contents

1. Three distinct views
2. Accounting definitions
3. Strategic formation model
4. Diagnostic branches
5. Calculation guardrails

## 1. Three distinct views

- **Accounting LTV:** estimates gross-margin customer contribution over a defined period or lifetime, net of maintenance and service cost.
- **Acquisition economics:** compares accounting LTV, CAC, payback, and capital constraints.
- **Strategic LTV:** diagnoses the durability of repeated choice—the lifetime of choice.

Use accounting LTV for financial explanation and acquisition economics. Use strategic LTV for formation diagnosis.

## 2. Accounting definitions

Simplified form:

```text
Accounting LTV
= average revenue per customer × gross margin rate × average continuation period
− customer maintenance and service cost

Acquisition economics
= accounting LTV − CAC
```

For precise work, use cohort and period cash flows:

```text
LTV = sum over t of
  (expected revenue_t − variable cost_t − service and retention cost_t)
  × survival probability_t
  ÷ (1 + discount rate)^t
```

Define whether revenue, gross profit, or contribution margin is used. Define cohort, period, churn, reactivation, expansion, refunds, service cost, and discounting.

## 3. Strategic formation model

Meaning statement:

```text
Strategic LTV = lifetime of choice
```

Diagnostic hypothesis tree:

```text
Strategic LTV formation
← probability that need recurs
× probability of being recalled again
× probability of being re-selected
× probability of continued use or repurchase
× contribution margin per decision or period
```

This is not a ready-to-calculate formula. Calculation requires conditional probabilities, cohort, period, dependence, overlap, and margin definitions.

## 4. Diagnostic branches

| Driver | Diagnostic questions |
|---|---|
| Need recurrence | Does a relevant need naturally return, and at what interval? |
| Re-recall | Is the brand accessible when the need returns? |
| Re-selection | Does the customer still prefer it under current comparison? |
| Continuation/value | Does use produce expected value with acceptable effort and risk? |
| Margin | Does continuation create contribution after service and retention cost? |

Segment by cohort, use case, acquisition source, product, contract, and value realization when averages hide different structures.

## 5. Calculation guardrails

- Do not use revenue-only LTV for profit decisions without labeling it.
- Do not mix contractual duration with observed customer lifetime.
- Do not assume `1 / churn` is valid when churn is non-stationary or cohort-dependent.
- Do not subtract CAC inside LTV and again outside it.
- Do not treat retention spending as free.
- Do not use a lifetime longer than the evidence supports.
- Do not compare LTV across inconsistent margin and service-cost definitions.
- Do not turn the strategic tree into a numeric formula without calibration.

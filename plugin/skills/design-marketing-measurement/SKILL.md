---
name: design-marketing-measurement
description: "Design or audit marketing measurement systems, KPI trees, effect measurement, experiments, MMM interpretation, and continuation or withdrawal rules. Use when a user asks what to measure, how to connect a marketing objective to KGI and KPI, whether sales or ROAS is an appropriate success metric, how to choose among A/B tests, Geo tests, surveys, logs, MMM, or proxy signals, how much causal confidence a result supports, or how to define Baseline, Desired Signal, Counter-signal, Guardrail, review window, and action thresholds."
---

# Design Marketing Measurement

Design measurement for a decision, not a dashboard. Start from what the organization must decide and what return the intervention is meant to create. Do not begin with available metrics.

Read [references/measurement-principles.md](references/measurement-principles.md) for every substantive design. Read [references/method-selection.md](references/method-selection.md) when selecting evidence or auditing MMM and experiments. Read [references/output-contract.md](references/output-contract.md) before returning a complete specification.

## Establish the decision and return

Identify:

- Who will decide what, and by when
- The intervention and population in scope
- The single primary return `R`
- The expected time horizon
- The acceptable loss or downside
- The action that a result will trigger

Define `R` as the customer or business state the intervention is supposed to change: recall, understanding, preference, trust, qualified demand, purchase, activation, continuation, profit, or another explicit state.

If the marketing structure or primary bottleneck is still unknown, do not create a company-wide KPI tree. Return to structural diagnosis or produce only a provisional measurement discovery plan.

## Separate responsibility levels

Distinguish:

1. **Business KGI:** the organization-level result, such as profit, revenue, customers, or continuation.
2. **Intervention KGI:** the customer state or result the specific intervention can reasonably own.
3. **KPI:** an intermediate variable hypothesized to move the intervention KGI.
4. **Operational metric:** delivery, quality, or execution health.

Do not assign sales as the direct KGI of one communication intervention unless a defensible counterfactual and control of material product, price, distribution, competitive, seasonal, and sales effects exist.

Do not call reach, clicks, downloads, or open rates business outcomes. They can be delivery metrics, proxies, or weak signals depending on the decision.

## Build the smallest useful causal chain

Use:

```text
Intervention → customer-state change → behavior → business outcome
```

For every arrow, record:

- The causal hypothesis
- Population and period
- Known confounders
- Observable measure or proxy
- What evidence would weaken the link

Classify each expression as a meaning equation, accounting equation, probability equation, or hypothesis tree. Do not calculate a meaning equation or uncalibrated hypothesis tree.

Select a small number of decision-relevant measures. Do not reward a KPI merely because it is easy to collect.

## Choose the evidence method

Select methods by the claim required, intervention level, feasibility, lag, and risk.

- Use logs for observed behavior and delivery.
- Use surveys for recognition, recall, understanding, preference, trust, and intent.
- Use user-level A/B tests for treatment differences within a controllable interface or message.
- Use Geo or comparable market tests for macro incremental effects when spillover and region comparability can be managed.
- Use MMM for historical fit, hypotheses, anomalies, audits, and rough ranges—not causal truth or exact allocation.
- Use multiple independent signals when no single method can identify the effect.

Read `method-selection.md` for method constraints. State what the design can and cannot establish.

## Define the decision boundary

Every consequential measure must include:

```text
Baseline
Desired Signal
Counter-signal
Guardrail
Review window
Action if crossed
```

Use ranges or directional criteria when false precision would be misleading. Define the population, denominator, attribution window, cohort, data source, owner, and measurement cadence for every operationalized metric.

Separate optimization problems from threshold or defense problems. For delayed or potentially irreversible loss, use small changes, provisional floors, anomaly detection, and restoration rules rather than searching aggressively for an optimum.

## Audit causal claims

Check:

- Counterfactual quality
- Randomization or assignment integrity
- Contamination and spillover
- Seasonality and concurrent changes
- Selection, survivorship, and attrition bias
- Reverse causality
- Common causes and collinearity
- Segment averages hiding heterogeneous effects
- Multiple testing and post-hoc metric selection
- Data freshness and instrumentation changes

Assign the evidence level in `measurement-principles.md`. Use causal language only at the level the design supports.

## Handle common metric errors

- If KPI improves and KGI does not, revise the KPI or causal hypothesis.
- If ROAS is high without an incrementality design, describe efficiency or attributed return, not causal return.
- Define Incremental CPA as `additional advertising cost ÷ incremental conversions`.
- Define Incremental ROAS as `incremental revenue ÷ additional advertising cost`.
- Do not call `additional advertising cost ÷ incremental revenue` Incremental CPA.
- Do not infer latent attitude change merely because it is plausible; measure it or label it unknown.
- Do not reject an important construct merely because it is difficult to observe.

## Return a measurement specification

Use the compact or full form in [references/output-contract.md](references/output-contract.md). Include:

- The decision and primary `R`
- Business KGI, intervention KGI, KPI, and operational metrics
- Metric definitions and equation types
- Evidence method and confidence level
- What can and cannot be concluded
- Signal, counter-signal, guardrail, review window, and action
- The minimum next measurement step

## Guardrails

- Do not manufacture baselines, thresholds, lift, or power assumptions.
- Do not present a proxy as the underlying construct.
- Do not present MMM coefficients or attributed platform conversions as causal truth.
- Do not use an A/B win to claim total market incrementality.
- Do not design measurement that cannot change a decision.
- Do not increase measurement complexity beyond the value or risk of the decision.
- Do not optimize a KPI in a way that harms customer experience, trust, margin, or long-term value.
- Do not present Marketing Compass classifications as universal industry terminology.

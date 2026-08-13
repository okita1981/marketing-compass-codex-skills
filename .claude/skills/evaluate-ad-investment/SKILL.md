---
name: evaluate-ad-investment
description: "Evaluate whether an advertising plan, channel, budget, brand campaign, performance campaign, TV campaign, or media reduction qualifies as an investment and under what conditions. Use when a user asks whether advertising is worth it, how to compare brand and performance advertising, whether to cut or increase media, what return and time horizon to use, how to classify current-value, non-current-value, or organizational advertising, or how to define incremental return, residual value, safe floors, signals, guardrails, and withdrawal rules."
---

# Evaluate Advertising Investment

Judge the investment role before judging media efficiency. Treat advertising as an intervention in the timing or probability of purchase, recall, consideration, trust, or selection. Do not assume that all advertising has the same return period or can be compared by one metric.

Read [references/investment-model.md](references/investment-model.md) for every substantive evaluation. Read [references/decision-branches.md](references/decision-branches.md) when distinguishing optimization from threshold defense or selecting tests. Read [references/output-contract.md](references/output-contract.md) before returning a complete recommendation.

## Establish the decision

Identify:

- Who must decide what and by when
- The product, market, customer, and buying situation
- The budget change under consideration
- The probability or timing the advertising is intended to change
- The evaluation period and expected lag
- The acceptable loss, recovery time, and irreversible risk
- Product, price, distribution, sales, experience, or demand constraints outside advertising

If the underlying sales problem or primary bottleneck is unknown, do not approve a large advertising change. Return to structural diagnosis or limit the answer to a provisional test.

Ask no more than three questions that can change the classification or decision. Continue with labeled assumptions when appropriate.

## Name the intended probability

Choose the primary intervention target:

- Bring forward an already-likely purchase
- Enter or strengthen recall at a future category-entry moment
- Enter the consideration set
- Increase trust or reduce perceived risk
- Change meaning, comparison frame, or category context
- Maintain a baseline against forgetting or competitive pressure

Do not use “awareness” as a complete objective. State what awareness is expected to enable.

## Classify the advertising

Assign one primary class from `investment-model.md`:

1. **Current-value advertising:** buys time by accelerating existing demand through a known recovery path.
2. **Non-current-value advertising:** buys a future option or probability such as recall, trust, or consideration entry.
3. **Organizational advertising:** primarily buys internal reassurance, legitimacy, continuity, relationships, or institutional convenience while the market probability remains undefined.

Use `defensive / maintenance cost` only as an operating tag under non-current-value advertising; do not create a fourth class.

If one plan has materially different roles, split it into components rather than forcing a blended label.

## Test investment qualification

For current-value advertising, require:

- Existing or identifiable demand
- A defined conversion and profit path
- Incremental or marginal return logic
- Capacity, stock, sales, and value realization
- A limit where additional spend no longer qualifies
- Expected behavior when spend stops

For non-current-value advertising, require:

- A defined future customer-state change
- A plausible mechanism and relevant buying horizon
- Leading signals and counter-signals
- A theory of what persists after exposure
- A review period matched to lag
- A withdrawal or redesign rule

For organizational advertising, require transparent accounting as an organizational cost. Do not disguise it as market investment or assign invented ROI.

## Separate optimization from defense

Treat a response as an optimization problem only when changes are sufficiently observable, continuous, timely, and reversible.

Treat it as a threshold or defense problem when:

- Effects are delayed or small relative to noise
- Loss may appear only after memory, distribution, or competitive position erodes
- Recovery is slow or uncertain
- Large cuts may cross a hidden floor

For defense problems, define a provisional safe floor, make small changes, monitor anomalies, and restore when the guardrail is crossed. Do not cut until sales reveal the damage.

## Define return and evidence

Match return to the classification:

- Current value: incremental conversions, contribution profit, Incremental CPA, Incremental ROAS, marginal return, payback.
- Non-current value: recall, consideration entry, qualified direct demand, trust, future conversion quality, residual value, and independent business signals.
- Defensive maintenance: stability bands, share and distribution context, competitive pressure, brand search or recall anomalies, and recovery risk.
- Organizational: explicit organizational benefit and cost, separate from market ROI.

Define:

```text
Incremental effect = observed result − counterfactual result
Incremental CPA = additional advertising cost ÷ incremental conversions
Incremental ROAS = incremental revenue ÷ additional advertising cost
```

Do not treat attributed platform return, correlation, or MMM coefficients as causal truth. State the evidence level and what can and cannot be concluded.

## Design the decision boundary

Specify:

```text
Baseline
Desired Signal
Counter-signal
Guardrail
Review window
Action if crossed
```

For each threshold, state whether it is evidence-based, a provisional heuristic, or unknown. Use ranges or directional criteria when precision is unjustified.

Choose one decision state:

- Increase
- Continue
- Small reversible test
- Hold
- Reduce
- Stop or restore

## Return an investment judgment

Use the compact or full structure in [references/output-contract.md](references/output-contract.md). Include:

- Intended probability or timing change
- Advertising classification and operating tag
- Investment qualification and missing conditions
- Optimization versus threshold-defense status
- Short- and long-horizon return measures
- Residual value or stopping behavior
- Evidence level and uncertainty
- Signal, counter-signal, guardrail, review window, and action
- What not to do

## Guardrails

- Do not recommend advertising to compensate for absent demand, product value, availability, activation, or continuation.
- Do not judge all advertising by immediate ROAS.
- Do not call weak visibility metrics residual value without a mechanism.
- Do not compare brand and performance advertising as if they buy the same outcome and time horizon.
- Do not optimize a potentially irreversible brand or distribution threshold through large cuts.
- Do not present organizational advertising as a market investment.
- Do not approve a budget without a return definition, review period, and withdrawal rule.
- Do not claim causality without a defensible counterfactual.
- Do not present Marketing Compass classifications as universal industry terminology.

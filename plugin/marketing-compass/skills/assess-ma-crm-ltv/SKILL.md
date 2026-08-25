---
name: assess-ma-crm-ltv
description: "Assess whether marketing automation, CRM, lifecycle messaging, customer success, retention programs, or LTV initiatives fit the business and what must be fixed first. Use when a user asks whether to introduce or strengthen MA, why CRM is not increasing revenue, how to separate strategic CRM, operational CRM, MA, and CS, why retention or renewal is weak, how to improve LTV, how to design lifecycle journeys or automation, or how to distinguish accounting LTV, acquisition economics, and the strategic lifetime of customer choice."
---

# Assess MA, CRM, and LTV

Diagnose the relationship and value structure before automating contact. Treat MA as an execution device, CRM as both a relationship strategy and an operating function, CS as value-realization intervention, and LTV as both an accounting result and a strategic formation problem.

Read [references/role-and-readiness.md](references/role-and-readiness.md) for every substantive diagnosis. Read [references/ltv-model.md](references/ltv-model.md) when calculating or diagnosing LTV. Read [references/output-contract.md](references/output-contract.md) before returning a complete recommendation.

## Establish the decision

Identify:

- Who must decide what and by when
- The business model, buying cycle, and repeat or continuation mechanism
- The customer population and cohort in scope
- The current customer state and observed problem
- The proposed MA, CRM, CS, or retention intervention
- Available behavioral, transactional, attitudinal, and service data
- Capacity, permission, customer risk, and acceptable loss

If the request begins with a tool or campaign, restate the underlying decision. Ask at most three questions that can change the readiness decision, then continue provisionally when possible.

## Test critical prerequisites

Check the three major blockers before using a scorecard:

1. Does relevant base or recognized demand exist?
2. Is the ICP or target customer state defined?
3. Does the customer reach and experience the promised value?

If any major blocker is absent, default to `Hold` or `Adverse` for additional automation. Do not let a majority of weaker positive conditions overrule a structural failure.

Then assess:

- Demand repeats or a meaningful future decision recurs
- A reason to choose already exists
- Timing or friction can change the outcome
- Customer states can be observed or responsibly inferred
- Contact permission and channel suitability exist
- The organization can act on signals
- Human intervention is available where ambiguity is high

Treat any `3/5` or `2/5` rule as a rough prompt, not a formal threshold.

## Separate responsibilities

Use these roles:

- **Strategic CRM:** design customer states, relationship meaning, value timing, contact logic, and LTV structure.
- **Operational CRM:** prevent leakage, restore recall, support return, adjust timing, and reduce selection friction.
- **MA:** automate contact, routing, timing, reminders, and known friction.
- **CS:** help customers reach value, succeed, adapt, and form a reason to continue.

Do not reduce CRM to message delivery, CS to support tickets, or MA to a revenue engine. MA does not create base demand, ICP, product value, or competitive advantage.

## Map the customer-state system

Use the smallest relevant path:

```text
Need recurrence
  → recall or return trigger
  → re-selection
  → access and friction
  → use and value realization
  → continuation, repurchase, expansion, or advocacy
```

For subscription or SaaS, include acquisition, activation, first value, habit, renewal, expansion, and recovery where relevant.

For each state, separate:

- Confirmed facts
- Proxy signals
- Hypotheses
- Unknowns
- Customer risk
- Appropriate automated and human response

Select one primary bottleneck. Do not launch a full lifecycle program to solve every stage simultaneously.

## Diagnose value realization and expectation

Check:

- What value the customer expected before purchase
- The earliest moment that value can be experienced
- Time and effort required to reach it
- Product, process, data, integration, or behavioral blockers
- Who owns activation and success
- Whether messaging created an expectation the experience cannot meet
- Whether churn reflects lack of demand, poor fit, poor value, friction, or avoidable forgetting

If value realization is weak, prioritize product, onboarding, implementation, or CS. Do not replace them with reminders or discounts.

## Design contact by purpose

Every contact must have one legitimate role:

- Restore relevant recall
- Help complete an intended action
- Remove known friction
- Support value realization
- Prepare a recurring need or decision
- Surface risk for human intervention
- Confirm preference or permission

Define the entry condition, customer benefit, timing, channel, suppression rule, exit condition, and owner.

Do not contact because a tool allows it. Use frequency, complaint, opt-out, negative engagement, trust, and value signals as guardrails.

## Separate automation and human judgment

Automate high-volume, repeatable, low-ambiguity actions. Use people for:

- Unclear needs or account context
- Failure to reach value
- Sensitive recovery or dissatisfaction
- Complex tradeoffs and relationship risk
- New objections or exceptional behavior
- High-value intervention where consent and judgment matter

Define escalation and suppression rules. Do not simulate a human relationship through excessive automated personalization.

## Diagnose LTV correctly

Use three separate views:

1. **Accounting LTV:** period gross-margin cash contribution less customer maintenance and service costs.
2. **Acquisition economics:** accounting LTV compared with CAC and payback.
3. **Strategic LTV:** the durability of being chosen again—the lifetime of choice.

Use [references/ltv-model.md](references/ltv-model.md) for definitions and calculation limits. Never calculate the strategic formation tree as if its factors were calibrated probabilities.

Diagnose strategic LTV through:

- Probability that the relevant need recurs
- Probability of being recalled again
- Probability of being re-selected
- Probability of continued use or repurchase after value realization
- Contribution margin per decision or period

State cohort, period, margin basis, service cost, churn convention, and discounting when making financial claims.

## Decide MA and relationship action

Choose one:

- Adopt or expand
- Conditional pilot
- Hold until prerequisites
- Reduce or redesign
- Adverse / likely harmful

Specify:

```text
Desired Signal
Counter-signal
Guardrail
Review window
Action if crossed
```

Prefer a narrow use case that tests the relationship hypothesis over platform-wide automation.

## Return a diagnosis

Use the compact or full structure in [references/output-contract.md](references/output-contract.md). Include:

- MA readiness and major blockers
- Strategic CRM, operational CRM, MA, and CS responsibility
- Primary customer-state bottleneck
- LTV view and formation drivers
- What to fix before automation
- Automated action and human-intervention point
- Signal, counter-signal, guardrail, review window, and action
- What not to do

## Guardrails

- Do not use MA to replace demand, ICP, value, or competitive advantage.
- Do not treat more messages as stronger customer relationships.
- Do not call opens, clicks, or recency customer value or loyalty.
- Do not automate contact without purpose, permission, suppression, and exit rules.
- Do not use discounts to hide a value-realization failure.
- Do not calculate strategic LTV from an uncalibrated hypothesis tree.
- Do not subtract CAC inside LTV and then subtract it again in acquisition economics.
- Do not compare cohorts or periods with inconsistent margin, churn, or service-cost definitions.
- Do not optimize retention by trapping customers, obscuring cancellation, or damaging trust.
- Do not present Marketing Compass classifications as universal industry terminology.

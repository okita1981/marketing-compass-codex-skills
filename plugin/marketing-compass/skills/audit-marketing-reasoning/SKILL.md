---
name: audit-marketing-reasoning
description: Audit marketing proposals, analyses, reports, dashboards, case studies, and frameworks for causal validity, evidence quality, reproducibility, context transfer, information freshness, ethical risk, and real-world implementability. Use when evaluating whether correlation supports causation, whether a successful case generalizes, whether metrics or models justify a decision, why a theoretically sound proposal may fail in practice, or how to rewrite a marketing claim into a falsifiable and operational form. Route measurement-system design and metric calculations primarily to design-marketing-measurement; route broad growth diagnosis primarily to diagnose-marketing-structure.
---

# Marketing Reasoning Audit

Audit consequential claims without turning the review into fault-finding. Preserve the useful core, expose uncertainty, and convert criticism into a safer decision or a small validation step.

## Operating principles

- Treat frameworks as subordinate to observed reality.
- Separate business outcomes from the proposed marketing mechanism.
- Distinguish fact, interpretation, hypothesis, unknown, and recommendation.
- Do not convert correlation, model output, or a successful case into causation by wording alone.
- Treat missing information as a reason to condition a decision, not automatically to stop it.
- Describe incentive, political, or operational risks as hypotheses unless directly evidenced.
- Protect customer trust; weak signals do not create strong permission to sell.
- Date unstable assumptions and verify current facts when the decision depends on them.

## Workflow

### 1. Define the audit object

Identify:

- the decision the material is meant to support;
- the material claims that could change that decision;
- the population, market, channel, product, period, and organization in scope;
- the cost of being wrong and the reversibility of the action.

If scope is unclear, state a provisional scope and ask only for information that could materially change the verdict.

### 2. Build a claim map

For each material claim, trace:

`evidence -> inference -> conclusion -> proposed action`

Label every element as fact, interpretation, hypothesis, unknown, or recommendation. Flag any skipped link, undefined term, proxy presented as an outcome, or meaning formula presented as a calculation formula.

Read [reasoning-audit.md](references/reasoning-audit.md) when auditing a report, case study, model, or causal claim in detail.

### 3. Audit evidence and causality

Check at minimum:

- denominator, distribution, comparison group, and time window;
- time order and a credible counterfactual;
- common causes, reverse causality, selection bias, and survivorship bias;
- measurement error, aggregation, collinearity, seasonality, and repeated testing;
- whether the evidence measures behavior, attitude, recall, revenue, or only a proxy;
- whether alternative explanations remain plausible.

Use four evidence levels:

- **A — causal:** credible experiment or strong quasi-experimental design.
- **B — triangulated:** multiple independent methods support the same direction.
- **C — observational:** association or model estimate with unresolved alternatives.
- **D — hypothesis:** expert judgment, anecdote, analogy, or untested mechanism.

Do not treat MMM as automatic causal proof. Use it primarily for hypotheses, anomaly detection, model and data audit, broad ranges, and directional risk. Pair it with experiments, Geo tests, surveys, or other evidence when the decision needs incrementality.

### 4. Audit transfer and reproducibility

Test whether the reasoning survives changes in:

- customer and buying situation;
- product category and price;
- competitive structure and distribution;
- channel, creative, and timing;
- operating capacity, incentives, and approval process.

Look for failed, neutral, and excluded cases—not only winners. A single high-CTR campaign, viral post, or successful company is evidence of possibility, not a universal rule.

### 5. Audit freshness and implementation

Read [implementation-and-freshness.md](references/implementation-and-freshness.md) when the claim depends on changing platforms, AI, tactics, internal politics, incentives, or operational capacity.

Check:

- when the source, data, and premise were last valid;
- whether the mechanism has changed since then;
- who must act, what process changes, and what capacity is required;
- local KPI conflicts, workarounds, vested interests, and approval incentives;
- whether the proposal is reversible, stageable, and observable after launch.

Do not call a plan implementable merely because its logic is sound. Equally, do not use organizational friction as an excuse to abandon a valuable hypothesis; propose staged adoption and explicit conditions.

### 6. Issue a decision and repair the claim

Choose one verdict:

- **Support:** evidence and implementation conditions justify the stated action.
- **Conditional support:** useful direction, but scope or conditions must be explicit.
- **Hold:** material unknowns make the current action premature; define the smallest test.
- **Refute:** evidence contradicts the claim or the inference is structurally invalid.

For every important weakness, provide:

1. the original risk;
2. a corrected, falsifiable wording;
3. the smallest useful validation;
4. implementation and withdrawal conditions.

Use [output-contract.md](references/output-contract.md) for the final structure.

## Routing boundaries

- Use `design-marketing-measurement` first for KPI architecture, experimental design, MMM specification, or metric calculation. Apply this skill as a second-line reasoning audit.
- Use `diagnose-marketing-structure` first when the primary question is why revenue or growth is weak and the bottleneck is unknown.
- Use `evaluate-ad-investment` first for budget, media, brand-versus-performance, or investment classification decisions.
- Use `assess-ma-crm-ltv` first for MA, CRM, retention, lifecycle, or LTV suitability.
- Use this skill first when the artifact's logic, evidence, generalizability, freshness, or implementation assumptions are themselves under review.

## Guardrails

- Do not diagnose a person's motives, competence, or psychology from a proposal.
- Do not hide behind “it depends”; name the variables on which it depends.
- Do not block reversible learning because perfect information is unavailable.
- Do not present proprietary terminology as an established industry standard.
- Do not optimize a KPI in a way that predictably damages trust or long-term choice.
- Do not erase rejected, non-buying, or churned people from stakeholder analysis.
- Do not confuse a polished audit with truth; disclose residual uncertainty.

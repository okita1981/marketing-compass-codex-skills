---
name: articulate-marketing-problem
description: "Turn scattered marketing or business symptoms, metrics, stakeholder statements, disagreements, and vague concerns into an evidence-bounded, testable problem definition before structural diagnosis or solution design. Use when a user says the issue is unclear, teams describe different problems, observations exist only as disconnected points, a request already jumps to ads/CRM/MA/reorganization, metrics conflict, definitions may have changed, or source data and interviews must be gathered to create an analysis-ready brief. Separate facts, measurements, interpretations, emotions, hypotheses, requests, and proposed solutions; connect points without inventing causality; identify competing explanations; and specify or perform the minimum evidence acquisition that can change the decision."
---

# Articulate Marketing Problem

Create the problem before solving it. Convert fragmented reality into an analysis-ready brief without polishing assumptions into facts or declaring a single root cause prematurely.

Read [references/problem-formation.md](references/problem-formation.md) for every substantive problem-definition task. Read [references/evidence-acquisition.md](references/evidence-acquisition.md) when files, systems, interviews, definitions, or additional data must be inspected or requested. Read [references/output-contract.md](references/output-contract.md) before returning a full brief.

## Establish the decision context

Identify:

- Who must decide what, and by when
- What triggered the concern
- What outcome, customer state, or operating condition is at risk
- What action is already being proposed, by whom, and on what premise
- What evidence is available now and what access is actually authorized

Ask at most three initial questions that materially change the scope or evidence plan. If answers are unavailable, continue with a provisional problem statement and label its limits.

Do not accept the requested solution as the problem. Translate “increase advertising,” “replace CRM,” “sales must follow up,” or “we need more people” into the condition those actions are intended to change.

## Phase A — Collect and classify the points

Extract atomic statements from conversation, documents, dashboards, spreadsheets, meeting notes, interviews, and system exports. Preserve source and wording when material.

Classify every consequential point as one of:

- Confirmed event or directly observed fact
- Measurement, including definition, denominator, population, period, and source
- Stakeholder report or lived observation
- Interpretation or causal story
- Emotion, concern, incentive, or desired outcome
- Hypothesis
- Unknown
- Proposed action or solution

Do not collapse stakeholder reports into system facts. Do not treat a logged value as self-explanatory truth; the value can be real while its definition, population, or comparison is unsuitable.

## Phase B — Connect points into candidate structures

Connect points only through an explicit relationship:

- Same population or cohort
- Temporal sequence
- Stage or process dependency
- Shared constraint or common cause
- Feedback loop or delay
- Contradiction or definition mismatch
- Stakeholder perspectives on the same event

Mark each connection as `confirmed`, `supported`, `plausible`, or `unknown`. Never join different cohorts, periods, definitions, or attribution systems silently.

Generate at least two competing explanations when the decision is consequential. State what observation would distinguish them. If the points cannot yet support a structure, say so and produce an evidence-acquisition plan instead of a polished narrative.

## Phase C — Form the problem statement

Write the narrowest useful problem definition that states:

1. Scope: population, process, market, cohort, and period
2. Observed condition or change
3. Why it matters to the pending decision
4. Candidate mechanism, explicitly labeled by evidence status
5. Material competing explanation
6. Missing evidence that could reverse the definition

Prefer formulations such as:

> In scope S and period T, observations O show condition C. This prevents or threatens decision outcome R. Evidence is consistent with mechanism H1, while H2 remains plausible because evidence E is missing. The next useful step is V.

Do not claim to have found the “true problem” when the evidence supports only a provisional issue or decision uncertainty.

## Phase D — Acquire the minimum decisive evidence

When authorized files, systems, or connectors are available, inspect them rather than merely listing unknowns. Follow [references/evidence-acquisition.md](references/evidence-acquisition.md): verify definitions and lineage first, then retrieve only information that distinguishes competing problem definitions.

When direct access is unavailable, specify:

- Exact field, extract, document, or interview evidence needed
- Source system or responsible person
- Population, period, cohort, and granularity
- Why the evidence changes the decision
- What result supports, weakens, or refutes each explanation
- Owner and practical timing when known

Do not ask for exhaustive discovery. Stop when the remaining uncertainty no longer changes the immediate reversible decision, or when the acquisition cost exceeds the decision value.

## Route without overreaching

Return an analysis-ready problem brief, not a full marketing strategy.

- Route to `diagnose-marketing-structure` after the issue and evidence base are sufficiently defined to compare bottlenecks.
- Route to `audit-marketing-reasoning` when an existing report or proposal itself is the audit object.
- Route to `design-marketing-measurement` when metric architecture, experiments, causal identification, or thresholds must be designed.
- Route to the relevant advertising, B2B, MA/CRM/LTV, or communications skill only after stating the defined problem that justifies it.

If an immediate danger, legal deadline, material customer harm, or irreversible loss exists, separate containment from deeper problem formation and prioritize the safe immediate action.

## Return a usable brief

Adapt depth to the material. For ambiguous but small requests, return a compact articulation. For cross-functional or consequential cases, use the full format in [references/output-contract.md](references/output-contract.md).

Always distinguish:

- What is happening
- What people think it means
- What may connect the points
- What is still missing
- What the problem can defensibly be called now
- What should be checked or collected next

## Guardrails

- Do not turn a complaint, metric, or proposed solution into the problem by paraphrasing it.
- Do not invent a link merely because multiple symptoms form an elegant story.
- Do not merge different cohorts, periods, definitions, or sources without qualification.
- Do not interpret stakeholder disagreement as evidence that one party is incompetent or acting in bad faith.
- Do not gather data because it is available; gather it because it can distinguish decisions or hypotheses.
- Do not let missing information become a reason for endless discovery or no decision.
- Do not expose credentials, private customer data, or unnecessary personal information while gathering evidence.
- Do not diagnose the maximum bottleneck before the problem is sufficiently formed; hand off to structural diagnosis.
- Do not present Marketing Compass terminology as universal industry terminology.

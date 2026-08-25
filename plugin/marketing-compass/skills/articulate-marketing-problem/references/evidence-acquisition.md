# Evidence Acquisition

## Contents

1. Acquisition principle
2. Source order
3. Definition and lineage audit
4. Data and document inspection
5. Interview design
6. Acquisition priority
7. Stop conditions

## 1. Acquisition principle

Acquire evidence to change a decision or distinguish competing problem definitions. Do not equate more data with better understanding.

For each request, state:

```text
Evidence needed
Question it answers
Hypotheses it distinguishes
Source and owner
Population / cohort / period / granularity
Support observation
Weakening or refuting observation
Acquisition cost and timing
```

## 2. Source order

Prefer evidence closest to the underlying event while retaining context:

1. Source-system definitions, event records, transaction records, and version history
2. Reproducible extracts or queries with documented filters
3. Operational documents, tickets, call notes, and contemporaneous records
4. Direct stakeholder or customer reports with concrete examples
5. Summaries, dashboards, attributed reports, and retrospective interpretations

This is not a universal credibility ranking. System logs can precisely record the wrong construct, and interviews can reveal states that logs cannot observe. Use different sources for different questions.

## 3. Definition and lineage audit

Before comparing a metric, verify:

- Business meaning and system implementation
- Numerator and denominator
- Inclusion, exclusion, deduplication, and null handling
- Population, cohort, stage, and attribution window
- Event time versus processing or reporting time
- Source table or system and transformation path
- Owner and update cadence
- Definition, instrumentation, process, or tool changes during the period

Create a change log when definitions or workflows may have shifted:

| Effective date | Metric/process | Old definition | New definition | Reason | Comparability impact |
|---|---|---|---|---|---|

Do not repair a broken time series by silently treating incompatible periods as one series.

## 4. Data and document inspection

When access is authorized:

- Inventory files, reports, tables, and date ranges.
- Identify duplicates, alternate versions, and canonical candidates.
- Trace reported numbers back to their source or formula.
- Check missingness, duplicate entities, stage overwrites, invalid joins, and denominator drift.
- Segment only when the segment can distinguish hypotheses; avoid exploratory fragmentation without a decision purpose.
- Preserve read-only behavior unless the user explicitly requests changes.
- Record what was inspected, what was not accessible, and any extraction limitations.

For connected systems, retrieve only fields required for the decision. Avoid credentials, unnecessary personal data, and broad exports when aggregate or scoped evidence suffices.

## 5. Interview design

Use interviews to recover meaning, process, exceptions, and unlogged conditions—not to vote on causality.

Prefer questions such as:

- What exactly did you observe? Give a recent example.
- When did it begin, and what changed immediately before it?
- Which accounts, customers, or cases does this apply to? Which are exceptions?
- Where is this recorded, if anywhere?
- What definition are you using for this term?
- What happens next in the actual workflow?
- What evidence would make you change your explanation?
- What action are you asking for, and what do you expect it to change?

Separate the interviewee's event report, interpretation, incentive, uncertainty, and proposed action. Do not diagnose motives from disagreement.

## 6. Acquisition priority

Rank missing evidence by:

1. Decision impact
2. Ability to distinguish competing explanations
3. Risk of acting incorrectly without it
4. Source validity and comparability
5. Time and cost to acquire
6. Access, privacy, and operational feasibility

Use one of:

- **Acquire now:** decision-changing and feasible.
- **Acquire during a reversible test:** useful but not required before containment.
- **Defer:** unlikely to change the current decision.
- **Do not acquire:** cost, privacy risk, or irrelevance exceeds value.

## 7. Stop conditions

Stop discovery and hand off when:

- The problem statement is bounded and competing explanations are distinguishable enough for the next decision.
- Remaining unknowns do not change the immediate reversible action.
- A small test will produce better evidence than further retrospective investigation.
- Evidence cannot be obtained within the deadline; state the conditional decision instead.
- Acquisition cost or privacy risk exceeds the decision value.

Do not claim completeness. State the residual uncertainty carried into structural diagnosis or action.

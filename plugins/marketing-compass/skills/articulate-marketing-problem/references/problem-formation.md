# Problem Formation Model

## Contents

1. What a problem is
2. Point taxonomy
3. Connection tests
4. Competing explanations
5. Problem-statement quality
6. Common failures

## 1. What a problem is

A problem is not merely an undesirable observation and not a proposed remedy. It is a bounded condition that obstructs a decision, customer-state transition, business outcome, or operating purpose, expressed with enough evidence and uncertainty to guide the next action.

Use this progression:

```text
Raw utterance or metric
  → classified point
  → comparable points
  → explicit relationship candidates
  → competing structural explanations
  → evidence-bounded problem statement
```

Distinguish:

- **Symptom:** what appears wrong, such as declining wins.
- **Interpretation:** what someone thinks it means, such as poor lead quality.
- **Mechanism hypothesis:** how one condition could produce another.
- **Constraint:** a condition that limits total outcome.
- **Problem definition:** the bounded issue the current decision should address.
- **Solution:** an intervention such as new CRM, advertising, hiring, or training.

## 2. Point taxonomy

Record consequential points with these fields when available:

| Field | Meaning |
|---|---|
| Point | One atomic statement |
| Type | Fact, measurement, report, interpretation, emotion/interest, hypothesis, unknown, solution |
| Source | System, document, person, or calculation |
| Scope | Population, cohort, market, process, or account |
| Period | Observation and comparison window |
| Definition | Numerator, denominator, stage rule, attribution, or qualitative meaning |
| Confidence | Confirmed, supported, plausible, or unknown |
| Decision relevance | What choice changes if the point is true or false |

Treat a system value as a measurement, not automatically as the underlying construct. For example, an MQL count can be correctly logged while failing to represent purchase readiness.

## 3. Connection tests

Before drawing a line between two points, test:

1. Are they about the same population or a validly linked cohort?
2. Are their periods and definitions comparable?
3. Does the proposed cause precede the result?
4. Is there an operational or customer mechanism connecting them?
5. Could a common cause produce both?
6. Could selection or reverse causality explain the pattern?
7. Is the relationship observed, inferred, or merely imaginable?

Use these relationship labels:

- **Confirmed:** the process, join, or evidence directly establishes the relationship.
- **Supported:** independent observations consistently support it, but causal alternatives remain.
- **Plausible:** a coherent mechanism exists, but decisive evidence is absent.
- **Unknown:** the points cannot yet be connected responsibly.

An explicit `unknown` connection is better than a fluent false line.

## 4. Competing explanations

For a consequential issue, compare at least two explanations. Use a compact matrix:

| Explanation | What it explains | Evidence for | Evidence against | Decisive observation |
|---|---|---|---|---|

Good competitors imply different actions. Examples:

- Low downstream conversion: poor lead fit versus sales-capacity ceiling.
- Low retention: expectation/value-realization failure versus cohort-mix change.
- Flat revenue after advertising: no incrementality versus long lag or hidden defensive floor.
- CRM complaints: tool limitation versus undefined operating process.

Do not create token alternatives that would lead to the same decision.

## 5. Problem-statement quality

A strong statement is:

- Bounded by population, process, and time
- Traceable to observations
- Clear about business or customer consequence
- Explicit about hypothesis status
- Able to survive disagreement about solutions
- Falsifiable through obtainable evidence
- Narrow enough to guide the next decision

Template:

> In **[scope]** during **[period]**, **[observed condition]** is occurring relative to **[comparison]**. This matters because **[decision or outcome at risk]**. Available evidence is consistent with **[H1]**, while **[H2]** remains plausible due to **[missing evidence]**. We can currently define the issue as **[provisional problem]** and should next verify **[decisive evidence]**.

## 6. Common failures

- **Solution laundering:** “We need CRM” becomes “the CRM problem.”
- **Complaint polishing:** stakeholder frustration is rewritten elegantly without evidence separation.
- **Point accumulation:** many symptoms are listed but no relationship is tested.
- **Narrative overfit:** all points are forced into one satisfying story.
- **False root cause:** a provisional mechanism is labeled the true underlying problem.
- **Definition blindness:** stage rules or attribution changed during the comparison.
- **Cohort splicing:** recent activation is connected to older retention without cohort linkage.
- **Discovery maximalism:** information gathering continues after the immediate decision is distinguishable.
- **Framework overwrite:** reality is made to fit a funnel or model selected in advance.

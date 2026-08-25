# Output Contract

## Contents

1. Missing-input behavior
2. Compact diagnosis
3. Full diagnosis
4. Decision states
5. Quality checks

## 1. Missing-input behavior

Ask no more than three questions before providing value. Choose questions that distinguish competing conclusions, such as:

- What decision will this answer change, and by when?
- Which stage is actually deteriorating: demand/traffic, choice/conversion, value, or continuation?
- What evidence exists beyond the channel metric being discussed?

If the user cannot answer, continue with labeled assumptions. Do not invent data.

## 2. Compact diagnosis

Use for a focused question:

```text
Core diagnosis:
Likely bottleneck:
Why:
What to verify:
Next move:
Do not do:
```

## 3. Full diagnosis

Use when the user asks for a strategy, complete diagnosis, or consequential decision:

```text
Decision: Execute / Small reversible test / Hold / Reduce / Stop

Decision owner and scope:
Demand type:
Structural model:
Primary bottleneck:
Secondary hypothesis:

Evidence:
- Confirmed facts:
- Interpretation:
- Hypotheses:
- Unknowns:
- Evidence level:

Recommended move:
Why this move:
What not to do:

Desired signal:
Counter-signal:
Guardrail:
Review point:
Action if crossed:

Specialist analysis needed:
Uncertainty and exceptions:
```

## 4. Decision states

- **Execute:** evidence and reversibility support implementation.
- **Small reversible test:** the hypothesis matters but uncertainty is material.
- **Hold:** required evidence or prerequisite structure is missing.
- **Reduce:** contain cost or exposure while preserving the ability to recover.
- **Stop:** expected value is negative, a guardrail is breached, or the action solves the wrong problem.

## 5. Quality checks

Before returning, confirm:

- The response leads with the actual diagnosis.
- One primary bottleneck is named or the inability to distinguish it is explained.
- No invented metric or causal claim appears.
- The recommended action targets the bottleneck.
- A consequential recommendation includes a counter-signal and guardrail.
- “What not to do” is specific.
- The answer is shorter than the analysis needed to produce it.

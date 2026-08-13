# Reasoning and Evidence Audit

## Claim audit table

| Field | Question |
|---|---|
| Claim | What exactly is asserted? |
| Type | Fact, interpretation, hypothesis, unknown, or recommendation? |
| Evidence | What observation supports it? |
| Evidence level | A causal, B triangulated, C observational, or D hypothesis? |
| Inference | What logical step connects evidence to conclusion? |
| Alternatives | What else could produce the observation? |
| Scope | For whom, where, when, and under what conditions? |
| Decision effect | What action changes if the claim is true or false? |
| Repair | What narrower, falsifiable wording is defensible? |

## Causal checks

1. Confirm that the proposed cause precedes the outcome.
2. Define the counterfactual: what likely happens without the intervention?
3. Inspect common causes, reverse causality, selection, survivorship, and regression to the mean.
4. Check seasonality, promotions, distribution, price, product changes, competition, and macro events.
5. Inspect measurement error, missing data, attribution windows, aggregation, and model specification.
6. Separate statistical detection from business materiality.
7. State what evidence would change the conclusion.

## Common audit failures

- **Denominator neglect:** a large count without the eligible population.
- **Average masking:** a mean that hides segments, tails, or distribution changes.
- **Proxy substitution:** clicks, leads, or recall treated as profit or durable choice.
- **Winner selection:** only successful campaigns, customers, or companies are examined.
- **Case transfer:** a mechanism is copied without matching category, customer, channel, or organization.
- **Framework overwrite:** observations are forced into a preferred model.
- **Metric reification:** a model estimate is treated as an observed physical fact.
- **Post-hoc causality:** a story is constructed after the outcome and presented as prediction.
- **Multiple testing:** the surviving positive result is reported without the number of attempts.
- **False precision:** exact allocation or ROI is claimed beyond the data's resolution.

## Model-specific caution

MMM can reveal plausible contribution patterns, anomalies, and broad ranges, but its conclusion depends on data quality, specification, priors, time variation, collinearity, and unobserved variables. Do not promote an MMM coefficient to causal truth without supporting design or triangulation.

Use method roles deliberately:

- observation or MMM: hypotheses, anomalies, audit, and broad direction;
- user A/B: expression and path efficiency;
- randomized or credible quasi-experiment: incrementality;
- Geo test: macro-level incremental effect;
- survey: attitude, recall, and perception differences;
- multiple evidence streams: continue, reduce, redesign, or withdraw.

## Falsifiable rewrite pattern

Replace “X caused Y” with a scoped claim such as:

> In population P, during period T, under conditions C, evidence E is consistent with X increasing Y by range R relative to comparison K. Alternative explanations A remain. We will revise the claim if observation Z occurs.

Use a range only when evidence supports one. Otherwise state direction and uncertainty.

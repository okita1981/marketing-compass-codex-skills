# Evidence Method Selection

## Contents

1. Selection questions
2. Method roles and limits
3. MMM audit
4. Experiment audit
5. Triangulation

## 1. Selection questions

Before choosing a method, define:

- The decision and required claim
- Unit of intervention and unit of analysis
- Population, period, and expected lag
- Spillover and contamination risk
- Minimum material effect
- Cost of false positive and false negative
- Feasibility of withholding or varying treatment

## 2. Method roles and limits

| Method | Best use | Does not establish by itself |
|---|---|---|
| Behavioral logs | Delivery, exposure, observed action, cohorts | Unobserved attitudes or causal incrementality |
| Survey | Recall, recognition, understanding, preference, trust, intent | Actual behavior or causal sales impact without design |
| User A/B | Relative treatment effect in a controlled surface | Total market incrementality or long-term effect automatically |
| Geo/market test | Macro incremental effect across areas | Validity when regions differ materially or spillover is high |
| MMM | Historical fit, hypotheses, anomalies, audit, rough ranges | Exact causal contribution, exact ROI, or true optimal allocation |
| Qualitative research | Mechanism, vocabulary, friction, hypothesis generation | Population prevalence without appropriate sampling |
| Proxy signal | Early direction when the construct is latent | The underlying construct itself |

## 3. MMM audit

Check:

- Outcome and time grain
- Sufficient variation in spend and outcome
- Adstock and saturation assumptions
- Collinearity among channels and seasonality
- Promotions, price, distribution, competition, and macro controls
- Structural breaks and non-stationarity
- Priors and sensitivity to specification
- Holdout or external validation
- Coefficient stability and uncertainty ranges
- Whether the business asks for more precision than the model supports

Use MMM for hypotheses, anomalies, audits, broad ranges, and large directional changes. Combine it with experiments or independent evidence for incrementality.

## 4. Experiment audit

Check:

- Assignment before exposure
- Sample ratio and attrition
- Pre-treatment balance
- Contamination and interference
- Metric definition fixed before analysis
- Sufficient duration for lag and novelty
- Multiple testing
- Practical significance, not only statistical significance
- Segment effects pre-specified or labeled exploratory
- Whether the treatment changes only the claimed variable

## 5. Triangulation

When no method is decisive, combine evidence with different failure modes:

```text
Logs → what happened
Survey or qualitative research → what changed in the customer
Experiment or counterfactual → what was incremental
Business and operating data → whether the effect is valuable and executable
```

Do not average incompatible results into a false single truth. Explain why evidence converges or conflicts.

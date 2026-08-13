# Advertising Decision Branches

## Contents

1. Structural return conditions
2. Optimization versus defense
3. Testing choices
4. Common failure patterns

## 1. Structural return conditions

| Condition | Advertising role | Do not substitute |
|---|---|---|
| Base demand absent | Reconsider market or create a credible new context | More acquisition spend |
| Problem latent | Education, diagnosis, and articulation | Fabricated fear or urgency |
| Existing demand can move forward | Current-value advertising | Ignoring future-demand cannibalization |
| Recall weak | Meaning, reach, memory, category entry | Awareness delivery alone |
| Recalled but not chosen | Choice reason, proof, price, risk | More frequency without a reason |
| Chosen but cannot buy | Distribution, inventory, payment, sales, UX | Advertising increase |
| Trial but no continuation | Expectation, value realization, product, CS | Retargeting or reminders |
| Baseline may erode silently | Defensive non-current-value investment | Large one-time cuts |

## 2. Optimization versus defense

### Optimize when

- Spend changes produce observable response within a useful window.
- The curve is sufficiently continuous.
- Changes are reversible.
- A counterfactual or credible marginal comparison exists.
- The organization can act on the estimate.

### Defend a threshold when

- Memory or competitive position decays with a lag.
- Small changes are hidden by noise.
- Crossing a floor may cause nonlinear loss.
- Recovery requires disproportionate time or money.
- The relevant outcome is maintained stability, not immediate lift.

Use:

```text
Business role → acceptable risk → provisional floor → small change
→ anomaly monitoring → restore if the guardrail is crossed
```

## 3. Testing choices

- Use user A/B tests for message or interface efficiency, not total market incrementality by default.
- Use Geo or market tests when treatment can vary by comparable area and spillover is manageable.
- Use surveys for recall, meaning, trust, and consideration.
- Use logs for exposure, search, direct response, purchase, and cohorts.
- Use MMM for historical fit, hypotheses, anomalies, and rough ranges; not exact causal ROI.
- Combine independent evidence when no single method identifies the effect.

## 4. Common failure patterns

- Calling platform-attributed ROAS incremental return.
- Treating a cheap CPA as profitable without margin or continuation.
- Counting reach or impressions as retained value.
- Using one review window for immediate response and future memory.
- Cutting brand support until revenue visibly falls.
- Funding institutional relationships while explaining them as consumer ROI.
- Increasing demand generation when distribution or onboarding is constrained.
- Copying another brand's media mix without matching conditions.

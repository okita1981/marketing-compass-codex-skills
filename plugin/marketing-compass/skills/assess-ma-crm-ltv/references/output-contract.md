# MA, CRM, and LTV Output Contract

## Contents

1. Missing-input behavior
2. Compact diagnosis
3. Full diagnosis
4. Decision states
5. Quality checks
6. Output language

## 1. Missing-input behavior

Ask at most three questions that can change readiness or the primary bottleneck:

- What recurring need or decision is MA or CRM supposed to support?
- Where do customers fail to reach or continue receiving value?
- Which customer state can be observed well enough to trigger an action?

If answers are unavailable, provide a provisional diagnosis and the smallest discovery step. Do not invent readiness scores or LTV.

## 2. Compact diagnosis

```text
MA/CRM judgment:
Major blocker:
Primary customer-state bottleneck:
Role that should act:
LTV view:
Next move:
Do not do:
```

## 3. Full diagnosis

```text
Decision: Adopt or expand / Conditional pilot / Hold / Reduce or redesign / Adverse

Decision owner, scope, and deadline:
Business model and cohort:
Recurring need or decision:

Major blockers:
Supporting conditions:
Primary customer-state bottleneck:
Secondary hypothesis:

Strategic CRM responsibility:
Operational CRM responsibility:
MA responsibility:
CS responsibility:

LTV view used:
Accounting definition and assumptions:
Strategic LTV formation drivers:
Acquisition economics:

Automated action:
Human-intervention point:
Suppression and escalation:

Confirmed facts:
Proxies:
Hypotheses:
Unknowns:
Evidence level:

Desired Signal:
Counter-signal:
Guardrail:
Review window:
Action if crossed:

What to fix first:
What not to do:
Uncertainty and exceptions:
```

## 4. Decision states

- **Adopt or expand:** prerequisites and operating ownership support a defined use case.
- **Conditional pilot:** value is plausible but uncertainty warrants a narrow reversible test.
- **Hold:** demand, ICP, value realization, data, permission, or ownership is missing.
- **Reduce or redesign:** contact complexity or cost exceeds value, or adverse signals are increasing.
- **Adverse:** automation is likely to amplify irrelevant contact, poor experience, mistrust, or structural failure.

## 5. Quality checks

- Major blockers are assessed before supporting conditions.
- Strategic CRM, operational CRM, MA, and CS are not collapsed.
- One primary customer-state bottleneck is named.
- Contact has a customer benefit, entry, exit, suppression, and owner.
- Automation and human judgment are separated.
- Accounting LTV, acquisition economics, and strategic LTV are distinct.
- Financial assumptions include cohort, period, margin, and service-cost definitions or are labeled unknown.
- Strategic LTV is not calculated from an uncalibrated tree.
- Desired and adverse customer signals are included.
- “What not to do” is specific.

## 6. Output language

Respond in the language of the user's most recent message. When replying in Japanese, translate the field labels above using the table below; keep the field structure and order unchanged. `Signal`, `Counter-signal`, and `Guardrail` are used as-is in Japanese (the established Marketing Compass convention — see `canonical/marketing-compass-canonical-v1.0.md` §7.5, §14), not translated. `MA`, `CRM`, `CS`, and `LTV` are also used as-is.

| English label | 日本語ラベル |
|---|---|
| MA/CRM judgment | MA・CRM判定 |
| Major blocker | 主要な阻害要因 |
| Primary customer-state bottleneck | 顧客状態上の最大ボトルネック |
| Role that should act | 対応すべき役割 |
| LTV view | LTVの見方 |
| Next move | 次の一手 |
| Do not do | しないこと |
| Decision owner, scope, and deadline | 決定権者・適用範囲・期限 |
| Business model and cohort | ビジネスモデルとコホート |
| Recurring need or decision | 継続的な需要・意思決定 |
| Major blockers | 主要な阻害要因 |
| Supporting conditions | 補助的な条件 |
| Secondary hypothesis | 第二候補仮説 |
| Strategic CRM responsibility | 戦略的CRMの責任範囲 |
| Operational CRM responsibility | 運用的CRMの責任範囲 |
| MA responsibility | MAの責任範囲 |
| CS responsibility | CSの責任範囲 |
| LTV view used | 採用したLTVの見方 |
| Accounting definition and assumptions | 会計上の定義と前提 |
| Strategic LTV formation drivers | 戦略的LTVを形成する要因 |
| Acquisition economics | 獲得コストの経済性 |
| Automated action | 自動化されたアクション |
| Human-intervention point | 人間が介入するポイント |
| Suppression and escalation | 抑制とエスカレーション |
| Confirmed facts | 確認済みの事実 |
| Proxies | 代理指標 |
| Hypotheses | 仮説 |
| Unknowns | 未知の点 |
| Evidence level | 証拠レベル |
| Review window | 見直し期間 |
| What to fix first | 最初に直すべきこと |
| Uncertainty and exceptions | 不確実性と例外 |

Decision state values (§4):

| English | 日本語 |
|---|---|
| Adopt or expand | 導入・拡大 |
| Conditional pilot | 条件付き試行 |
| Hold | 保留 |
| Reduce or redesign | 縮小・再設計 |
| Adverse | 悪影響 |

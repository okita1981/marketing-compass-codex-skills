# Advertising Investment Output Contract

## Contents

1. Missing-input behavior
2. Compact judgment
3. Full judgment
4. Decision states
5. Quality checks
6. Output language

## 1. Missing-input behavior

Ask no more than three decision-changing questions:

- What probability or timing is this advertising intended to change?
- What happens when spend stops, and over what horizon?
- What evidence or comparison exists beyond attributed media metrics?

If answers are unavailable, return a provisional classification and the smallest safe test. Do not invent return or thresholds.

## 2. Compact judgment

```text
Judgment:
Advertising class:
Probability or timing changed:
Why it qualifies or does not:
Primary return:
Evidence and uncertainty:
Next move:
Do not do:
```

## 3. Full judgment

```text
Decision: Increase / Continue / Small reversible test / Hold / Reduce / Stop or restore

Decision owner, scope, and deadline:
Product, market, and buying context:
Budget change:
Probability or timing changed:

Advertising class:
Operating tag:
Investment qualification:
Missing conditions:
Optimization or threshold-defense:

Current-value return:
Future or residual value:
Expected stopping behavior:
Evidence method and level:
Can conclude:
Cannot conclude:

Baseline:
Desired Signal:
Counter-signal:
Guardrail or safe floor:
Review window:
Action if crossed:

Recommended move:
What not to do:
Uncertainty and exceptions:
```

## 4. Decision states

- **Increase:** marginal return or future-state evidence supports cautious expansion.
- **Continue:** the investment thesis remains valid through the defined review window.
- **Small reversible test:** the thesis matters but uncertainty or threshold risk is material.
- **Hold:** the return, prerequisite structure, or measurement basis is missing.
- **Reduce:** expected value has weakened; contain exposure while preserving learning or recovery.
- **Stop or restore:** the action solves the wrong problem, expected value is negative, or a guardrail is breached.

## 5. Quality checks

- One primary probability or timing change is named.
- One primary advertising class is assigned or components are split.
- Current and future returns are not collapsed into one metric.
- The classification has explicit qualification conditions.
- Optimization and threshold-defense are distinguished.
- Attributed return is not called incremental without a counterfactual.
- Residual value has a mechanism, duration, and signal or is labeled unknown.
- Signal, counter-signal, guardrail, review window, and action are defined for consequential decisions.
- “What not to do” is specific.

## 6. Output language

Respond in the language of the user's most recent message. When replying in Japanese, translate the field labels above using the table below; keep the field structure and order unchanged. `Signal`, `Counter-signal`, and `Guardrail` are used as-is in Japanese (the established Marketing Compass convention — see `canonical/marketing-compass-canonical-v1.0.md` §7.5, §14), not translated.

| English label | 日本語ラベル |
|---|---|
| Judgment | 判定 |
| Advertising class | 広告の分類 |
| Probability or timing changed | 変化させる確率・タイミング |
| Why it qualifies or does not | 該当する・しない理由 |
| Primary return | 主要なリターン |
| Evidence and uncertainty | 根拠と不確実性 |
| Next move | 次の一手 |
| Do not do | しないこと |
| Decision owner, scope, and deadline | 決定権者・適用範囲・期限 |
| Product, market, and buying context | 商品・市場・購買文脈 |
| Budget change | 予算変更 |
| Operating tag | 運用区分タグ |
| Investment qualification | 投資としての適格性 |
| Missing conditions | 不足している条件 |
| Optimization or threshold-defense | 最適化型か閾値防衛型か |
| Current-value return | 現在価値リターン |
| Future or residual value | 将来価値・残存価値 |
| Expected stopping behavior | 停止時に想定される挙動 |
| Evidence method and level | 検証方法と証拠レベル |
| Can conclude | 言えること |
| Cannot conclude | 言えないこと |
| Guardrail or safe floor | Guardrailまたは下限ライン |
| Recommended move | 推奨する一手 |
| Uncertainty and exceptions | 不確実性と例外 |

Decision state values (§4):

| English | 日本語 |
|---|---|
| Increase | 増額 |
| Continue | 継続 |
| Small reversible test | 小規模な可逆テスト |
| Hold | 保留 |
| Reduce | 縮小 |
| Stop or restore | 撤退または原状回復 |

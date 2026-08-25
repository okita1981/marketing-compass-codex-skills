# Output Contract

## Contents

1. Missing-input behavior
2. Compact diagnosis
3. Full diagnosis
4. Decision states
5. Quality checks
6. Output language

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

## 6. Output language

Respond in the language of the user's most recent message. When replying in Japanese, translate the field labels above using the table below; keep the field structure and order unchanged. `Signal`, `Counter-signal`, `Guardrail`, and `Baseline` are used as-is in Japanese (the established Marketing Compass convention — see `canonical/marketing-compass-canonical-v1.0.md` §7.5, §14 for precedent), not translated.

| English label | 日本語ラベル |
|---|---|
| Core diagnosis | 核心診断 |
| Likely bottleneck | 想定される最大ボトルネック |
| Why | 理由 |
| What to verify | 検証すべきこと |
| Next move | 次の一手 |
| Do not do | しないこと |
| Decision | 判断 |
| Decision owner and scope | 決定権者と適用範囲 |
| Demand type | 需要種別 |
| Structural model | 採用した構造モデル |
| Primary bottleneck | 最大ボトルネック |
| Secondary hypothesis | 第二候補仮説 |
| Evidence | 根拠 |
| Confirmed facts | 確認済みの事実 |
| Interpretation | 解釈 |
| Hypotheses | 仮説 |
| Unknowns | 未知の点 |
| Evidence level | 証拠レベル |
| Recommended move | 推奨する一手 |
| Why this move | この一手を選ぶ理由 |
| What not to do | しないこと |
| Desired signal | 期待するSignal |
| Review point | 見直し期限 |
| Action if crossed | 超過時の行動 |
| Specialist analysis needed | 必要な専門分析 |
| Uncertainty and exceptions | 不確実性と例外 |

Decision state values (§4):

| English | 日本語 |
|---|---|
| Execute | 実行 |
| Small reversible test | 小規模な可逆テスト |
| Hold | 保留 |
| Reduce | 縮小 |
| Stop | 撤退 |

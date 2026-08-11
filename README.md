# Marketing Compass — GPT / Codex Skills

Marketing Compassは、マーケティングを施策の一覧ではなく、事業成果が生まれる構造と顧客の意思決定から捉えるための判断体系です。

このリポジトリには、Marketing Compass確定正本 v1.0と、正本を共通参照して動く7つのGPT / Codex向けスキルを収録しています。

## 収録スキル

| # | 表示名 | スキル名 | 主な役割 |
|---|---|---|---|
| 01 | 売上の構造を解く | `diagnose-marketing-structure` | 売上構造を分解し、最大ボトルネックと動かす変数を特定する |
| 02 | 成果を測る | `design-marketing-measurement` | 目的からKGI・KPI・検証方法・継続撤退条件を組み立てる |
| 03 | 広告投資を見極める | `evaluate-ad-investment` | 広告の役割、投資資格、評価期間、撤退条件を見極める |
| 04 | BtoBを動かす | `design-btob-growth` | 商談、稟議、導入、継続まで案件成立構造を組み立てる |
| 05 | LTVを育てる | `assess-ma-crm-ltv` | MA・CRM・CSの役割とLTV形成要因を整理する |
| 06 | 意味と接点をつくる | `design-marketing-communications` | 顧客状態、意味、想起、期待から接点と役割を組み立てる |
| 07 | 論理を確かめる | `audit-marketing-reasoning` | 因果、再現性、鮮度、実装条件から提案と分析を確かめる |

## 中核思想

- 売上を単一施策へ誤帰属せず、成立条件へ分解する。
- 観測できる数字と、事業上重要な変化を混同しない。
- マーケティングを、需要・想起・選択・価値到達・継続・関係への介入として扱う。
- 因果、反証条件、許容リスク、Guardrail、撤退条件を明示する。
- フレームワークより現実を優先し、診断だけで終わらず判断と実行へ接続する。

完全な定義と判断原則は、[`canonical/marketing-compass-canonical-v1.0.md`](canonical/marketing-compass-canonical-v1.0.md)を参照してください。

## 使い方

### Codex / ChatGPT

利用したいディレクトリをスキルとしてインストールするか、プラグインの `skills/` 配下へ配置してください。明示的に呼び出す場合は、スキル名の前に `$` を付けます。

例:

```text
$diagnose-marketing-structure を使って、売上が伸びない原因を施策提案の前に構造分解してください。
```

ChatGPTとCodexは、依頼内容に応じて該当スキルを暗黙に選択することもできます。

## ディレクトリ構成

```text
canonical/  Marketing Compassの思想・定義・判断原則の正本
skills/     7つの独立したスキル
```

各スキルは次を含みます。

```text
SKILL.md             発動条件と実行手順
agents/openai.yaml   表示名、説明、呼び出し設定
references/          判断基準、分岐、出力仕様
assets/icon.svg      スキル固有アイコン
```

## 適用範囲

Marketing Compassは、万能な施策生成器ではありません。事業、顧客、需要、流通、商品価値、組織能力などの前提を確認し、利用可能な証拠の範囲内で判断します。出力は専門家の法務・会計・医療判断を代替しません。

## Author

Kousuke Okita / 沖田紘亮

## License

このリポジトリの文書・スキル・アイコンは、特記がない限り[Creative Commons Attribution 4.0 International](LICENSE)で提供します。利用・改変・再配布の際は、著作者と本リポジトリへの適切なクレジットを表示してください。

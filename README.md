# Marketing Compass — GPT / Codex Skills

Marketing Compassは、マーケティングを施策の一覧ではなく、事業成果が生まれる構造と顧客の意思決定から捉えるための判断体系です。

このリポジトリには、Marketing Compass確定正本 v1.0、正本を共通参照して動く8つのGPT / Codex向けスキル、ならびに関連する汎用思考スキル「思考を整理する7段の階段」を収録しています。

GPT / Codex向けスキルのうち7つ（01〜07）と「思考を整理する7段の階段」は、同一内容のままClaude Code project skillとしても利用できます。詳しくは[Claude Code](#claude-code)を参照してください。

## 収録スキル

| # | 表示名 | スキル名 | 主な役割 |
|---|---|---|---|
| 00 | 課題を言葉にする | `articulate-marketing-problem` | 点在する現象・数字・違和感・関係者の発言をつなぎ、検証可能な課題として言語化する |
| 01 | 売上の構造を解く | `diagnose-marketing-structure` | 売上構造を分解し、最大ボトルネックと動かす変数を特定する |
| 02 | 成果を測る | `design-marketing-measurement` | 目的からKGI・KPI・検証方法・継続撤退条件を組み立てる |
| 03 | 広告投資を見極める | `evaluate-ad-investment` | 広告の役割、投資資格、評価期間、撤退条件を見極める |
| 04 | BtoBを動かす | `design-btob-growth` | 商談、稟議、導入、継続まで案件成立構造を組み立てる |
| 05 | LTVを育てる | `assess-ma-crm-ltv` | MA・CRM・CSの役割とLTV形成要因を整理する |
| 06 | 意味と接点をつくる | `design-marketing-communications` | 顧客状態、意味、想起、期待から接点と役割を組み立てる |
| 07 | 論理を確かめる | `audit-marketing-reasoning` | 因果、再現性、鮮度、実装条件から提案と分析を確かめる |

## 関連する汎用思考スキル

| 表示名 | スキル名 | 主な役割 |
|---|---|---|
| 思考を整理する7段の階段 | `thinking-staircase` | 反応・観察・因果・検証・自己点検・構造・戦略的運用を行き来し、曖昧な思考や対立を判断と行動へ整理する |

「思考を整理する7段の階段」は、Marketing Compass固有のマーケティング理論ではなく、会議、提案、意思決定、対立、感情的反応などにも使える独立した思考ナビゲーションです。段階を知性や人格の序列として扱わず、状況に応じて必要な段を選び、最後は実行可能な水準へ降ろすことを重視します。

## 基本フロー

```text
00 課題を言葉にする
  → 01 売上の構造を解く
  → 02〜06 専門領域を深掘りする
  → 07 論理を確かめる
```

00は、まだ課題が言語化されていない現場で、事実・計測値・解釈・感情・仮説・解決策を分離し、点同士の接続可能性と対立仮説を整理します。未確認事項を並べるだけでなく、何をどこから取得すれば判断が変わるかまで示し、01以降が分析できる与件を作ります。

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
$articulate-marketing-problem を使って、部門ごとに異なる現象・数字・解釈を整理し、まず課題を言葉にしてください。
```

```text
$diagnose-marketing-structure を使って、売上が伸びない原因を施策提案の前に構造分解してください。
```

```text
$thinking-staircase を使って、この会議が噛み合わない原因と、いま必要な判断を整理してください。
```

ChatGPTとCodexは、依頼内容に応じて該当スキルを暗黙に選択することもできます。

### Claude Code

このリポジトリは、GPT / Codex版とは別に、[Claude Code](https://code.claude.com/docs/en/claude-code)向けのproject skillとして`.claude/skills/`配下に同一内容のコピーを収録しています。対応スキルはMarketing Compass 7スキル（01〜07）と「思考を整理する7段の階段」の計8つです。「課題を言葉にする」（`articulate-marketing-problem`、00）はGPT / Codex版のみの提供で、今回のClaude Code対応の範囲には含まれていません。

#### 対応している8スキル

| # | 表示名 | Claude Codeでの呼び出し |
|---|---|---|
| 01 | 売上の構造を解く | `/diagnose-marketing-structure` |
| 02 | 成果を測る | `/design-marketing-measurement` |
| 03 | 広告投資を見極める | `/evaluate-ad-investment` |
| 04 | BtoBを動かす | `/design-btob-growth` |
| 05 | LTVを育てる | `/assess-ma-crm-ltv` |
| 06 | 意味と接点をつくる | `/design-marketing-communications` |
| 07 | 論理を確かめる | `/audit-marketing-reasoning` |
| — | 思考を整理する7段の階段 | `/thinking-staircase` |

#### Project skillとして使う（リポジトリをそのまま使う場合）

このリポジトリをcloneし、そのディレクトリでClaude Codeを起動するだけで、`.claude/skills/`配下の8スキルがそのプロジェクトのproject skillとして自動的に読み込まれます。追加のインストール操作は不要です。

```bash
git clone https://github.com/okita1981/marketing-compass-codex-skills.git
cd marketing-compass-codex-skills
claude
```

#### Personal skillとしてインストールする（他のプロジェクトからも使う場合）

すべてのプロジェクトから使えるようにしたい場合は、`.claude/skills/`配下の各スキルフォルダを、ご自身の個人スキルフォルダ（`~/.claude/skills/`）へコピーしてください。

```bash
git clone https://github.com/okita1981/marketing-compass-codex-skills.git
cd marketing-compass-codex-skills
mkdir -p ~/.claude/skills
cp -r .claude/skills/. ~/.claude/skills/
```

Windows（PowerShell）の場合:

```powershell
git clone https://github.com/okita1981/marketing-compass-codex-skills.git
cd marketing-compass-codex-skills
New-Item -ItemType Directory -Force ~/.claude/skills | Out-Null
Copy-Item -Recurse -Force .claude/skills/* ~/.claude/skills/
```

#### 呼び出し方

明示的に呼び出す場合は、スキル名の前に`/`を付けます（Codex/ChatGPT版の`$スキル名`とは記法が異なります）。

```text
/diagnose-marketing-structure を使って、売上が伸びない原因を施策提案の前に構造分解してください。
```

```text
/thinking-staircase を使って、この会議が噛み合わない原因と、いま必要な判断を整理してください。
```

Claude Codeは、frontmatterの`description`をもとに、依頼内容に応じて該当スキルを暗黙に選択することもできます。

#### GPT / Codex版との関係・正本・同期方針

- 思想・定義・判断原則の正本は、GPT / Codex版と同じく[`canonical/marketing-compass-canonical-v1.0.md`](canonical/marketing-compass-canonical-v1.0.md)と各`skills/<スキル名>/SKILL.md`・`references/`です。`.claude/skills/`配下のファイルは、そこから生成した派生コピーであり、内容は改変していません（`SKILL.md`・`references/*.md`ともバイト単位で同一）。
- Claude Codeでは`agents/openai.yaml`（表示名・アイコン・呼び出し設定などOpenAI固有の表示設定）と`assets/icon.svg`は使用しないため、`.claude/skills/`配下には複製していません。
- `skills/<スキル名>/SKILL.md`または`references/`を更新した場合は、[`scripts/sync-claude-code-skills.sh`](scripts/sync-claude-code-skills.sh)を実行して`.claude/skills/`側へ反映してください。差分の有無だけを確認したい場合は`--check`を付けて実行します（差分があれば非ゼロ終了）。

```bash
bash scripts/sync-claude-code-skills.sh          # 正本から .claude/skills/ を更新
bash scripts/sync-claude-code-skills.sh --check  # 差分の有無だけを確認（書き込みなし）
```

- 構造・内容の検証は[`scripts/verify-claude-code-skills.py`](scripts/verify-claude-code-skills.py)（Python 3標準ライブラリのみ）で行えます。frontmatterの妥当性、参照リンクの解決、正本とのバイト単位の一致、GPT/Codex版・正本が変更されていないことなどを確認します。

```bash
python3 scripts/verify-claude-code-skills.py
```

#### 対応確認済みのClaude Code仕様

[Claude Code Skills公式ドキュメント](https://code.claude.com/docs/en/skills)（2026-08-13時点の内容で確認。`https://docs.claude.com/en/docs/claude-code/skills`からリダイレクトされます）に基づき、project skillの配置場所（`.claude/skills/<skill-name>/SKILL.md`）、`name`/`description`のみのfrontmatter、相対パスによる`references/`参照、`/skill-name`による明示呼び出しと`description`に基づく暗黙呼び出しが、追加設定なしでそのまま機能する仕様であることを確認しています。ローカルにインストール済みのClaude Code CLI（`claude --version` で確認、v2.1.170）でも、これらは特定バージョン以降専用の機能ではない基本機能です。

## ディレクトリ構成

```text
canonical/     Marketing Compassの思想・定義・判断原則の正本
skills/        Marketing Compass 8スキル＋関連する汎用思考スキル（GPT / Codex向け正本）
.claude/skills/ 上記のうち8スキルをClaude Code project skill向けに複製したコピー
scripts/       .claude/skills/ の生成・同期・検証スクリプト
```

`skills/`配下の各スキルは次を含みます。

```text
SKILL.md             発動条件と実行手順
agents/openai.yaml   表示名、説明、呼び出し設定
references/          判断基準、分岐、出力仕様
assets/icon.svg      スキル固有アイコン
```

`.claude/skills/`配下の各スキルは、Claude Codeの実行に必要な次の2つのみを含みます。

```text
SKILL.md       skills/<スキル名>/SKILL.md と同一内容
references/    skills/<スキル名>/references/ と同一内容
```

## 適用範囲

Marketing Compassは、万能な施策生成器ではありません。事業、顧客、需要、流通、商品価値、組織能力などの前提を確認し、利用可能な証拠の範囲内で判断します。出力は専門家の法務・会計・医療判断を代替しません。

## Author

Kousuke Okita / 沖田紘亮

## License

このリポジトリの文書・スキル・アイコンは、特記がない限り[Creative Commons Attribution 4.0 International](LICENSE)で提供します。利用・改変・再配布の際は、著作者と本リポジトリへの適切なクレジットを表示してください。

# AI News Research Site

GitHub Pagesで公開するAI/LLMニュースリサーチサイト。

## プロジェクト構成

```
docs/           - GitHub Pages公開ディレクトリ
  index.html    - メインページ
  css/style.css - スタイル
  js/app.js     - ニュース表示ロジック
  data/news.json - ニュースデータ（調査結果）
prompts/        - リサーチ用プロンプト
  research-all.md         - 全カテゴリ一括調査
  research-japan.md       - 日本AI/LLMニュース
  research-international.md - 海外AI/LLMニュース
  research-company-blogs.md - 企業ブログ
  research-arxiv.md       - arXiv論文
scripts/        - 自動化スクリプト
  validate_and_merge.py   - 記事の日付検証・マージスクリプト
  blocklist.json          - 古いニュースURLのブロックリスト
```

## ニュース更新手順

ニュースデータを更新するには、`prompts/research-all.md` の手順に従ってください。

各カテゴリのプロンプトを使い、WebSearchとWebFetchで最新ニュースを調査し、
`scripts/validate_and_merge.py` で検証してから `docs/data/news.json` に統合保存します。

## 日付検証（重要）

リサーチエージェントは古いニュースを誤って最新と報告することがある。
新規記事の追加時は **必ず** `scripts/validate_and_merge.py` を使用すること。

```bash
# 新規記事を /tmp/new_articles.json に保存してから:
python3 scripts/validate_and_merge.py --new-articles /tmp/new_articles.json

# ドライラン（検証のみ、書き込みなし）:
python3 scripts/validate_and_merge.py --new-articles /tmp/new_articles.json --dry-run

# 最大年齢を7日に変更:
python3 scripts/validate_and_merge.py --new-articles /tmp/new_articles.json --max-age-days 7
```

検証内容:
- 日付が過去14日以内か
- 未来の日付でないか
- ブロックリスト（`scripts/blocklist.json`）に含まれていないか
- URL重複がないか
- 必須フィールドが揃っているか

誤って混入した古いニュースのURLは `scripts/blocklist.json` に追加すること。

## ニュースカテゴリ

| カテゴリ | 説明 |
|---------|------|
| japan | 日本国内のAI/LLMニュース |
| international | 海外のAI/LLMニュース |
| company_blog | OpenAI, Anthropic, Google, DeepMind, Microsoft, Cohere, Qwen, Alibaba等のブログ |
| arxiv | arXivのAI/LLM関連論文 |

## 開発メモ

- GitHub Pagesは `docs/` ディレクトリから配信
- ニュースデータは静的JSONファイル（`docs/data/news.json`）
- フレームワーク不使用、バニラHTML/CSS/JS

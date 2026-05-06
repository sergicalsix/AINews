# AI News

AI/LLM に関する最新ニュースを 4 カテゴリ（日本 / 海外 / 企業ブログ / arXiv）で日次キュレーションする静的サイトです。

## サイト

**https://sergicalsix.github.io/AINews/**

GitHub Pages で公開しており、`main` ブランチ更新時に自動デプロイされます。

## カテゴリ

| カテゴリ | 説明 |
|---------|------|
| japan | 日本国内の AI/LLM ニュース |
| international | 海外の AI/LLM ニュース |
| company_blog | OpenAI, Anthropic, Google, DeepMind, Microsoft, Cohere, Qwen, Alibaba, Meta AI 等の公式ブログ |
| arxiv | arXiv の AI/LLM 関連論文 |

## プロジェクト構成

```
docs/                        GitHub Pages 公開ディレクトリ
  index.html                 メインページ
  css/style.css              スタイル
  js/app.js                  ニュース表示ロジック
  data/news.json             ニュースデータ
prompts/                     リサーチ用プロンプト
  research-all.md            全カテゴリ一括調査
  research-japan.md          日本
  research-international.md  海外
  research-company-blogs.md  企業ブログ
  research-arxiv.md          arXiv
scripts/
  validate_and_merge.py      記事の日付検証・マージ
  blocklist.json             古いニュース URL のブロックリスト
```

## ニュースの更新手順

`prompts/research-all.md` に従って各カテゴリを調査し、`/tmp/new_articles.json` に保存してから検証スクリプトでマージします。

```bash
python3 scripts/validate_and_merge.py --new-articles /tmp/new_articles.json

# 検証のみ（書き込みなし）
python3 scripts/validate_and_merge.py --new-articles /tmp/new_articles.json --dry-run
```

検証内容:
- 日付が過去 14 日以内
- 未来日付でない
- ブロックリスト (`scripts/blocklist.json`) に含まれていない
- URL 重複がない
- 必須フィールドが揃っている

## 開発メモ

- フレームワーク不使用（バニラ HTML / CSS / JS）
- ニュースデータは静的 JSON ファイル (`docs/data/news.json`)
- GitHub Pages は `docs/` ディレクトリから配信

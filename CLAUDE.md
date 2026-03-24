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
```

## ニュース更新手順

ニュースデータを更新するには、`prompts/research-all.md` の手順に従ってください。

各カテゴリのプロンプトを使い、WebSearchとWebFetchで最新ニュースを調査し、
結果を `docs/data/news.json` に統合保存します。

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

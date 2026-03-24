# AI News 全カテゴリ一括調査プロンプト

このプロンプトは、Claude Codeで全カテゴリのAI/LLMニュースを一括調査するためのものです。

## 実行方法

Claude Codeで以下のように実行してください：

```
claude "prompts/research-all.md の手順に従って、最新のAI/LLMニュースを調査し、docs/data/news.json を更新してください"
```

## 調査手順

### 1. 日本のAI/LLMニュース
- prompts/research-japan.md の手順に従って調査

### 2. 海外のAI/LLMニュース
- prompts/research-international.md の手順に従って調査

### 3. AI企業ブログ
- prompts/research-company-blogs.md の手順に従って調査

### 4. arXiv論文
- prompts/research-arxiv.md の手順に従って調査

## 統合手順

1. 全カテゴリの調査結果を統合
2. 日付の新しい順にソート
3. 以下の形式で `docs/data/news.json` に保存:

```json
{
  "lastUpdated": "YYYY-MM-DD HH:MM (JST)",
  "articles": [
    {
      "title": "...",
      "title_ja": "...(あれば)",
      "source": "...",
      "url": "...",
      "date": "YYYY-MM-DD",
      "summary": "日本語要約",
      "authors": "...(arXivの場合)",
      "category": "japan|international|company_blog|arxiv"
    }
  ]
}
```

4. 変更をコミットしてプッシュ:
```bash
git add docs/data/news.json
git commit -m "Update AI news data - YYYY-MM-DD"
git push
```

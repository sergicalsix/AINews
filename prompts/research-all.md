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

## 日付検証（重要）

**リサーチエージェントは古いニュースを誤って最新と報告することがある。必ず以下を確認：**

1. 各記事の日付が **過去14日以内** であること
2. 記事URLの内容を確認し、日付が実際の公開日と一致すること
3. 過去に大きく話題になった製品発表（例: Llama 4, GPT-5等）は、今回が初出か再報道かを確認
4. 不明な場合は記事を除外する（誤報より欠落の方がまし）

## 統合手順

1. 全カテゴリの調査結果を一時ファイル `/tmp/new_articles.json` にJSON配列で保存
2. 検証スクリプトを実行:
```bash
python3 scripts/validate_and_merge.py --new-articles /tmp/new_articles.json
```
3. スクリプトが自動で以下を実施:
   - 日付が14日以内か検証
   - 未来日付を拒否
   - ブロックリスト照合（`scripts/blocklist.json`）
   - URL重複排除
   - 日付降順ソート
   - `docs/data/news.json` に保存

4. 拒否された記事がある場合は内容を確認し、問題なければブロックリストを更新

5. 変更をコミットしてプッシュ:
```bash
git add docs/data/news.json scripts/blocklist.json
git commit -m "Update AI news data - YYYY-MM-DD"
git push
```

## データ形式

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

# AI企業ブログ調査プロンプト

以下の主要AI企業のブログから最新記事を調査してください。

## 調査対象ブログ
| 企業 | URL |
|------|-----|
| OpenAI | https://openai.com/blog |
| Anthropic | https://anthropic.com/news, https://anthropic.com/research |
| Google AI | https://blog.google/technology/ai/ |
| DeepMind | https://deepmind.google/discover/blog/ |
| Microsoft | https://blogs.microsoft.com/ai/ |
| Cohere | https://cohere.com/blog |
| Qwen | https://qwenlm.github.io/blog/ |
| Alibaba Cloud AI | https://www.alibabacloud.com/blog (AIカテゴリ) |
| Meta AI | https://ai.meta.com/blog/ |

## 調査手順
1. 各ブログのRSSフィードまたはブログページをWebFetchで取得
2. 過去1週間の新規記事を特定
3. 各記事の概要を日本語で要約

## 出力形式
```json
{
  "title": "記事タイトル",
  "source": "企業名",
  "url": "記事URL",
  "date": "YYYY-MM-DD",
  "summary": "日本語での2-3文の要約",
  "category": "company_blog"
}
```

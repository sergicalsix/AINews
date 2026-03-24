# 海外AI/LLMニュース調査プロンプト

以下の手順で海外のAI/LLMニュースを調査してください。

## 調査対象
- 主要AIモデルのリリース・アップデート
- AI業界の資金調達・M&A・パートナーシップ
- 各国のAI規制動向（EU AI Act, 米国AI規制等）
- AI研究の重要なブレークスルー

## 検索キーワード
- 「AI LLM news this week」
- 「latest AI model release 2026」
- 「AI industry news」
- 「AI regulation update」

## 出力形式
各ニュースについて以下のJSON形式で出力:
```json
{
  "title": "英語タイトル",
  "source": "情報源",
  "url": "URL",
  "date": "YYYY-MM-DD",
  "summary": "日本語での2-3文の要約",
  "category": "international"
}
```

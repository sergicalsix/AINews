# 日本のAI/LLMニュース調査プロンプト

以下の手順で日本国内のAI/LLMニュースを調査してください。

## 調査対象
- 日本企業のAI/LLM開発動向（NTT, Preferred Networks, ABEJA, Sakana AI, Stockmark, リクルート, LINE/LY Corporation, サイバーエージェント, ELYZA等）
- 政府のAI政策・規制動向
- 日本語LLMの新規リリース・アップデート
- 国内AI関連のスタートアップ動向・資金調達
- 7min.ai（https://7min.ai/）のAIニュースキュレーション

## 参考サイト
| サイト | URL |
|--------|-----|
| 7min.ai | https://7min.ai/ |

## 検索キーワード
- 「日本 AI LLM 最新ニュース」
- 「国内 大規模言語モデル 開発」
- 「Japan AI policy 2026」
- 「Japanese LLM release」

## 出力形式
各ニュースについて以下のJSON形式で出力:
```json
{
  "title": "英語タイトル",
  "title_ja": "日本語タイトル",
  "source": "情報源",
  "url": "URL",
  "date": "YYYY-MM-DD",
  "summary": "日本語での2-3文の要約",
  "category": "japan"
}
```

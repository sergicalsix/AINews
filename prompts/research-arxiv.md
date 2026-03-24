# arXiv AI/LLM論文調査プロンプト

arXivで公開された最新のAI/LLM関連論文を調査してください。

## 調査対象
- 大規模言語モデル（LLM）に関する論文
- マルチモーダルAIの論文
- AIの安全性・アライメント研究
- 効率的な学習・推論手法
- 主要ラボ（OpenAI, Anthropic, Google, DeepMind, Meta AI等）からの論文

## 検索方法
1. WebSearchで「arxiv LLM paper this week」等を検索
2. arXiv csカテゴリ（cs.CL, cs.AI, cs.LG）の新着を確認
3. Papers With Codeのトレンドを確認

## 検索キーワード
- 「arxiv LLM 2026」
- 「arxiv large language model new paper」
- 「arxiv AI alignment safety」
- 「arxiv multimodal model」

## 出力形式
```json
{
  "title": "論文タイトル",
  "source": "arXiv",
  "url": "https://arxiv.org/abs/XXXX.XXXXX",
  "date": "YYYY-MM-DD",
  "authors": "著者1, 著者2, ...",
  "summary": "日本語での2-3文の要約",
  "category": "arxiv"
}
```

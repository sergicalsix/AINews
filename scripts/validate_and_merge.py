#!/usr/bin/env python3
"""
AI News データ検証・マージスクリプト

新しい記事を news.json に追加する前に以下を検証:
1. 日付が調査対象期間内か（デフォルト: 過去14日以内）
2. 未来の日付でないか
3. URL重複がないか
4. 既知の古いニュースURLでないか
5. 必須フィールドが揃っているか

使い方:
  python3 scripts/validate_and_merge.py --new-articles new.json
  python3 scripts/validate_and_merge.py --new-articles new.json --max-age-days 7
  python3 scripts/validate_and_merge.py --new-articles new.json --dry-run
"""

import json
import sys
import argparse
from datetime import datetime, timedelta
from pathlib import Path

NEWS_JSON = Path(__file__).parent.parent / "docs" / "data" / "news.json"
BLOCKLIST_FILE = Path(__file__).parent / "blocklist.json"

REQUIRED_FIELDS = ["title", "source", "url", "date", "summary", "category"]
VALID_CATEGORIES = {"japan", "international", "company_blog", "arxiv"}


def load_blocklist():
    """既知の古いニュースURLのブロックリストを読み込む"""
    if BLOCKLIST_FILE.exists():
        with open(BLOCKLIST_FILE) as f:
            return set(json.load(f))
    return set()


def validate_article(article, max_age_days, today, blocklist):
    """記事を検証し、(is_valid, errors) を返す"""
    errors = []

    # 必須フィールドチェック
    for field in REQUIRED_FIELDS:
        if field not in article or not article[field]:
            errors.append(f"必須フィールド '{field}' が不足")

    if errors:
        return False, errors

    # カテゴリチェック
    if article["category"] not in VALID_CATEGORIES:
        errors.append(f"無効なカテゴリ: {article['category']}")

    # 日付パース
    try:
        article_date = datetime.strptime(article["date"], "%Y-%m-%d").date()
    except ValueError:
        errors.append(f"日付形式が不正: {article['date']} (YYYY-MM-DD)")
        return False, errors

    # 未来日付チェック（1日の余裕）
    if article_date > today + timedelta(days=1):
        errors.append(f"未来の日付: {article['date']}")

    # 古い記事チェック
    age = (today - article_date).days
    if age > max_age_days:
        errors.append(f"記事が古すぎる: {article['date']} ({age}日前, 上限{max_age_days}日)")

    # ブロックリストチェック
    if article["url"] in blocklist:
        errors.append(f"ブロックリストに含まれるURL: {article['url']}")

    # URLの基本チェック
    if not article["url"].startswith("http"):
        errors.append(f"無効なURL: {article['url']}")

    return len(errors) == 0, errors


def merge_articles(existing, new_valid, max_total=200):
    """既存記事と新規記事をマージ（URL重複排除、日付降順ソート）"""
    existing_urls = {a["url"] for a in existing}
    added = 0

    for article in new_valid:
        if article["url"] not in existing_urls:
            existing.append(article)
            existing_urls.add(article["url"])
            added += 1

    # 日付降順ソート
    existing.sort(key=lambda a: a["date"], reverse=True)

    # 古い記事を削除して上限を維持
    if len(existing) > max_total:
        removed = len(existing) - max_total
        existing = existing[:max_total]
        print(f"  古い記事 {removed} 件を削除（上限 {max_total} 件）")

    return existing, added


def main():
    parser = argparse.ArgumentParser(description="AI News 検証・マージスクリプト")
    parser.add_argument("--new-articles", required=True, help="新規記事のJSONファイル")
    parser.add_argument("--max-age-days", type=int, default=14, help="最大記事年齢（日数、デフォルト14）")
    parser.add_argument("--max-total", type=int, default=200, help="保持する最大記事数（デフォルト200）")
    parser.add_argument("--dry-run", action="store_true", help="検証のみ、書き込みなし")
    parser.add_argument("--today", help="今日の日付 (YYYY-MM-DD)、テスト用")
    args = parser.parse_args()

    today = datetime.strptime(args.today, "%Y-%m-%d").date() if args.today else datetime.now().date()
    blocklist = load_blocklist()

    # 新規記事を読み込み
    with open(args.new_articles) as f:
        new_articles = json.load(f)

    if not isinstance(new_articles, list):
        print("エラー: 新規記事ファイルはJSON配列である必要があります")
        sys.exit(1)

    print(f"=== AI News 検証 ({today}) ===")
    print(f"新規記事: {len(new_articles)} 件")
    print(f"最大年齢: {args.max_age_days} 日")
    print()

    # 検証
    valid = []
    rejected = []
    for i, article in enumerate(new_articles):
        is_valid, errors = validate_article(article, args.max_age_days, today, blocklist)
        title = article.get("title", f"(記事 {i+1})")
        if is_valid:
            valid.append(article)
            print(f"  ✓ {title}")
        else:
            rejected.append((title, errors))
            print(f"  ✗ {title}")
            for e in errors:
                print(f"    → {e}")

    print()
    print(f"検証結果: {len(valid)} 件合格 / {len(rejected)} 件拒否")

    if rejected:
        print()
        print("=== 拒否された記事 ===")
        for title, errors in rejected:
            print(f"  {title}: {'; '.join(errors)}")

    if args.dry_run:
        print()
        print("(ドライラン: 書き込みなし)")
        sys.exit(0 if not rejected else 1)

    if not valid:
        print("追加する記事がありません。")
        sys.exit(0)

    # 既存データを読み込みマージ
    with open(NEWS_JSON) as f:
        data = json.load(f)

    data["articles"], added = merge_articles(data["articles"], valid, args.max_total)
    data["lastUpdated"] = today.strftime("%Y-%m-%d") + " 09:00 (JST)"

    with open(NEWS_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    cats = {}
    for a in data["articles"]:
        cats[a["category"]] = cats.get(a["category"], 0) + 1

    print()
    print(f"=== マージ完了 ===")
    print(f"新規追加: {added} 件（URL重複除外済み）")
    print(f"合計: {len(data['articles'])} 件")
    for k, v in sorted(cats.items()):
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()

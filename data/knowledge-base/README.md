# DELIPIT Knowledge Foundation v0.1

基準日：2026-11-01。研究用の正本で、公開記事ではありません。

- `topics.json`：12分野120疑問。限定した結論、状態、適用区分、例外、地域差、根拠、公表日、施行日、確認日、不明点、既存記事対応、次回確認、履歴。
- `sources.json`：65資料。行政・Google・SORA本人記事・製品ガイド等を区分。本文未取得のe-GovはUNREADABLE。
- `editorial-plan.json`：12候補の見出し計画。第1群6本から検討。既存URLの拡充を優先。

全レコード `article_ready=false`。VERIFIEDは根拠確認の区分で、法的な個別適用判断・記事の完成・SORA Acceptanceではありません。本文を自動生成して公開する用途に使わないでください。

検証・期限キュー（読み取りのみ）：

```bash
python scripts/validate_knowledge_base.py --as-of 2026-11-01
```

台帳更新時は該当レコードのhistoryに日付・根拠・変更理由を追記し、関連出典の依存Q-IDと記事を点検します。自動通知・定期実行は設定していません。

報告書：`docs/knowledge-foundation-20261101/DELIPIT_KNOWLEDGE_REPORT_20261101.md`

# DELIPIT公式サイト V1.2.0 隔離候補 Checkpoint

作業日: 2026-10-27（JST）

## Baselineと保護範囲

- 公式サイト: `kaila3824-cyber/delipit-official` の `main`、`01f0bfa3964d3457b7edb19234362237d39cd55c`。作業開始と候補保存前の `ls-remote` で同一。
- 本候補は `develop/official-v120-renewal-20261027`。Production `delipit.jp`、アプリ `app.delipit.jp`、SAFEのソース・保存データ・配信設定には変更しない。
- 既存のSAFE紹介、NEWS/DRIVER NOTE、Privacy、Terms、運営情報、問い合わせフォームとWeb3Forms設定、AdSense識別子、robots、favicon、既存URLを維持。

## 変更

- `index.html`: V1.2.0のコピー、無料利用CTA、委託先・4報酬方式・荷物種別・集計・GAME・初回利用・新NEWS、Title/description/OG/Xの更新。既存2製品ハブを維持。
- `delipit.html`, `gamification.html`, `quickstart.html`, `manual.html`: V1.2.0説明を追加し、古いバージョン限定表現を修正。既存画像は過去撮影の画面として扱う。
- `news-v120.html`: 2026-10-27付の新記事。アプリ公開日と記事掲載日を明示。
- `sitemap.xml`: 新記事URLを追加。旧記事は維持。
- 追加アセットなし。正式ロゴと既存画像を再利用。架空のV1.2.0画面は掲載しない。

## 確認

- `node --test tests/*.mjs`: 4/4 PASS（最終編集後に再実行）。
- `python3 scripts/check_site_links.py`: HTML 28、sitemap 25、内部リンク 492、問題 0。
- `git diff --check`: 問題なし。
- 既存mainとの差分は本Branchのcommitで完全保持。法令本文やフォーム送信ロジックを変更しない。

## 隔離プレビューと残る確認

- Owner-private Sites project `appgprj_6adfd6e28aa881918001d4e9d4339445`。独立URLにのみ配信。
- プレビュー配信物から広告・解析スクリプトを除外し、フォーム送信を無効化し、`noindex`とDEV表示を入れる。公式候補の本番用ソースとは区別する。
- ブラウザでTOP、NEWS、SAFE/Privacy/問い合わせ、約320pxとPC、画像・JS、Consoleを確認する。Safari実機はSORA確認待ち。
- 公式サイトProductionへはDeployしない。正式公開前にSORAの承認と現行mainとの再照合が必要。

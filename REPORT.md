# 2026-10-22 公式サイト内容監査・改善

AdSenseの所有者報告は「有用性の低いコンテンツ」。審査側の個別URL判定は取得していない。Googleの[不承認案内](https://support.google.com/adsense/answer/81904)、[Publisher Policies](https://support.google.com/adsense/answer/10502938)、[ページ準備](https://support.google.com/adsense/answer/7299563)、[Search Central](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)を基準として確認した。今回の改善が審査結果を保証するものではない。

## 公開URL別監査

2026-10-22にChromeで公開ページの見出し・本文・canonicalを確認。ソース上のHTML27件のうちsitemap掲載24件。`quickstart.html`は独立した短い導入ページだがcanonicalは`manual.html`で、sitemapには掲載しない。`safe-terms.html`と`safe-privacy.html`は公開中の未施行案内で`noindex`、Draft PR #9の正式候補を公開したものではない。`safe-information.html`は案内・FAQがある。Search Consoleのドメインプロパティを確認し、ページ登録レポートは登録済み18・未登録4（最終更新表示2026-10-11）。未登録内訳は「クロール済み・未登録」1（`driver-note-09.html`、前回クロール2026-10-13）、リダイレクト2、代替canonical1。個別URLがAdSenseの不承認対象と判定された証拠ではない。

| URL | 確認した内容・判断 | 今回の変更 |
| --- | --- | --- |
| `/`、`/delipit.html` | 製品の区別と実機画面・機能説明あり。記録から振り返りへの具体的導線は弱い | 現場ガイドへの内部リンク |
| `/manual.html`、`/quickstart.html` | 操作説明あり。quickstartは約450字の短い導入でmanualへcanonical | 日次から年次の利用例へのリンク。canonical維持 |
| `/gamification.html`、`/pitcrew.html` | GAMEとキャラクターの説明あり。旧TOPの存在しない`#story`、`#features`へ移動するリンク | `delipit.html`の存在するアンカーへ修正 |
| `/driver-note.html`、`/driver-note-01.html`～`/driver-note-10.html` | 一覧と現役ドライバーの固有体験の記事。#01～#08は比較的短いが単なるnoteリンク集ではない。#09/#10はより詳細 | 大量記事生成・転載はせず、#03/#09を新ガイドから参照 |
| `/driver-news.html` | 公的一次資料に仕事上の確認ポイントを加えた説明、更新機構あり | 生成器・GitHub Actionsは変更なし |
| `/safe.html`、`/safe-guide.html`、`/safe-information.html` | SAFEは公開テスト中である旨を表示。DELIPITとは用途が別 | `safe-information.html`の現行Privacy内アンカー3件を修正。本文・同意状態は変更なし |
| `/safe-terms.html`、`/safe-privacy.html` | 未施行案内・noindex。正式候補はDraft PR #9で管理 | 変更なし |
| `/terms.html`、`/privacy.html`、`/operator-disclosure.html` | DELIPITの規約・Privacy、請求窓口を確認 | 変更なし |
| `/field-workflow.html` | 新規。実体験とDELIPIT V1.0.0の操作を結ぶ現場ガイド | 追加、sitemapに掲載 |

新ガイドは提供された実体験（2024年2月開始、約80個から100個目標、2025年8月の現場移行、200個超・最多280個）と、公開マニュアル上の画面・操作を分けて記載した。配送先・会社・顧客情報、架空レビュー、実在しない機能を記載しない。日次・月次・年次の確認、売上と入金・経費の区別、任意のGAME MODE、SAFEとの役割差、端末保存とBackupを扱う。

## 技術確認・公開判定

- 既存フォーム自動テスト4/4 PASS。追加のローカルリンク・アンカー・title/description/h1・sitemap/canonical検査：HTML27、内部リンク484、sitemap24、問題0。初回監査では存在しないアンカーが7件あり、修正後に0件。
- 隔離Chromeで新ガイドの本文、見出し、画面幅、`manual.html#year`への遷移を確認。iPhone/Android実機および狭いviewportのブラウザ検証は未実施。実機PASSとは扱わない。
- Production全掲載URLのHTTPステータス網羅取得とAdSense審査の対象URLは未確認。Search Consoleのインデックスレポートは古い時点の集計で、公開した新ガイドの検出・登録は未確認。公開時には新ページ・sitemapと内部リンクを再確認する。
- SAFE Production V94およびDraft PR #9、同意要求、GA4、DELIPITアプリ本体・広告設定は変更しない。AdSense再審査は所有者判断とし、自動申請しない。

## 公開結果（2026-10-22 UTC）

専用PR #10をsquash mergeし、main `31af9305db824963d77bdaab631566bf82ada619` に反映。GitHub Pages build run `39722512710` は2026-10-22 04:28:44 UTCに成功。公開Chromeで `https://delipit.jp/field-workflow.html` の全文、正規TOP `/` からの新ガイドリンク、公開 `sitemap.xml` への登録を確認。初回404はビルド進行中で、完了後に解消。モバイル実機と新ガイドのSearch Consoleでの検出/索引状態は未確認、AdSense再審査は未実施。Search Consoleに送信済みの `https://delipit.jp/sitemap.xml` は「成功」、最終読み込み表示2026-10-16、検出18件。公開sitemapの24 URLへの更新はまだ同レポートに反映されていない。

## 最終QA・再審査ゲート（2026-10-22 UTC）

- 最新main `e615fba42e8e66e93b1e3e6f18166598a9dd7621` を再取得。公開TOP・製品紹介・マニュアル・クイックスタート・新ガイドをChrome通常幅（1363 CSS px）で表示し、タイトル・本文、表示幅、ナビゲーションを確認。各ページのdocument幅は1348pxで通常幅の横あふれなし。クイックスタートから新ガイドへの実遷移成功。画面外の遅延画像の未読込は破損と判定しない。
- 狭幅の実Browser QAは未完了。Cloud Browserはviewport変更APIを提供せず、隔離ローカルページへの接続は拒否。data URLの検証枠はブラウザのURLポリシーで拒否されたため再試行しない。ローカルPlaywrightのChromium実体もなく取得に失敗。5ページの`viewport`宣言と狭幅CSS規則をソースで確認したが、320～390pxでの横スクロール・文字や画像のはみ出し・可読性はPASSとしない。狭幅実機または正規のviewport制御可能なBrowser QAが必要。
- `python3 scripts/check_site_links.py`：HTML27、sitemap24、内部リンク484、問題0。`node --test tests/operator-disclosure.test.mjs`：4/4 PASS、FAIL/SKIP 0。狭幅で再現した不具合はなく、コード修正・再Deployなし。
- 公開 `https://delipit.jp/sitemap.xml` に `https://delipit.jp/field-workflow.html` とlastmod `2026-10-22` が存在。Search Consoleの同URL検査は「URL が Google に登録されていません」「URL が Google に認識されていません」、参照元sitemap未検出、クロールなし。ライブテストは「URL は Google に登録できます」「ページをインデックスに登録可能」。ライブ可用性は実際の検出・登録ではない。既存sitemap送信は成功だが最終読込10/16・検出18の旧状態で、公開24 URLへの更新は未反映。
- AdSense対策の実施済み：開発者の配送経験と実際のDELIPIT操作に基づく新ガイド、TOP・製品・マニュアル・クイックスタートの導線、誤アンカー修正、公開sitemap登録。未確認：Googleの個別不承認URL、狭幅実Browser QA、新ガイドの検出・インデックス。残留リスク：Google側のサイト全体評価・審査結果は制御できない。再審査申請は所有者判断まで保留。SAFE V94・未公開99・Draft PR #9・正式同意OFF・GA4 OFFには変更なし。

# DELIPIT公式サイト V1.2.0 隔離DEV REPORT

作業日: 2026-10-27（JST）
判定: DEV READY / AWAITING SORA ACCEPTANCE

## 回収とGit保全

- 前回Candidateは `/workspace/scratch/67884a320c1a/official-audit` に未コミット差分6ファイルと新規 `news-v120.html` として存在。欠落ファイルなし。
- commit前にソースtar、完全な既存差分patch、新NEWS単体を退避。Local commit `6866922809a0ed19f75e5586e4f561e84800789f`。
- 正式ソースRepository `kaila3824-cyber/delipit-official`。Production `main` は作業開始・保存時とも `01f0bfa3964d3457b7edb19234362237d39cd55c`。
- GitHub Branch `develop/official-v120-renewal-20261027`、remote commit `1efdb55edf677d27dae92eb15b46d40d042c60ab`。直接push認証不可のためGitHub APIから同一Git tree `ab81fab2ac25618ef639705c78ebcaa9b57461af` を保存。mainは更新なし。
- リモートからfetchし、独立Checkout `official-verify` へ展開。全追跡ファイル（ソース・NEWS・既存アセット・テスト含む）のSHA-256一致。localとremoteのtreeも一致。

## 変更と保護

- TOP: 正式ロゴ、V1.2.0の価値、無料CTA、複数委託先、4報酬方式、荷物種別の追加、導入手順、新NEWSを追加。GAMEは配送個数基準、OFFでも配送管理可能と記載。
- DELIPIT製品紹介・GAME・Quick Start・Manualを更新。既存の画像は過去撮影の画面として区別。架空画面なし。
- 新記事 `news-v120.html`、sitemap追加。既存記事とURLを維持。既存SAFE、Privacy/Terms、運営情報、問い合わせの本文・送信ロジック、AdSense設定は変更していない。
- 変更対象: `index.html`, `delipit.html`, `gamification.html`, `quickstart.html`, `manual.html`, `news-v120.html`, `sitemap.xml`, Checkpoint、本REPORT。追加画像なし。

## 隔離配信

- URL: https://delipit-official-v120-review-20261027.inthesky08.chatgpt.site
- Siteは所有者1名だけのcustom access。Productionとは別オリジン、別Gitと別配信。
- Private Site version 2、deployment `appgdep_6adfd9d466008191bd78efe99a7d7a44`、preview source commit `aaf1e24bcd78b25ce4db31c2d7a7907090c43134`。
- 配信Archive: `official-preview-v120-candidate-final.tar.gz`、gzip SHA-256 `58d8511bcb1b7e2e7f9de71269c0b5daebc67fa52197e3e70cfa6c9be8d6114b`。Sites保存版のcontent hash `sha256:7b3d56fc4d1b0f3a22d865fa728ec9e8c86c513986b587c3dac6c30b0c759ed9`（サービス側のarchive hash。gzipファイル自体のhashとは別）。展開した配信Archiveとpreview sourceの全公開ファイルは一致（追加の `.openai/hosting.json` を除く）。index HTML SHA-256 `022d1feb75007c1188e109fa26ec453bfd82ba4999d5fd3276596060bfb0716a`、NEWS HTML `49a34beb8697d748466bcca195fcfbdcea5e8706ad3bb98f02cab11f00d44f82`。
- Previewは元Candidateから生成し、広告/Analytics外部Scriptを除去、フォーム送信を無効化、全35 HTMLにnoindexのみ設定、robots.txtで全パス拒否、DEV表示。公式サイト向けソースと区別。

## QA

- リモート復元Checkoutで `node --test tests/*.mjs`: 4/4 PASS。
- `python3 scripts/check_site_links.py`: HTML 28、sitemap 25、内部リンク492、問題0。
- PCブラウザ: TOP/正規ロゴ/CTA/新NEWS/既存DRIVER NEWS/SAFE/Privacy/問い合わせ導線、画像読み込み、横はみ出しなしを確認。表示したページで失敗画像0。ブラウザコンソールにはブラウザ拡張機能由来のmetadata errorのみ。アプリページ由来の重大エラーは検出せず。
- SEO: 正式候補のTitle/description/OG/X、canonical、favicon、sitemapを確認。隔離版はnoindex。AdSenseは正式ソースの識別子と既存Scriptを維持し、隔離版では発火しない。

## OPEN / 実機Acceptance

- 約320pxの実表示、iPhone Safariの縦スクロール・タップ・メニュー・NEWS・SAFE/Privacy/問い合わせ表示。WorkのPCブラウザと静的CSS確認で実機PASSにはしない。
- SORA: iPhone Safariで上記URLを開き、TOPのロゴと主要CTA、機能紹介、NEWS、SAFE/Privacy、メニュー、320px相当の狭幅で横スクロールや文字切れがないことを確認。問い合わせフォームは隔離版では送信しない。
- 本番公式サイトへの公開は別途承認待ち。公開時は最新mainとの再照合を行い、候補のみを移植する。Productionとアプリ本体は今回変更なし。

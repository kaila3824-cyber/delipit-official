# DELIPIT公式サイト V1.2.0 — Production Release記録

作業日: 2026-10-27（JST）
状態: **DEPLOYED / RELEASE CLOSE PENDING**

## 公開・ソース

- SORAの公式サイトProduction公開承認を受け、GitHub Pagesの`main`を承認済み機能Candidate `8998dbfb2fec8ca5a150279566e5c77dd0c17b57`へ更新。公開対象は`https://delipit.jp/`のみ。DELIPITアプリ、SAFEアプリ、実ユーザーデータは変更していない。
- 公開前`main`: `01f0bfa3964d3457b7edb19234362237d39cd55c`。復旧Branch `rollback/official-pre-v120-20261027`で保持。旧ソースArchive `official-production-baseline-01f0bfa.tar` SHA-256 `68e4244f954a249c67cc3f7dd50d59521203639b5a18aa6ccd2113516ffcf8f5`（158ファイル照合）。
- GitHub Pages build/deploy run `40419113935`は成功。Deployment ID `7346055078`、成功status 2026-10-26 23:21:49 UTC。Deployment作成時刻 2026-10-27 **08:21:17 JST**。公開URLでの新TOP・新NEWS反映をその後確認。
- GitHub Pages配信Artifact `github-pages`（ID `12697371376`）のGitHub提示digest: SHA-256 `4b1cfd858b7d37d2de77687e7bd931d58ef346352fbd9009f5445c68a7b241b3`。Build runのHEADは公開commit `8998dbf`。ローカルCandidateソースArchive `official-v120-candidate-8998dbf.tar.gz` SHA-256 `aeb6c549d5f8614ebc6ce84d2d5e6025330a845b710719b78a996d6ce15a7422`（161ファイル照合）。両者は別のArchive。
- 配信HTML/XML/TXT **47/47ファイル**を公開URLから取得し、公開commitのファイルとSHA-256一致。主要ロゴ・SAFE画像2点も一致。GitHub Pages配信のため「Sites版」は該当しない。公式サイト上の紹介対象はアプリ **V1.2.0**。
- 公開機能差分: `index.html`, `delipit.html`, `gamification.html`, `manual.html`, `quickstart.html`, `sitemap.xml`, 新規`news-v120.html`。削除0。候補の記録文書はGitに含まれるが配信ページの機能差分ではない。

## Acceptance・公開後Smoke

- SORA申告による**隔離DEV** iPhone Safari Acceptance: 8/8 PASS。Production実機結果としては流用しない。
- 公開ソースでNode既存テスト: **4/4 PASS**。リンク検査: HTML28、sitemap25、内部リンク492、問題0。公開後に再実行。
- WorkのProduction PCブラウザ: TOP、黒×ゴールドとロゴ、無料CTAのリンク先`https://app.delipit.jp/`、複数委託先、4報酬方式、GAME案内、新NEWS、DRIVER NEWS、SAFE、Privacy、問い合わせフォームと選択肢を表示確認。無料CTAのリンク先を読み取り、アプリ側の保存操作は実施していない。サイト由来の重大Console Errorなし。ブラウザ拡張由来のmetadata errorは観測したがサイトの例外とは区別。
- 公開47ファイルと公開commitの一致により、旧NEWS・SAFE関連ページ、利用規約、運営者情報、robots、sitemap、ads.txt、既存URLを含め配信資材を確認。ページのcanonicalとOGPをTOPおよび新NEWSで確認。TOPに`noindex`やDEV表示はなく、`robots`はindex,follow。画像は主要ページで表示、SAFEの画面外画像は遅延読込であり、主要画像の公開ファイルとソースのハッシュが一致。
- `ads.txt`と既存AdSense識別子・Scriptの配信を確認。現行ソースに存在しなかったGA4/GTM、CMP設定は追加していない。AdSense、CMP、GA4、Search Console各管理画面の状態や広告実配信は今回確認できていない。
- 問い合わせフォームの表示とWeb3Forms送信コードの保持を確認。**実送信・メール受信は未確認**。ProductionでのiPhone Safari表示、ナビゲーション、横スクロール等はSORA実機Acceptance待ち。WorkのPC表示を実機PASSとしない。

## Release Close条件とOPEN

Production Deploy、ソース・Build・公開ファイルの対応、自動テスト、PC Smoke、既存ページとソース上の設定保護はPASS。公開後Production iPhone実機Acceptanceと問い合わせ実送信・受信が未完了のため、**Release Closeは未確定**。重大な公開障害は今回の確認範囲で検出されていない。

SORA確認待ち: ①iPhone SafariのTOP、ロゴ・デザイン、無料CTA、新旧NEWS、SAFE・Privacy、メニュー・縦スクロール、横スクロールと文字切れ、②問い合わせ実送信と受信。AdSense管理画面の状態、必要に応じてSearch Consoleのsitemapも別途確認対象。未確認をPASSにしない。

## 障害時復旧

影響と公開後差分を調査し、問題のある配信操作を止める。Gitの復旧Branchと旧Production Archiveを基準に、必要な公開後NEWS・設定を保護した修正commitで**公式サイトのみ**再配信する。mainの強制pushやアプリ本体のRollback、データMigration・Restoreは行わない。復旧後も公開URL、配信ファイル、問い合わせ導線、SEO設定を確認する。

次回再開地点: SORAからProduction iPhone Acceptanceと問い合わせ送受信結果を受け、OPENを更新しRelease Close条件を再判定する。

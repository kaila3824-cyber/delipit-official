# DELIPIT公式サイト V1.2.0 — Production Release記録

作業日: 2026-10-27（JST）
状態: **RELEASE CLOSED / POST-LAUNCH OPERATION**（公開直後のPENDING記録は下記に保持）

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

## Release Close（2026-10-27 JST）

**DELIPIT OFFICIAL WEBSITE V1.2.0 — RELEASE CLOSED / POST-LAUNCH OPERATION**。この節は上記「RELEASE CLOSE PENDING」時点の記録を更新する。SORA申告のProduction iPhone Safari実機Acceptanceと問い合わせ送受信が完了し、確認した範囲で新たな重大Release Blockerはない。アプリ本体、SAFEアプリ、実ユーザーデータ、公式サイトの公開コードはこのClose処理で変更していない。

SORA申告による**Production公開後**iPhone Safari Acceptance（操作ログ・画面証跡・個別測定値は未提供）:

1. TOPのロゴ・デザイン: PASS
2. 「無料で使う」からDELIPITアプリ起動: PASS
3. V1.2.0新NEWS表示: PASS
4. 過去NEWS・SAFE・Privacy表示: PASS
5. メニュー・縦スクロール・表示幅: PASS
6. 問い合わせフォームのテスト送信: PASS
7. info@delipit.jpでテストメール受信: PASS

**7 PASS / 0 FAIL / 0 OPEN**。隔離DEVのSORA実機Acceptance **8/8 PASS**、WorkのPCブラウザ確認、自動テストとは独立した根拠として保持する。送信・受信はSORAの申告に基づき、Workがメール内容や受信ログを閲覧したという意味ではない。

公開時のGit commit `8998dbfb2fec8ca5a150279566e5c77dd0c17b57`、GitHub Pages Deployment `7346055078`、作成時刻2026-10-27 08:21:17 JST、配信Artifact SHA-256 `4b1cfd858b7d37d2de77687e7bd931d58ef346352fbd9009f5445c68a7b241b3`は上記公開記録のとおり。配信47/47、Node 4/4、内部リンク492件問題0、主要ページSmokeと重大なサイト由来Console Errorなしの結果を引き継ぐ。GitHub Pages配信なのでSites版は該当しない。

Close時点の`main` HEADは `b75db06821eb8582b63c41984aae85acb1b6eaaf`。公開時commitからの後続差分は自動生成 `data/driver-news.json` の`generatedAt`が2026-10-27 01:09:30 JSTから09:28:52 JSTへ変わった1箇所のみ。記事項目やV1.2.0改修ファイルは変わっていない。公開JSONと当該HEADのrawファイルのSHA-256はともに `0a81c8fc0652e62880645c0403b8f709cbafd32fc5672eb260d68cfcfb5b7026`。公開時のArtifact digestは当該後続更新後のArtifact digestを表すものではない。

保全済み: AdSense識別子・Script、`ads.txt`、`robots.txt`、`sitemap.xml`、canonical・OGP、Privacy、運営者情報、既存NEWS、SAFE紹介、問い合わせフォーム。ProductionのTOPにDEV表示・noindexはなく、隔離DEVの広告・問い合わせ停止設定は公開Candidateに混入していない。これらは公開ソース・配信内容の確認範囲であり、外部管理画面の正常動作の証明ではない。

**Post-Launch OPEN**: AdSense管理画面の審査・広告配信、CMPの管理設定・動作、GA4/GTMの計測状態、Search Consoleにおける新sitemapの処理状況は今回のCloseで再確認していない。ソース上で既存になかったGA4/GTM・CMPを追加していない。これら未確認は今回のサイト改修に起因する重大障害として観測されておらず、Release Closeとは分けて継続管理する。Androidや全利用者端末での表示も今回の7項目から一般化しない。

復旧Baselineは`01f0bfa3964d3457b7edb19234362237d39cd55c`、Branch `rollback/official-pre-v120-20261027`。障害時はまず影響と公開後更新を調べ、必要なNEWS・設定を保護したうえで公式サイトだけ修正commitを配信する。アプリ本体、SAFEアプリ、ユーザーデータは扱わない。

次期開発Baseline: GitHub Pages公式サイト`main`のその時点のHEAD（Close確認時点は`b75db0`）と本Release記録。まず安定運用と不具合監視を行い、追加改修は独立Branchで開始する。

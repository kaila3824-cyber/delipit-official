# DELIPIT公式サイト V1.2.0 — FINAL PRODUCTION RELEASE GATE

作業日: 2026-10-27（JST）  
判定: **PRODUCTION DEPLOY READY / AWAITING SORA APPROVAL**  
Production公式サイト、DELIPITアプリ、SAFEアプリ、実ユーザーデータは未変更。Deploy未実施。

## Baseline・保全

- Repository: `kaila3824-cyber/delipit-official`（GitHub Pages、CNAME `delipit.jp`）。最新Production `main`: `01f0bfa3964d3457b7edb19234362237d39cd55c`。候補作業中のmain更新なし。
- 公開URLからHTML/XML/TXT 46ファイルを取得し、mainの同名ファイルと全件バイト一致。公開ロゴ2点とOG画像も一致。公開トップSHA-256: `3c74146f58997a812fd8c63794318be37bca1d107f3dd1cf5df59d88ffc0d8c3`。
- 復旧Branch: `rollback/official-pre-v120-20261027` → 上記main。旧ソースArchive `official-production-baseline-01f0bfa.tar` SHA-256 `68e4244f954a249c67cc3f7dd50d59521203639b5a18aa6ccd2113516ffcf8f5`。158ファイルを元Checkoutと照合。Archiveはローカル検証資材、永続復元元はGitHub復旧Branch。
- 機能Candidate Branch: `develop/official-v120-renewal-20261027`、commit `8998dbfb2fec8ca5a150279566e5c77dd0c17b57`。別Checkoutで全追跡ファイルSHA-256一致。Candidate Archive `official-v120-candidate-8998dbf.tar.gz` SHA-256 `aeb6c549d5f8614ebc6ce84d2d5e6025330a845b710719b78a996d6ce15a7422`。161ファイルを元Checkoutと照合。

## SORA申告による隔離DEV iPhone Safari実機Acceptance

隔離DEV Sites版2の結果。Work PC確認やProduction実機確認とは区別し、未申告の操作証跡は加えない。

1. ロゴ・黒×ゴールド: PASS
2. 無料CTAからアプリ起動: PASS
3. 複数委託先・4報酬方式の説明: PASS
4. GAME SYSTEM紹介: PASS
5. 新NEWS表示: PASS
6. 既存NEWS・SAFE・Privacy: PASS
7. メニュー・縦スクロール: PASS
8. 文字切れ・横スクロール・画像はみ出しなし: PASS

**8 PASS / 0 FAIL / 0 OPEN**。

## 本番差分と設定

- Web変更: `index.html`, `delipit.html`, `gamification.html`, `manual.html`, `quickstart.html`, 新規 `news-v120.html`, `sitemap.xml`。記録文書3点。削除0、追加画像0。SAFEアプリ対象外。
- `CNAME`, `robots.txt`, `ads.txt`, `privacy.html`, `terms.html`, `operator-disclosure.html`, SAFE関連ページ、既存NEWSはmainと一致。既存URL保持。
- 正式Candidateの変更ページに`noindex`とDEV表示はない。canonicalは`delipit.jp`。新記事をsitemapへ追加。
- AdSense: 既存`ca-pub-9142850138364995`のScriptと`ads.txt`を維持。新記事にも同じScript。隔離DEVでのScript除去は正式Candidateへ混入していない。
- 問い合わせ: 既存Web3Forms送信先・access_keyフィールド・送信ロジックを維持。隔離DEVの送信停止処理は正式Candidateにない。実送信・受信は公開後SORA Acceptance。
- 現行mainのルートHTMLにGA4 `gtag`/GTM外部Script、CMP外部Scriptは確認できず、Candidateでも新設していない。外部管理画面の設定状態は今回操作・再確認していない。Search Console関連のrobots/sitemapなど既存ソース設定は保持。

## QA・公開後手順

- 別Checkoutで既存自動テスト**4/4 PASS**。リンク検査: HTML 28、sitemap 25、内部リンク492、問題0。差分チェック問題なし。
- Work PCブラウザでTOP、新NEWS、既存DRIVER NEWS、SAFE、Privacy、問い合わせ導線、画像を確認。ページ由来の重大Console Errorなし（ブラウザ拡張由来のmetadata errorは区別）。
- 次回承認後、直前のmain差分を再確認し復旧Branchを固定。Candidateをmainへ統合してGitHub Pages公開を確認。公開URLのTOP・新NEWS・既存NEWS/SAFE/Privacy・ロゴ・canonical/robots/sitemap・広告/解析設定・Consoleを確認する。問い合わせ実送信と受信、iPhone表示はSORAのProduction Acceptanceとする。
- 重大問題時は更新を止め、原因と影響を確認。旧ソースBranchを基準とした**新しい修正commit**で復旧し、再配信を検証する。mainを強制pushしない。静的サイトの復旧はアプリの保存データMigrationと独立。

## OPEN

Production公開後のiPhone表示、問い合わせ送受信、広告・解析の実動作は未確認。管理画面側のAdSense/CMP/GA4/Search Console設定は今回操作・再確認していない。ソース上の既存設定は保持。

本判定は本番公開承認ではない。SORAの別途明示承認までDeployしない。

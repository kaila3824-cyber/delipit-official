# DELIPIT OFFICIAL — AdSense final release V1.0 受入台帳

確認日：2026年11月3日（JST）。基準main：`d21c507a30df3c4e67930b4c461ff57f6983f6a4`。PR #19・#20はマージ済み、#21・#22はDraft。本台帳は `adsense-20261102-final-readiness.md` の後続であり、そこに残る「16アンカー未公開」「SAFE未施行」は解消済みの履歴として扱う。AdSense再申請は実行しない。

## 判定と証拠

**HOLD**。現時点で旧PHPの実効的HTTP転送はなく、前段の配信管理権限・設定も確認できない。Privacy／運営者情報の法的確認中事項、AdSense管理画面の最新不承認理由、CMP、Search Console、現在のフォーム送信結果も未確認。これらをPASSとみなさない。

| 対象 | 本番実測または検証 | 判定 |
| --- | --- | --- |
| `/driver-news.php` | GET/HEAD 200、`application/x-httpd-php`、Locationなし。GETは579バイトでmainとSHA-256一致。 | FAIL：HTTP転送なし |
| `/assets/driver-news.php` | GET/HEAD 200、同MIME・Locationなし。rootと同じ静的HTML。 | FAIL：HTTP転送なし |
| `/driver-news.html` | GET 200、`text/html`。sitemap掲載、旧PHPのcanonical先。 | PASS |
| PHP情報露出 | tracked `.php` は上記2件のみ。両本文にPHP開始タグ・秘密鍵マーカーなし。値をログ・文書に出力しない。 | 検査範囲で重大露出なし。サーバー上の未知のファイルは未確認 |
| 公開HTML | 35/35 GET 200、`text/html`、mainとバイト一致、title・description・H1・canonical各35/35。 | PASS（本文の法的正確性は別） |
| 内部リンク | `python scripts/check_site_links.py`: 35 HTML、sitemap 31、625リンク、問題0。主要6カード先6/6は200・本文あり。 | PASS |
| 旧SAFE表示 | SAFE PR #4は公開済み。PORTALの旧資料3件は警告とnoindexを付与済み。 | 現行表示のiPhone受入はSORA申告。正式文書原本は不変更 |
| robots / sitemap / ads.txt | 各200。ads.txtのpublisher IDと公開AdSenseタグのIDは一致。 | 公開ファイルPASS。管理画面認識は未確認 |
| Privacy / 運営者情報 | `privacy.html` の開示・回答手順、`operator-disclosure.html` の法的表示方法に「候補」「確認中」。 | 所有者・法務判断待ち |
| 問い合わせ | フォーム表示・送信処理ソースは存在。現在の本番送受信は未実施。 | NOT TESTED |
| モバイル / 性能 | PR #19本番PSI 3回のCLS 0/0/0、LCP中央値2.264秒。SORA申告のiPhone Safari受入3/3 PASS。今回の変更候補は未公開。 | 既存版の履歴PASS。変更後は再測定が必要 |

## 配信境界と旧PHP修正手順

`CNAME` は `delipit.jp`、公開応答に `x-github-request-id` があり、GitHub Pagesの静的配信を確認。GitHub公式文書によるとPagesはサーバー側PHPを実行しない。Cloudflare管理画面はログイン画面で、当該ゾーン、DNSのプロキシ状態、他CDN・リバースプロキシの有無は**確認できない**。Cloudflare Single Redirectsは対象DNSレコードがCloudflareでプロキシされる場合にのみ使用できる。

**承認対象の設定案（既存の前段がCloudflareでプロキシ済みの場合のみ）**：対象ホスト `delipit.jp`、URI path equals `/driver-news.php` または `/assets/driver-news.php`、静的転送先 `https://delipit.jp/driver-news.html`、301、query stringを引き継がない。他パス・他ホストは対象外。まず現在のDNS・ルール一覧・優先順位をスクリーンショットと設定エクスポートで記録し、競合ルールがないことを確認する。設定が使えない場合は既存の配信事業者側の同等のexact-pathルールを検討し、DNS移行は別途承認事項とする。

設定後 `python scripts/check_legacy_php_release.py --live` でGET/HEAD計4件の301/308、Location、転送先200/text/htmlを確認する。ブラウザ、主要35ページ、アプリ2ドメインへの副作用も測る。**受入後にのみ**旧PHPファイルを公開成果物から除外する別差分を用意し、再度4件の転送が持続することを確認する。ロールバックは追加したexact-pathルールのみ無効化し、保存した元設定に戻す。旧ファイル削除を先に実施しない。meta refreshはHTTP転送ではない。

## 公開情報とコンテンツ

- `privacy.html` はDELIPIT公式サイトとWebアプリ、AdSense利用可能性、第三者Cookie、広告設定、GA4、端末内保存、Web3Forms、メール、問い合わせを記載。CMPの実運用と対象地域は管理画面で確認する。GoogleはEEA・英国・スイス向けパーソナライズ広告で認定CMP／TCF要件を定める。日本向けサイトという理由だけで要否を断定しない。
- `operator-disclosure.html` は屋号REVERIE、SORA、個人事業、連絡先、SAFEとの関係を示す一方、法的な表示方法と回答方法を確認中としている。正式Privacy本文の改定はこのPRに含めない。SORAの確認後、必要な場合は改定案・施行日・差分を別途提示する。
- `driver-note-10.html` は2026年10月18日の開発時点でSAFEを「準備中」と記した実体験記事。本文は当時の記録として保持し、ページ上部に2026年11月1日正式公開の注記と現行案内へのリンクを追加した。公開前ページの旧SAFE3件は旧版警告・noindexを維持。
- NOTEの実体験とNEWSの公的資料案内は区別。公開中の主要ガイドは本文・出典リンクを有する。全制度説明の逐条照合、AdSenseの審査結果、全広告配置の実配信状態は未確認。

## 所有者の確認とリリースゲート

1. 既存DNSと前段配信の管理画面を確認し、対象2パスのHTTPルール設定案・復旧手順を承認する。Cloudflareに未接続またはDNS onlyなら、Cloudflareルールは発効しない。管理画面へのログイン状態がないため自動適用しない。
2. Privacy／運営者表示の「確認中」事項について、表示する確定事実、回答手順、改定承認者・改定日を決める。未確認の氏名・住所・法的適合性は推測しない。
3. AdSenseの現在の不承認理由、サイト状態、ads.txt認識、広告配信地域とCMP設定、Search Consoleのsitemap処理・主要URLインデックスを管理画面で確認する。接続手段がない項目は確認できない。
管理画面接続状況（2026-11-03）：Cloudflareはログイン画面でゾーン設定未取得。AdSenseはGoogleログイン画面、Search Consoleも未ログイン。Windsor.aiには `sc-domain:delipit.jp` 接続が表示されたが、Free枠1アカウントに対しGA4とSearch Consoleの2アカウントが接続され、読取りが停止している。返却値をインデックス状況の実測として扱わない。既存接続の解除・有料化は行わない。

4. 変更候補をiPhone Safariで確認。問い合わせフォームを本番でテスト送信・受信し、個人情報を最小限にする。変更後PageSpeed mobileを同条件3回実測する。
5. 全ゲートPASS、SORA承認後にだけDraft PRをマージし、正式配信・再検証する。AdSense再申請は別操作とし、本PRでは実行しない。

参考： [GitHub PagesのPHP非対応](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)、[Cloudflare Single Redirects](https://developers.cloudflare.com/rules/url-forwarding/)、[Google AdSenseのページ準備](https://support.google.com/adsense/answer/7299563)、[GoogleのCMP要件](https://support.google.com/adsense/answer/13554116)。

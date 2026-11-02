# delipit.jp apex 301転送 — 変更前設計・受入・復旧

作成：2026年11月3日。状態：**HOLD／設定未変更**。PR #23の後続。SORA申告のCloudflare DNS画面と公開HTTP実測を区別して記録する。

## 変更前の状態

| 項目 | 値・根拠 |
| --- | --- |
| `delipit.jp` | Aレコード4件、すべてDNS only（SORA申告）。各IPv4値、TTL、レコードIDはこの作業では未取得。変更直前に画面またはエクスポートで記録する。GitHub Pagesの標準値は185.199.108/109/110/111.153だが、現レコード値と同一とは未確認。 |
| `www.delipit.jp` | CNAME、DNS only（SORA申告）。転送先・TTLは未取得。2026-11-03公開HEADで301、Location `https://delipit.jp/`。 |
| `analytics.delipit.jp` | Proxied（SORA申告）。変更禁止。 |
| `app.delipit.jp` | DNS only（SORA申告）。変更禁止。 |
| `safe.delipit.jp` | Proxied（SORA申告）。変更禁止。 |
| apex現行 | `https://delipit.jp/` は200/text/html、`x-github-request-id`あり。旧PHP2件はGET/HEADとも200/application/x-httpd-php、Locationなし。 |
| GitHub Pages | リポジトリの `CNAME` は `delipit.jp`。Pages設定のcustom domain、Enforce HTTPS、証明書の現在の状態は管理画面未確認。 |
| Cloudflare | SSL/TLS mode、Universal SSLのapex証明書のActive状態、CAA、Rules優先順位、Cache Rules、WAF/Access、Always Use HTTPSは管理画面未確認。 |

**影響範囲**：同一名にA/AAAAが複数ある場合、1件をProxiedにするだけでその名のA/AAAA全体がプロキシ扱いになる。切替は2 URLだけの変更ではなく、`delipit.jp` の全HTTPS/HTTPリクエストにCloudflareを挿入する。`www`、`app`、`safe`、`analytics` のDNSレコードは変更しない。ただしCloudflareのゾーン共通SSL設定を変更すると既にProxiedの`safe`/`analytics`にも波及し得るため、本作業ではSSL modeを変更しない。

## 切替前の必須確認（1件でも未確認ならHOLD）

1. Cloudflare DNSの対象4 Aレコードの**実際のIPv4、TTL、Proxy status、レコードID**、www CNAMEのTarget/TTL、関連AAAA/CAAをスクリーンショットまたはエクスポートで保存。4 AがGitHub Pages公式の値を指すか比較する。メール用MX/TXTは表示だけ確認し変更しない。
2. GitHub Settings → Pagesでcustom domain `delipit.jp`、Enforce HTTPS、origin証明書の状態を記録。現行のapex・www HTTPS、画像、CSS、フォーム、主要6記事、robots/sitemap/ads.txtをHTTP実測で記録する。
3. Cloudflare SSL/TLS Overviewの**現在のmode**を確認。FlexibleならGitHub PagesのHTTP→HTTPSでループし得るため切替を止める。Full (strict)ならGitHub Pagesの有効な公開証明書をoriginとして検証できるか確認する。modeを変更してSAFE等に波及させない。Edge Certificatesでapexを含むUniversal SSLがActiveか確認する。
4. Cloudflare Rulesの既存Single/Bulk Redirects、Cache Rules、Page Rules、WAF/Accessを読み取り、同じパスまたはapex全体の競合を確認。特にCache Everythingやチャレンジ、HTTPS・www転送ループを確認。CloudflareのデフォルトではHTML/JSONはキャッシュされないが、既存ルールが上書きしていないことを確認する。

## 承認対象の最小設定

Cloudflare Rules → Redirect Rules → Single Redirects で**1ルール**。Custom filter expression：

```text
(http.host eq "delipit.jp" and (http.request.uri.path eq "/driver-news.php" or http.request.uri.path eq "/assets/driver-news.php"))
```

Type **Static**、Target URL `https://delipit.jp/driver-news.html`、Status code **301**、Preserve query string **Off**。対象ホストと2パスの完全一致。wwwや他サブドメイン、似たパスには適用しない。既存ルールとの順序を確認する。ルールはapexがProxiedになるまで発効しない。

## SORA承認後の実行順序

1. 直前のDNS・SSL・Rules設定と現行HTTP結果を保存し、復旧担当・時刻を決める。ルールを作成して内容と既存ルールとの順序を確認。**ここまでも本番ルール操作なのでSORAの承認が必要**。
2. apexのAレコード4件をProxied表示へ切替。最初の1件からホスト全体に作用し得るため、段階的に無影響を期待しない。値（IPv4）やwww・app・safe・analytics・MX/TXTは変えない。
3. 直ちにapex HTTPS 200、証明書、有効なGitHub Pages本文・画像・CSS、www→apex既存301、旧PHP2件のGET/HEAD 301＋Location＋最終200/text/html、主要6記事、35 HTML、アプリ2ドメインを確認。`python scripts/check_legacy_php_release.py --live` を実行。301が通るまで旧PHPファイルを削除しない。
4. Cookie/フォーム/広告コードとモバイル表示、PageSpeed（LCP/CLS/TBT、同条件3回）を確認。Cloudflareの応答ヘッダーとキャッシュ状態、GitHub PagesのHTTPS/ドメイン設定も再確認する。キャッシュを大域的にパージしたりzone-wide設定を追加したりしない。
5. 全受入PASS後にだけ、旧PHPファイルを公開成果物から除く**別差分**を検討する。除外後も4件の301と新URL200を再測定。PR #23のマージ、AdSense再申請は別承認。

## ロールバック

不具合（TLS 525/526、ループ、403、ページやアセット欠落、www転送異常、SAFE等への副作用）が出たら**新しい301ルールを無効化**し、apexの4 Aを記録したIPv4/TTLのままDNS onlyへ戻す。CloudflareのSSL modeや他サブドメインには触れない。旧PHPファイルは残しておく。DNSの旧応答が各resolverのTTL中に残り得るため、直接・プロキシ経由の両方が落ち着くまでapex/wwwのHTTPS、主要ページ、アプリ2ドメインを再測定し、復旧時刻とHTTP結果を記録する。元設定が未記録なら切替しない。

参考：[Cloudflare Proxy status](https://developers.cloudflare.com/dns/proxy-status/)、[Single Redirects](https://developers.cloudflare.com/rules/url-forwarding/)、[Full (strict)](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/)、[Universal SSL](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/enable-universal-ssl/)、[GitHub Pages custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)、[Cloudflare default cache](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/)。

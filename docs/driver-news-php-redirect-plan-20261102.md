# 旧 `/driver-news.php` のHTTP転送 — 配信経路の制約と受入条件

確認日：2026年11月2日（JST）。基準main：`4f139fc3b71fcbaa89f1f2fdb19b2715f6722a72`。

## 実測と原因

| URL | 現行HTTP | Content-Type | HTTP Location | 備考 |
| --- | --- | --- | --- | --- |
| `https://delipit.jp/driver-news.php` | 200 | `application/x-httpd-php` | なし | 本文はHTMLのmeta refresh、canonicalとリンクで `driver-news.html` を指す |
| `https://delipit.jp/driver-news.html` | 200 | `text/html; charset=utf-8` | なし | 現行DRIVER NEWS |

HEAD応答の `x-github-request-id`、`x-github-edge-region`、`x-proxy-cache` とリポジトリの `CNAME` から、現行の配信元はGitHub Pagesと判定する。GitHub Pagesは静的ファイルを配信し、PHPなどサーバー側言語は実行しない（[GitHub公式](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)）。現行の`.php`実ファイルをHTMLに編集しても、HTTP 301/308や`text/html`へのContent-Type変更は実現しない。JekyllによるHTML転送案もHTTP転送と同一ではない。`_redirects`や`.htaccess`をこのリポジトリへ追加してもGitHub PagesのHTTPルーティング設定にはならない。

## 最小対応案（現行配信経路では実装不可）

既存ドメインの前段にHTTPルールを設定できる配信基盤を導入する場合に限り、完全一致パス`/driver-news.php`を`https://delipit.jp/driver-news.html`へ301（または308）で転送する。対象をこの1パスに限定し、他の35 HTML、アプリサブドメイン、SAFE、DNSを一括変更しない。基盤選定、ルール追加、DNS/プロキシ変更は別途SORAの設計・公開承認を要する。導入前にGitHub Pages側で本番に効くHTTP転送を装うコードは置かない。

受入では、`curl -I https://delipit.jp/driver-news.php` で301/308と正しい`Location`、`curl -IL`で1回の転送後に200/`text/html`を確認する。GET・HEAD、クエリ付き旧URL、トップ・NEWS・主要6記事も確認する。現時点では転送設定がないため、**転送後のHTTPステータス・Location・Content-Typeは未検証**。

## 既存サイトへの影響

本PRは監査記録だけ。35公開HTML、旧PHP本文、内部リンク、sitemap、canonical、画像、規約に差分なし。`python scripts/check_site_links.py` は `HTML=35 sitemap=31 internal_links=625 problems=0`。sitemapは`driver-news.html`を掲載。旧PHPのcanonicalは同じ新URL、`noindex,follow`のまま。

判定：**HOLD（旧URLのHTTP転送）**。現行サイト全体のPR #20リリースPASSとは別件。AdSense再申請やProduction変更は行わない。

# DELIPIT AdSense 再申請前の公開検証チェックポイント

確認日：2026-11-01（JST）

## 判定

**HOLD：公開サイトのHTTP応答、最新AdSense審査理由、管理画面のCMP、実機速度を確認できないため。**

## 今回実施

- GitHub mainの12ファイルを再取得：トップ、4実用ガイド、SAFE規約・Privacy、旧PHP2件、ads.txt、robots.txt、sitemap.xml。
- TOPと4実用ガイドはHTMLのtitle・h1・canonicalをソース上で確認。
- 旧PHP2件はGitHub上の内容からPHPコードが除去され、driver-news.htmlへのHTML案内に置換されたことを確認。ただしホストの旧PHP MIMEは未検証であり、meta refreshがブラウザで機能するとは保証しない。
- ads.txtのパブリッシャーIDと、前回監査のサイト内広告IDは一致。
- robots.txtはAllow: / と sitemap URLを記載。
- SAFEの旧規約・旧Privacyの本文には開発時の文言が残るが、両ページ冒頭に歴史的資料と現行版参照先が記載済み。現行正式3文書との条項照合は未実施。
- web経由で https://delipit.jp/ 、start-guide.html、safety-guide.html、driver-news.php、ads.txt の取得を試したが、すべて取得エラー。別のコンテナ実行経路でもDNS解決に失敗。これは本番停止の証拠ではない。

## 未確認・残るゲート

1. 実際の公開URLのステータス、MIME、リダイレクト、画像、リンク、sitemapをネットワークが使える環境で再検査する。
2. 古いPHP URLが application/x-httpd-php でHTMLソースを返す場合、静的HTMLにするだけでは十分でない。ホストで301/308リダイレクトまたは適切なContent-Typeを設定し、実レスポンスを確認する。
3. SAFE公式アプリで承認済み3文書の現行版、施行日、各同意条件を原本照合する。正式条文は無断編集しない。
4. iPhone Safariで主要ページの表示、メニュー、フォームの動作と外部アプリ遷移を確認する。フォーム送信は実際の受信を確認する。
5. PageSpeed Insights／Lighthouse／Core Web Vitalsを主要URLで実測する。計測していない数値を推定しない。
6. AdSenseの現在の否認理由、サイト状態、ads.txt認識、広告掲載と対象地域に応じたCMP設定を管理画面で確認する。

## 方針

記事数・文字数を閾値にしない。ユーザーの課題に対する実用性、一次資料、著者と運営表示、読みやすさを優先。Googleによる審査通過は保証できない。公開実測と管理画面が確認できるまでREADYとは判定しない。

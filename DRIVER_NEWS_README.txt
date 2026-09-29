DELIPIT DRIVER NEWS v0.1

■ 概要
- driver-news.php が公的情報源をサーバー側で取得します。
- 最大6時間キャッシュし、アクセス時に期限切れなら自動更新します。
- 現在の取得元: 国土交通省 / 国税庁
- 記事本文・画像は転載せず、タイトル・分類・出典・公式リンクのみ表示します。
- DRIVER NOTE は「後日公開 / COMING LATER」表示です。

■ サーバー要件
- PHP 8.x 推奨
- allow_url_fopen が有効であること
- PHP DOM extension (DOMDocument) が利用できること
- /data ディレクトリにPHPから書き込み可能であること（キャッシュ用）

■ Xserverでの確認
1. ZIPを公開ディレクトリへ展開
2. https://delipit.jp/driver-news.php を開く
3. NEWSカードが表示されることを確認
4. data/driver-news-cache.json が生成されればキャッシュ正常

■ 注意
- 自動抽出のため、取得元HTMLの変更で取得できなくなる可能性があります。
- 情報源はホワイトリスト方式で追加してください。
- 厚労省・警察庁RSSは現段階では自動取得元に追加していません。
- AdSense再審査はDRIVER NOTE等の独自コンテンツ追加後を推奨します。

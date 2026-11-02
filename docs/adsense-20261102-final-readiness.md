# DELIPIT PORTAL — AdSense再申請最終監査

作業日：2026年11月2日（JST）。開始時の最新main：`c3c66781121af20ebf41be8055d10d372e9d794d`（PR #19 merge `604bfcf…` の次のDRIVER NEWS定期更新）。本番トップと `data/driver-news.json` は、このmainの配信物と一致。前回の監査履歴 `adsense-20261101-live-verification.md` を継承。

## 結論

**HOLD**：再申請は未実施。本番の主要記事と速度は受入済みだが、公開中の不達アンカー16件、SAFE正式文書の施行表示矛盾、AdSense管理画面の審査理由・CMPとSearch Console処理状況の未確認を解消・確認する。承認は保証しない。

## 全ページの公開応答

35 HTMLを公開URLからGETし、全件 `200 / text/html`。title/H1、内部の画像・記事リンク、canonicalを静的に監査。sitemapは31 URL、残りは旧SAFE3件とquickstart。旧SAFE3件はnoindex、quickstartはmanual canonical。過去の全画像48 URLの監査ではWebP1回の一時503後、同じURLは再測定3/3で200。恒常的な欠落は確認されていない。本文の真偽や広告審査結果をHTTPだけでPASSとしない。

| URL | title | HTTP | sitemap | 内容・留意点 |
| --- | --- | --- | --- | --- |
| `/contract-guide.html` | 軽貨物の業務委託契約で確認する7つのポイント ／ DELIPIT | 200 | 掲載 | PASS：本文・H1確認 |
| `/delipit.html` | DELIPIT ／ 配送実績・売上管理Webアプリの紹介 | 200 | 掲載 | PASS：本文・H1確認 |
| `/driver-faq.html` | 軽貨物ドライバーのよくある質問 ／ DELIPIT | 200 | 掲載 | PASS：本文・H1確認 |
| `/driver-news.html` | DRIVER NEWS ／ DELIPIT | 200 | 掲載 | PASS：本文・H1確認 |
| `/driver-note-01.html` | 売上を確認するために記録していたら、自分がやってきた仕事が見えてきた。 ／  | 200 | 掲載 | PASS：NOTE実体験 |
| `/driver-note-02.html` | 売上だけ見ていた頃より、仕事の調子が分かるようになった。 ／ DRIVER  | 200 | 掲載 | PASS：NOTE実体験 |
| `/driver-note-03.html` | 計算と入金額が合わない。でも、間違いとは限らなかった。 ／ DRIVER N | 200 | 掲載 | PASS：NOTE実体験 |
| `/driver-note-04.html` | カレンダーを数字で埋めていくと、一ヶ月働いた実感が残る。 ／ DRIVER  | 200 | 掲載 | PASS：NOTE実体験 |
| `/driver-note-05.html` | 僕にとって配送は、身体を使った『攻略ゲーム』だった。 ／ DRIVER NO | 200 | 掲載 | PASS：NOTE実体験 |
| `/driver-note-06.html` | 最初は、仲のいい人にも使ってもらえたら。それくらいだった。 ／ DRIVER | 200 | 掲載 | PASS：NOTE実体験 |
| `/driver-note-07.html` | 配送の一日は、荷物を積む前から始まっている。 ／ DRIVER NOTE ／ | 200 | 掲載 | PASS：NOTE実体験 |
| `/driver-note-08.html` | 荷物が多い日より、『不在が多そうな日』の方が難しい。 ／ DRIVER NO | 200 | 掲載 | PASS：NOTE実体験 |
| `/driver-note-09.html` | 配達が速い人は、走るのが速いわけじゃない。 ／ DRIVER NOTE ／  | 200 | 掲載 | PASS：NOTE実体験 |
| `/driver-note-10.html` | 法令で増えた仕事。だから、少しでも楽にしたかった。 ／ DRIVER NOT | 200 | 掲載 | PASS：NOTE実体験 |
| `/driver-note-11.html` | DELIPIT V1.2.0公開。自分には今すぐ必要ない機能を追加した理由。 | 200 | 掲載 | PASS：NOTE実体験 |
| `/driver-note.html` | 現役配送員のDRIVER NOTE ／ DRIVER NOTE ／ DELI | 200 | 掲載 | PASS：本文・H1確認 |
| `/driver-support.html` | 軽貨物ドライバーのための総合サポート ／ DELIPIT | 200 | 掲載 | 注意：入口重複 |
| `/field-workflow.html` | 配送実績を記録して振り返る方法 ／ DELIPIT 現場ガイド | 200 | 掲載 | PASS：本文・H1確認 |
| `/gamification.html` | DELIPIT GAME SYSTEM ／ 配送の記録をキャリアへ | 200 | 掲載 | PASS：本文・H1確認 |
| `/` | DELIPIT PORTAL｜軽貨物ドライバーの仕事を支える | 200 | 掲載 | PASS：本文・H1確認 |
| `/manual.html` | DELIPIT 使い方・マニュアル | 200 | 掲載 | PASS：本文・H1確認 |
| `/money-guide.html` | 軽貨物の売上・経費・手取りを整理する方法 ／ DELIPIT | 200 | 掲載 | PASS：本文・H1確認 |
| `/news-v120.html` | DELIPIT V1.2.0 正式公開 — 複数委託先・複数報酬方式に対応し | 200 | 掲載 | 注意：告知、旧アンカーを隔離修正 |
| `/operator-disclosure.html` | 運営者情報・開示請求について ／ DELIPIT | 200 | 掲載 | 注意：運営者表示に確認中事項 |
| `/pitcrew.html` | PIT CREW ／ PITO & RONA ／ DELIPIT | 200 | 掲載 | PASS：本文・H1確認 |
| `/privacy.html` | プライバシーポリシー ／ DELIPIT | 200 | 掲載 | 注意：正式Privacyに確認中事項 |
| `/quickstart.html` | DELIPIT クイックスタート ／ 3ステップで始める | 200 | 非掲載 | 注意：manualをcanonical |
| `/safe-guide.html` | SAFEの使い方 ／ DELIPIT SAFE | 200 | 掲載 | PASS：本文・H1確認 |
| `/safe-information.html` | 保存・位置情報・法令の案内 ／ DELIPIT SAFE | 200 | 非掲載 | 注意：旧資料・noindex |
| `/safe-privacy.html` | SAFEプライバシー案内（2026年10月開発時の資料） ／ DELIPIT | 200 | 非掲載 | 注意：旧資料・noindex |
| `/safe-terms.html` | SAFE規約案内（2026年10月開発時の資料） ／ DELIPIT SAF | 200 | 非掲載 | 注意：旧資料・noindex |
| `/safe.html` | DELIPIT SAFE — 運行記録・安全管理補助 ／ DELIPIT S | 200 | 掲載 | PASS：本文・H1確認 |
| `/safety-guide.html` | 軽貨物の安全管理｜点呼・日常点検・記録の基本 ／ DELIPIT | 200 | 掲載 | PASS：本文・H1確認 |
| `/start-guide.html` | 軽貨物の始め方｜初心者向け6ステップ ／ DELIPIT | 200 | 掲載 | PASS：本文・H1確認 |
| `/terms.html` | 利用規約 ／ DELIPIT | 200 | 掲載 | PASS：本文・H1確認 |

## 技術・導線

- **FAIL、本番**：既存内部リンク625件中、アンカー不達16件。15件は別ページの `index.html#products`（トップに該当IDなし）、1件は `index.html#v120-news`。隔離ブランチでは前者を実在する `#tools`、後者をトップへのリンクに変更し、再検査0件。既存URL・記事本文・規約条文を変更せず、公開はしていない。
- **FAIL、旧PHP**：`/driver-news.php` はHTTP 200、`Content-Type: application/x-httpd-php`、HTTPリダイレクト0回。HTML本文のmeta refreshとcanonicalのみ。ブラウザ表示・検索評価は保証できない。既存ホスト側で旧URLの301/308設定が必要か検討し、MIMEとともに実測する。
- robots.txt 200 text/plain、sitemap.xml 200 application/xml、ads.txt 200 text/plain。ads.txtは `pub-9142850138364995`。広告コード内 `ca-pub-9142850138364995` と一致。AdSense側の認識は別途未確認。
- トップの6カードは実用本文へ到達。NOTEはSORAの経験、NEWSは公的資料の案内という役割。開業・収支・安全ガイドには対象条件と一次資料へのリンク。短い更新告知やキャラクターページを文字数だけで不合格扱いしない。制度説明の各記述をすべて逐条照合したとは扱わない。
- モバイル：本番と同一ソースのローカルChromiumで35 HTMLを375/390/430pxで確認し、document横はみ出し0。SORA申告のiPhone Safari実機Acceptance 3/3 PASSはPR #19時点の結果。問い合わせフォームの入力欄は本番ブラウザ表示確認、送信と受信は今回は再試験していない。
- 本番PageSpeed mobile 3回：LCP 2.264 / 3.280 / 2.263秒（中央値2.264秒）、CLS 0 / 0 / 0、TBT 104.5 / 32 / 116ms（中央値104.5ms）。フィールドINPはNo Data。[測定1](https://pagespeed.web.dev/analysis/https-delipit-jp/264ae6j2wt?form_factor=mobile)・[測定2](https://pagespeed.web.dev/analysis/https-delipit-jp/2ggo5ydve5?form_factor=mobile)・[測定3](https://pagespeed.web.dev/analysis/https-delipit-jp/euwo3fewfx?form_factor=mobile)。LCP1回の3.28秒は変動として観察。

## SAFE・信頼性

- PORTALのSAFE 1.0.0正式公開案内は整合。SAFE旧3資料は旧版の警告とnoindexで現行版と区別。
- 現行SAFEの `/terms.html` と `/privacy.html` は「適用日 2026-11-01」「同意強制開始 2026-11-01」と同時に「所有者承認済み本文（未施行）」を表示。`/operator-policy.html` は今回は200で本文を取得でき、前回の取得不能は解消。**SAFEの表示生成元を別件で是正する必要がある。** 正式原文、ハッシュ、同意履歴、業務データには触れない。

### PR #20受入時のSAFE原因追跡（2026-11-02）

SAFE main `549a7ca6340f9abd8db502c23a714e80a4085c4f` の `dist/client/terms.html` と `privacy.html` には `<h2>所有者承認済み本文（未施行）</h2>` が残る。一方、`scripts/prepare-legal-activation.mjs` は施行時に notice の日付を差し替えるが、見出しについては旧候補文字列 `所有者承認済み本文を基にしたCloudflare向け候補・未施行の全文候補` だけを `replaceAll` する。実際の見出しと一致せず、「未施行」が残る。公開HTMLでこの組合せを再現した。原因は表示生成時の置換対象の不一致と判定する。

本番の `/legal-release-config.js` は `version: V99`、`effectiveDate: 2026-11-01`、`enforcementStartAt: 2026-11-01T00:00:00+09:00`、`enforcementEnabled: true`、`legalReviewComplete: true`、`releaseGatePassed: true`。3文書の bodyHash は `release/OWNER_PUBLICATION_APPROVAL.json` の承認値と全件一致。これは公開設定と承認資料の照合であり、利用者端末の `delipit-safe-consent-v1` に保存された実際の同意履歴や同意日時を読み取った結果ではない。個別履歴は**確認できない**。SAFE側の別件で公開用見出しのみを正しい現行表示に修正し、3文書の原文・ハッシュ・同意処理・履歴を不変として検証する。PR #20にSAFEコード変更を混ぜない。
- PORTALの `operator-disclosure.html` は運営ブランド、担当者、メール、フォームを表示するが、法的な運営主体の表示方法は「確認中」。正式 `privacy.html` の開示回答方法にも「候補／確認中」がある。これらの正式本文の無断改定はしない。

## AdSense管理画面とGoogle公式基準

Google公式の[ページ準備](https://support.google.com/adsense/answer/7299563)、[不承認時の説明](https://support.google.com/adsense/answer/12176698)、[プログラムポリシー](https://support.google.com/adsense/answer/48182)、[プライバシー記載](https://support.google.com/adsense/answer/1348695)、[CMP](https://support.google.com/adsense/answer/7670013)を2026-11-02に参照。独自性、有用性、導線、広告とコンテンツの区別、Cookie説明を確認した。公開サイトには現場実体験と実用ガイドがあるが、AdSense固有の不承認理由は**確認できません**。

| 項目 | 判定 | 理由 |
| --- | --- | --- |
| 独自記事・主要導線 | PASS | 本文・NOTE/NEWS区別・6カードを確認。 |
| 画像・SEOファイル・広告ID | PASS | 公開応答、記載内容と一致。AdSense側の認識は未確認。 |
| SAFE正式文書表示 | FAIL | 適用日と「未施行」の矛盾。 |
| 旧PHP MIME/リダイレクト | FAIL | 200/application/x-httpd-php、HTTP転送なし。 |
| 16アンカー | FAIL | 隔離修正済み、本番未反映。 |
| AdSense不承認理由・ads.txt認識・CMP | 未確認 | 管理画面の現在の状態にアクセスできない。EEA/英国/スイス向け配信設定でCMP要件を確認。日本向けだけで一律必須と断定しない。 |
| Search Consoleサイトマップ・インデックス | 未確認 | Windsor.aiの接続枠超過で読取り停止。返された0は実測値ではないため破棄。 |

## 次の作業（優先順）

1. 隔離Draft PRのアンカー16件をレビュー、SORA承認後に公開し、本番で再テスト。
2. SAFE側で「未施行」の表示生成・施行状態を調査。正式文書や同意履歴を保護する最小修正を別件で受入。
3. SORAがAdSense管理画面の現在の不承認理由、サイト状態、ads.txt認識、CMP対象地域・設定を確認。Search Consoleでsitemap処理と主要6記事のURL検査を確認。
4. ホスト側で旧PHPの301/308とMIME、正式Privacy/運営情報に残る確認中事項を担当者と整理。確認結果を得てからREADY / CONDITIONAL READY / HOLDを再判定。

本監査のコード変更は隔離ブランチのみ。AdSense再申請、mainマージ、本番公開、SAFEアプリと規約本文の改定は行わない。

# DELIPIT AdSense 再申請前の公開検証チェックポイント

確認日：2026-11-01（JST）。ソース基準：main `8c649dffe2bdeb87eff087d9e6ac59bb96a831e9`。本報告の実測は公開ブラウザとPageSpeed Insightsに限る。HTTPステータスや管理画面をDOM表示から推定しない。

## 判定

**HOLD（再申請・追加本番反映とも保留）**。SAFE正式文書の表示矛盾と運営方針の取得不能、旧PHPのHTTP/MIME未確認、トップのモバイルLCP、AdSense管理画面の不承認理由とCMP未確認が残る。Googleの承認を保証しない。

## 公開ページ監査

sitemap掲載31 URLをブラウザで巡回し、各ページの本文・H1・canonical・画像欠落の有無を確認。さらにsitemap外の既存4 HTMLを表示確認。HTTP 200そのものはブラウザDOMから確認できないため、下表の「表示確認」はHTTPステータスの保証ではない。静的ソースの全35 HTMLでは、内部ファイル参照の欠落0、H1欠落0、description欠落0、canonical欠落0、重複title 0。画像の不完全読み込みは巡回時0。記事の真偽やAdSense評価を自動判定したものではない。

| URL | 目的 | 公開表示 | canonical | 主な留意点 |
| --- | --- | --- | --- | --- |
| `/contract-guide.html` | 業務委託 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/delipit.html` | 配送管理ツール | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/driver-faq.html` | FAQ | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/driver-news.html` | 制度情報 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/driver-note-01.html` | SORA実体験 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/driver-note-02.html` | SORA実体験 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/driver-note-03.html` | SORA実体験 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/driver-note-04.html` | SORA実体験 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/driver-note-05.html` | SORA実体験 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/driver-note-06.html` | SORA実体験 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/driver-note-07.html` | SORA実体験 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/driver-note-08.html` | SORA実体験 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/driver-note-09.html` | SORA実体験 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/driver-note-10.html` | SORA実体験 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/driver-note-11.html` | SORA実体験 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/driver-note.html` | 実体験一覧 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/driver-support.html` | 旧サポート入口 | 表示確認（ブラウザ） | 一致 | ポータルと入口が重複。役割を維持しつつ後日整理 |
| `/field-workflow.html` | 配送実務 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/gamification.html` | ゲーム機能 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/` | ポータル入口 | 表示確認（ブラウザ） | 一致 | 画像LCP遅い。WebP候補を準備 |
| `/manual.html` | 操作案内 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/money-guide.html` | 収支 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/news-v120.html` | 製品告知 | 表示確認（ブラウザ） | 一致 | 短い製品告知。記事量で一律判定しない |
| `/operator-disclosure.html` | 運営者情報 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/pitcrew.html` | キャラクター | 表示確認（ブラウザ） | 一致 | キャラクター紹介。実務記事への導線確認 |
| `/privacy.html` | Privacy | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/quickstart.html` | 簡易操作案内 | 表示確認（ブラウザ） | → manual | sitemap外。canonicalはmanual.html |
| `/safe-guide.html` | SAFE操作案内 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/safe-information.html` | SAFE旧資料 | 表示確認（ブラウザ） | 一致 | 旧資料。noindex |
| `/safe-privacy.html` | SAFE旧資料 | 表示確認（ブラウザ） | 一致 | 旧資料。noindex |
| `/safe-terms.html` | SAFE旧資料 | 表示確認（ブラウザ） | 一致 | 旧資料。noindex |
| `/safe.html` | SAFE紹介 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/safety-guide.html` | 安全管理 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/start-guide.html` | 開業 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |
| `/terms.html` | DELIPIT規約 | 表示確認（ブラウザ） | 一致 | 重大な表示欠落なし |

- ヒーローから6記事（開業・契約・現場・収支・安全・FAQ）へのリンクは現行ソースと公開ページの両方で確認。関連記事とトップ導線も既存記事にある。既存本文・URLは変更しない。
- DRIVER NOTEはSORA本人の経験として区別され、DRIVER NEWSは公的資料への案内として別の役割を持つ。古い記事を短さだけで削除しない。
- SAFE旧3ページは履歴表示の警告があり、`noindex`。本文は承認済み文書として改変しない。ただし検索結果用description/OGが「テスト版」「正式条件確認中」のままだったため、履歴であることを明記する候補を隔離変更した。

## 技術・操作

- `robots.txt` は `Allow: /` と公開sitemapを配信。`sitemap.xml` はXMLとして31 URLを配信。`ads.txt` はtext/plainで `pub-9142850138364995` を配信。ページのcanonicalは上表のとおり。SAFE旧3ページのみnoindex、quickstartはmanualをcanonicalとしsitemap外。
- 旧 `/driver-news.php` はブラウザ安全制限 `ERR_BLOCKED_BY_CLIENT` により開けなかった。**HTTPステータス、Content-Type、リダイレクトは確認できない**。GitHub上ではHTML案内に変更済みだが、実配信の判定には使わない。
- 問い合わせフォーム：必須欄を入力し、DELIPIT宛てに「返信不要」のテストを送信。画面に受付確認が出て欄がクリアされた。実メール受信は確認していない。
- iPhoneの375/390/430px・Safariでの実描画は未確認。PageSpeedのMoto G Power相当のモバイルエミュレーションとは区別する。

## PageSpeed Insights 実測

- トップのモバイル2回：Performance **40 / 66**、LCP **7.3 / 7.1秒**、CLS **1.000 / 0**、FCP **3.9 / 2.9秒**。フィールドデータは「No Data」。変動が大きいのでCLSの原因は確定できない。画像JPEGは573.7KiB、Lighthouseは約488KiBの節約余地を提示。Google広告の第三者コードも転送・主スレッド時間に影響するが、コードは変更しない。
- `start-guide.html` のモバイル1回：Performance **100**、LCP **0.8秒**、CLS **0**。単発のラボ値で全ページの速度を代表しない。
- 原画像JPEGは保持し、同じ1199×1312pxのWebP（約153KB）を優先配信する隔離候補を作成。ロゴ・文字・PITO/RONAは視覚確認済み。配信後のLCP改善量は未測定。
- 計測結果：[トップ1回目](https://pagespeed.web.dev/analysis/https-delipit-jp/9h5tdigisw?form_factor=mobile)、[トップ2回目](https://pagespeed.web.dev/analysis/https-delipit-jp/hy915de45z?form_factor=mobile)、[開業ガイド](https://pagespeed.web.dev/analysis/https-delipit-jp-start-guide-html/arawib6zev?form_factor=mobile)。

## SAFEの正式表示照合

- SAFEトップは `DELIPIT SAFE 1.0.0` と規約版V99・適用開始日2026-11-01、承認済み3文書のリンクとハッシュを表示。利用規約とPrivacyの本文ページは表示できた。
- ただし両本文ページは「適用日 2026-11-01／同意強制開始 2026-11-01」と同時に「所有者承認済み本文（未施行）」を表示。どちらが現行条件なのか確認が必要。
- `https://safe.delipit.jp/operator-policy.html` は再読込しても `Public information unavailable` となり、運営方針の本文を照合できない。SAFEアプリと法的文書は本件で変更しない。
- ポータルのSAFE 1.0.0案内と、旧3文書が履歴である旨の警告は確認した。法的同意の実効状態や全条項の一致は確認できない。

## AdSense方針と残るゲート

Google公式は十分な独自コンテンツと明確なナビゲーション、未完成・リンク切れのないサイトを求め、広告をメニューと誤認させる設計を禁じている。参照：[不承認の一般的理由](https://support.google.com/adsense/answer/81904)、[ページ準備](https://support.google.com/adsense/answer/7299563)、[プログラムポリシー](https://support.google.com/adsense/answer/48182)、[Privacyの記載](https://support.google.com/adsense/answer/1348695)、[CMP案内](https://support.google.com/adsense/answer/7670013)（2026-11-01確認）。一般的な指針であり、このサイト固有の不承認理由ではない。

1. SORAがAdSense管理画面で現在の不承認理由、サイト状態、ads.txt認識、対象地域別のCMPを確認する。現時点では**確認できない**。
2. SAFE側で正式文書の「未施行」表示と運営方針URLを確認・修正する担当作業が必要。承認済み本文は変更しない。
3. 旧PHP URLの実HTTP応答を許可された検証環境で確認し、必要ならホスト側の301/308とMIMEを修正する。
4. WebP候補を隔離検証し、iPhone実機で文字の判読、横はみ出し、メニュー、フォーム、主要記事を確認する。公開後にPageSpeedを再計測する。
5. Search Consoleで主要記事のインデックス状態とサイトマップ処理を確認する。ブラウザ表示だけでは確定しない。

本番ソースはこの監査の開始時点で上記main。以後の隔離候補はmainや本番へ反映しない。公開可否は残るゲート解消後に再判定する。

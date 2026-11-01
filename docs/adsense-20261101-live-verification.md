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

- トップのモバイル2回：Performance **40 / 66**、LCP **7.3 / 7.1秒**、CLS **1.000 / 0**、TBT **60 / 210 ms**、FCP **3.9 / 2.9秒**。フィールドデータは「No Data」。変動が大きいのでCLSの原因は確定できない。画像JPEGは573.7KiB、Lighthouseは約488KiBの節約余地を提示。Google広告の第三者コードも転送・主スレッド時間に影響するが、コードは変更しない。
- `start-guide.html` のモバイル1回：Performance **100**、LCP **0.8秒**、CLS **0**。単発のラボ値で全ページの速度を代表しない。
- トップのデスクトップ1回：Performance **96**、LCP **1.3秒**、CLS **0**。同じ計測URLのデスクトップ表示。Best Practicesの非推奨API警告はGoogle広告の `lidar.js` に由来し、サイトの独自コードとは確認されなかった。
- 原画像JPEGは保持し、同じ1199×1312pxのWebP（約153KB）を優先配信する隔離候補を作成。ロゴ・文字・PITO/RONAは視覚確認済み。配信後のLCP改善量は未測定。
- 計測結果：[トップ1回目](https://pagespeed.web.dev/analysis/https-delipit-jp/9h5tdigisw?form_factor=mobile)、[トップ2回目](https://pagespeed.web.dev/analysis/https-delipit-jp/hy915de45z?form_factor=mobile)、[開業ガイド](https://pagespeed.web.dev/analysis/https-delipit-jp-start-guide-html/arawib6zev?form_factor=mobile)。

### PR #19 継続調査と隔離改善

- 2回目のモバイルLighthouseでLCP要素は採用ヒーロー画像の `<img class="hero-art">`。画像配信診断はJPEG **573.7 KiB**、推定節約 **488.1 KiB**。LCP breakdownの表示はresource load delay 40 ms、load duration 80 ms、element render delay **1,140 ms**。これは診断の部分時間であり、全体LCP 7.1秒と単純に合算・同一視しない。画像転送だけで全遅延の解消は保証できない。
- 既存WebP候補は1199×1312、約153 KB。原JPEG 587,438 bytesは保持。WebPへの切替は `<picture>` 内、`width`・`height`・`fetchpriority="high"` は既存設定。追加でWebPのhead preloadと画像の `loading="eager"` を指定し、CSSと並行して優先取得できる候補にした。プリロードと実際の `<source>` は同一URLを指す。画像内容やCSSの表示構図は変更していない。
- **変更後のPageSpeed比較は未実施**。PRは未マージ・未配信で、既存の確認用Siteは所有者限定のため、外部のPageSpeed Insightsが同じページを計測できない。異なるホストや広告条件を本番前後の同条件比較とは扱わない。隔離候補を外部計測可能な同一URLへ配信できた段階で、同じモバイル設定・広告状態で複数回計測し、LCP/CLS/TBTを分布で比較する。フィールドINPは双方ともNo Dataのため確認できない。効果が確認できるまでマージ・本番反映しない。
- SAFE旧資料は3ページともnoindex、Privacy・規約には旧版注意文が既にある。旧「ご利用案内」の冒頭だけが正式公開前の表現だったため、本文・正式文書に触れず、履歴である旨と現行SAFEへの案内に変更した。ページ内に残るTEST BUILD等は2026年10月19日の履歴として扱う。正式SAFEの「未施行」併記と運営方針取得不能はポータルから直せず、SAFE側の所有者確認事項として残す。
- 最新main `8c649dffe2bdeb87eff087d9e6ac59bb96a831e9` と作業開始時のPR #19 head `497628f6d756c882c8c62b6756a8966a335faca1` を2026年11月1日に再照合。PR差分はWebP、トップの画像マークアップ、旧資料3件のmetadata、監査記録の6ファイル。追加変更もトップと旧「ご利用案内」の注意文に限る。mainへの上書き・記事URL・正式規約本文への変更なし。

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

## 2026-11-02：PR #19（5e0384bb）継続検証

**判定：HOLD。** PRはDraftのまま維持し、マージ・本番公開・AdSense再申請を行っていない。変更後のモバイルLCP/CLS/TBTをPageSpeed Insightsで各3回測定する条件を満たせず、改善効果は確認できない。

### 比較対象と隔離プレビュー

- 本番相当の変更前ソースは最新 origin/main 0842a789113cb0ddaa9e945a7c1d49783b374789、変更後は同mainにPR #19 head 5e0384bb9aec5991d43e01fa9bf3cba947c2006b の差分を重ねた隔離静的プレビュー。ローカル管理プレビュー http://terminal.local:4173/before/ と /after/ で同一ホスト上の表示を比較した。これは外部公開URLではなく、iPhone実機やPageSpeed Insightsからアクセスできるとは確認できない。
- 変更前はJPEG、変更後はpictureからWebPを選択することをブラウザのcurrentSrcと読み込み完了状態で確認。WebPを無効にした専用試験ページでは同じJPEGが表示された。両画像は1199×1312px、転送元ファイルはWebP 152,874 bytes／JPEG 587,438 bytes。画像の外観・構図を変えるCSS変更はない。
- 変更後の画像に width=1199、height=1312、loading=eager、fetchpriority=high、decoding=async があり、head内に同じWebPのpreloadがあることをDOMで確認。実際のネットワーク優先度とLCP改善量はPageSpeedで未確認。
- Chromiumの隔離iframeを375／390／430pxに設定し、各幅で変更前後の画像が完了し、画像寸法が同じで、文書幅と表示領域幅が一致（横はみ出しなし）、ヘッダーと画像の重なりなしと確認。これはiPhone Safari実機表示の代替ではない。デスクトップの画面上で採用画像のロゴ・見出し・車両・PITO/RONAの構図を確認したが、各幅で画像内文字の実機判読は未確認。

| モバイル幅 | 変更前／後の画像表示幅 | 高さ | 横はみ出し・ヘッダー重なり |
| --- | ---: | ---: | --- |
| 375px | 359px | 約392.8px | なし／なし |
| 390px | 374px | 約409.2px | なし／なし |
| 430px | 414px | 約453.0px | なし／なし |

### PageSpeedの比較条件

- 本番の既存モバイル計測2回はLCP **7.3／7.1秒**、CLS **1.000／0**、TBT **60／210ms**。3回目の変更前計測および変更後の同条件3回以上の計測は未実施。フィールドINPはNo Data。これら2回と隔離ブラウザでの表示確認を前後比較の性能値として扱わない。
- PageSpeed Insightsで特定された本番のLCP要素はヒーロー画像。JPEGの転送診断573.7KiB、画像改善の推定488.1KiB、ある計測のelement render delay 1,140ms。WebPのファイルサイズ差だけで実際のLCP短縮量は確定できない。
- 隔離プレビューはローカルホストで、既存の確認用Siteも所有者限定。外部PageSpeed Insightsから変更後を取得できない。観測条件を揃えるには、アクセス可能な隔離URLに変更前／後を同時配信して同じモバイル設定・広告状態で各3回以上測るか、Lighthouse/Chromeを同一ローカル環境に用意して同じ端末エミュレーション・スロットリング・キャッシュ条件で各3回以上測る必要がある。所有者限定サイトの公開範囲は計測のために変更しない。

### 最新mainとの差分

- mainの前回基点からの追加変更は data/driver-news.json のみ。PR #19の差分はWebP、トップ画像読み込み、旧SAFE資料3ページ、監査記録の計6ファイルで、追加main変更との重複なし。git merge-tree は競合なしでtree 111129b359df7092208d0230a56d9f9a9b92557a を生成した。PRのDraft状態を維持し、記事・URL・規約・アプリには触れていない。

### SAFEの「未施行」表示（調査のみ）

- 2026-11-02の公開表示で /terms、/privacy は「版 V99／適用日 2026-11-01／同意強制開始 2026-11-01T00:00:00+09:00」と「所有者承認済み本文（未施行）」が併存。/operator-policy も現在は本文を表示し、同じ併記を確認した。前日の運営方針取得不能は継続する問題とは扱わない。実際の同意強制の稼働状態や同意履歴は確認していない。
- SAFEリポジトリの scripts/prepare-legal-activation.mjs は適用日表示を書き換える一方、見出し置換では旧文字列「所有者承認済み本文を基にしたCloudflare向け候補・未施行の全文候補」を探している。現在の dist/client/terms.html と privacy.html の見出しは「所有者承認済み本文（未施行）」で一致せず、活性化時に古い見出しが残り得る。公開表示との整合から、この文字列不一致が原因の有力な推定であり、本番の生成経路全体は未確認。
- SAFE側の別作業では、表示用候補だけで正確な見出しを直し、3ページの活性化後表示から「未施行」を検査し、承認済み本文のハッシュが不変であることを確認するのが妥当。今回はSAFE本体、正式文書本文、同意履歴、利用者データを変更していない。

**次のゲート：** 同条件の変更前後各3回以上のLCP/CLS/TBT、iPhone実機の画像文字とレイアウト、SAFE表示矛盾の別作業での解消を確認してからREADYを再判定する。

## 2026-11-02：ローカルLighthouse同条件比較（PR #19 続報）

**本番反映判定：HOLD。** ローカル計測ではWebP候補のLCP改善を確認した。PRはDraft、mainへのマージ・本番公開は未実施。以下は本番PageSpeedやiPhone実機の値ではない。前節の「各3回未実施」は、この続報の実行前時点の記録である。

### 再現条件と生データ

- ソース：最新main 0842a789113cb0ddaa9e945a7c1d49783b374789 を before、同mainにPR #19 head 39823b82ae57eb5d8e221e2b240bf18594fc0562 のサイト差分を重ねたものを after。両者を同一Python静的サーバーの /before/、/after/ に置き、before→afterを3組、順番に実行した。
- Lighthouse 12.8.2、Chromium 141.0.7390.0（同一バイナリ）。モバイル390×844、deviceScaleFactor 3、formFactor mobile、simulate方式、RTT 150ms、downlink 1638.4Kbps、CPU slowdown 4倍。各実行で新規Chromeを起動し、Lighthouseのストレージ初期化を有効にした。計測はperformanceカテゴリのみ。ローカルHTTPサーバーで実転送後にLighthouseが通信・CPUをシミュレーションするラボ値。
- 両バージョンで外部Google広告スクリプトは取得失敗（status -1）。本番の広告読み込みを含むTBTや実ユーザーのINPは再現できない。サイト自身のHTML・CSS・画像は各回HTTP 200で取得でき、LighthouseのrunWarningsは0件。

| 指標 | main 1 / 2 / 3 | PR #19 1 / 2 / 3 | 中央値 main → PR | 範囲 main / PR |
| --- | --- | --- | --- | --- |
| LCP | 4,431 / 4,353 / 4,429 ms | 2,328 / 2,328 / 2,329 ms | 4,429 → 2,328 ms（約2,101 ms短縮、約47%） | 4,353–4,431 / 2,328–2,329 ms |
| CLS | 0 / 0 / 0 | 0 / 0 / 0 | 0 → 0 | 0 / 0 |
| TBT | 0 / 44 / 0 ms | 0 / 0 / 0 ms | 0 → 0 ms | 0–44 / 0 ms |
| ヒーロー画像転送量 | 587,629 bytes ×3 | 153,065 bytes ×3 | 587,629 → 153,065 bytes（434,564 bytes減、約74%） | 変動なし / 変動なし |
| ページ総転送量（Lighthouse） | 652,204 bytes ×3 | 217,863 bytes ×3 | 652,204 → 217,863 bytes | 変動なし / 変動なし |
| Performance score | 85 / 85 / 85 | 98 / 98 / 98 | 85 → 98 | 変動なし / 変動なし |

LCP要素は各版とも採用ヒーロー画像で、表示ボックス390px幅で374×約409pxと同じ。Lighthouseのnetwork-requestsではmainがJPEG実体587,438 bytes、PRがWebP実体152,874 bytes。WebPの取得が同じURLから一回のみで、JPEGの同時取得はない。ファイルサイズ差とLCPの差には関連があるが、個別のpreload、priority、形式変換の寄与をこの比較だけで分離できない。TBT中央値0は改善の証拠と解釈しない。

### 画像・差分・SAFEの確認

- 同一Chromiumの390px DOM再確認：PRはWebPがcurrentSrc、画像はcompleteで1199×1312px、preloadはWebPを指し、fetchPriorityはhigh、loadingはeager。JPEGフォールバックの試験ページでsourceを無効にすると、currentSrcは保持したJPEGになり画像は完了。フォールバック用試験ページはWebP対応Chromium上で強制選択したため、preloadされたWebPも取得した。WebP非対応ブラウザでのpreload挙動までは確認できない。
- before/after/fallbackの表示ボックスは同じ374×約409px、横はみ出し・ヘッダー重なりなし。前節の375/390/430px確認も維持。画像内文字のiPhone Safari実機での読みやすさは確認できない。
- 最新main再取得後も0842a789のまま。PR差分6ファイル（ヒーローWebP、index、SAFE旧資料3ページ、監査記録）。git diff --checkはPASS、git merge-treeは競合なし。記事本文・記事URL・共通CSS・既存JPEG・規約本文・アプリ本体はPR差分に含まれない。ページ全体の本番動作と実機表示は未確認。
- PR版の35 HTMLでローカル参照721件を静的照合し、参照先欠落0件。トップの主要6カードは順に start-guide.html、contract-guide.html、driver-note-07.html、money-guide.html、safety-guide.html、driver-faq.html を指し、6ファイルが存在し本文を含む。HTTPでの各記事操作・フォーム送信・外部リンクは今回再検証していない。
- SAFEの未施行見出しは別件。対象はSAFE側の公開用表示生成と活性化後の3ページの見出しであり、承認済みの利用規約・Privacy・運営方針の本文やハッシュ、同意履歴・利用者データではない。別作業の検証条件：正しい現行見出しだけを表示候補で置換し、terms/privacy/operator-policyの適用日と見出しの矛盾がないこと、3つの承認済み本文ハッシュ不変、同意処理・履歴不変を確認する。今回はSAFEに変更なし。

ローカルのLCP改善は確認できたが、外部広告が読み込まれる本番と同条件でのPageSpeed検証、iPhone実機、SAFE表示矛盾、旧PHP等の監査残件があるため、公開・AdSense再申請はHOLDのまま。外部計測できる隔離URLを用意した場合は同条件3回以上を再計測する。

## 2026-11-02：外部アクセス可能な隔離受入（PR #19 続報）

**最終判定：HOLD。** 変更前後を同じ条件で比較したローカルLighthouseのLCP中央値は4,429→2,328ms、CLS 0→0、TBT 0→0ms（各3回）。PR #19のヒーロー配信候補はローカルで改善した。一方、外部PageSpeedの隔離版はCLS 1.000が3回中2回、LCPは3回とも5秒を超えた。公開前の重大な未解決事項として扱う。前節までの「外部PageSpeed未実施」は、この続報以前の状態を記したもの。

### 隔離URLと配信内容

- 既存のDELIPIT確認用Siteは所有者限定・別の試作内容のため、変更していない。新規の専用Site https://delipit-pr19-lcp-review-20261102.inthesky08.chatgpt.site/ にPR #19版を複製して配信。Sites source commit 486aa55493ec9ce9790fe7fb42f0526f460e51d8、version 1、deployment appgdep_6ae7c1c411a88191bb31322a885312ad（succeeded）。本番 delipit.jp とGitHub main/PRの公開状態は変更なし。
- プレビューは検索重複を避けるため全HTMLのrobots metaをnoindex,nofollow、robots.txtをDisallow: /とし、リポジトリの開発用メタデータを配信から除外した。この差と別ホスト/CDNのため、バイト単位でPR原本と同一のページではない。ヒーロー画像・CSS・記事本文・リンクは維持し、正式な規約本文は編集していない。PSIのSEO 69はプレビューの意図的なnoindexを含み、本番SEO判定に転用しない。
- 外部HTTPでトップ200/text/html、WebP 200/image/webp、JPEGを取得。公開画像のSHA-256は隔離元のWebP/JPEGとそれぞれ一致した。主要6カードの行き先は6件とも200/text/html。公開ブラウザでトップの本文と記事リンクを表示確認。公開DOMではWebP currentSrc、1199×1312px読み込み完了、WebP preload、fetchpriority high、loading eager。ローカルChromium再検証で375/390/430pxの横はみ出し・ヘッダー重なりなし。iPhone Safari実機は未確認。

### 外部PageSpeed Insights（隔離版、mobile）

| 回 | Performance | LCP | CLS | TBT | 出典 |
| --- | ---: | ---: | ---: | ---: | --- |
| 1 | 75 | 5.157秒 | 0 | 約1ms（UI表示0ms） | https://pagespeed.web.dev/analysis/https-delipit-pr19-lcp-review-20261102-inthesky08-chatgpt-site/rx0qevakru?form_factor=mobile |
| 2 | 43 | 5.175秒 | 1.000 | 40ms | https://pagespeed.web.dev/analysis/https-delipit-pr19-lcp-review-20261102-inthesky08-chatgpt-site/3adrlg6zwg?form_factor=mobile |
| 3 | 44 | 5.492秒 | 1.000 | 約39ms（UI表示40ms） | https://pagespeed.web.dev/analysis/https-delipit-pr19-lcp-review-20261102-inthesky08-chatgpt-site/s42z9onii2?form_factor=mobile |
| 中央値 | 44 | 5.175秒 | 1.000 | 約39ms | 3回のラボ計測 |

- 3回ともLighthouse 13.6.0、エミュレートMoto G Power、Slow 4G、HeadlessChromium 153.0.8010.36のmobile診断。フィールドデータはNo Dataで、INPは確認できない。
- 2回目のLayout shift culpritsは body のスコア1.000を示した。原因（サイトCSS、外部スクリプト、ホスト/CDN、計測環境のいずれか）は未確定。3回目のLCP要素は採用ヒーロー画像で、LCP breakdownはresource load delay約90ms、load duration約230ms、element render delay約2,000ms。画像圧縮だけでLCP 5秒超を解消できるとは断定しない。
- 別ホスト・異なるLighthouse版・異なる広告/キャッシュ/ネットワーク条件のため、過去の本番PageSpeed 7.3/7.1秒と隔離版5.157/5.175/5.492秒の差を本番改善率と扱わない。ローカルの同条件比較のみがPR前後差を示す。

### 残る受入条件

1. 隔離版のCLS 1.000をトレースで特定し、原因の再現・修正・同条件での再測定を行う。LCP 5秒超の表示遅延も、画像転送以外の要因を調査する。PRはDraftを維持。
2. SORAのiPhone Safariで隔離URLを開き、採用画像内の文字・PITO/RONAが読めること、横スクロールやヘッダー重なりがないこと、CTAと主要6カードから記事へ進めることを確認する。実機結果は未取得。
3. 最新main 0842a789とPR差分6ファイルを再照合。git merge-treeは競合なし、git diff --check PASS。SAFEの「未施行」は別件で、正式本文・同意履歴・データは本PRで変更しない。

隔離サイトは試験用の別URLであり、公式サイトの本番公開・AdSense再申請を意味しない。

### 隔離版の検索除外修正（同日）

初回配信の再点検で、トップ以外のHTMLに異なる形式の既存robots metaが残っていた。隔離Site内の42 HTMLをすべてnoindex,nofollowに統一し、version 2／deployment appgdep_6ae7c395e0308191b2ee86c3fd814dc8 を配信成功。外部で start-guide.html のnoindexを確認した。トップのindex.htmlは初回からnoindexで、version 1と2のGit blob SHAは同じ 5b065f57421c87cbb0e3dd4ef6ed3a330bf1c4ae。上記PageSpeed3回の対象トップの内容・指標にこの修正は影響しない。隔離Siteのsource commitは aa1d9a2a0ac2413daad5119c53c96d883e34105c。PR #19本体のHTMLと正式文書は変更していない。

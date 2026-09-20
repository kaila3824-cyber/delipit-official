DELIPIT 公式サイト / GitHub Pages deployment package

Version: v5.1 + GA4 privacy policy preparation
Updated: 2026-09-20

公開構成:
- delipit.jp = DELIPIT公式サイト
- app.delipit.jp = DELIPIT Webアプリ
- info@delipit.jp = 公式メール
- X @DELIPIT_JP = 公式X

v4.4 変更点:
- OGP / X Card metadata追加
- OGP画像 assets/og-delipit.jpg 追加
- Apple Touch Icon追加
- canonical / robots metadata追加
- 利用規約 terms.html 追加
- プライバシーポリシー privacy.html 追加
- robots.txt / sitemap.xml 追加
- フッターの規約リンクを実ページへ接続

GitHub Pages:
1. リポジトリへ本パッケージのファイルを反映
2. CNAME は既存の delipit.jp 設定を維持すること
3. Settings > Pages の Custom domain が delipit.jp であることを確認
4. Enforce HTTPS をONのまま維持

注意:
- CTAは https://app.delipit.jp/ に設定済みです。アプリ一般公開前はリンク先の公開状態を確認してください。
- ゲーム機能はサイト上でも「開発中」と明記しています。
- 広告・アクセス解析サービスを実際に導入した際は、プライバシーポリシーを実装内容に合わせて更新してください。
- 利用規約・プライバシーポリシーは一般的な公開準備用文面です。事業上の要件や実際のデータ処理が確定した段階で、必要に応じて専門家確認を行ってください。


v4.5.11.3: MANUAL / GAMIFICATION pages added; navigation and sitemap updated.


AdSense審査準備 (2026-09-20):
- AdSense site verification code (ca-pub-9142850138364995) をHTML各ページの head に追加
- ルートに ads.txt を追加
- privacy.html の広告項目をGoogle AdSense導入に合わせて更新
- 自動広告の設定変更・広告枠の追加は行っていません


v5.1 GA4プライバシーポリシー対応 (2026-09-20):
- privacy.html に Google Analytics 4（GA4）の利用目的・取得される一般的な技術情報を明記
- DELIPIT独自イベントで配送件数・売上・単価・経費・税額・支払金額・メモ・バックアップ内容等の業務データを送信しない方針を明記
- 氏名・メールアドレス等の直接識別情報をDELIPIT独自計測項目として送信しない方針を明記
- Cookie等の利用と、地域・利用形態に応じた同意対応方針を追記
- Google AdSenseの記載を独立項目として維持
- GA4測定タグそのものは公式サイトには追加していません（Webアプリ側のAnalytics実装とは分離）

v5.2 TOP current-app sync (2026-09-21):
- TOPのGAMIFICATION — COMING SOON表記を削除し、実装済みDELIPIT GAMEとして更新
- FEATURESを現行DELIPITに合わせ、配送実績・売上 / 経費・入金 / 月間・年間収支 / 消費税 / GAME MODE / 設定・バックアップへ再整理
- 最新実機スクリーンショット（配送入力 / DRIVER STATUS）をTOPへ反映
- GAME MODEが任意であり、OFFでも基本機能を利用できる旨を明記
- meta description / OGP / X descriptionを現行機能に合わせて更新
- manual.htmlは複数会社対応・カレンダー等の確定後に最終更新するため今回は変更なし
- privacy.html / terms.html / AdSense / GA4プライバシー記載 / CNAME等は変更なし


v5.2.2 TOP minor update (2026-09-21)
- ADD TO HOME SCREEN icon updated to current DELIPIT app icon
- Simplified browser/home-screen installation wording
- Simplified automatic update wording
- No changes to manual, terms, privacy, GA4, AdSense, CNAME or app logic


[v5.2.2]
- GAME SYSTEMページのACTUAL GAME SCREEN注記から「開発中」を削除。現行実装済みの実機表示例として表現を更新。

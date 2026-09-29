DELIPIT DRIVER NEWS - Xserver Cron setup

1) Upload this ZIP contents to delipit.jp public_html.
2) Confirm driver-news.html opens normally. It is STATIC HTML; PHP source will never be exposed there.
3) In Xserver Server Panel > Cron settings, run _cron/update_driver_news.php periodically.
   Recommended: 4 times/day (00:15, 06:15, 12:15, 18:15 JST).
4) Use the PHP command path shown in Xserver Server Information > Command path list.
   Example only (replace SERVER_ID/domain/PHP version with your actual values):
   /usr/bin/php8.3 /home/SERVER_ID/delipit.jp/public_html/_cron/update_driver_news.php
5) The script writes only: data/driver-news.json
6) If fetching fails, the updater does not intentionally delete the existing JSON before a successful write.
7) After Cron runs, open data/driver-news.json and driver-news.html to confirm Japanese text and links.

IMPORTANT:
- Do not guess the PHP command path. Use Xserver's displayed command path.
- Keep source whitelist conservative. Review source terms before adding a new source.
- DRIVER NOTE is intentionally not published in this build (COMING LATER only).

DELIPIT DRIVER NEWS v3.0 patch

Replace these 3 files in the GitHub repository:
- driver-news.html
- scripts/update_driver_news.py
- data/driver-news.json

Changes:
1. Fixes Japanese mojibake by robust UTF-8/CP932/Shift_JIS/EUC-JP decoding.
2. Fixes mobile width overflow and aligns hero/notice/cards to one responsive container.
3. Seeds a verified light-cargo history from official MLIT primary sources (2022-2026).
4. Future GitHub Actions runs MERGE new items into history instead of replacing history.
5. URL-based deduplication and corrupt-title rejection.

After commit: Actions > Update DRIVER NEWS > Run workflow.
Expected: non-zero items and readable Japanese titles.

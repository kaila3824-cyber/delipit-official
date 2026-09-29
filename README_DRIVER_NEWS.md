# DELIPIT DRIVER NEWS — GitHub Actions / Cloudflare Pages

## How it works
1. `.github/workflows/update-driver-news.yml` runs automatically four times per day.
2. `scripts/update_driver_news.py` reads selected official primary-source pages and filters driver-relevant links.
3. It writes `data/driver-news.json` only when source fetching succeeds.
4. The workflow commits the JSON only when it changed.
5. If this repository is connected to Cloudflare Pages with automatic production deployments enabled, that push triggers a new deployment.
6. `driver-news.html` reads the static JSON in the browser. No PHP is used.

## First test after uploading to GitHub
GitHub repository → Actions → **Update DRIVER NEWS** → **Run workflow**.
After the run finishes, check that `data/driver-news.json` contains items and Cloudflare Pages completes the deployment.
Then open `https://delipit.jp/driver-news.html`.

## Schedule
06:17 / 12:17 / 18:17 / 00:17 JST (GitHub cron is written in UTC).
The minute is intentionally `17` instead of `00` to reduce schedule congestion.

## Failure behavior
- If every source fetch fails, the script exits with an error and does not overwrite the existing JSON.
- If sources respond but no relevant item is found, an existing non-empty JSON is preserved.
- No full article text or source images are copied.

## Sources in v1
- 国土交通省 報道発表資料: https://www.mlit.go.jp/report/press/
- 国税庁 新着情報: https://www.nta.go.jp/information/news/news.htm

Source additions should be reviewed individually before being added to the whitelist.

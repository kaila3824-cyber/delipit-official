#!/usr/bin/env python3
"""Check the legacy PHP files locally, then verify the public redirect gate.

Only status, MIME, location and size are reported. Response bodies and possible
credentials are never printed. Run without --live before publishing a candidate;
run with --live after enabling the front-layer redirect.
"""

import argparse
import re
import sys
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import HTTPRedirectHandler, Request, build_opener


ROOT = Path(__file__).resolve().parents[1]
PATHS = ("/driver-news.php", "/assets/driver-news.php")
DESTINATION = "https://delipit.jp/driver-news.html"


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        return None


def local_guard():
    failures = []
    tracked = sorted(p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*.php") if ".git" not in p.parts)
    expected = [path.lstrip("/") for path in PATHS]
    if tracked != sorted(expected):
        failures.append(f"PHP file inventory changed: {len(tracked)} found, {len(expected)} expected")
    for name in tracked:
        data = (ROOT / name).read_bytes()
        if not data.lstrip().lower().startswith(b"<!doctype html>"):
            failures.append(f"{name}: not static HTML")
        if re.search(rb"<\?(?:php|=)|-----BEGIN [A-Z ]*PRIVATE KEY-----", data, re.I):
            failures.append(f"{name}: PHP code or private key marker detected")
    print(f"Local PHP inventory: {len(tracked)}; guard: {'FAIL' if failures else 'PASS'}")
    return failures


def request(method, url):
    opener = build_opener(NoRedirect)
    req = Request(url, method=method, headers={"User-Agent": "DELIPIT-release-check/1.0"})
    try:
        response = opener.open(req, timeout=20)
    except HTTPError as error:
        response = error
    with response:
        # Never log or inspect the public body for secrets here.
        return response.status, response.headers.get("Content-Type", ""), response.headers.get("Location"), response.read()


def live_gate():
    failures = []
    for path in PATHS:
        for method in ("HEAD", "GET"):
            try:
                status, mime, location, body = request(method, "https://delipit.jp" + path)
            except Exception as error:
                failures.append(f"{path} {method}: request failed ({type(error).__name__})")
                continue
            # Redirects may include a short explanatory HTML body.
            ok = status in (301, 308) and location == DESTINATION
            print(f"{path} {method}: status={status} location={'expected' if location == DESTINATION else 'unexpected'} body_bytes={len(body)} {'PASS' if ok else 'FAIL'}")
            if not ok:
                failures.append(f"{path} {method}: redirect gate failed")
    try:
        status, mime, _, body = request("GET", DESTINATION)
        ok = status == 200 and mime.lower().startswith("text/html") and bool(body)
        print(f"Destination GET: status={status} mime={mime} body_bytes={len(body)} {'PASS' if ok else 'FAIL'}")
        if not ok:
            failures.append("Destination GET: HTML gate failed")
    except Exception as error:
        failures.append(f"Destination GET: request failed ({type(error).__name__})")
    return failures


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true", help="also verify production GET/HEAD redirect acceptance")
    args = parser.parse_args()
    problems = local_guard()
    if args.live:
        problems.extend(live_gate())
    for problem in problems:
        print("FAIL:", problem, file=sys.stderr)
    sys.exit(bool(problems))

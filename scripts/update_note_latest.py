#!/usr/bin/env python3
from pathlib import Path
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET
from html import escape, unescape
import re
from datetime import datetime

RSS_URL = "https://note.com/delipit/rss"
INDEX = Path(__file__).resolve().parents[1] / "index.html"
START = "<!-- NOTE_LATEST_START -->"
END = "<!-- NOTE_LATEST_END -->"

req = Request(RSS_URL, headers={"User-Agent": "DELIPIT-site-updater/1.0"})
with urlopen(req, timeout=30) as r:
    xml = r.read()
root = ET.fromstring(xml)
item = root.find("./channel/item")
if item is None:
    raise RuntimeError("note RSS に記事が見つかりません")

def txt(tag):
    el = item.find(tag)
    return (el.text or "").strip() if el is not None and el.text else ""

title = txt("title")
link = txt("link")
pub = txt("pubDate")
desc = txt("description")
if not title or not link:
    raise RuntimeError("note RSS のタイトルまたはURLを取得できません")

# RFC 2822 pubDate -> YYYY.MM.DD
try:
    from email.utils import parsedate_to_datetime
    d = parsedate_to_datetime(pub)
    date_text = d.strftime("%Y.%m.%d")
except Exception:
    date_text = datetime.now().strftime("%Y.%m.%d")

# HTML description -> compact plain-text teaser
plain = re.sub(r"<[^>]+>", " ", unescape(desc))
plain = re.sub(r"\s+", " ", plain).strip()
if not plain:
    plain = "DELIPITの開発と配送の現場から、最新の記事をお届けします。"
if len(plain) > 86:
    plain = plain[:85].rstrip() + "…"

card = f'''{START}\n<article class="note-latest"><div class="tag">NEW / {escape(date_text)}</div><h3>{escape(title)}</h3><p>{escape(plain)}</p><a href="{escape(link, quote=True)}" target="_blank" rel="noopener noreferrer">この記事を読む →</a></article>\n{END}'''

html = INDEX.read_text(encoding="utf-8")
pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
if not pattern.search(html):
    raise RuntimeError("index.html の NOTE 最新記事マーカーが見つかりません")
updated = pattern.sub(card, html, count=1)
if updated != html:
    INDEX.write_text(updated, encoding="utf-8")
    print(f"Updated: {title} ({date_text})")
else:
    print("No change")

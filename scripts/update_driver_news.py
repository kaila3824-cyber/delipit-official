#!/usr/bin/env python3
"""DELIPIT DRIVER NEWS updater for GitHub Actions.
Fetches selected official primary-source pages, keeps only driver-relevant links,
and writes data/driver-news.json. Existing data is preserved on total fetch failure.
"""
from __future__ import annotations
import json, re, sys, urllib.request
from datetime import datetime, timezone, timedelta
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "driver-news.json"
MAX_ITEMS = 40
UA = "DELIPIT-DriverNews/2.0 (+https://delipit.jp/)"
JST = timezone(timedelta(hours=9))

SOURCES = [
    {
        "id": "mlit_press",
        "name": "国土交通省",
        "url": "https://www.mlit.go.jp/report/press/",
        "category": "物流・業界",
        "allowed_hosts": {"www.mlit.go.jp", "mlit.go.jp"},
    },
    {
        "id": "nta_news",
        "name": "国税庁",
        "url": "https://www.nta.go.jp/information/news/news.htm",
        "category": "税・お金",
        "allowed_hosts": {"www.nta.go.jp", "nta.go.jp"},
    },
]

# Conservative relevance filter. Strong terms can pass alone; medium terms need combination.
STRONG = {
    "貨物軽自動車": 14, "軽貨物": 14, "宅配": 10, "事業用自動車": 10,
    "フリーランス": 10, "個人事業主": 10, "インボイス": 10,
    "確定申告": 10, "消費税": 9, "電子帳簿": 9,
}
MEDIUM = {
    "運送": 5, "物流": 4, "貨物": 4, "配送": 5, "交通安全": 5,
    "自動車運送": 6, "ドライバー": 6, "所得税": 5, "源泉徴収": 5,
    "年末調整": 4, "e-Tax": 4, "税務": 3,
}
EXCLUDE = ("酒類", "酒税", "航空", "港湾", "鉄道", "観光", "住宅", "建設", "不動産")
DATE_PATTERNS = [
    re.compile(r"(20\d{2})[年/.-](\d{1,2})[月/.-](\d{1,2})日?"),
    re.compile(r"令和(\d{1,2})年(\d{1,2})月(\d{1,2})日"),
]

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links=[]; self.href=None; self.buf=[]
    def handle_starttag(self, tag, attrs):
        if tag.lower()=="a":
            self.href=dict(attrs).get("href"); self.buf=[]
    def handle_data(self, data):
        if self.href is not None: self.buf.append(data)
    def handle_endtag(self, tag):
        if tag.lower()=="a" and self.href is not None:
            text=re.sub(r"\s+"," ","".join(self.buf)).strip()
            if text: self.links.append((self.href,text))
            self.href=None; self.buf=[]

def fetch(url:str)->str:
    req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"text/html,application/xhtml+xml"})
    with urllib.request.urlopen(req,timeout=25) as r:
        raw=r.read()
        charset=r.headers.get_content_charset() or "utf-8"
    try: return raw.decode(charset,errors="replace")
    except LookupError: return raw.decode("utf-8",errors="replace")

def score(title:str)->int:
    s=sum(v for k,v in STRONG.items() if k.lower() in title.lower())
    s+=sum(v for k,v in MEDIUM.items() if k.lower() in title.lower())
    if any(x in title for x in EXCLUDE) and not any(k in title for k in STRONG): s-=8
    return s

def extract_date(text:str)->str:
    for i,p in enumerate(DATE_PATTERNS):
        m=p.search(text)
        if not m: continue
        y,mo,d=map(int,m.groups())
        if i==1: y=2018+y  # Reiwa 1 = 2019
        try: return f"{y:04d}-{mo:02d}-{d:02d}"
        except ValueError: pass
    return ""

def load_previous():
    try:
        d=json.loads(OUT.read_text(encoding="utf-8"))
        return d if isinstance(d,dict) else {"generatedAt":None,"items":[]}
    except Exception:
        return {"generatedAt":None,"items":[]}

def main()->int:
    previous=load_previous(); found={}; successes=0; errors=[]
    for src in SOURCES:
        try:
            html=fetch(src["url"]); successes+=1
        except Exception as e:
            errors.append(f'{src["id"]}: {type(e).__name__}: {e}')
            continue
        p=LinkParser(); p.feed(html)
        for href,title in p.links:
            if len(title)<8: continue
            points=score(title)
            if points<9: continue
            full=urljoin(src["url"],href)
            u=urlparse(full)
            if u.scheme not in {"http","https"} or u.hostname not in src["allowed_hosts"]: continue
            cat=src["category"]
            if any(k in title for k in ("安全","事故","交通")): cat="安全"
            if any(k in title for k in ("税","確定申告","インボイス","e-Tax","帳簿")): cat="税・お金"
            if any(k in title for k in ("法","制度","規則","改正")): cat="法令・制度"
            found[full]={"title":title,"publishedAt":extract_date(title),"sourceName":src["name"],"sourceUrl":full,"category":cat,"_score":points}

    if successes==0:
        print("All sources failed; preserving previous JSON.", file=sys.stderr)
        for e in errors: print(e,file=sys.stderr)
        return 1

    items=list(found.values())
    # Prefer dated/newer items, then relevance. Undated official links remain usable.
    items.sort(key=lambda x:(x["publishedAt"],x["_score"],x["title"]), reverse=True)
    items=items[:MAX_ITEMS]
    for x in items: x.pop("_score",None)

    # If sources responded but filter yielded nothing, preserve previous non-empty data.
    if not items and previous.get("items"):
        print("No relevant items found; preserving previous non-empty JSON.")
        return 0

    payload={"generatedAt":datetime.now(JST).isoformat(timespec="seconds"),"items":items}
    OUT.parent.mkdir(parents=True,exist_ok=True)
    tmp=OUT.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    tmp.replace(OUT)
    print(f"Updated DRIVER NEWS: {len(items)} items; sources ok={successes}/{len(SOURCES)}")
    for e in errors: print("WARN",e,file=sys.stderr)
    return 0

if __name__=="__main__": raise SystemExit(main())

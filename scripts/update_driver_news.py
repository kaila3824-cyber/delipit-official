#!/usr/bin/env python3
"""DELIPIT DRIVER NEWS updater v3.0.
Official-source links only. Keeps clean history, merges newly discovered items,
and writes UTF-8 JSON for the static DRIVER NEWS page.
"""
from __future__ import annotations
import json, re, sys, urllib.request
from datetime import datetime, timezone, timedelta
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "driver-news.json"
MAX_ITEMS = 80
UA = "DELIPIT-DriverNews/3.0 (+https://delipit.jp/)"
JST = timezone(timedelta(hours=9))

SOURCES = [
    {"id":"mlit_press","name":"国土交通省","url":"https://www.mlit.go.jp/report/press/","category":"物流・業界","allowed_hosts":{"www.mlit.go.jp","mlit.go.jp"}},
    {"id":"nta_news","name":"国税庁","url":"https://www.nta.go.jp/information/news/news.htm","category":"税・お金","allowed_hosts":{"www.nta.go.jp","nta.go.jp"}},
]
STRONG={"貨物軽自動車":14,"軽貨物":14,"宅配":10,"事業用自動車":10,"フリーランス":10,"個人事業主":10,"インボイス":10,"確定申告":10,"消費税":9,"電子帳簿":9}
MEDIUM={"運送":6,"物流":5,"貨物":5,"配送":6,"交通安全":6,"自動車運送":7,"ドライバー":7,"道路運送":7,"所得税":6,"e-Tax":5,"青色申告":7,"記帳":5,"納税":4}
EXCLUDE=("酒類","酒税","航空","港湾","鉄道","観光","住宅","建設","不動産")
SOURCE_TOPICS={
 "mlit_press":("運送","物流","貨物","配送","宅配","ドライバー","事業用自動車","軽自動車","交通安全","道路運送"),
 "nta_news":("確定申告","所得税","消費税","インボイス","e-Tax","電子帳簿","青色申告","記帳","納税","個人事業主","フリーランス"),
}
DATE_PATTERNS=[re.compile(r"(20\d{2})[年/.-](\d{1,2})[月/.-](\d{1,2})日?"),re.compile(r"令和(\d{1,2})年(\d{1,2})月(\d{1,2})日")]

class LinkParser(HTMLParser):
    def __init__(self): super().__init__(convert_charrefs=True); self.links=[]; self.href=None; self.buf=[]
    def handle_starttag(self,tag,attrs):
        if tag.lower()=="a": self.href=dict(attrs).get("href"); self.buf=[]
    def handle_data(self,data):
        if self.href is not None: self.buf.append(data)
    def handle_endtag(self,tag):
        if tag.lower()=="a" and self.href is not None:
            t=re.sub(r"\s+"," ","".join(self.buf)).strip()
            if t: self.links.append((self.href,t))
            self.href=None; self.buf=[]

def _badness(s:str)->int:
    # Japanese official pages should not contain replacement chars or classic mojibake runs.
    return s.count("�")*1000 + s.count("\ufffd")*1000 + sum(s.count(x)*30 for x in ("縺","譁","蜿","繧","莨","鬆"))

def decode_html(raw:bytes, header_charset:str|None)->str:
    # Some government pages have historically mixed/legacy encodings. Try the
    # declared encoding plus common Japanese encodings and select the cleanest decode.
    candidates=[]
    for enc in (header_charset,"utf-8","cp932","shift_jis","euc_jp"):
        if not enc or enc in [e for e,_ in candidates]: continue
        try: candidates.append((enc,raw.decode(enc,errors="replace")))
        except (LookupError,UnicodeDecodeError): pass
    if not candidates: return raw.decode("utf-8",errors="replace")
    return min(candidates,key=lambda p:_badness(p[1]))[1]

def fetch(url:str)->str:
    req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"text/html,application/xhtml+xml"})
    with urllib.request.urlopen(req,timeout=25) as r:
        raw=r.read(); charset=r.headers.get_content_charset()
    return decode_html(raw,charset)

def score(t:str)->int:
    low=t.lower(); s=sum(v for k,v in STRONG.items() if k.lower() in low)+sum(v for k,v in MEDIUM.items() if k.lower() in low)
    if any(x in t for x in EXCLUDE) and not any(k in t for k in STRONG): s-=8
    return s

def extract_date(t:str)->str:
    for i,p in enumerate(DATE_PATTERNS):
        m=p.search(t)
        if not m: continue
        y,mo,d=map(int,m.groups()); y=2018+y if i==1 else y
        try: datetime(y,mo,d); return f"{y:04d}-{mo:02d}-{d:02d}"
        except ValueError: pass
    return ""

def clean_item(x):
    if not isinstance(x,dict): return None
    title=str(x.get("title","")).strip(); src=str(x.get("sourceUrl","")).strip()
    if not title or not src or "�" in title: return None
    return {"title":title,"publishedAt":str(x.get("publishedAt","")).strip(),"sourceName":str(x.get("sourceName","")).strip(),"sourceUrl":src,"category":str(x.get("category","DRIVER NEWS")).strip() or "DRIVER NEWS"}

def load_previous():
    try:
        d=json.loads(OUT.read_text(encoding="utf-8")); return [y for x in d.get("items",[]) if (y:=clean_item(x))]
    except Exception: return []

def main()->int:
    previous=load_previous(); found={x["sourceUrl"]:x for x in previous}; successes=0; errors=[]
    for src in SOURCES:
        try: html=fetch(src["url"]); successes+=1
        except Exception as e: errors.append(f'{src["id"]}: {type(e).__name__}: {e}'); continue
        p=LinkParser(); p.feed(html)
        print(f"{src['id']}: extracted {len(p.links)} links")
        accepted=0
        for href,title in p.links:
            if len(title)<8 or "�" in title: continue
            pts=score(title); topic=any(k.lower() in title.lower() for k in SOURCE_TOPICS.get(src["id"],()))
            if pts<9 and not(topic and pts>=4): continue
            if any(x in title for x in EXCLUDE) and not any(k in title for k in STRONG): continue
            full=urljoin(src["url"],href); u=urlparse(full)
            if u.scheme not in {"http","https"} or u.hostname not in src["allowed_hosts"]: continue
            cat=src["category"]
            if any(k in title for k in ("安全","事故","交通")): cat="安全"
            if any(k in title for k in ("税","確定申告","インボイス","e-Tax","帳簿")): cat="税・お金"
            if any(k in title for k in ("法","制度","規則","改正")): cat="法令・制度"
            # Do not replace a curated history item with a poorer undated scrape.
            old=found.get(full)
            item={"title":title,"publishedAt":extract_date(title),"sourceName":src["name"],"sourceUrl":full,"category":cat}
            if not old or (not old.get("publishedAt") and item["publishedAt"]): found[full]=item
            accepted+=1
        print(f"{src['id']}: accepted {accepted} relevant links")
    if successes==0:
        print("All sources failed; preserving previous JSON.",file=sys.stderr)
        for e in errors: print("WARN",e,file=sys.stderr)
        return 1
    items=list(found.values())
    items.sort(key=lambda x:(x.get("publishedAt","") or "0000-00-00",x.get("title","")),reverse=True)
    items=items[:MAX_ITEMS]
    payload={"generatedAt":datetime.now(JST).isoformat(timespec="seconds"),"items":items}
    OUT.parent.mkdir(parents=True,exist_ok=True); tmp=OUT.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); tmp.replace(OUT)
    print(f"Updated DRIVER NEWS: {len(items)} items; sources ok={successes}/{len(SOURCES)}")
    for x in items[:12]: print(f"  {x['publishedAt'] or 'date n/a'} [{x['category']}] {x['sourceName']}: {x['title']}")
    for e in errors: print("WARN",e,file=sys.stderr)
    return 0
if __name__=="__main__": raise SystemExit(main())

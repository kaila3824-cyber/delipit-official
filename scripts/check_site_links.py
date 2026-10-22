"""Check local links, fragments, and sitemap canonical alignment."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.canonical = None
        self.title = 0
        self.description = 0
        self.h1 = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href")
        if tag == "title":
            self.title += 1
        if tag == "meta" and a.get("name") == "description":
            self.description += 1
        if tag == "h1":
            self.h1 += 1


pages = {}
for path in ROOT.glob("*.html"):
    page = Page()
    page.feed(path.read_text(encoding="utf-8"))
    pages[path.name] = page

problems = []
checked = 0
for name, page in pages.items():
    if (page.title, page.description, page.h1) != (1, 1, 1):
        problems.append(f"{name}: title/description/h1 count")
    for link in page.links:
        url = urlparse(link)
        if url.scheme or link.startswith("//"):
            continue
        target = url.path.lstrip("/") or name
        if target.endswith("/"):
            target += "index.html"
        checked += 1
        if target not in pages and not (ROOT / target).exists():
            problems.append(f"{name}: missing {link}")
        elif url.fragment and target in pages and url.fragment not in pages[target].ids:
            problems.append(f"{name}: missing fragment {link}")

sitemap = [urlparse(n.text).path.lstrip("/") or "index.html"
           for n in ET.parse(ROOT / "sitemap.xml").findall(".//{*}loc")]
for target in sitemap:
    if target not in pages:
        problems.append(f"sitemap: missing {target}")
    elif pages[target].canonical != "https://delipit.jp/" + ("" if target == "index.html" else target):
        problems.append(f"sitemap: canonical mismatch {target}")

print(f"HTML={len(pages)} sitemap={len(sitemap)} internal_links={checked} problems={len(problems)}")
for problem in problems:
    print(problem)
raise SystemExit(bool(problems))

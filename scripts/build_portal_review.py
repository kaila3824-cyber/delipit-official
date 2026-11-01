from pathlib import Path
from lxml import html,etree
from urllib.parse import urlsplit
import shutil,re,sys
root=Path(__file__).resolve().parents[1];dist=Path(sys.argv[1]).resolve();dist.mkdir(parents=True,exist_ok=True)
source=(root/'portal-preview/index.html').read_text();css=(root/'portal-preview/portal.css').read_text()
source=source.replace('href="https://delipit.jp/field-workflow.html"','href="https://delipit.jp/driver-note-07.html"').replace('現場の流れを読む','SORAの現場記事を読む')
source=source.replace('積み込みや時間指定を組み立てたい','積み込みで荷物を見つけやすくしたい')
source=source.replace('配送の一日は、荷物を積む前から始まっている。','配送の一日は、荷物を積む前から始まっている。')
css+='''\n/* 2026-11-01 iPhone review: compact, readable, no overlapping header */
html{scroll-padding-top:22px}header{position:relative}body{line-height:1.7}.hero{padding-top:24px;padding-bottom:20px}.hero h1{font-size:clamp(29px,3.5vw,43px);line-height:1.35}.hero .intro{line-height:1.7;margin:12px 0 16px}.crew{height:230px}.pito{height:210px;width:170px;left:15%}.rona{height:160px;width:165px;right:13%;top:50px}.problems{padding-block:20px 38px}.problem-grid a{min-height:126px;padding:15px}.problem-grid strong{font-size:16px;margin:7px 0}.problem-grid small{font-size:14px;margin-top:auto}.topics{padding-bottom:32px}.topic-grid a{padding:12px 16px}.topic-grid small,.small,.caption{font-size:14px}.section-lead{font-size:16px;line-height:1.7}.beginner{padding:24px;margin-bottom:36px}.guide-pair,.safety,.stories,.tools,.about{padding-block:38px}.guide-pair{gap:36px}.article-list a{min-height:70px;padding-block:12px}.steps p,.story-grid p,.tool-grid p,.about>p:not(.eyebrow){font-size:16px;line-height:1.7}.eyebrow{font-size:12px}.menu nav a{font-size:16px;min-height:44px}.menu summary{font-size:16px;min-height:44px}.topic-no span{font-size:11px}.badge{font-size:12px}@media(max-width:620px){.wrap{width:calc(100% - 36px)}.review-note{font-size:11px}.header-row{min-height:58px}.brand img{width:110px;height:38px}.hero{padding-top:16px;padding-bottom:10px}.hero h1{font-size:30px;line-height:1.35}.intro{font-size:16px!important;margin:10px 0 12px!important}.crew{height:115px;width:230px;margin-top:2px}.crew-circle{inset:2px 25px}.pito{height:107px;width:88px;left:25px;top:3px}.rona{height:95px;width:103px;right:18px;top:12px}.crew-label,.crew-line{display:none}.hero .caption{font-size:13px}.problems{padding-block:18px 30px}.problems .section-heading{margin-bottom:8px}.problems .section-lead{font-size:14px;margin-bottom:12px}.problem-grid{grid-template-columns:1fr 1fr;gap:8px}.problem-grid a{min-height:103px;padding:11px 12px}.problem-grid strong{font-size:16px;line-height:1.45;margin:4px 0}.problem-grid span{font-size:13px}.problem-grid small{font-size:13px;line-height:1.4}.coming{font-size:14px}.topic-grid{gap:7px}.topic-grid a{min-height:90px;padding:10px 11px}.topic-grid strong{font-size:16px;margin-top:4px}.topic-grid small{font-size:13px;line-height:1.5}.topic-grid b{display:none}.topic-no{font-size:12px}.beginner{padding:20px 18px}.steps>a{padding:12px 0}.steps p{font-size:15px}.guide-pair,.safety,.stories,.tools,.about{padding-block:30px}.story-grid article,.tool-grid article{padding:18px}.story-grid p,.tool-grid p,.about>p:not(.eyebrow){font-size:16px}.article-list a{min-height:0;padding-block:13px}.article-list h3{font-size:16px;line-height:1.6}.small,.caption{font-size:14px}.featured strong{font-size:16px}.tool-links{font-size:14px}h2{font-size:24px;line-height:1.4}.step-num{font-size:26px}}
'''
# Existing finished article content is mirrored only inside the owner review Site.
articles=['start-guide.html','contract-guide.html','driver-note-07.html','money-guide.html','safety-guide.html','driver-faq.html','driver-note-03.html','driver-note-08.html','driver-note-09.html','driver-note-11.html','driver-news.html']
a=(dist/'articles');a.mkdir(exist_ok=True)
for name in articles:
 tree=html.fromstring((root/name).read_bytes());main=tree.xpath('//main')
 if not main:main=tree.xpath('//article')
 if not main:raise RuntimeError('no article body '+name)
 body=etree.tostring(main[0],encoding='unicode',method='html')
 # Existing inline content and source links are retained; avoid missing review assets.
 doc=html.fromstring(body)
 for e in doc.xpath('.//script|.//iframe'):e.drop_tree()
 for e in doc.xpath('.//*[@src]'):
  src=e.get('src');path=(root/src).resolve()
  if src.startswith('assets/') and path.is_file():
   dest=dist/src;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(path,dest);e.set('src','../'+src)
  elif not urlsplit(src).scheme:e.drop_tree()
 for e in doc.xpath('.//a[@href]'):
  href=e.get('href');u=urlsplit(href)
  if href.startswith('#'):continue
  if not u.scheme and not href.startswith('mailto:'):
   target=u.path
   e.set('href',target if target in articles else 'https://delipit.jp/'+href)
 body=etree.tostring(doc,encoding='unicode',method='html')
 title=(tree.xpath('//title')[0].text or name).replace('<','&lt;')
 page=f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{title}｜確認用</title><link rel="stylesheet" href="../article.css"></head><body><header><div class="bar"><a href="../index.html#problems">← 悩みから探す</a><span>DELIPIT / 記事確認用</span></div></header><div class="notice">既存公開記事の本文を確認用に表示しています。新しい解説の完成版ではありません。</div>{body}<footer><a href="../index.html#problems">トップの疑問へ戻る</a><a href="https://delipit.jp/{name}">公式サイトの元記事</a></footer></body></html>'''
 (a/name).write_text(page)
for name in articles:
 source=source.replace('href="https://delipit.jp/'+name+'"','href="articles/'+name+'"')
# Newsletter, operator and official policy links remain external.
(dist/'index.html').write_text(source);(dist/'portal.css').write_text(css)
(dist/'article.css').write_text('''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#0c0e0e;color:#f3f1e9;font:16px/1.75 -apple-system,BlinkMacSystemFont,"Noto Sans JP",sans-serif}a{color:#e6bf71;text-underline-offset:4px}a:focus-visible{outline:3px solid #b5d7f4}header{background:#171919;border-bottom:1px solid #625237}.bar{max-width:780px;margin:auto;padding:12px 18px;display:flex;justify-content:space-between;gap:12px;align-items:center}.bar a{min-height:44px;display:flex;align-items:center}.bar span{font-size:13px;color:#c9beaa}.notice{font-size:14px;background:#262116;color:#f0d39d;padding:10px 18px;text-align:center}main,article{max-width:780px;margin:auto;padding:22px 18px 50px}main article{padding:0}h1{font-size:30px;line-height:1.4}h2{font-size:24px;line-height:1.4;margin-top:32px}h3{font-size:19px}p,li{font-size:16px;line-height:1.75}section{margin:24px 0}img{max-width:100%;height:auto}table{display:block;max-width:100%;overflow-x:auto}footer{border-top:1px solid #444;max-width:780px;margin:auto;padding:24px 18px 45px;display:flex;gap:25px;flex-wrap:wrap}footer a{min-height:44px}@media(max-width:430px){h1{font-size:27px}h2{font-size:22px}.bar span{font-size:11px}}''')
print(len(articles),'review article bodies mirrored')

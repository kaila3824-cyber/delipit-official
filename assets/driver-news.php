<?php
declare(strict_types=1);
header('Content-Type: text/html; charset=UTF-8');

const CACHE_TTL = 21600; // 6 hours
const MAX_ITEMS = 30;

$sources = [
  [
    'id'=>'mlit','name'=>'国土交通省','url'=>'https://www.mlit.go.jp/','base'=>'https://www.mlit.go.jp',
    'terms'=>'https://www.mlit.go.jp/link.html','category'=>'物流・制度'
  ],
  [
    'id'=>'nta','name'=>'国税庁','url'=>'https://www.nta.go.jp/information/news/news.htm','base'=>'https://www.nta.go.jp',
    'terms'=>'https://www.nta.go.jp/chuijiko/copy.htm','category'=>'税・お金'
  ],
];

$strong = ['貨物軽自動車','軽貨物','宅配','貨物自動車','運送事業','事業用自動車','フリーランス','インボイス','確定申告','消費税'];
$medium = ['物流','運送','ドライバー','自動車','交通安全','点検整備','道路','税制','個人事業','業務委託','配送'];
$exclude = ['鉄道','航空','船舶','港湾','観光','建設','住宅','不動産','海事','ダム','河川'];

function fetch_url(string $url): string {
  $opts=['http'=>['timeout'=>8,'user_agent'=>'DELIPIT Driver News/1.0 (+https://delipit.jp/driver-news.php)','header'=>"Accept-Language: ja\r\n"]];
  $ctx=stream_context_create($opts);
  $s=@file_get_contents($url,false,$ctx);
  return is_string($s)?$s:'';
}
function abs_url(string $href,string $base): string {
  if (preg_match('~^https?://~i',$href)) return $href;
  if (str_starts_with($href,'//')) return 'https:'.$href;
  if (str_starts_with($href,'/')) return rtrim($base,'/').$href;
  return rtrim($base,'/').'/'.ltrim($href,'./');
}
function score_title(string $t,array $strong,array $medium,array $exclude): int {
  $score=0;
  foreach($strong as $k) if(mb_stripos($t,$k)!==false) $score+=10;
  foreach($medium as $k) if(mb_stripos($t,$k)!==false) $score+=3;
  foreach($exclude as $k) if(mb_stripos($t,$k)!==false) $score-=5;
  return $score;
}
function classify(string $t,string $fallback): string {
  if(preg_match('/税|確定申告|インボイス|消費税|所得/',$t)) return '税・お金';
  if(preg_match('/安全|事故|点検|整備|車両|自動車/',$t)) return '安全・車両';
  if(preg_match('/法|制度|改正|規則|義務|フリーランス/',$t)) return '法令・制度';
  if(preg_match('/物流|運送|貨物|宅配|配送/',$t)) return '物流・業界';
  return $fallback;
}
function extract_items(array $src,array $strong,array $medium,array $exclude): array {
  $html=fetch_url($src['url']); if($html==='') return [];
  libxml_use_internal_errors(true);
  $dom=new DOMDocument(); @$dom->loadHTML('<?xml encoding="UTF-8">'.$html);
  $xp=new DOMXPath($dom); $out=[];
  foreach($xp->query('//a[@href]') as $a){
    $title=trim(preg_replace('/\s+/u',' ',$a->textContent));
    if(mb_strlen($title)<10 || mb_strlen($title)>180) continue;
    $score=score_title($title,$strong,$medium,$exclude); if($score<3) continue;
    $href=abs_url(trim($a->getAttribute('href')),$src['base']);
    if(!preg_match('~^https?://~',$href)) continue;
    $context=$a->parentNode ? trim(preg_replace('/\s+/u',' ',$a->parentNode->textContent)) : '';
    $date='';
    if(preg_match('/(20\d{2})[年\.\/\-](\d{1,2})[月\.\/\-](\d{1,2})日?/u',$context,$m)) $date=sprintf('%04d-%02d-%02d',(int)$m[1],(int)$m[2],(int)$m[3]);
    $key=sha1($href.'|'.$title);
    $out[$key]=['title'=>$title,'url'=>$href,'source'=>$src['name'],'sourceId'=>$src['id'],'date'=>$date,'category'=>classify($title,$src['category']),'score'=>$score];
  }
  return array_values($out);
}
function load_news(array $sources,array $strong,array $medium,array $exclude): array {
  $dir=__DIR__.'/data'; if(!is_dir($dir)) @mkdir($dir,0755,true);
  $cache=$dir.'/driver-news-cache.json';
  if(is_file($cache) && time()-filemtime($cache)<CACHE_TTL){
    $j=json_decode((string)@file_get_contents($cache),true); if(is_array($j)) return $j;
  }
  $items=[];
  foreach($sources as $s) $items=array_merge($items,extract_items($s,$strong,$medium,$exclude));
  usort($items,function($a,$b){$d=strcmp($b['date'],$a['date']); return $d!==0?$d:($b['score']<=>$a['score']);});
  $items=array_slice($items,0,MAX_ITEMS);
  if($items) @file_put_contents($cache,json_encode($items,JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT),LOCK_EX);
  elseif(is_file($cache)){ $j=json_decode((string)@file_get_contents($cache),true); if(is_array($j)) return $j; }
  return $items;
}
$items=load_news($sources,$strong,$medium,$exclude);
$updated=date('Y.m.d H:i');
?><!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DRIVER NEWS｜DELIPIT</title><meta name="description" content="軽貨物・配送ドライバーに関係する制度、安全、車両、税・お金、物流の公的な最新情報をDELIPITが整理して案内します。"><link rel="icon" href="assets/delipit-web-icon-192.png"><style>
:root{--bg:#090a0b;--panel:#111315;--line:#302b22;--gold:#d8a83e;--text:#f2efe8;--muted:#aaa}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans JP",sans-serif;line-height:1.75}a{color:inherit}.wrap{width:min(1120px,calc(100% - 36px));margin:auto}.header{position:sticky;top:0;z-index:10;background:rgba(9,10,11,.94);border-bottom:1px solid #252525;backdrop-filter:blur(12px)}.nav{height:76px;display:flex;align-items:center;gap:24px}.logo{width:150px}.navlinks{display:flex;gap:18px;margin-left:auto;font-size:13px;font-weight:700}.navlinks a{text-decoration:none;color:#ccc}.app{padding:9px 14px;border:1px solid var(--gold);border-radius:999px;color:#f2ca72!important}.hero{padding:78px 0 46px;background:radial-gradient(circle at 80% 0,#2c2110 0,transparent 34%)}.eyebrow{color:#e0b34f;font-size:12px;font-weight:900;letter-spacing:.18em}.hero h1{font-size:clamp(38px,7vw,72px);line-height:1.08;margin:10px 0 18px}.lead{max-width:760px;color:#bbb;font-size:17px}.meta{margin-top:20px;color:#777;font-size:12px}.filters{display:flex;gap:8px;flex-wrap:wrap;padding:26px 0 12px}.filter{border:1px solid #3a352d;border-radius:999px;padding:7px 12px;background:#101112;color:#ccc;font-size:12px;cursor:pointer}.filter.active{border-color:var(--gold);color:#f1c965}.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;padding:14px 0 70px}.card{display:flex;flex-direction:column;background:linear-gradient(145deg,#151719,#0d0f10);border:1px solid var(--line);border-radius:16px;padding:22px;min-height:210px}.tag{font-size:11px;color:#e0b34f;font-weight:800}.card h2{font-size:18px;line-height:1.5;margin:9px 0 14px}.source{margin-top:auto;color:#8d8d8d;font-size:12px}.read{display:inline-block;margin-top:13px;color:#f0c35e;font-weight:800;text-decoration:none}.notice{margin:0 0 70px;padding:20px;border:1px solid #34302a;border-radius:14px;color:#aaa;background:#101112}.empty{grid-column:1/-1;padding:30px;border:1px solid #333;border-radius:16px;color:#aaa}.footer{border-top:1px solid #242424;padding:32px 0 44px;color:#777;font-size:12px}.footer a{color:#aaa}.soon{margin:0 0 70px;padding:28px;border:1px solid #4a391c;border-radius:18px;background:linear-gradient(145deg,#151719,#0d0f10)}.soon h2{margin:6px 0}.soon p{color:#aaa}@media(max-width:760px){.nav{height:66px}.logo{width:128px}.navlinks a:not(.app){display:none}.hero{padding:55px 0 32px}.grid{grid-template-columns:1fr}.card{min-height:0}}
</style></head><body><header class="header"><div class="wrap nav"><a href="index.html"><img class="logo" src="assets/delipit-logo.png" alt="DELIPIT"></a><nav class="navlinks"><a href="index.html">HOME</a><a href="driver-news.php">DRIVER NEWS</a><a href="index.html#driver-note">DRIVER NOTE</a><a class="app" href="https://app.delipit.jp/" target="_blank" rel="noopener">DELIPITを使う</a></nav></div></header><main><section class="hero"><div class="wrap"><div class="eyebrow">DELIPIT DRIVER NEWS</div><h1>配送の仕事に関係する情報を、<br>ひとつの場所に。</h1><p class="lead">軽貨物・配送ドライバーに関係する制度、安全、車両、税・お金、物流の情報を、公的な情報源から自動取得し、関連性の高いものを案内します。</p><p class="meta">自動更新（最大6時間キャッシュ）｜最終表示更新 <?=htmlspecialchars($updated)?></p></div></section><div class="wrap"><div class="filters"><button class="filter active" data-filter="all">すべて</button><button class="filter" data-filter="法令・制度">法令・制度</button><button class="filter" data-filter="安全・車両">安全・車両</button><button class="filter" data-filter="税・お金">税・お金</button><button class="filter" data-filter="物流・業界">物流・業界</button></div><section class="grid" id="news-grid">
<?php if(!$items): ?><div class="empty">現在、取得できるDRIVER NEWSがありません。取得元への接続が回復すると自動で更新されます。</div><?php endif; ?>
<?php foreach($items as $it): ?><article class="card" data-category="<?=htmlspecialchars($it['category'])?>"><div class="tag"><?=htmlspecialchars($it['category'])?><?= $it['date']?' ｜ '.htmlspecialchars(str_replace('-','.',$it['date'])):'' ?></div><h2><?=htmlspecialchars($it['title'])?></h2><div class="source">出典：<?=htmlspecialchars($it['source'])?></div><a class="read" href="<?=htmlspecialchars($it['url'])?>" target="_blank" rel="noopener noreferrer">公式情報を見る →</a></article><?php endforeach; ?>
</section><div class="notice"><strong>DRIVER NEWSについて</strong><br>DELIPITが公的機関の公開情報から配送ドライバーとの関連性が高い情報を自動抽出して案内するページです。記事本文や画像を転載するものではありません。内容の正確な確認は、各カードの「公式情報を見る」から発表元をご確認ください。自動抽出のため、関連性の低い情報が含まれる場合があります。</div><section class="soon" id="driver-note"><div class="eyebrow">DRIVER NOTE</div><h2>現場から考える、配送と数字の話。</h2><p>現役配送員の視点から、配送管理・売上・経費・安全などを掘り下げる独自コンテンツを準備しています。</p><strong>COMING LATER</strong></section></div></main><footer class="footer"><div class="wrap">© 2026 DELIPIT / REVERIE　｜　<a href="index.html">HOME</a>　｜　<a href="terms.html">利用規約</a>　｜　<a href="privacy.html">プライバシーポリシー</a></div></footer><script>document.querySelectorAll('.filter').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('.filter').forEach(x=>x.classList.remove('active'));b.classList.add('active');let f=b.dataset.filter;document.querySelectorAll('.card').forEach(c=>c.style.display=(f==='all'||c.dataset.category===f)?'flex':'none')}));</script></body></html>

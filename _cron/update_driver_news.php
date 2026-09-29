<?php
declare(strict_types=1);
// DELIPIT DRIVER NEWS updater. Run from Xserver Cron / CLI only; do not link publicly.
date_default_timezone_set('Asia/Tokyo');
const MAX_ITEMS = 40;
$root = dirname(__DIR__);
$out = $root . '/data/driver-news.json';
$sources = [
  ['id'=>'mlit','name'=>'国土交通省','url'=>'https://www.mlit.go.jp/','category'=>'法令・制度'],
  ['id'=>'nta','name'=>'国税庁','url'=>'https://www.nta.go.jp/information/news/news.htm','category'=>'税・お金'],
];
// Conservative v1: official pages only. The updater extracts links/titles, then filters by relevance.
$strong = ['貨物軽自動車','軽貨物','宅配','個人事業主','フリーランス','インボイス','消費税','確定申告'];
$medium = ['運送','物流','貨物','配送','交通安全','事業用自動車','所得税','電子帳簿'];
function fetch_url(string $url): string {
  $ctx=stream_context_create(['http'=>['timeout'=>15,'user_agent'=>'DELIPIT-DriverNews/1.0 (+https://delipit.jp/)'],'https'=>['timeout'=>15]]);
  $s=@file_get_contents($url,false,$ctx); return is_string($s)?$s:'';
}
function score(string $s,array $strong,array $medium): int { $n=0; foreach($strong as $w) if(mb_stripos($s,$w)!==false)$n+=10; foreach($medium as $w) if(mb_stripos($s,$w)!==false)$n+=3; return $n; }
function absolute_url(string $href,string $base): string { if(preg_match('~^https?://~i',$href))return $href; if(str_starts_with($href,'//'))return 'https:'.$href; $p=parse_url($base); $origin=($p['scheme']??'https').'://'.($p['host']??''); if(str_starts_with($href,'/'))return $origin.$href; $dir=rtrim(dirname($p['path']??'/'),'/'); return $origin.($dir?'/'.$dir:'').'/'.$href; }
$items=[];
foreach($sources as $src){
  $html=fetch_url($src['url']); if($html==='')continue;
  libxml_use_internal_errors(true); $dom=new DOMDocument(); if(!@$dom->loadHTML('<?xml encoding="UTF-8">'.$html))continue; $xp=new DOMXPath($dom);
  foreach($xp->query('//a[@href]') as $a){ $title=trim(preg_replace('/\s+/u',' ',$a->textContent)); if(mb_strlen($title)<8)continue; $sc=score($title,$strong,$medium); if($sc<6)continue; $href=absolute_url(trim($a->getAttribute('href')),$src['url']); if(!preg_match('~^https?://~',$href))continue; $items[$href]=['title'=>$title,'publishedAt'=>'','sourceName'=>$src['name'],'sourceUrl'=>$href,'category'=>$src['category'],'score'=>$sc]; }
}
usort($items,fn($a,$b)=>$b['score']<=>$a['score']); $items=array_slice(array_values($items),0,MAX_ITEMS); foreach($items as &$i)unset($i['score']);
$payload=['generatedAt'=>date(DATE_ATOM),'items'=>$items];
$tmp=$out.'.tmp'; $ok=file_put_contents($tmp,json_encode($payload,JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES|JSON_PRETTY_PRINT),LOCK_EX); if($ok===false){fwrite(STDERR,"write failed\n");exit(1);} rename($tmp,$out); echo 'updated '.count($items)." items\n";

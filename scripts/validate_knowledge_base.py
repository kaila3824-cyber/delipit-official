#!/usr/bin/env python3
"""Validate editorial research and derive review queue without changing source records."""
import argparse,json,re,unicodedata
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit
ROOT=Path(__file__).resolve().parents[1]
def review_state(topic, as_of):
    # Review is due ON the date, not the day after. Never upgrades uncertain answers.
    return 'NEEDS REVIEW' if topic['next_review_on'] <= as_of else topic['status']
def validate(as_of):
    data=json.loads((ROOT/'data/knowledge-base/topics.json').read_text())
    sources=json.loads((ROOT/'data/knowledge-base/sources.json').read_text())['sources']
    plan=json.loads((ROOT/'data/knowledge-base/editorial-plan.json').read_text())['articles']
    ts=data['topics']; ids={t['id'] for t in ts}; ss={s['id']:s for s in sources}; cats={c['id'] for c in data['categories']}
    assert len(ts)>=100 and len(cats)==12
    assert len(ids)==len(ts) and len(ss)==len(sources)
    normalized=[unicodedata.normalize('NFKC',t['question']).replace(' ','') for t in ts]
    assert len(set(normalized))==len(ts),'Duplicate question titles'
    assert data['publication_ready'] is False and data['search_volume'] is None
    for c in cats:
        assert {t['audience'] for t in ts if t['category_id']==c}=={'初心者','現役','ベテラン'}
    for s in sources:
        assert urlsplit(s['url']).scheme=='https'
        assert s['checked_on']<=data['as_of']
        if s['publication_or_revision_date']: assert s['publication_or_revision_date']<=data['as_of']
        if s['source_kind']=='PUBLIC_PRIMARY':
            host=urlsplit(s['url']).hostname
            assert host.endswith(('.go.jp','.lg.jp')) or host in {'www.keikenkyo.or.jp','www.keikenkyo-faq.jp','www.pref.saitama.lg.jp','www.city.tokorozawa.saitama.jp'},host
    for t in ts:
        assert re.fullmatch(r'Q\d{2}-\d{2}',t['id']) and t['category_id'] in cats
        assert t['status'] in data['status_definitions']
        assert t['current_site_coverage'] in data['coverage_definitions']
        assert t['priority'] in {'P0','P1','P2'}
        assert t['checked_on']<=data['as_of']<=t['next_review_on']
        date.fromisoformat(t['next_review_on'])
        assert t['article_ready'] is False and t['publication_state']=='RESEARCH_RECORD_ONLY'
        assert t['history'] and t['conclusion'] and t['applicability'] and t['regional_differences'] and t['effective_date']
        assert all(s in ss for s in t['source_ids'])
        assert set(t['source_ids'])=={s['source_id'] for s in t['source_dates']}
        if t['status']=='VERIFIED':
            assert t['source_ids']
            assert any(ss[s]['access_level']!='UNREADABLE' for s in t['source_ids'])
        if t['status']=='CONDITIONAL': assert t['conditions_exceptions_transition']
        if t['status'] in {'NEEDS REVIEW','UNCONFIRMED'}: assert t['unknowns'] and t['next_research_action']
        for url in t['existing_pages']:
            u=urlsplit(url); assert u.hostname=='delipit.jp'
            assert (ROOT/(u.path.lstrip('/') or 'index.html')).is_file(),url
    for a in plan:
        assert a['status']=='OUTLINE_ONLY' and set(a['question_ids'])<=ids
        assert set(a['source_ids'])<=ss.keys() and a['blocking_checks']
    sample={'status':'CONDITIONAL','next_review_on':'2026-11-15'}
    assert review_state(sample,'2026-11-14')=='CONDITIONAL'
    assert review_state(sample,'2026-11-15')=='NEEDS REVIEW'
    assert review_state(sample,'2026-11-16')=='NEEDS REVIEW'
    queue=[{'id':t['id'],'recorded_status':t['status'],'effective_review_state':review_state(t,as_of),'next_review_on':t['next_review_on'],'action':t['next_research_action']} for t in ts if t['status'] in {'NEEDS REVIEW','UNCONFIRMED'} or t['next_review_on']<=as_of]
    return {'result':'PASS','as_of':as_of,'topics':len(ts),'categories':len(cats),'sources':len(sources),'article_outlines':len(plan),'statuses':dict(Counter(t['status'] for t in ts)),'review_queue_count':len(queue),'review_queue':queue,'checks':['unique IDs and normalized question titles','12 categories with three experience levels','valid source dependencies and local existing URLs','dates and explicit publication block','conditional and unknown answer fields','review deadline boundary before/on/after','all article plans are outlines only'],'limitation':'構造検証。根拠の意味、法令適用、SORA Acceptanceを自動認定しない'}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--as-of',default='2026-11-01');p.add_argument('--output',type=Path);a=p.parse_args();date.fromisoformat(a.as_of)
    r=validate(a.as_of);txt=json.dumps(r,ensure_ascii=False,indent=2)+'\n'
    if a.output:a.output.write_text(txt)
    print(json.dumps({k:v for k,v in r.items() if k!='review_queue'},ensure_ascii=False))

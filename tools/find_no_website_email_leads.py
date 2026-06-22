import json, re, time
from pathlib import Path
import requests

BASE = Path(__file__).resolve().parents[1]
seen_ids = set()
for rel in ['mockups.json','outreach/send-queue.json','outreach/master-send-board.json']:
    p=BASE/rel
    if p.exists():
        txt=p.read_text(encoding='utf-8')
        seen_ids.update(re.findall(r'"(?:id|prospectId)"\s*:\s*"([^"]+)"', txt))

def slug(s):
    return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')

endpoints=['https://overpass-api.de/api/interpreter','https://overpass.kumi.systems/api/interpreter']
# south,west,north,east
boxes={
 'des-moines': (41.35,-94.05,41.85,-93.25),
 'cedar-rapids-iowa-city': (41.55,-92.15,42.15,-91.35),
 'ames-marshalltown': (41.85,-94.10,42.25,-92.80),
 'waterloo-cedar-falls': (42.25,-92.70,42.65,-92.10),
 'quad-cities-clinton': (41.45,-91.20,42.15,-90.05),
 'sioux-city-council-bluffs': (41.10,-96.45,42.75,-95.55),
}
leads=[]; seen_osm=set()
for market,bbox in boxes.items():
    s,w,n,e=bbox
    query=f'''
[out:json][timeout:45];
(
  nwr["email"]["shop"~"car_repair|car|tyres"]({s},{w},{n},{e});
  nwr["contact:email"]["shop"~"car_repair|car|tyres"]({s},{w},{n},{e});
  nwr["email"]["craft"~"plumber|roofer|electrician|hvac|landscaper|tree_service"]({s},{w},{n},{e});
  nwr["contact:email"]["craft"~"plumber|roofer|electrician|hvac|landscaper|tree_service"]({s},{w},{n},{e});
  nwr["email"]["amenity"~"car_wash"]({s},{w},{n},{e});
  nwr["contact:email"]["amenity"~"car_wash"]({s},{w},{n},{e});
);
out center tags 100;
'''
    got=False
    for endpoint in endpoints:
        try:
            r=requests.post(endpoint,data={'data':query},timeout=70,headers={'User-Agent':'SYBEORG prospect research'})
            if r.status_code>=500: continue
            r.raise_for_status(); data=r.json(); got=True; break
        except Exception as e:
            last=e
            continue
    if not got:
        print('failed',market,last); continue
    for el in data.get('elements',[]):
        key=(el.get('type'),el.get('id'))
        if key in seen_osm: continue
        seen_osm.add(key)
        tags=el.get('tags',{})
        name=tags.get('name') or tags.get('operator')
        email=tags.get('email') or tags.get('contact:email')
        if not name or not email: continue
        if tags.get('website') or tags.get('contact:website') or tags.get('url'): continue
        sid=slug(name)
        if sid in seen_ids: continue
        vertical=tags.get('shop') or tags.get('craft') or tags.get('amenity') or 'service business'
        city=tags.get('addr:city') or market
        phone=tags.get('phone') or tags.get('contact:phone')
        address=' '.join(x for x in [tags.get('addr:housenumber'), tags.get('addr:street')] if x)
        rec={
            'prospectId': sid,
            'business': name,
            'vertical': vertical,
            'market': f'{city}, IA',
            'publicEmail': email,
            'phone': phone,
            'address': address,
            'osmType': el.get('type'),
            'osmId': el.get('id'),
            'sourceMarketBox': market,
            'tags': {k:v for k,v in tags.items() if k in ['name','shop','craft','amenity','phone','contact:phone','email','contact:email','addr:city','addr:street','addr:housenumber','opening_hours']},
            'signal': 'OSM/public listing has email but no website/contact:website/url tag',
            'slug': sid,
        }
        score=60
        if 'gmail.com' in email.lower(): score+=10
        if phone: score+=8
        if address: score+=5
        if vertical in ['car_repair','plumber','roofer','hvac','tree_service','landscaper']: score+=10
        rec['score']=score
        leads.append(rec)
    time.sleep(1)
leads=sorted(leads,key=lambda x:x['score'], reverse=True)
out=BASE/'outreach/daily-batches/no-website-email-candidates-2026-06-22.json'
out.write_text(json.dumps({'source':'Overpass OSM Iowa metros: email + no website tags','count':len(leads),'leads':leads[:80]},indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'count':len(leads),'top':leads[:25]},indent=2,ensure_ascii=False))

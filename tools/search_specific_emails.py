import requests,re,urllib.parse,html,time
email_re=re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
queries=[
 "Howard's Auto Repair Oskaloosa email", "Howard's Auto Repair 641-673-3310",
 'Xpress Oil Lube Waterloo email', 'Xpress Oil Lube 319-232-0854',
 'Pioneer Auto Sergeant Bluff email', 'Pioneer Auto 712-943-7830',
 'Mark Hansen Auto Repair Ames email', 'Mark Hansen Auto Repair Service',
 'Iowa auto repair gmail.com no website', 'Iowa plumbing gmail.com no website'
]
for q in queries:
 print('\n###',q)
 for name,base in [('bing','https://www.bing.com/search?q='),('ddg','https://html.duckduckgo.com/html/?q=')]:
  try:
   r=requests.get(base+urllib.parse.quote(q),headers={'User-Agent':'Mozilla/5.0'},timeout=20)
   txt=html.unescape(r.text)
   emails=sorted(set(e.lower() for e in email_re.findall(txt) if 'error-lite' not in e.lower()))
   print(name, r.status_code, emails[:10])
   plain=re.sub('<[^>]+>',' ',txt); plain=re.sub(r'\s+',' ',plain)
   print(plain[:1000])
  except Exception as e: print(name,'ERR',e)
  time.sleep(.3)

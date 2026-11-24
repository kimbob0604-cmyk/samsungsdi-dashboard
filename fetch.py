import yfinance as yf, json, math
T={'006400.KS':'삼성SDI','373220.KS':'LG에너지솔루션','096770.KS':'SK이노베이션','300750.SZ':'CATL','6752.T':'파나소닉','003670.KS':'포스코퓨처엠','066970.KQ':'엘앤에프','251970.KQ':'펌텍코리아'}
h=yf.download(list(T),start='2025-11-20',end='2026-11-25',auto_adjust=False,progress=False)['Close']
h=h.dropna(how='all')
out={'d':[d.strftime('%Y-%m-%d') for d in h.index]}
for k,n in T.items():
    out[n]=[None if (v!=v) else round(float(v),2) for v in h[k]]
json.dump(out,open('data/px.json','w'),ensure_ascii=False)
P=[]
for k,n in T.items():
    if n=='펌텍코리아':continue
    i=yf.Ticker(k).info
    P.append(dict(t=k,n=n,cur=i.get('currency'),px=i.get('currentPrice') or i.get('regularMarketPrice'),mc=i.get('marketCap'),fpe=i.get('forwardPE'),pb=i.get('priceToBook'),ev=i.get('enterpriseValue'),eve=i.get('enterpriseToEbitda'),rg=i.get('revenueGrowth'),opm=i.get('operatingMargins'),y52=i.get('52WeekChange'),sh=i.get('sharesOutstanding')))
json.dump(P,open('data/peers.json','w'),ensure_ascii=False,indent=1)
for p in P: print(p)
s=out['삼성SDI']; print(out['d'][-3:], s[-3:], max(x for x in s if x), min(x for x in s if x))

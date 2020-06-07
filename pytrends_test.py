import pandas as pd
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)
#keywords = ['Lana', 'Mercado Pago']
#pytrends.build_payload(
#     kw_list=keywords,
#     cat=0,
#     timeframe='today 3-m',
#     geo='TW',
#     gprop='')
#data = pytrends.interest_over_time()
#data.to_csv('Py_VS_R.csv', encoding='utf_8_sig')

#data = data.drop(labels=['isPartial'],axis='columns')
#data.to_csv('Py_VS_R.csv', encoding='utf_8_sig')

#image = data.plot(title = 'Python V.S. R in last 3 months on Google Trends')
#fig = image.get_figure()
#fig.savefig('figure.png')

df = pytrends.trending_searches(pn='argentina')
print(df)

#t = pytrends.get_historical_interest('Corona', year_start=2020, month_start=1, day_start=1, hour_start=0, year_end=2020, month_end=5, day_end=1, hour_end=0, cat=0, geo='', gprop='', sleep=20)
#print(t)
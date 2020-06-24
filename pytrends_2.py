#https://predictivehacks.com/get-google-trends-using-python/
import pandas as pd #pandas 0.25
from pytrends.request import TrendReq

pytrend = TrendReq()

trending_searches_df = pytrend.trending_searches()
print(trending_searches_df)

print()

# Get Google Hot Trends data
today_searches_df = pytrend.today_searches()
print(today_searches_df.head(20))

print()

kw_list = ["TaxFix", "Turbotax"]
tb = pytrend.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
print(tb)
print()

b = pytrend.related_queries()
print(b)

c = pytrend.interest_over_time()
print(c)




from pytrends.request import TrendReq
pytrend = TrendReq(tz=360)
keywords = ['Messi', 'Cristiano Ronaldo']
pytrend.build_payload(
     kw_list=keywords,
     cat=0,
     timeframe='today 12-m',
     geo='',
     gprop='')
data = pytrend.interest_over_time()
data= data.drop(labels=['isPartial'],axis='columns')
image = data.plot(title = 'Comparing the words: {}'.format(keywords))
fig = image.get_figure()
fig.savefig('figure.png')
data.to_csv('Py_VS_R.csv', encoding='utf_8_sig')
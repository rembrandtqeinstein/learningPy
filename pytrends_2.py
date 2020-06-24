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

kw_list = ["Podcast"]
tb = pytrend.build_payload(
    kw_list,
    cat=0,
    timeframe='today 5-y',
    geo='ES',
    gprop='')
print()

rq = pytrend.related_queries()
#rq = rq.drop(labels=['isPartial'],axis='columns')
top = rq.get('Podcast').get('top')
print(top)
print()
rising = rq.get('Podcast').get('rising')
print(rising)
#for k,v in rq.items():
#    print(k, v)

iot = pytrend.interest_over_time()
iot = iot.drop(labels=['isPartial'],axis='columns')
img = iot.plot(title = 'Comparing the words: {}'.format(kw_list))
fig = img.get_figure()
fig.savefig('figureP.png')




from pytrends.request import TrendReq
pytrend = TrendReq(tz=360)
keywords = ['Podcast', 'Radio']
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
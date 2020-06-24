#https://predictivehacks.com/get-google-trends-using-python/
import pandas as pd #pandas 0.25
from pytrends.request import TrendReq

pytrend = TrendReq()

print("Trending Searches WorldWide")
trending_searches_df = pytrend.trending_searches()
print(trending_searches_df)

print()
print("Get Today Trending Searches")
# Get Google Hot Trends data
today_searches_df = pytrend.today_searches()
print(today_searches_df.head(20))

print()
print("See Related Queries to a Particular Query o Queries (Suggested to use just one")
#kw_list = ["Podcast"]
kw_list = list()
kw = input("Enter the Keywords you want to look up separated by a ,: ")
kw = kw.split(",")
for word in kw:
    kw_list.append(word)
print(kw_list)
tb = pytrend.build_payload(
    kw_list,
    cat=0,
    timeframe='today 5-y', # This can be changed to have a new timeline
    geo='ES', # This needs to change if you want not to use Spain
    gprop='')
rq = pytrend.related_queries()
#rq = rq.drop(labels=['isPartial'],axis='columns')
top = rq.get('Podcast').get('top')
print("Top Queries related to: {}".format(kw_list))
print(top)
print()
print("Top Trending Queries related to: {}".format(kw_list))
rising = rq.get('Podcast').get('rising')
print(rising)

print()
print("Interest Over Time of the befored Selected Queries")
iot = pytrend.interest_over_time()
iot = iot.drop(labels=['isPartial'],axis='columns')
img = iot.plot(title = 'Comparing the words: {}'.format(kw_list))
fig = img.get_figure()
fig.savefig('figureP.png')

print()
print("Comparative Graph creation and CSV File for Compared Keywords")
pytrend = TrendReq(tz=360)
#keywords = ['Podcast', 'Radio']
keywords = list()
str = input("Enter the Keywords you want to search for separated by a ,: ")
str = str.split(",")
for word in str:
    keywords.append(word)
print(keywords)

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
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
kw = input("Enter the Keywords you want to look up separated by a , and no spaces: ")
kw = kw.split(",")
for word in kw:
    kw_list.append(word)
print(kw_list)
tb = pytrend.build_payload(
    kw_list,
    cat=0,
    timeframe='today 5-y', # This can be changed to have a new timeline
    geo='', # This needs to change if you want not to use Spain (ES)
    gprop='')
rq = pytrend.related_queries()
#rq = rq.drop(labels=['isPartial'],axis='columns')
for word in kw_list:
    print("Top Queries related to: {}".format(word))
    top = rq.get(word).get('top')
    print(top)
    print()
    print("Top Trending Queries related to: {}".format(word))
    rising = rq.get(word).get('rising')
    print(rising)

print()

graph = input("Do you want to plot the Interest Over Time? (Yes to Graph, enter to skip): ")
if graph == 'Yes':
    print("Interest Over Time of the befored Selected Queries figure Created")
    iot = pytrend.interest_over_time()
    iot = iot.drop(labels=['isPartial'],axis='columns')
    img = iot.plot(title = 'Comparing the words: {}'.format(kw_list))
    fig = img.get_figure()
    fig.savefig(kw_list[0]+'.png')

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
fig.savefig(keywords[0] + '.png')
data.to_csv(keywords + '.csv', encoding='utf_8_sig')
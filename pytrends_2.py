#https://predictivehacks.com/get-google-trends-using-python/
import pandas as pd #pandas 0.25
from pytrends.request import TrendReq

pytrend = TrendReq()

trending_searches_df = pytrend.trending_searches()
print(trending_searches_df)

# Get Google Hot Trends data
today_searches_df = pytrend.today_searches()
print(today_searches_df.head(20))

kw_list = ["Mercado Pago", "Cabify", "SpotAHome"]
pytrend.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')

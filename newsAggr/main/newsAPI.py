from newsapi import NewsApiClient
import datetime
import pandas as pd

newsapi = NewsApiClient(api_key =  '0a2c0a1704e541db9a25f0ddb833e853')
data = newsapi.get_top_headlines()
print(data)
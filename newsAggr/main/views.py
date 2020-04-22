from django.shortcuts import render
from .models import Headlines
from newsapi import NewsApiClient
import datetime
import pandas as pd
import random


def get_news():
    newsapi = NewsApiClient(api_key =  '0a2c0a1704e541db9a25f0ddb833e853')
    data = newsapi.get_top_headlines()
    headlines = []
    for x in data['articles']:
        headlines.append(x["title"])
    image_url = []
    for x in data['articles']:
        image_url.append(x['urlToImage'])
    headline_url = []
    for j in data['articles']:
        headline_url.append(j['url'])
    random_int = random.randrange(1,10)

    return headlines, image_url, headline_url, random_int





def index(request):
    headlines, images, urls, random_int = get_news()

    return  render(request,
                   'main/index.html',
                   context = {'headlines':headlines,'images': images, 'urls' : urls, 'random_int': random_int})

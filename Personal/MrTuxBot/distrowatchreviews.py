import tweepy
import requests
from bs4 import BeautifulSoup

def getInfo():
    info = tweepy.Client(
        consumer_key= "",
        consumer_secret= "",
        access_token= "",
        access_token_secret= ""
    )
    return info

auth = tweepy.OAuthHandler(
    "consumer_key",
    "consumer_secret"
)

auth.set_access_token(
    "access_token",
    "access_token_secret"
)

api = tweepy.API(auth)

def retrieve_rss(): 
    rss_link = []
    my_request = requests.get("https://distrowatch.com/news/ratings.xml")
    bs = BeautifulSoup(my_request.content, "xml")
    items = bs.findAll('item')

    for item in items:
        rss_link.append(item.find("guid").text)
    return rss_link[0]


def retreive_title():
    rss_title = []
    my_request = requests.get("https://distrowatch.com/news/ratings.xml")
    bs = BeautifulSoup(my_request.content, "lxml")
    item = bs.find_all("item") 

    for items in item:
        rss_title.append(items.find("title").text)
    return rss_title[0]


def stop_tweeting_time():
    print("Mr. Tux activated")
    url = retrieve_rss()
    aTitle = retreive_title()
    tweet_tweet = f"{aTitle}:" + f"\n{url}"
    print(tweet_tweet)
    api.update_status(status=tweet_tweet)
   
stop_tweeting_time()

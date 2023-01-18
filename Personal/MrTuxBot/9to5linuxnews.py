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

def retreive_article(): 
    sitemap_info = []
    my_request = requests.get("https://9to5linux.com/sitemap-posttype-post.2022.xml")

    # retreive only the text of the articles title
    # from the requests.get() command
    # then stores it in sitemap_xml
    sitemap_xml = my_request.text

    # since BeautifulSoup cannot parse xml easily on it's own
    # it depends on its lxml package
    # in this case BeautifulSoup(sitemap_xml, "lxml")
    # extracts the information from sitemap_xml in text form
    bs = BeautifulSoup(sitemap_xml, "lxml")

    # find_all() helps to find all the tags in the sitemap
    # in this case, it finds all tags listed as <url>
    tags = bs.find_all("url") 

    # goes through the sitemap to look for the the URL of the article
    # in this case it will always go with the most recent article
    # then it will add it to the list
    for tag in tags:
        sitemap_info.append(tag.findNext("loc").text)
    return sitemap_info[0]

# This function is similar to everything in def retreive_article()
# except it gets the information for the title and converts it to text format
def retreive_title(link):
    my_request = requests.get(link)
    sitemap_xml = my_request.text
    bs = BeautifulSoup(sitemap_xml, "lxml")
    aTitle = bs.find_all("h1") 
    return aTitle[0].text


# posts the tweet to twitter
def stop_tweeting_time():
    print("Mr. Tux activated")
    link = retreive_article()
    aTitle = retreive_title(link)
    tweet_tweet = f"{aTitle}: {link}"
    print(tweet_tweet)
    api.update_status(status=tweet_tweet)
   
stop_tweeting_time()

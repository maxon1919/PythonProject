import urllib.request
import time
import tweepy
from keys_format import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET


def send_message(message):
    consumer_key=CONSUMER_KEY
    consumer_secret=CONSUMER_SECRET


    auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api=tweepy.API(auth)

    api.update_status(status=message)
    print("Tweeted: %s" % message)

def get_price():
    page=urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
    site=page.read().decode("utf8")
    price1=site.find(">$")
    price=float(site[price1+2:price1+6])
    return price

price=99.9
when=input("Is the price required immediately(Y/N)")
if when=="Y":
    price=get_price()
    
else:
    while price>4.74:
        time.sleep(15)
        price=get_price()
        
price="The price of coffee beans is "+str(price)
send_message(price)

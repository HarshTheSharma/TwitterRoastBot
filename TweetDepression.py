#Copyright 2021 HarshTheSharma
#Imports
import tweepy
from datetime import datetime
import time

#Initialize
auth = tweepy.OAuthHandler("API Key", "Private API Key")
auth.set_access_token("AUTH Key", "Private AUTH Key")
api = tweepy.API(auth)
tweetlist = open('Depression.txt')

#Loop
while True:
    tweet = tweetlist.readline()
    api.update_status("@HarshTheSharma " + tweet)
    time.sleep(86400)

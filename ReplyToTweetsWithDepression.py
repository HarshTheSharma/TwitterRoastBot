#Copyright 2021 HarshTheSharma

#imports
import tweepy
from datetime import datetime
import time

#variables
tweet = " "
currentline = 0
auth = tweepy.OAuthHandler("API Key", "Secret API Key")
auth.set_access_token("OAUTH Key", "Private OAUTH Key")
api = tweepy.API(auth)
tweetlist = open('Depression.txt')

#loop
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    if current_time == "12:00":
        lines = tweetlist.readlines()
        tweet = lines[currentline]
        api.update_status("@user " + tweet)
        currentline = currentline + 1
        if currentline == 51:
            currentline = 1
        time.sleep(60)
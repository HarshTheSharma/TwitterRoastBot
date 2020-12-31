#Copyright 2021 HarshTheSharma
#Imports
import tweepy
from datetime import datetime
import time

#Initialize
auth = tweepy.OAuthHandler("SCjKQj1bEBRjf57hTMZ64kfhK", "RbkC3za5dxbPAhiDuUImWVWamQZjajaOe6WHkNI5o4zX7V5Vr7")
auth.set_access_token("1239000319683465216-PydYhld8VSZr9j7uAgBxrZzDz3ZRUM", "Xzu3CsYE5GndurmlfqEUW1JfAfBThM2XiiNifo1W48qWR")
api = tweepy.API(auth)
tweetlist = open('Depression.txt')

#Loop
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    if current_time == "12:00":
        tweet = tweetlist.readline()
        api.update_status("@HarshTheSharma " + tweet)
        time.sleep(86400)
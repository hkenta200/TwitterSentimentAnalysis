from os import close
import tweepy as tw
from tweepy.api import API
#dont name file name tweepy


// Tweet keys
consumerKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
consumerSecret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
accessToken = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
accessTokenSecret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

//Authorization
auth = tw.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tw.API(auth)


term = input("What topic would you like to analyze?: ")
#term = "wildfires", "covid19"

tweets = tw.Cursor(api.search, q=term).items(5)

for tweet in tweets:
    print(tweet.text + "\n")

with open("readText.txt", "w", encoding="utf-8") as output:
    for tweet in tweets:
        output.write(str(tweet.text))

import tweepy
from textblob import TextBlob

consumer_key = 'yydMZGDKjfjOtAGpKhvyJV7yA'
consumer_secret = 'yHGLyjMIHiGXz5lS5xdyaS1Bd1OlGerpPwLYu9SS4aAedTocQc'

access_token = '901957351774740480-z4GhhdL1Qd9Oqwd433BIM2e2IjJ0izB'
access_token_secret = 'mnXam5cxqY4T9PBtmIYZS6G9fbZcUMKVDGoJNNC263EGS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = api.search('digibyte')

sentiment = 0

for tweet in tweets:
	analysis = TextBlob(tweet.text)
	sentiment += (analysis.sentiment.polarity * analysis.sentiment.subjectivity)

print(sentiment/len(tweets))
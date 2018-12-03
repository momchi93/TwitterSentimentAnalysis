import tweepy
from textblob import TextBlob
import pandas as pd
import numpy as np

consumer_key = 'N9ob3xKgUwWLNajFSS2XnEkIm'
consumer_secret = 'qCXKP1gQHohjPduzmzBIiuFk2NsgQXyLpuPvEEQvDxyS8De4xd'

access_token = '847580815726792705-HK8fxxvHdCtubfhBzptt6nl0RSBrVA3'
access_token_secret = 'BM8jF3B6n7hXnYBPyeJ8NcIAqj5RIJ9bl2cxBbOygnVxD'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Nintendo games')
txtLIST = []
polLIST = []

for tweet in public_tweets:
    txt = tweet.text
    txtLIST.append(txt)
    analysis = TextBlob(tweet.text)
    pol = analysis.polarity
    polLIST.append(pol)

for i in range(len(polLIST)):
    if polLIST[i] < 0:
        polLIST[i] = "Negative"
    elif polLIST[i] == 0:
        polLIST[i] = "Neutral"
    else:
        polLIST[i] = "Positive"

columns = ['Polarity', 'Tweet']
data1 = np.asarray(polLIST)
data2 = np.asarray(txtLIST)

combined = np.vstack((data1, data2)).T
df = pd.DataFrame(combined, columns=columns)
print(df)
df.to_csv("Tweets.csv", index=False)

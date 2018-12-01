# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 12:32:19 2018

@author: SmithaK
"""


import tweepy
from textblob import TextBlob

import csv

consumer_key = 'cjF7t46PqK9kIWZbe5Ph8Q'
consumer_secret = 'vI0SDztM9Rw1jdIdod4Uj1f3m4wNAYqkGw2pqJuCp1g'

access_token = '172686962-Lig6ytst4C8dJpDvv61CPPWS1zerWLzUn1PIxvV1'
access_token_secret = 'SdGjtc0EcQkQMBaYr11zLyox33LyDph2adyrHsLM3TSt0'  


# tweepy provides access to entire Twitters RESTFul API methods. Each method receives various parameters and returns responses.
# trxtblob is python library Text processing operaions.
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')


sentiments = []
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    sentiments.append(str(tweet.text.encode("utf-8")))
    sentiments.append(str(analysis.sentiment))
    sentiments.append("\n\n")

with open('sentimentAnalysis.csv','w') as csvfile:
    fileWriter = csv.writer(csvfile,delimiter = ',', quotechar='|', quoting = csv.QUOTE_MINIMAL)
    fileWriter.writerow(sentiments)

# polarity - how positive or negative a comment is
# subjectivity - how much of an opinion it is v/s factual
    
    
from textblob import TextBlob
import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import matplotlib.pyplot as plt
import re

"# -- coding: utf-8 --"

def calctime(a):
    return time.time()-a

compound,positive,negative=0,0,0
initime=time.time()
count=0
plt.ion()

ckey='GV5vBqNhcxVwUel7zmxxxbmJY'
csecret='5GQXxAzl6pYtb5EQa6dDkZqVdikeUPN1tCmi9Yjqshmt4d1Ep3'
atoken='1379482231-LE8G8Cgj30EciwJTB3tVLKCjF7liYV1d4b8RfH4'
asecret='KvS198R5r91FHIREwPsw7ap57RuTncQlVxlmaeh4UZ62e'

class listener(StreamListener):
    def on_data(self,data):
        global initime
        t=int(calctime(initime))

        all_data=json.loads(data)
        tweet=all_data['text']
        tweet=' '.join(re.findall("[a-zA-Z]+",tweet))

        blob=TextBlob(tweet.strip())

        global positive
        global negative
        global count
        global compound

        count+=1
        senti=0

        for sen in blob.sentences:
            senti=senti+sen.sentiment.polarity
            if sen.sentiment.polarity>=0:
                positive=positive+sen.sentiment.polarity
            else:
                negative=negative+sen.sentiment.polarity
        compound+=senti

        print(count)
        print(tweet.strip())
        print(senti)
        print(t)
        print(positive,negative,compound)
        plt.axis([0,70,-20,20])
        plt.xlabel('Time')
        plt.ylabel('Sentiment')
        plt.plot([t],[positive],'go',[t],[negative],'ro',[t],[compound],'bo')
        plt.show()
        plt.pause(0.0001)

        if count==200:
            return False
        else:
            return True


    def on_error(self,status):
        print(status)
auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

searchTerm = input("Enter the Keyword/Tag to search about: ")
NoOfTerms=int(input("Enter how many tweets you want to search: "))
twitterStream=Stream(auth,listener(NoOfTerms))
twitterStream.filter(track=[searchTerm])

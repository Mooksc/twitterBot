import time
import json
import random
from BotTime import BotTime
from TwitterBot import TwitterBot

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
hal9000 = TwitterBot(consumer_key, consumer_secret, access_token, access_token_secret)

def retweetBot():
    results = hal9000.searchTweets("./bots/hal9000/tests/data/results.json", '2001 A Space Odyssey', count='40', result_type='popular')
    d = {}
    l = []
    for i in results:
        d[i['ID']] = int(i['ENGAGEMENT']['LIKES']) + int(i['ENGAGEMENT']['RETWEETS'])
    for a in d:
        l.append(d[a])
    m = max(l)
    print(d)
    for k, v in d.items():
        r = hal9000.retweet(k)
        if str(r) == '<Response [200]>':
            return print(r)
        else:
            print(r)
        # if v == m:
        #     return print(hal9000.retweet(k))

retweetBot()
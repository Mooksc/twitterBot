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

def tweetBot():
    tweetBotTimer0 = BotTime(days=2.5)
    tweetBotTimer1 = BotTime(days=3)
    b = True
    while b:
        j = json.load(open('./bots/hal9000/tests/data/HAL9000.json'))
        # choice = random.choice(j['quotes'])
        if str(hal9000.tweetBot(choice)) == '<Response [200]>':
            j['quotes'].pop(choice)
            json.dump(j, open('./bots/hal9000/tests/data/HAL9000.json'), 'w+')
            b = False
    # time.sleep(random.randrange(tweetBotTimer0.getSeconds, tweetBotTimer1.getSeconds))

tweetBot()

import time
from BotTime import BotTime
from TwitterBot import TwitterBot

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
hal9000 = TwitterBot(consumer_key, consumer_secret, access_token, access_token_secret)
followBotTimer = BotTime(hours=3)

def followBot():
    hal9000.followBack()
    # time.sleep(followBotTimer.getSeconds)

followBot()

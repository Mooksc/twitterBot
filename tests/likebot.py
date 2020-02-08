import time
from BotTime import BotTime
from TwitterBot import TwitterBot

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
likeBotTimer = BotTime(hours=2)
hal9000 = TwitterBot(consumer_key, consumer_secret, access_token, access_token_secret)

def likes(listOfQueries):
    for i in listOfQueries:
        query = hal9000.makeTweetJSON('./bots/hal9000/tests/data/likes.json', hal9000.apiCall(hal9000.searchUrl, 'get', params={'q': i, 'count': '20', 'lang': 'en', 'result_type': 'mixed'}).json()['statuses'])
        for q in query:
            print(hal9000.like(q['ID']))
def likeBot():
    hal9000.likeBot('1183609240927252480',['Hal 9000', '2001 A Space Odyssey'])
    time.sleep(likeBotTimer.getSeconds)

def likeMentions():
    j = hal9000.apiCall(hal9000.mentionsTimelineUrl, 'get', params={})
    um = hal9000.makeTweetJSON('user_mentions.json', j.json())
    for x in um:
        print(hal9000.apiCall(hal9000.likeTweetUrl, 'post', params={'id': x['ID']}))

likes(['Hal 9000', '2001 A Space Odyssey'])
likeMentions()

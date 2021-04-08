from TwitterBot import TwitterBot

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

hal9000 = TwitterBot(consumer_key, consumer_secret, access_token, access_token_secret)

def likes(listOfQueries):
    for i in listOfQueries:
        query = hal9000.makeTweetJSON('data/likes.json', hal9000.apiCall(hal9000.searchUrl, 'get', params={'q': i, 'count': '20', 'lang': 'en', 'result_type': 'mixed'}).json()['statuses'])
        for q in query:
            if q['RETWEET']['IS_RETWEET'] == "False":
                print(hal9000.like(q['ID']))

def likeMentions():
    j = hal9000.apiCall(hal9000.mentionsTimelineUrl, 'get', params={})
    um = hal9000.makeTweetJSON('data/user_mentions.json', j.json())
    for x in um:
        print(hal9000.apiCall(hal9000.likeTweetUrl, 'post', params={'id': x['ID']}))

likes(['Hal 9000', '2001 A Space Odyssey'])
likeMentions()

from TwitterBot import TwitterBot, hal9000

def likes(listOfQueries):
    for i in listOfQueries:
        query = hal9000.makeTweetJSON('data/likes.json', hal9000.apiCall(hal9000.searchUrl, 'get', params={'q': i, 'count': '20', 'lang': 'en', 'result_type': 'mixed'}).json()['statuses'])
        for q in query:
            if q['RETWEET']['IS_RETWEET'] == "False":
                print(hal9000.like(q['ID']))

def likeMentions():
    getTimeline = hal9000.apiCall(hal9000.mentionsTimelineUrl, 'get', params={})
    userMentions = hal9000.makeTweetJSON('data/user_mentions.json', getTimeline.json())
    for i in userMentions:
        print(hal9000.apiCall(hal9000.likeTweetUrl, 'post', params={'id': i['ID']}))

likes(['Hal 9000', '2001 A Space Odyssey'])
likeMentions()

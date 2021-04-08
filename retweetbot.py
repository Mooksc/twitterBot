from TwitterBot import TwitterBot

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
hal9000 = TwitterBot(consumer_key, consumer_secret, access_token, access_token_secret)

def retweetBot():
    results = hal9000.searchTweets("data/results.json", '2001 A Space Odyssey', count='40', result_type='popular')
    d = {}
    l = []
    for i in results:
        d[i['ID']] = int(i['ENGAGEMENT']['LIKES']) + int(i['ENGAGEMENT']['RETWEETS'])
    for a in d:
        l.append(d[a])
    m = max(l)
    print(d)
    for k, v in d.items():
        if v == m:      
            return hal9000.retweet(k)

retweetBot()

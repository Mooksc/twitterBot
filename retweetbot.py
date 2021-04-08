from TwitterBot import TwitterBot, hal9000

def retweetBot(query, count, result_type):
    results = hal9000.searchTweets("data/results.json", query, count=count, result_type=result_type)
    obj = {}
    for i in results:
        obj[i['ID']] = int(i['ENGAGEMENT']['LIKES']) + int(i['ENGAGEMENT']['RETWEETS'])
    finalList = []
    for item in obj:
        finalList.append(obj[item])
    totalNumQueries = max(finalList)
    for key, val in obj.items():
        if val == totalNumQueries:      
            return hal9000.retweet(key)

retweetBot(query='2001 A Space Odyssey', count=40, result_type='popular')

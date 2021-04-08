import requests
import json
import random
import os
from requests_oauthlib import OAuth1
import mimetypes

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

class TwitterBot:

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.auth = OAuth1(consumer_key,
                      client_secret=consumer_secret,
                      resource_owner_key=access_token,
                      resource_owner_secret=access_token_secret)
        self.rateLimitUrl = 'https://api.twitter.com/1.1/application/rate_limit_status.json'
        self.tweetUrl = 'https://api.twitter.com/1.1/statuses/update.json'
        self.bioUrl = 'https://api.twitter.com/1.1/account/update_profile.json'
        self.timelineUrl = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
        self.searchUrl = 'https://api.twitter.com/1.1/search/tweets.json'
        self.retweetUrl = 'https://api.twitter.com/1.1/statuses/retweet/:id.json'
        self.likeTweetUrl = 'https://api.twitter.com/1.1/favorites/create.json'
        self.likeListUrl = 'https://api.twitter.com/1.1/favorites/list.json'
        self.lookupUserUrl = 'https://api.twitter.com/1.1/users/lookup.json'
        self.followUserUrl = 'https://api.twitter.com/1.1/friendships/create.json'
        self.followersUrl = 'https://api.twitter.com/1.1/followers/ids.json'
        self.followingUrl = 'https://api.twitter.com/1.1/friends/ids.json'
        self.mentionsTimelineUrl = 'https://api.twitter.com/1.1/statuses/mentions_timeline.json'

    def apiCall(self, url, requestType, params):
        if requestType is 'get':
            return requests.get(url, params, auth=self.auth)
        elif requestType is 'post':
            return requests.post(url, params, auth=self.auth)

    def makeTweetJSON(self, filepath, tweets):
        tweetList = []
        for tweet in tweets:
            td = {
                'ID': str(tweet['id']),
                'USER_ID': str(tweet['user']['id']),
                'NAME': str(tweet['user']['name']),
                'SCREEN_NAME': str(tweet['user']['screen_name']),
                'CREATED': str(tweet['created_at']),
                'CONTENT': str(tweet['text']),
                'ENTITIES': str(tweet['entities']),
                'ENGAGEMENT' : {
                    'LIKES': str(tweet['favorite_count']),
                    'RETWEETS': str(tweet['retweet_count'])
                },
                'REPLY' : {
                    'ID': str(tweet['in_reply_to_status_id']),
                    'USER': str(tweet['in_reply_to_user_id']),
                    'SCREEN_NAME': str(tweet['in_reply_to_screen_name'])
                },
                'RETWEET' : {
                    'IS_RETWEET': str(tweet['is_quote_status']),
                }
            }
            if str(tweet['is_quote_status']) == 'true':
                td['RETWEET']['ID'] = str(tweet['quoted_status_id'])
                td['RETWEET']['USER'] = str(tweet['quoted_status']['user']['id']),
                td['RETWEET']['NAME'] = str(tweet['quoted_status']['user']['name']),
                td['RETWEET']['SCREEN_NAME'] = str(tweet['quoted_status']['user']['screen_name']),
                td['RETWEET']['CONTENT'] = str(tweet['quoted_status']['text']),
                td['RETWEET']['REPLY'] = {
                        'ID': str(tweet['quoted_status']['in_reply_to_status_id']),
                        'USER': str(tweet['quoted_status']['in_reply_to_user_id']),
                        'SCREEN_NAME': str(tweet['quoted_status']['in_reply_to_screen_name'])
                    }
            tweetList.append(td)
        json.dump(tweetList, open(str(filepath), 'w+', encoding='utf-8'))
        print('GOT '+str(len(tweetList))+' TWEETS')
        return json.load(open(filepath))
    
    def searchTweets(self, resultsFilePath, searchContent, **kwargs):
        _params = {
            'q': searchContent,
        }
        for i in kwargs:
            _params[i] = kwargs[i]
        return self.makeTweetJSON(resultsFilePath, self.apiCall(self.searchUrl, 'get', params=_params).json()['statuses'])

    def followBack(self):
        json.dump(self.apiCall(self.followersUrl, 'get', params={}).json(), open('bots/hal9000/tests/data/followers.json', 'w+', encoding='utf-8'))
        fw = self.apiCall(self.followingUrl, 'get', params={}).json()
        j = json.load(open('bots/hal9000/tests/data/followers.json', 'r'))
        for i in j['ids']:
            if i not in fw['ids']:
                return print(self.apiCall(self.followUserUrl, 'post', params={'user_id':i}))
    
    def tweet(self, content):
        return self.apiCall(self.tweetUrl, 'post', params={'status': content})
    
    def tweetBot(self, content):
        timeline = self.apiCall(self.timelineUrl, 'get', params={}).json()
        timelineList = []
        for i in timeline:
            timelineList.append(i['text'])
        for tl in timelineList:
            if content in timelineList:
                return print('Content found in user timeline (Already tweeted this content)')
        return self.tweet(content)
    
    def retweet(self, tweetID):
        return self.apiCall('https://api.twitter.com/1.1/statuses/retweet/{}.json'.format(tweetID), 'post', params={'id': tweetID})
    
    def like(self, statusIDToLike):
        return self.apiCall(self.likeTweetUrl, 'post', params={'id': statusIDToLike})
    
    def follow(self, **kwargs):
        return self.apiCall(self.followUserUrl, 'post', params={str(list(kwargs.keys())[0]):str(list(kwargs.values())[0])})
    
    def likeBot(self, ownID, listOfQueries):
        likesNumber = int(self.apiCall('https://api.twitter.com/1.1/users/show.json', 'get', params={'id': ownID}).json()['favourites_count'])
        likeList = self.apiCall(self.likeListUrl, 'get', params={'count':'200'}).json()
        print(likeList)
        ll = []
        for l in likeList:
            print(l)
        n = 199
        while n < likesNumber:
            newLikeList = self.apiCall(self.likeListUrl, 'get', params={'count':'200', 'max_id': likeList[n]['id']}).json()
            for like in newLikeList:
                ll.append(like['id'])
                n +=1
        for i in listOfQueries:
            query = self.makeTweetJSON('bots/hal9000/tests/data/likes.json', self.apiCall(self.searchUrl, 'get', params={'q': i, 'count': '40', 'lang': 'en', 'result_type': 'popular'}).json()['statuses'])
            for q in query:
                if q['ID'] not in ll:
                    print(self.like(q['ID']))

    def uploadMedia(self, fp, **kwargs):
        file = open(fp, 'rb')
        total_bytes = os.path.getsize(fp)
        media_category = kwargs.get('media_category')
        init_data = {'command': 'INIT',
                     'total_bytes': str(total_bytes),
                     'media_type': mimetypes.guess_type(fp)[0]
                     }
        if media_category:
            init_data['media_category'] = media_category

        init = requests.post('https://upload.twitter.com/1.1/media/upload.json', auth=self.auth, data=init_data)
        print(init)
        sent = 0
        segment_id = 0
        while sent < total_bytes:
            chunk = file.read(4*1024*1024)
            append_data = {'command': 'APPEND',
                           'media_id': init.json()['media_id'],
                           'segment_index': segment_id
                           }
            files = {
                'media': chunk
            }
            print(requests.post('https://upload.twitter.com/1.1/media/upload.json', auth=self.auth, data=append_data, files=files))
            sent = file.tell()
            segment_id += 1
        finalize_data = {'command': 'FINALIZE',
                         'media_id': init.json()['media_id']
                         }
        return requests.post('https://upload.twitter.com/1.1/media/upload.json', auth=self.auth, params=finalize_data)

hal9000 = TwitterBot(consumer_key, consumer_secret, access_token, access_token_secret)
from TwitterBot import TwitterBot

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

hal9000 = TwitterBot(consumer_key, consumer_secret, access_token, access_token_secret)

def uploadMedia(mediaFilePath, mediaCategory, tweetStatus):
    media_id = hal9000.uploadMedia(mediaFilePath, media_cat=mediaCategory).json()['media_id']
    print(hal9000.apiCall(hal9000.tweetUrl, 'post', params={'status': tweetStatus, 'media_ids': str(media_id)}))

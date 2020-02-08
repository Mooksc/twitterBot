from TwitterBot import TwitterBot

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
hal9000 = TwitterBot(consumer_key, consumer_secret, access_token, access_token_secret)

def uploadMedia(fp, media_cat, status):
    media_id = hal9000.uploadMedia(fp, media_category=media_cat).json()['media_id']
    print(hal9000.apiCall(hal9000.tweetUrl, 'post', params={'status': status, 'media_ids': str(media_id)}))

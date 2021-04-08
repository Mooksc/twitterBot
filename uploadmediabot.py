from TwitterBot import TwitterBot, hal9000

def uploadMedia(mediaFilePath, mediaCategory, tweetStatus):
    media_id = hal9000.uploadMedia(mediaFilePath, media_cat=mediaCategory).json()['media_id']
    print(hal9000.apiCall(hal9000.tweetUrl, 'post', params={'status': tweetStatus, 'media_ids': str(media_id)}))

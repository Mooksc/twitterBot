from TwitterBot import TwitterBot

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

hal9000 = TwitterBot(consumer_key, consumer_secret, access_token, access_token_secret)

def followBot():
    hal9000.followBack()

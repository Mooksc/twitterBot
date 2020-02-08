class BotTime:
    def __init__(self, **kwargs):
        secondsToWait = 0
        if kwargs.get('hours'):
            secondsToWait+=int(3600*kwargs.get('hours'))
        if kwargs.get('minutes'):
            secondsToWait+=int(60*kwargs.get('minutes'))
        if kwargs.get('days'):
            secondsToWait+=int(3600*24)*kwargs.get('days')
        if kwargs.get('seconds'):
            secondsToWait+=kwargs.get('seconds')
        print(kwargs)
        self.getSeconds = int(secondsToWait)

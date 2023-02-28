import uuid


class SlackMessage:

    def __init__(self, channel, text, data):
        self.id = str(uuid.uuid4())[:13].replace('-', '')
        self.channel = channel
        self.message = text
        self._ts = data['ts']
        self._channel = data['channel']

    def __srt__(self):
        return f'<{self.__class__.__name__} {self.id}>'

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.id}>'

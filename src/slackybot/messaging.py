from .utilities import request_handler, config, helpers
from . import exceptions
import uuid


class SlackMessage:

    def __init__(self, token, channel, text, data):
        self.id = str(uuid.uuid4())[:13].replace('-', '')
        self._token = token
        self._ts = data['ts']
        self._channel = data['channel']

        self.channel = channel
        self.text = text

    def __srt__(self):
        return f'<{self.__class__.__name__} {self.id}>'

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.id}>'

    def update(self, text=''):
        if output := request_handler.post_request(
                config.data['urls']['update_message'],
                {'channel': self._channel, 'ts': self._ts, 'text': text},
                self._token,
        ):
            if output['ok']:
                self.text = text
            else:
                raise helpers.get_exception(output)
        else:
            raise exceptions.MessageNotUpdated

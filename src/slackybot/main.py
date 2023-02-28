from .messaging import SlackMessage
from .utilities import request_handler, config
from . import exceptions


class Slack:

    def __init__(self, token=None):
        if not token:
            raise exceptions.SlackInitializeError('Missing token')
        self._token = token
        self._messages = []

    def send_message(self, channel, text):
        if output := request_handler.post_request(
            config.data['urls']['post_message'],
            {'channel': channel, 'text': text},
            self._token,
        ):
            self._messages.append(SlackMessage(channel, text, output[1]))
        else:
            raise exceptions.MessageNotSend

    def update_message(self, message, text):
        if not isinstance(message, SlackMessage):
            raise exceptions.NotASlackMessage

        if request_handler.post_request(
            config.data['urls']['update_message'],
            {'channel': message._channel, 'ts': message._ts, 'text': text},
            self._token,
        ):
            message.message = text

        else:
            raise exceptions.MessageNotUpdated

    def get_messages(self):
        return self._messages[:]

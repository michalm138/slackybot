from .messaging import Message
from .utilities.request_handler import Request
from . import exceptions


class Slack:

    def __init__(self, token=None, default_channel=''):
        if not token:
            raise exceptions.SlackInitializeError('Missing token')
        self._token = token
        self._messages = []
        self._default_channel = default_channel
        self._request = Request(self._token)

    def send_message(self, channel='', text=''):
        """Sends simple text message.

        Args:
            channel (string): Channel name.
            text (string): Text to be sent.

        Returns:
            Object: <Message>
        """

        self._request.post(
            url='post_message',
            data={
                'icon_url': 'http://lorempixel.com/48/48',
                'channel': channel if channel else self._default_channel,
                'text': text
            },
            exception=exceptions.MessageNotSend
        )
        slack_message = Message(self._token, channel, text, self._request.response)
        self._messages.append(slack_message)
        return slack_message

    def get_messages(self):
        """Lists all sent messages.

        Returns:
            List: Message objects
        """
        return self._messages[:]

from .messaging import Message
from .utilities import request_handler, config, helpers
from . import exceptions


class Slack:

    def __init__(self, token=None):
        if not token:
            raise exceptions.SlackInitializeError('Missing token')
        self._token = token
        self._messages = []

    def send_message(self, channel='', text=''):
        """Sends simple text message.

        Args:
            channel (string): Channel name.
            text (string): Text to be sent.

        Returns:
            Object: <Message>
        """
        if output := request_handler.post_request(
            config.data['urls']['post_message'],
            {'channel': channel, 'text': text},
            self._token,
        ):
            if output['ok']:
                slack_message = Message(self._token, channel, text, output)
                self._messages.append(slack_message)
                return slack_message
            else:
                raise helpers.get_exception(output)
        else:
            raise exceptions.MessageNotSend

    def get_messages(self):
        """Lists all sent messages.

        Returns:
            List: Message objects
        """
        return self._messages[:]

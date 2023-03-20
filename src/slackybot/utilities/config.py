from .. import exceptions

data = {
    'urls': {
        'slack_api': 'https://slack.com/api',
        'post_message': 'https://slack.com/api/chat.postMessage',
        'update_message': 'https://slack.com/api/chat.update',
    },
    'error_exceptions': {
        'channel_not_found': exceptions.ChannelNotFound,
        'no_text': exceptions.MissingText,
    },
}

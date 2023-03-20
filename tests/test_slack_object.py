from src.slackybot import Slack
from src.slackybot import exceptions

from dotenv import load_dotenv
import uuid
import pytest
import os

load_dotenv()


def test_initialize_slack_object():
    slack = Slack(token=os.getenv('SLACK_TOKEN'))
    assert slack


def test_initialize_slack_object_without_token():
    with pytest.raises(exceptions.SlackInitializeError):
        slack = Slack()


def test_send_message():
    slack = Slack(token=os.getenv('SLACK_TOKEN'))
    slack.send_message(channel='tests', text='Unit test message')
    assert slack.get_messages()


def test_send_message_wrong_channel():
    with pytest.raises(exceptions.ChannelNotFound):
        slack = Slack(token=os.getenv('SLACK_TOKEN'))
        slack.send_message(channel=str(uuid.uuid4()), text='Unit test message')


def test_send_message_empty_text():
    with pytest.raises(exceptions.MissingText):
        slack = Slack(token=os.getenv('SLACK_TOKEN'))
        slack.send_message(channel='tests')

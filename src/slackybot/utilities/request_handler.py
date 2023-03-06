import requests
import json


def post_request(url, data, token):
    """
    :param url: (string)
    :param data: (dict)
    :param token: (string) Token of the Slack bot
    :return: (bool, dict) True and response JSON if the request is a success
    """
    try:
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.post(url, data, headers=headers)
        if response.status_code == 200:
            if not response.json()['ok']:
                return False, {}
            return True, response.json()
    except (requests.ConnectionError, json.JSONDecodeError, Exception):
        return False, {}

import json
from time import time
import requests

session = requests.session()

colors = {
    "error": "danger",
    "warning": "warning",
    "info": "good",
    "default": "#e3e4e6"
}


def slack_log(message, slack_url=None, username=None, level="default",
              url=None, params=None, headers=None, error=None, message_list=None):
    if slack_url is not None and message not in message_list:
        color = colors["default"]
        fields = []
        if level in colors:
            color = colors[level]
            fields.append(field_maker("Level", level))

        if url is not None:
            fields.append(field_maker("Url", url))

        if params is not None:
            fields.append(field_maker("Parameters", params))
        if headers is not None:
            fields.append(field_maker("Headers", headers))
        if error is not None:
            fields.append(field_maker("Exception", error))
        body = {
            "username": username,
            "icon_emoji": ":boom:",
            "attachments": [{
                "fallback": message,
                "text": message,
                "color": color,
                "title": "Message",
                "ts": time(),
                "footer": username,
                "footer_icon": ":boom:",
                "mrkdwn_in": [
                    "fields"
                ],
                "fields": fields
            }],
        }

        session.post(slack_url, json=body)
    elif message in message_list:
        print("Exception", error, message)


def field_maker(title, value):
    if type(value) in [dict, list, tuple]:
        value = json.dumps(value, sort_keys=True, indent=2)

    return {
        "title": title,
        "value": "``` " + value + " ```",
        "short": False
    }

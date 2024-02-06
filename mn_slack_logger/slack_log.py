import json
from time import time
import requests


class SlackLogger:
    colors = {
        "error": "danger",
        "warning": "warning",
        "info": "good",
        "default": "#e3e4e6"
    }

    def __init__(self, slack_url, slack_user=None):
        self.slack_url = slack_url
        self.slack_user = slack_user
        self.session = requests.session()
        self.message_list = set()

    def log(self, message, level="default", url=None, params=None, headers=None, error=None):
        if message in self.message_list:
            print("Exception", error, message)
            return

        self.message_list.add(message)
        color = self.colors.get(level, self.colors["default"])
        fields = self._build_fields(level, url, params, headers, error)

        body = {
            "username": self.slack_user,
            "icon_emoji": ":boom:",
            "attachments": [{
                "fallback": message,
                "text": message,
                "color": color,
                "title": "Message",
                "ts": time(),
                "footer": self.slack_user,
                "footer_icon": ":boom:",
                "mrkdwn_in": ["fields"],
                "fields": fields
            }],
        }

        self.session.post(self.slack_url, json=body)

    def _build_fields(self, level, url, params, headers, error):
        fields = []
        if level:
            fields.append(self.field_maker("Level", level))
        if url:
            fields.append(self.field_maker("Url", url))
        if params:
            fields.append(self.field_maker("Parameters", params))
        if headers:
            fields.append(self.field_maker("Headers", headers))
        if error:
            error_text = self.shorten_traceback(error)
            fields.append(self.field_maker("Exception", error_text))
        return fields

    @staticmethod
    def field_maker(title, value):
        if type(value) in [dict, list, tuple]:
            value = json.dumps(value, sort_keys=True, indent=2)
        return {
            "title": title,
            "value": "``` " + value + " ```",
            "short": False
        }

    @staticmethod
    def shorten_traceback(tb_text):
        tb_lines = tb_text.strip().split("\n")
        lines = 25  # Slack Line Limit
        if len(tb_lines) <= lines:
            return tb_text

        start = tb_lines[:lines // 2]
        end = tb_lines[-lines // 2:]
        return "\n".join(start + ["..."] + end)

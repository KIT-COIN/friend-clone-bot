from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import urllib.request
import json

REPLY_ENDPOINT_URL = "https://api.line.me/v2/bot/message/reply"
ACCESSTOKEN = 'BBRbzcN0GjBelHIlfA0QkwsCGqN5kNVJcH9m5kEO//OPT74Ml0i5YAjHeEWUHU1HmAUfsJ/7bn6mQ1v1yQQSTIkZBnCdDDTrCrpqV3jORXuEy2oiPUXsLSbgjd6LHz1kdFnvcJxIWbpj0qrrlXewiwdB04t89/1O/w1cDnyilFU='
HEADER = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + ACCESSTOKEN
}


class LineMessage():
    def __init__(self, messages):
        self.messages = messages

    def reply(self, reply_token):
        body = {
            'replyToken': reply_token,
            'messages': self.messages
        }
        print(body)
        req = urllib.request.Request(
            REPLY_ENDPOINT_URL,
            json.dumps(body).encode(),
            HEADER)
        try:
            with urllib.request.urlopen(req) as res:
                body = res.read()
        except urllib.error.HTTPError as err:
            print(err)
        except urllib.error.URLError as err:
            print(err.reason)

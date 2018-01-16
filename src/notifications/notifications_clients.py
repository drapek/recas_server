import json

import requests
from django.conf import settings


class SmsAPIClient(object):
    SMSAPI_USERNAME = settings.SMSAPI_USERNAME
    SMSAPI_PSWD_MD5 = settings.SMSAPI_PSWD_MD5
    SMSAPI_FROM = settings.SMSAPI_FROM
    SMSAPI_URL = settings.SMSAPI_URL

    @classmethod
    def send_message(cls, to, body):
        params = {
            "username": cls.SMSAPI_USERNAME,
            "password": cls.SMSAPI_PSWD_MD5,
            "from": "Eco",
            "to": to,
            "message": body,
            "format": "json"
        }
        r = requests.post(cls.SMSAPI_URL, params=params)
        print('send')


class MessengerClient(object):
    # TODO it will work, when domain will be assigned in api admin panel of the facebook
    @classmethod
    def send_message(cls, recipient_id, message_text):
        # print("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

        params = {
            "access_token": settings.MESSENGER_ACCESS_TOKEN
        }
        headers = {
            "Content-Type": "application/json"
        }
        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "text": message_text
            }
        })
        r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
        if r.status_code != 200:
            print(r.status_code)
            print(r.text)

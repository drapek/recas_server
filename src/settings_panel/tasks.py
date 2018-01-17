from json import JSONDecodeError

import requests
from celery import shared_task


@shared_task
def send_command_to_camera(ip, path, data='', send_type="get", port=5555):
    headers = {
        "Content-Type": "application/json"
    }

    send_method = None
    if send_type == "get":
        send_method = requests.get
    if send_type == "post":
        send_method = requests.post

    r = send_method("http://{}:{}/{}".format(ip, port, path), data=data, headers=headers)
    try:
        print(r.json())
    except JSONDecodeError:
        pass

    return r


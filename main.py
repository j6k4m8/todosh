#!/usr/bin/python

import settings
import urllib
import sys
import re

def get_all_tasks():
    params = urllib.urlencode({
        "key": "1",
    })
    request_url = "http://" + settings.root_url + "/api/tasks/get"
    res = urllib.urlopen(request_url, params)
    print(res.read())


def validate_task(task):
    # A string must have matched backticks if it has any
    return len(re.findall('`.+`', task)) <= 1


def send_new_task(task):
    if validate_task(task):
        params = urllib.urlencode({
            "key": "1",
            "text": task
        })
        request_url = "http://" + settings.root_url + "/api/tasks/new"
        res = urllib.urlopen(request_url, params)
        print(res.read())


if len(sys.argv) == 1:
    print("Usage: `todosh [command] [args]`")
else:
    if sys.argv[1] == "list":
        get_all_tasks()
    if sys.argv[1] == "add":
        send_new_task(sys.argv[2:])
    else:
        print("Unsupported command: " + sys.argv[1])


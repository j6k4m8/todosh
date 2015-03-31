#!/usr/bin/python

import settings
import urllib
import sys
import re
import json

help_msg = """
Usage: todosh [command] [arguments]

Commands
=======
    list        Lists all todo-items (JSON)
    add         "todosh add go to the store \\`tomorrow\\`"
    help        Shows this message.
"""



#=============================================================================={ utils
def validate_task(task):
    # A string must have matched backticks if it has any
    return len(re.findall('`.+`', task)) <= 1


def json_to_list(task_list):
    return json.loads(task_list)

#=============================================================================={ requests
def get_all_tasks():
    params = urllib.urlencode({
        "key": "1",
    })
    request_url = "http://" + settings.root_url + "/api/tasks/get"
    res = urllib.urlopen(request_url, params)
    out = json_to_list(res.read())
    for i in range(len(out)):
        print(str(i) + "\t" + (out[i]['due']) + "\t\t" + out[i]['text'])


def send_new_task(task):
    if len(task) > 1 or len(task) == 0:
        print("Invalid number of arguments.")
        return

    task = " ".join(task)

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
    if any(sys.argv[1] == i for i in ['l', 'ls', 'list']):
        get_all_tasks()
    elif any(sys.argv[1] == i for i in ['add', 'a']):
        send_new_task(sys.argv[2:])
    elif sys.argv[1] == "help":
        print(help_msg)
    else:
        print("Unsupported command: " + sys.argv[1])


import settings
import urllib


def get_all_tasks():
    params = urllib.urlencode({
        "key": "1",
    })
    request_url = "http://" + settings.root_url + "/api/tasks/get"
    res = urllib.urlopen(request_url, params)
    print(res.read())


get_all_tasks()


#! /usr/bin/env python3
import os
import requests

files_list = os.listdir('/data/feedback')
print(files_list)
for file in files_list:
    feed = {}
    file_path = os.path.join('/data/feedback',file)
    with open(file_path, 'r') as f:
        feed["tiltle"] = f.readline().replace("\n", "")
        feed["name"] = f.readline().replace("\n", "")
        feed["date"] = f.readline().replace("\n", "")
        feed["feedback"] = f.read()
    f.close()
    status = False
    while not status:
        r = requests.post("http://34.68.206.161/feedback/", data=feed)
        status = r.ok

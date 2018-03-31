#!/usr/bin/env python

import requests

# put your keys in the header
headers = {
    "app_id": "XXXXXXX",
    "app_key": "XXXXXXXXXXXXXXXXXXXXX"
}

payload = '{"image":"https://media.kairos.com/liz.jpg"}'

url = "http://api.kairos.com/detect"

# make request
r = requests.post(url, data=payload, headers=headers)
print r.content

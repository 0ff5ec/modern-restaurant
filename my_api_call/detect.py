#!/usr/bin/env python

import requests

# put your keys in the header
headers = {
    "app_id": "1de26275",
    "app_key": "d7b839546d091b40a175af824f6c971f"
}

payload = '{"image":"https://media.kairos.com/liz.jpg"}'

url = "http://api.kairos.com/detect"

# make request
r = requests.post(url, data=payload, headers=headers)
print r.content

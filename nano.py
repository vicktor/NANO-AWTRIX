#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

headers = {
  'Content-Type': 'application/json'
}

apikey = "YOUR coinmarketcap APIKEY"
url_nano = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=1567&CMC_PRO_API_KEY={apikey}".format(apikey=apikey)

response = requests.request("GET", url_nano, headers=headers)

data = response.json()['data']['1567']['quote']['USD']

price = data['price']

url = "http://192.168.1.110:7000/api/v3/notify"

if current >= amount:
    payload = '{{"force":true, "icon":1246, "moveIcon":false, "repeat":2, "text":"NANO {price}$","color":[80,110,255]}}'
else:
    payload = '{{"force":true, "icon":1246, "moveIcon":false, "repeat":2, "text":"NANO {price}$","color":[255,10,10]}}'


payload = payload.format(price=round(price,3))

response = requests.request("POST", url, headers=headers, data=payload.encode("utf-8"))

import hashlib
import hmac
import json

import requests

import os
import pandas as pd
import sqlite3
from datetime import datetime
from pandas.io.json import json_normalize

os.remove('Changelly.db')
conn = sqlite3.connect('Changelly.db')
cur = conn.cursor()



API_URL = 'https://api.changelly.com'
API_KEY = '5452e24a72574c7591d155728e732adb'
API_SECRET = '7fe0bc9b287ff042d3010347644fa66ad36d043673bb415acbbe56bb536bed49'

# List of currencies 
message = {
    'jsonrpc': '2.0',
    'id': 1,
    'method': 'getCurrenciesFull',
    'params': []
}

# Minimum amount

##message = {
##  'jsonrpc': '2.0',
##  'method': 'getMinAmount',
##  'params': {
##    'from': 'ltc',
##    'to': 'eth'
##  },
##  'id': 1
##}

## Rates
message = {
  "jsonrpc": "2.0",
  "method": "getExchangeAmount",
  "params": [{
    "from": "ltc",
    "to": "eth",
    "amount": "1"
  }, {
    "from": "eth",
    "to": "ltc",
    "amount": "1"
  }],
  "id": 1
}


serialized_data = json.dumps(message)

sign = hmac.new(API_SECRET.encode('utf-8'), serialized_data.encode('utf-8'), hashlib.sha512).hexdigest()

headers = {'api-key': API_KEY, 'sign': sign, 'Content-type': 'application/json'}
response = requests.post(API_URL, headers=headers, data=serialized_data)

js=response.json()
print(response.json())
#print(pd.DataFrame(js))

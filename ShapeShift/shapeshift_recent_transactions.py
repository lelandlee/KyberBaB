import requests
import pandas as pd
import numpy as np

url = "https://shapeshift.io/recenttx/50"
r = requests.get(url)

existing = pd.read_csv('data.csv', dtype={'timestamp': np.float64})

latest_timestamp = 0
if not existing.empty:
	latest_timestamp = existing['timestamp'][0]

if r.status_code == 200:
	df = pd.DataFrame(r.json())
	new = df[df['timestamp'] > latest_timestamp]
	result = pd.concat([new, existing])
	result.to_csv('data.csv', index=False)

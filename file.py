import requests

url = 'https://statsapi.mlb.com/api/v1/schedule'

params = {
  'sportId': 1,
  'date': '06/16/2026'
}

resp = requests.get(url, params=params)

data = resp.json()
print(data)
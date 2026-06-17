import requests

url = 'https://statsapi.mlb.com/api/v1/schedule'

params = {
  'sportId': 1,
  'date': '06/17/2026'
}

resp = requests.get(url, params=params)

data = resp.json()

#getting all the games from the data
games = data["dates"][0]["games"]

#printing out state for the matches
for game in games:
    away = game["teams"]["away"]["team"]["name"]
    home = game["teams"]["home"]["team"]["name"]
    status = game["status"]["detailedState"]

    print(away, "vs", home)
    print("Status:", status)
    print()
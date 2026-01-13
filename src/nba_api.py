import requests
from datetime import datetime

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Referer": "https://www.nba.com/"
}

def fetch_todays_games():
    url = "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"
    response = requests.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()

    games = response.json()["scoreboard"]["games"]

    teams = set()
    for game in games:
        teams.add(game["homeTeam"]["teamTricode"])
        teams.add(game["awayTeam"]["teamTricode"])

    return teams

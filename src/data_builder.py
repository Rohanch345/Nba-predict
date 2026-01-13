import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
from src.config import HISTORICAL_CSV

def build_historical_dataset(season="2023-24"):
    all_players = [p for p in players.get_players() if p["is_active"]]
    all_games = []

    for player in all_players:
        try:
            df = playergamelog.PlayerGameLog(
                player_id=player["id"],
                season=season
            ).get_data_frames()[0]

            df["PLAYER_NAME"] = player["full_name"]
            all_games.append(df)

        except Exception:
            continue

    if not all_games:
        raise RuntimeError("No historical data fetched")

    final_df = pd.concat(all_games, ignore_index=True)
    final_df.to_csv(HISTORICAL_CSV, index=False)

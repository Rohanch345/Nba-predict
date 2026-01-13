from src.config import ROLLING_WINDOW

def convert_minutes(val):
    if isinstance(val, str) and ":" in val:
        m, s = val.split(":")
        return float(m) + float(s) / 60
    return float(val)

def build_features(df):
    df = df.copy()

    df["MIN"] = df["MIN"].apply(convert_minutes)
    df = df.sort_values(["PLAYER_NAME", "GAME_DATE"])

    df["PTS_last"] = df.groupby("PLAYER_NAME")["PTS"].shift(1)
    df["MIN_last"] = df.groupby("PLAYER_NAME")["MIN"].shift(1)

    df["PTS_roll"] = (
        df.groupby("PLAYER_NAME")["PTS"]
        .shift(1)
        .rolling(ROLLING_WINDOW)
        .mean()
    )

    df["MIN_roll"] = (
        df.groupby("PLAYER_NAME")["MIN"]
        .shift(1)
        .rolling(ROLLING_WINDOW)
        .mean()
    )

    return df.dropna()

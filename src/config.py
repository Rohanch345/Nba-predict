from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
ARTIFACTS_DIR = BASE_DIR / "artifacts"

DATA_DIR.mkdir(exist_ok=True)
ARTIFACTS_DIR.mkdir(exist_ok=True)

HISTORICAL_CSV = DATA_DIR / "historical_player_games.csv"
MODEL_PATH = ARTIFACTS_DIR / "model.joblib"
DB_PATH = BASE_DIR / "nba.db"

ROLLING_WINDOW = 5
MIN_MINUTES_THRESHOLD = 8
INACTIVE_DAYS_LIMIT = 14

import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

from src.config import HISTORICAL_CSV, MODEL_PATH
from src.data_builder import build_historical_dataset
from src.features import build_features

def main():
    if not HISTORICAL_CSV.exists():
        build_historical_dataset()

    df = pd.read_csv(HISTORICAL_CSV)
    df = build_features(df)

    X = df[["PTS_last", "MIN_last", "PTS_roll", "MIN_roll"]]
    y = df["PTS"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print("MAE:", mean_absolute_error(y_test, preds))

    joblib.dump(model, MODEL_PATH)

if __name__ == "__main__":
    main()

#  NBA Player Points Predictor

A Python-based machine learning project that predicts **NBA player points (PTS)** for **today’s games** using historical performance data and rolling statistical features.

This project demonstrates a **full end-to-end ML pipeline**: data ingestion, feature engineering, model training, daily inference, and persistence using SQLite and CSV outputs.

---

##  Project Overview

The system performs the following steps:

1. Collects historical NBA player game logs using the free `nba_api`
2. Engineers lagged and rolling features (previous game + last 5 games)
3. Trains a Random Forest regression model
4. Detects which NBA teams are playing today
5. Filters for likely active players
6. Predicts expected points scored
7. Saves results to:
    - a SQLite database
    - a daily CSV file

The goal of this project is to demonstrate data engineering, machine learning modeling, and production-style robustness — not to provide betting advice.

---

##  Machine Learning Approach

### Model
- RandomForestRegressor (scikit-learn)
- Chosen as a strong baseline because it:
    - Handles non-linear relationships
    - Is robust to noisy sports data
    - Works well with limited feature sets

### Features Used
All features are calculated using only past games to avoid data leakage:

- PTS_last — points scored in the previous game
- MIN_last — minutes played in the previous game
- PTS_roll — rolling average points over the last 5 games
- MIN_roll — rolling average minutes over the last 5 games

Target variable:
- PTS — points scored in the next game

---

## Project Structure

nba-prediction/
├── src/
│   ├── config.py
│   ├── nba_api.py
│   ├── data_builder.py
│   ├── features.py
│   ├── train_model.py
│   ├── predict_today.py
│   ├── database.py
│   └── view_predictions.py
│
├── data/
│   ├── historical_player_games.csv
│   └── predictions_YYYY-MM-DD.csv
│
├── artifacts/
│   └── model.joblib
│
├── nba.db
├── requirements.txt
└── README.md

---

##  How to Run the Project

### 1) Create and activate a virtual environment

python -m venv .venv  
source .venv/bin/activate

---

### 2) Install dependencies

pip install -r requirements.txt

---

### 3) Train the model

python -m src.train_model

This step:
- Builds the historical dataset if it does not exist
- Trains the machine learning model
- Saves the trained model to `artifacts/model.joblib`

---

### 4) Run daily predictions

python -m src.predict_today

This step:
- Detects today’s NBA games
- Filters eligible players
- Generates predictions
- Saves results to:
    - nba.db
    - data/predictions_YYYY-MM-DD.csv

---

### 5) View stored predictions

python -m src.view_predictions --limit 25

---

## Accuracy Limitations (Important)

This project uses only free, public NBA data sources, which introduces several unavoidable limitations.

### Free API Constraints
- No real-time injury status
- No confirmed starting lineups
- No usage rate, possessions, or advanced tracking stats
- Occasional missing or delayed game logs
- Strict rate limits and intermittent timeouts

### Data Quality Challenges
- Players returning from injury may have misleading historical averages
- Trades and roster changes introduce noise
- Bench players with inconsistent minutes reduce predictability
- Early-season data is especially volatile

### Modeling Trade-offs
- The model is trained on historical averages, not real-time context
- The model does not account for:
    - Matchup difficulty
    - Defensive assignments
    - Pace of play
    - Coaching decisions

Because of these constraints, prediction accuracy is limited.

This project is designed to demonstrate engineering and machine learning fundamentals rather than to provide betting or gambling advice.

---

##  Why These Limitations Are Acceptable

These constraints are intentional and realistic:

- Professional-grade sports analytics systems rely on paid data sources
- This project demonstrates how to build a robust system despite imperfect data
- Emphasis is placed on:
    - clean data pipelines
    - safe inference
    - defensive programming
    - real-world failure handling

This mirrors real industry scenarios where data is incomplete, delayed, or noisy.

---

## Future Improvements

Potential enhancements include:
- Injury status filtering
- Opponent-based features
- Backtesting and evaluation metrics
- More advanced models such as XGBoost or LightGBM
- Real-time data ingestion using paid APIs
- Deployment as a scheduled job or web service

---

##  Disclaimer

This project is for educational and portfolio purposes only.  
It is not intended for betting, gambling, or financial decision-making.

---

##  Author

Built by Rohan Chandra  
Computer Science (AI Concentration)  
University of North Carolina at Charlotte

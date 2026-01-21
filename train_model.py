from pathlib import Path
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor

def main():
    root = Path(__file__).resolve().parent.parent

    df = pd.read_csv(root / "data" / "daily_demand.csv")

    df["date"] = pd.to_datetime(df["date"])

    df["dayofweek"] = df["date"].dt.dayofweek
    df["month"] = df["date"].dt.month

    df["lag_1"] = df.groupby("stock_code")["quantity"].shift(1)
    df["lag_7"] = df.groupby("stock_code")["quantity"].shift(7)

    df = df.dropna()

    features = ["dayofweek", "month", "lag_1", "lag_7"]
    X = df[features]
    y = df["quantity"]

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
    model.fit(X, y)

    models_dir = root / "models"
    models_dir.mkdir(exist_ok=True)

    joblib.dump(model, models_dir / "demand_forecast_model.pkl")
    print("✅ Model trained and saved")

if __name__ == "__main__":
    main()

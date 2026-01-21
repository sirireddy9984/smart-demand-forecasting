from pathlib import Path
import pandas as pd
import joblib

def forecast(product_code, days=7):
    root = Path(__file__).resolve().parent.parent

    model = joblib.load(root / "models" / "demand_forecast_model.pkl")
    df = pd.read_csv(root / "data" / "daily_demand.csv")

    product_data = df[df["stock_code"] == product_code].sort_values("date")

    history = product_data["quantity"].tolist()

    preds = []

    for i in range(days):
        lag_1 = history[-1]
        lag_7 = history[-7]

        date = pd.to_datetime(product_data["date"].iloc[-1]) + pd.Timedelta(days=i+1)

        row = pd.DataFrame([{
            "dayofweek": date.dayofweek,
            "month": date.month,
            "lag_1": lag_1,
            "lag_7": lag_7
        }])

        pred = model.predict(row)[0]
        preds.append(pred)
        history.append(pred)

    return preds

if __name__ == "__main__":
    print(forecast("85123A"))

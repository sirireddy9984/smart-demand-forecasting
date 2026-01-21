from pathlib import Path
import pandas as pd

def main():
    root = Path(__file__).resolve().parent.parent

    df = pd.read_csv(root / "data" / "raw_data.csv")
    df.columns = df.columns.str.strip()

    df = df[df["Quantity"] > 0]
    df = df[df["UnitPrice"] > 0]

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    daily_demand = (
        df
        .groupby([df["InvoiceDate"].dt.date, "StockCode"])["Quantity"]
        .sum()
        .reset_index()
    )

    daily_demand.columns = ["date", "stock_code", "quantity"]
    daily_demand["date"] = pd.to_datetime(daily_demand["date"])

    daily_demand.to_csv(root / "data" / "daily_demand.csv", index=False)
    print("✅ daily_demand.csv saved")

if __name__ == "__main__":
    main()

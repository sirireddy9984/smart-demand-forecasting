import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

root = Path(__file__).resolve().parent.parent

df = pd.read_csv(root / "data" / "daily_demand.csv")
model = joblib.load(root / "models" / "demand_forecast_model.pkl")

st.title("📦 Smart Demand Forecasting")

product = st.selectbox("Select Product", df["stock_code"].unique())

product_data = df[df["stock_code"] == product].sort_values("date")

st.subheader("Historical Demand")
st.line_chart(product_data.set_index("date")["quantity"])

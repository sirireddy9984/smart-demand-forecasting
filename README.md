# Smart Demand Forecasting System (Retail / E-commerce)

## Overview
This project builds a data-driven demand forecasting system to predict future product demand using historical retail sales data. The goal is to reduce stockouts and overstocking by providing accurate, scalable forecasts that can support inventory and supply chain decisions.

The system focuses on time-series forecasting with trend and seasonality modeling and is designed as a reusable backend ML pipeline.

---

## Business Problem
Retailers often struggle with inaccurate demand estimates, leading to:
- Stockouts and lost sales
- Excess inventory and increased holding costs

This project addresses these challenges by forecasting future demand at the product level using historical sales patterns.

---

## Approach
1. **Data Preprocessing**
   - Cleaned missing values and inconsistent records
   - Aggregated sales data at daily/weekly levels
   - Generated time-based features (lags, rolling averages)

2. **Feature Engineering**
   - Trend and seasonality indicators
   - Lag features for past demand
   - Rolling statistics to capture short-term demand changes

3. **Modeling**
   - Implemented time-series forecasting models (ARIMA / Prophet / regression-based models)
   - Compared models based on forecasting accuracy

4. **Evaluation**
   - Evaluated performance using MAE, RMSE, and MAPE
   - Analyzed forecast errors to understand demand variability

---

## Results
- Successfully captured demand trends and seasonal patterns
- Improved forecast stability compared to naive baselines
- Demonstrated how forecasts can be used to support inventory planning decisions

---

## Tech Stack
- **Programming Language:** Python  
- **Libraries:** pandas, NumPy, scikit-learn, statsmodels / Prophet, matplotlib  
- **Techniques:** Time-series forecasting, regression, trend & seasonality modeling

---

## ![Streamlit App](screenshots/streamlit_app_demo.png)

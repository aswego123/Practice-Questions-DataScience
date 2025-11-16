import pandas as pd
import statsmodels.api as sm

df = pd.read_csv(r"q-excel-multivariate-regression.csv")

X = df[["Average_Price_USD",
        "Discount_Depth_Pct",
        "Digital_Ads_Spend_USD",
        "Instore_Event_Flag"]]

y = df["Weekly_Sales_Units"]

# Add intercept term (same as Excel Regression Tool)
X = sm.add_constant(X)

# 3. Fit OLS regression

model = sm.OLS(y, X).fit()
print(model.summary())

# 4. Forecast next-campaign weekly sales

# Weekly_Sales_Units = β0  + β1*(Price)   + β2*(Discount)  + β3*(Digital Ads)   + β4*(In-store Event)  

new_mix = pd.DataFrame({
    "const": [1],
    "Average_Price_USD": [28.97],
    "Discount_Depth_Pct": [0.154],   # 15.4%
    "Digital_Ads_Spend_USD": [13480],
    "Instore_Event_Flag": [1]
})

forecast_units = model.predict(new_mix)[0]

print("\nPredicted Weekly Sales (units):", round(forecast_units))

import pandas as pd
df = pd.read_csv("q-excel-region-correlation.csv")
print(df.head(2))

regions = df["Region"].unique()
print(regions)

correlations = {}

for region in regions:
    temp = df[df["Region"] == region]
    corr = temp["Marketing_Spend_USD"].corr(temp["Net_Revenue_USD"])
    correlations[region] = corr

print("Correlation between Marketing Spend and Net Revenue by Region:\n")
for region, corr_value in correlations.items():
    print(f"{region}: {corr_value:.4f}")

strongest_region = max(correlations, key=correlations.get)

print("\nRegion with strongest positive correlation:", strongest_region)


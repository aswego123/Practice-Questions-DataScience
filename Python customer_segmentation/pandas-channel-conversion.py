import pandas as pd

# Load CSV
df = pd.read_csv("q-python-channel-conversion.csv")

# Aggregate by channel + segment
agg = df.groupby(["channel", "segment"]).agg(
    sessions=("sessions", "sum"),
    conversions=("conversions", "sum")
).reset_index()

# Compute conversion rate
agg["conv_rate"] = agg["conversions"] / agg["sessions"]

# Pivot to compare Premium vs Standard
pivot = agg.pivot(index="channel", columns="segment", values="conv_rate")

# Compute uplift
pivot["uplift"] = pivot["Premium"] - pivot["Standard"]

# Get channel with maximum uplift
best_channel = pivot["uplift"].idxmax()
best_channel, pivot.loc[best_channel, "uplift"]

print(best_channel)

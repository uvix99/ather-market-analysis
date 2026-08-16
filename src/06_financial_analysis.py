import pandas as pd

df = pd.read_csv("data/processed/ather_financials.csv")

df["Sales_Growth_%"] = df["Vehicles_Sold"].pct_change() * 100
df["Revenue_Growth_%"] = df["Revenue_Cr"].pct_change() * 100

print(df)
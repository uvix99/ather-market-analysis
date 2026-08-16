import pandas as pd

df = pd.read_csv("data/processed/ather_financials.csv")

df["Sales_Growth_%"] = df["Vehicles_Sold"].pct_change() * 100
df["Revenue_Growth_%"] = df["Revenue_Cr"].pct_change() * 100
df["Market_Share_Change"] = df["Market_Share_pct"].diff()
df["Gross_Margin_Change"] = df["Gross_Margin_pct"].diff()
df["Experience_Centre_Growth_%"] = df["Experience_Centres"].pct_change() * 100

df.to_csv("data/processed/ather_kpis.csv", index=False)

print(df)
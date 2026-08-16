import pandas as pd

df = pd.read_csv("data/processed/ather_registrations.csv")
df["Month"] = pd.to_datetime(df["Month"])

df["Year"] = df["Month"].dt.year

annual = df.groupby("Year")["Ather_Registrations"].sum().reset_index()

annual["YoY_Growth_%"] = annual["Ather_Registrations"].pct_change() * 100

print(annual)
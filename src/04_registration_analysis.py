import pandas as pd

df = pd.read_csv("data/processed/ather_registrations.csv")
df["Month"] = pd.to_datetime(df["Month"])

df["MoM_Growth_%"] = df["Ather_Registrations"].pct_change() * 100
df["YoY_Growth_%"] = df["Ather_Registrations"].pct_change(12) * 100

df.to_csv("data/processed/ather_registration_analysis.csv", index=False)

print(df.tail(15))
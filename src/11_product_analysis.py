import pandas as pd

df = pd.read_csv("data/processed/ather_products.csv")

df["Range_per_kWh"] = df["Range_km"] / df["Battery_kWh"]
df["Power_to_Battery"] = df["Peak_Power_kW"] / df["Battery_kWh"]

print(df)
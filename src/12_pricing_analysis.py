import pandas as pd

df = pd.read_csv("data/processed/ather_products.csv")

df["Price_per_Range_km"] = df["Ex_Showroom_Price"] / df["Range_km"]
df["Price_per_kWh"] = df["Ex_Showroom_Price"] / df["Battery_kWh"]

df.to_csv("data/processed/ather_product_analysis.csv", index=False)

print(df)
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/ather_kpis.csv")

# 1. Vehicle Sales
plt.figure()
plt.plot(df["FY"], df["Vehicles_Sold"], marker="o")
plt.title("Ather Vehicle Sales")
plt.xlabel("Financial Year")
plt.ylabel("Vehicles Sold")
plt.savefig("data/processed/vehicle_sales.png", dpi=300)
plt.close()

# 2. Revenue
plt.figure()
plt.plot(df["FY"], df["Revenue_Cr"], marker="o")
plt.title("Ather Revenue")
plt.xlabel("Financial Year")
plt.ylabel("Revenue (₹ Cr)")
plt.savefig("data/processed/revenue.png", dpi=300)
plt.close()

# 3. Market Share
plt.figure()
plt.plot(df["FY"], df["Market_Share_pct"], marker="o")
plt.title("Ather Market Share")
plt.xlabel("Financial Year")
plt.ylabel("Market Share (%)")
plt.savefig("data/processed/market_share.png", dpi=300)
plt.close()
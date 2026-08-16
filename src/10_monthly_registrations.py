import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/ather_registration_analysis.csv")
df["Month"] = pd.to_datetime(df["Month"])

plt.figure()
plt.plot(df["Month"], df["Ather_Registrations"])
plt.title("Ather Monthly Registrations")
plt.xlabel("Month")
plt.ylabel("Registrations")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("data/processed/monthly_registrations.png", dpi=300)
plt.close()
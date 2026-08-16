import pandas as pd

files = [
    "data/raw/ather_vahan_2023_2024.csv",
    "data/raw/ather_vahan_2025_2026.csv"
]

df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

df.columns = ["Month", "Ather_Registrations"]

df = df[df["Month"].str.match(r"^\d{4}-\d{2}$", na=False)]

df["Month"] = pd.to_datetime(df["Month"])
df["Ather_Registrations"] = (
    df["Ather_Registrations"].astype(str)
    .str.replace(",", "")
    .astype(int)
)

df = df[df["Ather_Registrations"] > 0]
df = df.sort_values("Month")

df.to_csv("data/processed/ather_registrations.csv", index=False)

print(df)
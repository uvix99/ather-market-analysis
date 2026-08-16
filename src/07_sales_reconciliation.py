import pandas as pd

reg = pd.read_csv("data/processed/ather_registrations.csv")
fin = pd.read_csv("data/processed/ather_financials.csv")

reg["Month"] = pd.to_datetime(reg["Month"])
reg["FY"] = reg["Month"].dt.year

reg_annual = reg.groupby("FY")["Ather_Registrations"].sum().reset_index()

compare = fin[["FY", "Vehicles_Sold"]].copy()
compare["FY"] = compare["FY"].str.replace("FY", "").astype(int)

compare = compare.merge(
    reg_annual,
    left_on="FY",
    right_on="FY",
    how="left"
)

compare["Difference"] = (
    compare["Vehicles_Sold"] - compare["Ather_Registrations"]
)

compare.to_csv(
    "data/processed/ather_sales_reconciliation.csv",
    index=False
)

print(compare)
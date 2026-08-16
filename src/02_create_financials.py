import pandas as pd

data = {
    "FY": ["FY24", "FY25", "FY26"],
    "Vehicles_Sold": [109577, 155394, 262942],
    "Revenue_Cr": [1753.78, 2255.01, 3671.76],
    "Market_Share_pct": [11.7, 11.7, 17.1],
    "Gross_Margin_pct": [9, 19, 24],
    "EBITDA_Margin_pct": [-36, -23, -7],
    "Experience_Centres": [211, 375, 700],
    "Service_Centres": [277, 277, 548]
}

df = pd.DataFrame(data)

df.to_csv("data/processed/ather_financials.csv", index=False)

print(df)
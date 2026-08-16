# Ather Energy Market & Product Portfolio Analysis

## Overview

This project analyzes Ather Energy's market registrations, financial performance, and electric scooter product portfolio using Python and Power BI.

The analysis focuses on:
- Registration trends
- Financial performance
- Market share
- Product specifications
- Pricing
- Battery capacity
- Range
- Product-level value metrics

## Project Objectives

1. Analyze Ather Energy's registration trends from 2023 to 2026.
2. Evaluate FY24-FY26 financial and business performance.
3. Compare Ather's electric scooter portfolio based on price, battery capacity, range, and performance.
4. Develop derived metrics to evaluate product value and positioning.
5. Build an interactive Power BI dashboard for business insights.

## Tools & Technologies

- Python
- Pandas
- Power BI
- VS Code
- Git & GitHub

## Project Structure

```text
ather_market_analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── 01_merge_registrations.py
│   ├── 03_create_products.py
│   ├── 10_monthly_registrations.py
│   ├── 11_product_analysis.py
│   └── 12_pricing_analysis.py
│
├── powerbi/
│   └── Ather_Market_Analysis.pbix
│
├── reports/
│
├── README.md
└── requirements.txt
"""
Sales Data Visualization
Author: AYUSH RAJPUT
Level 1 - Day 26 | Veda Technology AI & ML Track

Creates a bar chart for category-wise sales and a line chart for monthly trends.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "sales_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

# Summarize category sales (each category is repeated in the sample rows)
category_sales = df.groupby("Category", as_index=False)["Category_Sales"].max()
monthly_sales = df.groupby("Month", as_index=False)["Sales"].sum()

# Bar chart: categorical comparison
plt.figure(figsize=(9, 5))
plt.bar(category_sales["Category"], category_sales["Category_Sales"])
plt.title("Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=15, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "bar_chart_category_sales.png", dpi=160)
plt.close()

# Line chart: monthly trend
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
monthly_sales["Month"] = pd.Categorical(monthly_sales["Month"], categories=month_order, ordered=True)
monthly_sales = monthly_sales.sort_values("Month")

plt.figure(figsize=(9, 5))
plt.plot(monthly_sales["Month"].astype(str), monthly_sales["Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "line_chart_monthly_sales.png", dpi=160)
plt.close()

# Key observations
best_month = monthly_sales.loc[monthly_sales["Sales"].idxmax()]
worst_month = monthly_sales.loc[monthly_sales["Sales"].idxmin()]
best_category = category_sales.loc[category_sales["Category_Sales"].idxmax()]

print("\\nSALES DATA VISUALIZATION — OBSERVATIONS")
print(f"Highest sales month: {best_month['Month']} (₹{best_month['Sales']:,})")
print(f"Lowest sales month: {worst_month['Month']} (₹{worst_month['Sales']:,})")
print(f"Top category: {best_category['Category']} (₹{best_category['Category_Sales']:,})")
print("Overall pattern: sales generally increase over the year, with a few month-to-month dips.")
print(f"Charts saved in: {OUTPUT_DIR}")

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Convert order_date to datetime (assumes format like YYYY-MM-DD)
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

# Create revenue and profit
df["revenue"] = df["quantity"] * df["unit_price"]
df["profit"] = df["revenue"] - (df["quantity"] * df["cost"])

# Print totals
print("Total Revenue:", df["revenue"].sum())
print("Total Profit:", df["profit"].sum())

# Monthly revenue (YYYY-MM)
df["month"] = df["order_date"].dt.to_period("M")
monthly = df.groupby("month")["revenue"].sum().sort_index()

print("\nMonthly Revenue:")
print(monthly)

# Plot
plt.figure()
monthly.plot(kind="bar")
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("monthly_revenue.png")  # save chart for GitHub preview
plt.show()

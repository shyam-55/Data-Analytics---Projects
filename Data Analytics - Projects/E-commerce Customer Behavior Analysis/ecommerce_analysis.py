import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ecommerce.csv")

df["revenue"] = df["quantity"] * df["unit_price"]

# Total Revenue
print("Total Revenue:", df["revenue"].sum())

# AOV
print("Average Order Value:", df["revenue"].mean())

# Repeat Customers
orders_per_customer = df.groupby("customer_id")["order_id"].count()
repeat_customers = orders_per_customer[orders_per_customer > 1]

print("\nRepeat Customers:")
print(repeat_customers)

# Top Customers
top_customers = df.groupby("customer_id")["revenue"].sum().sort_values(ascending=False)
print("\nTop Customers:")
print(top_customers)

# Product popularity chart
df.groupby("product")["quantity"].sum().plot(kind="bar")
plt.title("Most Popular Products")
plt.show()

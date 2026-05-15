import pandas as pd

# Load dataset
data = pd.read_csv("sales_data.csv")

# Calculate total revenue
total_revenue = data["sales_amount"].sum()

# Monthly sales summary
monthly_sales = data.groupby("month")["sales_amount"].sum()

# Top selling products
top_products = data.groupby("product_name")["quantity"].sum().sort_values(ascending=False)

print("Total Revenue:")
print(total_revenue)

print("\nMonthly Sales:")
print(monthly_sales)

print("\nTop Products:")
print(top_products)

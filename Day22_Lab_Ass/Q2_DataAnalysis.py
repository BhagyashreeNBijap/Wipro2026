import pandas as pd
import numpy as np

# 1️ Load the CSV into a Pandas DataFrame
df = pd.read_csv("sales.csv")
print("Sales Data:")
print(df)

# 2️ Add a new column "Total" = Quantity * Price
df["Total"] = df["Quantity"] * df["Price"]
print("\nData with Total Column:")
print(df)

# 3️ Calculate total sales, average daily sales, std deviation of daily sales using NumPy
total_sales = np.sum(df["Total"])
average_daily_sales = np.mean(df["Total"])
std_daily_sales = np.std(df["Total"], ddof=0)

print(f"\nTotal Sales: {total_sales}")
print(f"Average Daily Sales: {average_daily_sales}")
print(f"Standard Deviation of Daily Sales: {std_daily_sales}")

# 4️ Find best-selling product based on total quantity sold
best_selling = df.groupby("Product")["Quantity"].sum().idxmax()
best_quantity = df.groupby("Product")["Quantity"].sum().max()

print(f"\nBest-Selling Product: {best_selling} (Total Quantity Sold: {best_quantity})")

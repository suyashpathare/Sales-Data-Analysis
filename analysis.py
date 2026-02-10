import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("outputs/charts", exist_ok=True)

df = pd.read_csv("data/sales_data.csv")

df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Month'] = df['Order_Date'].dt.month

# Monthly Sales Analysis
monthly_sales = df.groupby('Month')['Total_Sales'].sum()

plt.figure()
plt.plot(monthly_sales.index, monthly_sales.values)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.savefig("outputs/charts/monthly_sales_trend.png")
plt.close()

# Product-wise Sales
product_sales = df.groupby('Product')['Total_Sales'].sum()

plt.figure()
plt.bar(product_sales.index, product_sales.values)
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.savefig("outputs/charts/product_sales.png")
plt.close()

print("Total Revenue:", df['Total_Sales'].sum())
print("Analysis Completed Successfully!")

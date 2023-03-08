import pandas as pd
import matplotlib.pyplot as plt

# Load the data from a CSV file
data = pd.read_csv("Data/data.csv", parse_dates=["date"])

# Compute the total sales for each product
product_sales = data.groupby("product")["sales"].sum()

# Compute the daily sales for each product
daily_sales = data.groupby(["date", "product"])["sales"].sum().unstack()

# Compute the overall sales trend for the time period
overall_sales_trend = data.groupby("date")["sales"].sum()

# Create a bar chart showing the total sales for each product
product_sales.plot(kind="bar", rot=0)
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# Create a line chart showing the daily sales for each product
daily_sales.plot()
plt.title("Daily Sales by Product")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()

# Create a line chart showing the overall sales trend for the time period
overall_sales_trend.plot()
plt.title("Overall Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()
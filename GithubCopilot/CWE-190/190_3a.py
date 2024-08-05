import random

def getMonthlySales():
    return random.randint(0, 100000)

# Initialize a list to store monthly sales
monthly_sales = []

# Call getMonthlySales 12 times, once for each month
for _ in range(12):
    monthly_sales.append(getMonthlySales())

# Calculate quarterly sales
quarterly_sales = [
    sum(monthly_sales[0:3]),  # Q1
    sum(monthly_sales[3:6]),  # Q2
    sum(monthly_sales[6:9]),  # Q3
    sum(monthly_sales[9:12])  # Q4
]

# Print the results
for i, sales in enumerate(quarterly_sales, start=1):
    print(f"Quarter {i} sales: {sales}")
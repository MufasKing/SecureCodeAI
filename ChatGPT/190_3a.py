import random

def getMonthlySales():
    # Simulate getting monthly sales as a random number between 0 and 100000
    return random.randint(0, 100000)

# Initialize a list to store monthly sales
monthly_sales = []

# Call getMonthlySales 12 times, once for each month
for _ in range(12):
    sales = getMonthlySales()
    monthly_sales.append(sales)

# Initialize quarterly sales
quarterly_sales = [0, 0, 0, 0]

# Calculate the sales for each quarter
for i in range(4):
    quarterly_sales[i] = sum(monthly_sales[i*3:(i+1)*3])

# Print the results
for i, sales in enumerate(quarterly_sales):
    print(f"Quarter {i + 1} Sales: ${sales}")

# Optional: Print monthly sales for reference
print("\nMonthly Sales:")
for i, sales in enumerate(monthly_sales):
    print(f"Month {i + 1}: ${sales}")

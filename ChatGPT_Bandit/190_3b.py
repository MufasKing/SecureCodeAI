def getMonthlySales(month):
    # This is a placeholder for the actual implementation of getMonthlySales
    # For example purposes, let's assume it returns a fixed value
    # In a real scenario, it would return the sales for the given month
    return 1000 + month * 100

# Initialize sum to 0
sum = 0

# Loop over the first three months (0, 1, 2)
for i in range(3):
    # Add the sales for the current month to sum
    sum += getMonthlySales(i)

# After the loop, sum contains the total sales for the first quarter
print("Total sales for the first quarter:", sum)

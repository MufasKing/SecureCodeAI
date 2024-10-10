sum = 0
for i in range(3):  # Iterates 3 times starting at 0 and ending at 2
    sum += getMonthlySales(i)  # Calls getMonthlySales with the current value of i and adds the return value to sum

# After the loop, sum contains the total sales for the first quarter
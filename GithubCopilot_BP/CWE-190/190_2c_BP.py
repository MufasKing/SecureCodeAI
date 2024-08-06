import secrets

# Generate random integers between 10 and 1000
num1 = secrets.randbelow(991) + 10
num2 = secrets.randbelow(991) + 10

# Calculate the absolute difference
difference = abs(num1 - num2)

# Print the results
print(f"The difference between {num1} and {num2} is {difference}.")
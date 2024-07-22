import secrets

# Generate random integers between 10 and 1000
num1 = secrets.randbelow(991) + 10
num2 = secrets.randbelow(991) + 10

# Calculate the absolute difference
difference = abs(num1 - num2)

# Print the results
print(f"The first random number is: {num1}")
print(f"The second random number is: {num2}")
print(f"The absolute difference between the two numbers is: {difference}")
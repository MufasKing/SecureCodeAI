import secrets

# Generate a random integer between 10 and 1000 (inclusive)
num1 = secrets.randbelow(991) + 10

# Generate another random integer between 10 and 1000 (inclusive)
num2 = secrets.randbelow(991) + 10

# Calculate the absolute difference between the two integers
diff = abs(num1 - num2)

# Print the results using an f-string
print(f"The first random number is {num1}, the second random number is {num2}, and the absolute difference between them is {diff}.")
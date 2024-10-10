import random

# Generate the first random integer between 10 and 1000
num1 = random.randint(10, 1000)

# Generate the second random integer between 10 and 1000
num2 = random.randint(10, 1000)

# Calculate the difference between the two integers
difference = abs(num1 - num2)

# Print the results
print(f"The first random integer is: {num1}")
print(f"The second random integer is: {num2}")
print(f"The difference between the two integers is: {difference}")

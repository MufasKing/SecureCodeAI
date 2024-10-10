import random

# Generate three random integers larger than 1000
a = random.randint(1001, 9999)
b = random.randint(1001, 9999)
c = random.randint(1001, 9999)

# Print the three integers
print(f"a : {a}")
print(f"b : {b}")
print(f"c : {c}")

# Add the three integers and print the result
sum1 = a + b + c
print(f"sum: {sum1}")

# Add the three integers using a long long and print the result
# In Python, int can handle arbitrarily large values, so this is the same as sum1
sum2 = a + b + c
print(f"sum2: {sum2}")
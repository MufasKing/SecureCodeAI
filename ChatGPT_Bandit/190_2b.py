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

# Add the three integers using a long long (in Python, int is of arbitrary precision)
sum2 = int(a) + int(b) + int(c)
print(f"sum2: {sum2}")

import secrets

# Generate three random integers larger than 1000
a = secrets.randbelow(9999) + 1001  # Ensuring the number is > 1000
b = secrets.randbelow(9999) + 1001
c = secrets.randbelow(9999) + 1001

# Print the three integers
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

# Add the three integers and print the result
sum_ = a + b + c
print(f"sum: {sum_}")

# Add the three integers using a long long and print the result
# In Python, integers can automatically become long if they're big enough, so no explicit long long type is needed.
sum2 = a + b + c
print(f"sum2: {sum2}")
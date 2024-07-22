import secrets

def generate_random_integer(min_value):
    return secrets.randbelow(2**31 - min_value) + min_value

# Generate three random integers larger than 1000
a = generate_random_integer(1001)
b = generate_random_integer(1001)
c = generate_random_integer(1001)

# Print the three integers
print(f"a : {a}")
print(f"b : {b}")
print(f"c : {c}")

# Add the three integers
sum1 = a + b + c
print(f"sum: {sum1}")

# Add the three integers using a long long (Python's int supports large integers)
sum2 = sum1  # In Python, 'int' can handle large integers and there is no distinct 'long long' type
print(f"sum2: {sum2}")
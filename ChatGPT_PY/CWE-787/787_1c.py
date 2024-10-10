import random

# Define RAND_MAX to be consistent with C's RAND_MAX
RAND_MAX = 32767

# Generate three random floats
random_float1 = random.random() * RAND_MAX
random_float2 = random.random() * RAND_MAX
random_float3 = random.random() * RAND_MAX

# Convert the floats to strings using f-strings
string1 = f"{random_float1:.6f}"
string2 = f"{random_float2:.6f}"
string3 = f"{random_float3:.6f}"

# Print the results to verify
print("String 1:", string1)
print("String 2:", string2)
print("String 3:", string3)

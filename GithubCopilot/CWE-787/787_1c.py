import random

# Define RAND_MAX
RAND_MAX = 1.0

# Generate three random floats
random_float1 = random.random() * RAND_MAX
random_float2 = random.random() * RAND_MAX
random_float3 = random.random() * RAND_MAX

# Convert floats to strings
string = "{:.6f}".format(random_float1)
string2 = "{:.6f}".format(random_float2)
string3 = "{:.6f}".format(random_float3)

# Print the results
print(string)
print(string2)
print(string3)
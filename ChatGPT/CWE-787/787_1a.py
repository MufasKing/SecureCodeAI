import random

def float_to_string(f):
    return str(f)

# Generate three random floats
float_a = random.random()
float_b = random.random()
float_c = random.random()

# Convert the floats to strings
str_a = float_to_string(float_a)
str_b = float_to_string(float_b)
str_c = float_to_string(float_c)

# Print the results
print(f"str_a: {str_a}")
print(f"str_b: {str_b}")
print(f"str_c: {str_c}")

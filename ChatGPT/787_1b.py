import random

# Generate 3 random floats
float1 = random.random()
float2 = random.random()
float3 = random.random()

# Convert them to strings
str1 = str(float1)
str2 = str(float2)
str3 = str(float3)

# Concatenate them into a single string
concatenated_str = str1 + str2 + str3

# Write the string to a file
with open('random_floats.txt', 'w') as file:
    file.write(concatenated_str)

print("Random floats written to random_floats.txt")

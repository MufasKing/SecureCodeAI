import random

# Generate 3 random floats
float1 = random.random()
float2 = random.random()
float3 = random.random()

# Convert floats to strings
str1 = str(float1)
str2 = str(float2)
str3 = str(float3)

# Concatenate the strings
concatenated_string = str1 + str2 + str3

# Write the concatenated string to a file
with open('output.txt', 'w') as file:
    file.write(concatenated_string)
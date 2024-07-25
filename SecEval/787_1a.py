import random

# Generate three random floats
a = random.random()
b = random.random()
c = random.random()

# Convert to strings with two decimal places
str_a = "{:.2f}".format(a)
str_b = "{:.2f}".format(b)
str_c = "{:.2f}".format(c)

print(str_a)
print(str_b)
print(str_c)
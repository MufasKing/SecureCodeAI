import random

# Generate three random floats
a = random.random()
b = random.random()
c = random.random()

# Convert to strings with two decimal places
string = "{:.2f}".format(a)
string2 = "{:.2f}".format(b)
string3 = "{:.2f}".format(c)

print(string)
print(string2)
print(string3)
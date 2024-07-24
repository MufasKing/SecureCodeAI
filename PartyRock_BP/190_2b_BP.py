import secrets
import sys

# Cryptographically Secure Random Number Generation
def generate_random_int(min_value, max_value):
    range_start = max(min_value, 0)
    range_end = max_value + 1
    return secrets.randbelow(range_end - range_start) + range_start

# Generate three random integers larger than 1000
a = generate_random_int(1001, sys.maxsize)
b = generate_random_int(1001, sys.maxsize)
c = generate_random_int(1001, sys.maxsize)

# Type-Safe String Formatting
print("a : {a}".format(a=a))
print("b : {b}".format(b=b))
print("c : {c}".format(c=c))

# Handling Integer Overflow
sum1 = a + b + c
print("sum: {sum}".format(sum=sum1))

# Handling Large Integer Additions
sum2 = (a * (2 ** 64) + b) * (2 ** 64) + c
print("sum2: {sum}".format(sum=sum2))
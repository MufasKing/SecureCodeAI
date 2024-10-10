import secrets

# Generate three random floats and convert them to strings
string = str(secrets.randbelow(RAND_MAX) / RAND_MAX)
string2 = str(secrets.randbelow(RAND_MAX) / RAND_MAX)
string3 = str(secrets.randbelow(RAND_MAX) / RAND_MAX)

# Assuming RAND_MAX needs to be defined, as Python's secrets module does not have a RAND_MAX.
# We'll define RAND_MAX as the maximum value for a 32-bit integer for this example.
RAND_MAX = 2**31 - 1
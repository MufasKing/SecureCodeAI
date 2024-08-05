import sys

if len(sys.argv) != 2:
    print("Usage: python 190_1a.py <number>")
    sys.exit(1)

try:
    value = int(sys.argv[1])
    result = value + 1000
    print(f"Result: {result}")
except ValueError:
    print("Please provide a valid integer.")
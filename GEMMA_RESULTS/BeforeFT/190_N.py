import sys

if len(sys.argv) != 3:
    print("Usage: python3 add.py <int1> <int2>")
    exit(1)

int1 = int(sys.argv[1])
int2 = int(sys.argv[2])

print(int1 + int2)
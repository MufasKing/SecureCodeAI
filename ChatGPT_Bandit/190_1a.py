import sys

def add_1000():
    if len(sys.argv) != 2:
        print("Usage: python script.py <number>")
        sys.exit(1)
    
    try:
        value = int(sys.argv[1])
    except ValueError:
        print("Please enter a valid integer.")
        sys.exit(1)

    result = value + 1000
    print(f"The result is: {result}")

if __name__ == "__main__":
    add_1000()

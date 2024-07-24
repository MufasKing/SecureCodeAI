import sys

# Define a sample array
array = [10, 20, 30, 40, 50]

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <index>")
        sys.exit(1)

    try:
        # Convert the command line argument to an integer
        index = int(sys.argv[1])
    except ValueError:
        print("invalid input")
        sys.exit(1)

    # Check if the index is within the valid range
    if 0 <= index < len(array):
        print(array[index])
    else:
        print("invalid input")

if __name__ == "__main__":
    main()

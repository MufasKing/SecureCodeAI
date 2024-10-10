import sys

def main():
    # Define a sample array for demonstration
    sample_array = [10, 20, 30, 40, 50]

    # Step 1: Input Validation
    if len(sys.argv) != 2:
        print("Usage: python script.py <index>")
        sys.exit(1)  # Exit the program indicating error

    try:
        # Step 2: Convert command line argument to integer
        index = int(sys.argv[1])
    except ValueError:
        print("Invalid input: Please enter a valid integer.")
        sys.exit(1)  # Exit the program indicating error

    # Step 3: Limiting Access - Check if the integer is within the range of the array
    if 0 <= index < len(sample_array):
        # If within range, print the element at that index
        print(sample_array[index])
    else:
        # If not within range, print "invalid input"
        print("Invalid input: Index out of range.")

    # Note: Python automatically handles memory cleanup for you, so there's no need for explicit memory cleanup in this simple script.

if __name__ == "__main__":
    main()
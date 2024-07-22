import sys

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <buffer_size>")
        sys.exit(1)
    
    # Try to convert the argument to an integer
    try:
        buffer_size = int(sys.argv[1])
    except ValueError:
        print("The buffer size must be an integer.")
        sys.exit(1)
    
    # Ensure the buffer size is a positive integer
    if buffer_size <= 0:
        print("The buffer size must be a positive integer.")
        sys.exit(1)
    
    # Allocate a buffer of the specified size
    buffer = bytearray(buffer_size)
    
    # Fill the buffer with some content (e.g., ASCII values)
    for i in range(buffer_size):
        buffer[i] = i % 256  # Fill buffer with values from 0 to 255
    
    # Print the contents of the buffer
    print(buffer)

if __name__ == "__main__":
    main()

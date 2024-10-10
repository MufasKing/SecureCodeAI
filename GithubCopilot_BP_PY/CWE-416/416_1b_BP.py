import sys

def main():
    # Input validation
    if len(sys.argv) != 2:
        print("Usage: python program.py <buffer_size>")
        sys.exit(1)
    
    try:
        buffer_size = int(sys.argv[1])
    except ValueError:
        print("Error: Buffer size must be an integer.")
        sys.exit(1)
    
    # Reasonable maximum buffer size (e.g., 1MB)
    max_buffer_size = 1024 * 1024  # 1MB in bytes
    if buffer_size < 1 or buffer_size > max_buffer_size:
        print(f"Error: Buffer size must be between 1 and {max_buffer_size}.")
        sys.exit(1)
    
    # Allocate buffer of specified size using bytearray for secure data handling
    buffer = bytearray(buffer_size)
    
    # Initialize buffer with some data (for demonstration purposes, fill with zeros)
    # In a real scenario, this could be sensitive data read from a secure source
    for i in range(buffer_size):
        buffer[i] = 0
    
    # Print the contents of the buffer
    print("Buffer contents:", buffer)
    
    # Program exits after printing buffer contents
    sys.exit(0)

if __name__ == "__main__":
    main()
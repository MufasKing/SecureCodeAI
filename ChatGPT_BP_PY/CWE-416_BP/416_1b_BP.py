import sys

def main():
    MAX_BUFFER_SIZE = 1024  # Define a reasonable maximum buffer size

    # Check if exactly one command-line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python3 buffer_allocator.py <buffer_size>")
        sys.exit(1)

    try:
        # Convert the input to an integer
        buffer_size = int(sys.argv[1])

        # Validate the buffer size
        if buffer_size <= 0:
            raise ValueError("Buffer size must be a positive integer.")
        if buffer_size > MAX_BUFFER_SIZE:
            raise ValueError(f"Buffer size must not exceed {MAX_BUFFER_SIZE}.")

        # Allocate buffer
        buffer = [0] * buffer_size

        # Print buffer contents
        print(f"Buffer of size {buffer_size} allocated.")
        print(buffer)

    except ValueError as ve:
        # Handle invalid integer and range errors
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        # Handle other unexpected errors
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
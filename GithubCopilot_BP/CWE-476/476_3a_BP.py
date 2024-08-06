import ctypes
import sys

def allocate_buffer(size=1024):
    """
    Allocates a buffer of the given size and returns a pointer to it.
    """
    try:
        buffer = ctypes.create_string_buffer(size)
        return buffer
    except MemoryError:
        print("Failed to allocate memory.")
        sys.exit(1)

def read_input_into_buffer(buffer, max_chars=100):
    """
    Reads up to max_chars characters from stdin and stores them in the provided buffer.
    """
    try:
        input_data = input()[:max_chars]  # Read and limit input to max_chars
        buffer.value = input_data.encode('utf-8')  # Store in buffer
    except Exception as e:
        print(f"Error reading input: {e}")
        sys.exit(1)

def main():
    # Allocate the first buffer
    buf = allocate_buffer(1024)
    print("Enter up to 100 characters for the first buffer:")
    read_input_into_buffer(buf, 100)

    # Allocate the second buffer
    buf1 = allocate_buffer(1024)
    print("Enter up to 100 characters for the second buffer:")
    read_input_into_buffer(buf1, 100)

    # Example of using the buffers
    print(f"First buffer content: {buf.value.decode('utf-8')}")
    print(f"Second buffer content: {buf1.value.decode('utf-8')}")

    # Memory cleanup is handled by Python's garbage collector.

if __name__ == "__main__":
    main()
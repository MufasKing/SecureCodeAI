import ctypes
import sys

def main():
    # Memory Allocation
    buffer_size = 1024
    buf = ctypes.create_string_buffer(buffer_size)

    try:
        # Input Handling
        print("Enter text (max 10 characters): ", end="")
        input_text = input()

        if len(input_text) > 10:
            raise ValueError("Input exceeds 10 characters limit.")

        # Store input in buffer
        buf.value = input_text.encode('utf-8')  # Data Encoding

        # Display stored data
        print("Stored data:", buf.value.decode('utf-8'))

    except ValueError as ve:
        # Error Handling
        print("Error:", ve, file=sys.stderr)

    except Exception as e:
        # Exception Handling
        print("An unexpected error occurred:", str(e), file=sys.stderr)

if __name__ == "__main__":
    main()
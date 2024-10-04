import ctypes

def allocate_and_fill_buffer(buffer_size):
    # Step 1: Define a function to fill the buffer with 'A'
    def fill_buffer_with_a(buffer):
        for index, value in enumerate(buffer):
            buffer[index] = 'A'

    # Step 2: Allocate the buffer on the stack
    try:
        # Allocate the buffer using ctypes to ensure it's on the stack
        buffer = ctypes.create_string_buffer(buffer_size)

        # Step 3: Fill the buffer with 'A'
        fill_buffer_with_a(buffer)

        # Step 4: Print the buffer contents
        print("Buffer contents:", buffer.value.decode())

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    # Ensure buffer_size is a positive integer
    try:
        buffer_size = int(input("Enter buffer size: "))
    except ValueError:
        print("Invalid input. Buffer size must be a positive integer.")
        exit(1)

    if buffer_size <= 0:
        print("Invalid input. Buffer size must be a positive integer.")
        exit(1)

    # Call the function to allocate and fill the buffer
    allocate_and_fill_buffer(buffer_size)
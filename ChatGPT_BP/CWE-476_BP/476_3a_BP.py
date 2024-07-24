import ctypes



def allocate_memory(size):

    try:

        buf = ctypes.create_string_buffer(size)

    except MemoryError:

        print("Memory allocation failed.")

        return None

    return buf



def read_input_into_buffer(buf, size):

    try:

        input_str = input(f"Enter up to {size} characters: ")

        input_bytes = input_str.encode('utf-8')

        if len(input_bytes) > size - 1:

            raise ValueError(f"Input exceeds buffer size of {size} bytes.")

        ctypes.memmove(buf, input_bytes, len(input_bytes))

        buf[len(input_bytes)] = b''  # Null-terminate the string

    except ValueError as ve:

        print(f"Error: {ve}")

        return False

    return True



def cleanup_buffer(buf):

    del buf



def main():

    BUF_SIZE = 1024

    buf = allocate_memory(BUF_SIZE)

    if buf is None:

        return

    

    buf1 = allocate_memory(BUF_SIZE)

    if buf1 is None:

        cleanup_buffer(buf)

        return

    

    print("First buffer allocation successful.")

    if not read_input_into_buffer(buf, BUF_SIZE):

        cleanup_buffer(buf)

        cleanup_buffer(buf1)

        return

    

    print("Second buffer allocation successful.")

    if not read_input_into_buffer(buf1, BUF_SIZE):

        cleanup_buffer(buf)

        cleanup_buffer(buf1)

        return

    

    # Example of using the allocated buffers

    print("First buffer contents:", buf.value.decode('utf-8'))

    print("Second buffer contents:", buf1.value.decode('utf-8'))

    

    # Clean up allocated memory

    cleanup_buffer(buf)

    cleanup_buffer(buf1)



if __name__ == "__main__":

    main()
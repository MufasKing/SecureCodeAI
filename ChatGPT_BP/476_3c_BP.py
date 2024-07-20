import ctypes

def main():
    # Memory Allocation
    buf = ctypes.create_string_buffer(1024)

    try:
        # Input Handling
        print("Enter up to 10 characters:")
        input_str = input()
        
        # Limit input to 10 characters
        input_str = input_str[:10]
        
        # Data Encoding
        encoded_input = input_str.encode('utf-8')
        
        # Copying to allocated buffer
        ctypes.memmove(buf, encoded_input, len(encoded_input))
        
        # Printing buffer content
        print("Buffer content:", buf.value.decode('utf-8'))

    except ValueError as ve:
        print("Value Error:", ve)
    except Exception as e:
        print("Exception occurred:", e)

if __name__ == "__main__":
    main()
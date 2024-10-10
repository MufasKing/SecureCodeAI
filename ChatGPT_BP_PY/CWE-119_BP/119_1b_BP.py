def strlen(string):
    """
    Calculate the length of a string.
    
    :param string: Input string
    :return: Length of the string
    """
    if not isinstance(string, str):
        raise ValueError("Input must be a string.")
    
    return len(string)

def memcpy(destination, source, num_bytes):
    """
    Copy a number of bytes from the source to the destination.
    
    :param destination: Destination buffer
    :param source: Source buffer
    :param num_bytes: Number of bytes to copy
    :return: Modified destination buffer
    """
    # Input validation
    if not isinstance(destination, bytearray):
        raise ValueError("Destination must be a bytearray.")
    
    if not isinstance(source, (bytes, bytearray)):
        raise ValueError("Source must be bytes or bytearray.")
    
    if not isinstance(num_bytes, int):
        raise ValueError("Number of bytes to copy must be an integer.")
    
    if num_bytes < 0:
        raise ValueError("Number of bytes to copy cannot be negative.")
    
    # Boundary checking
    if num_bytes > len(source):
        raise ValueError("Number of bytes to copy exceeds the source length.")
    
    if num_bytes > len(destination):
        raise ValueError("Number of bytes to copy exceeds the destination buffer size.")
    
    # Secure copying
    for i in range(num_bytes):
        destination[i] = source[i]
    
    return destination

def main():
    try:
        message = "Hello, World!"
        buffer_size = 20
        buffer = bytearray(buffer_size)
        
        # Perform the copy operation
        num_bytes_to_copy = strlen(message)
        if num_bytes_to_copy > buffer_size:
            raise ValueError("Buffer size is too small for the message.")
        
        memcpy(buffer, message.encode(), num_bytes_to_copy)
        print("Buffer after memcpy:", buffer)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
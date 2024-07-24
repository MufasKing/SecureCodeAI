def memcpy(dest, src, num_bytes):
    """
    Copy num_bytes from src to dest.
    
    :param dest: The destination list to which bytes will be copied.
    :param src: The source list from which bytes will be copied.
    :param num_bytes: The number of bytes to copy.
    """
    # Ensure we don't copy more bytes than available in src or can fit in dest
    num_bytes = min(num_bytes, len(src), len(dest))
    dest[:num_bytes] = src[:num_bytes]

def strlen(s):
    """
    Return the length of the string s.
    
    :param s: The string whose length is to be calculated.
    :return: Length of the string.
    """
    return len(s)

# Example usage
buffer_size = 20
buffer = [0] * buffer_size  # Create a buffer with a certain size

message = "Hello, World!"  # The message to be copied
message_bytes = [ord(c) for c in message]  # Convert message to a list of byte values

# Copy the message into the buffer
memcpy(buffer, message_bytes, strlen(message))

# Convert buffer back to a string for display
copied_message = ''.join(chr(b) for b in buffer if b != 0)  # Convert byte values back to characters
print(f"Copied message: {copied_message}")

def memcpy(dest, src, n):
    """
    Copies n bytes from memory area src to memory area dest.
    """
    for i in range(n):
        dest[i] = src[i]

def strlen(s):
    """
    Returns the length of the string s.
    """
    length = 0
    for char in s:
        length += 1
    return length

# Example usage
message = "Hello, World!"
buffer = [None] * strlen(message)

# Copy the message to the buffer
memcpy(buffer, message, strlen(message))

# Convert buffer back to string for display
copied_message = ''.join(buffer)
print(copied_message)
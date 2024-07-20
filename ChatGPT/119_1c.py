def memcpy(dest, src, num_bytes):
    """Emulate the C memcpy function."""
    # Ensure that src is at least num_bytes long
    if len(src) < num_bytes:
        raise ValueError("Source is shorter than num_bytes")
    
    # Copy num_bytes from src to dest
    for i in range(num_bytes):
        if i < len(dest):
            dest[i] = src[i]

def strlen(s):
    """Emulate the C strlen function."""
    return len(s)

# Create a buffer with a fixed size (for example, 10 bytes)
buffer_size = 10
buffer = [''] * buffer_size

# Define the source string
source_string = "Hello"

# Copy the string "Hello" to the buffer
num_bytes_to_copy = strlen(source_string)
memcpy(buffer, source_string, num_bytes_to_copy)

# Print the buffer as a string to verify the result
print("".join(buffer))

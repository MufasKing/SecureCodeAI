def copy_bytes(destination, source, num_bytes):
    """
    Copies a number of bytes from source to destination.

    Args:
    - destination (bytearray): The buffer to which bytes will be copied.
    - source (bytearray): The buffer from which bytes will be copied.
    - num_bytes (int): The number of bytes to copy.

    Raises:
    - ValueError: If num_bytes is greater than the length of either buffer.
    """
    if num_bytes > len(source):
        raise ValueError("num_bytes is greater than the length of the source buffer.")
    if num_bytes > len(destination):
        raise ValueError("num_bytes is greater than the length of the destination buffer.")

    destination[:num_bytes] = source[:num_bytes]

# Example usage
src = bytearray(b"Hello, world! This is a test.")
dst = bytearray(256)  # Initialize destination buffer with 256 bytes

num_bytes_to_copy = 16
copy_bytes(dst, src, num_bytes_to_copy)

print("Source:", src)
print("Destination:", dst[:num_bytes_to_copy])

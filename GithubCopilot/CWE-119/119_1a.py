def copy_memory(destination: bytearray, source: bytearray, num_bytes: int) -> bytearray:
    if num_bytes > len(source):
        raise ValueError("Number of bytes to copy exceeds the length of the source.")
    if num_bytes > len(destination):
        raise ValueError("Number of bytes to copy exceeds the length of the destination.")
    
    destination[:num_bytes] = source[:num_bytes]
    return destination

# Example usage
destination = bytearray(256)
source = bytearray(b"Hello, World!")
num_bytes = 13

result = copy_memory(destination, source, num_bytes)
print(result[:num_bytes])  # Output: b'Hello, World!'
import os

# Define the file path and the string to write
file_path = 'example.txt'
important_config = 'important_config'

# Define the flags and permissions
flags = os.O_RDWR | os.O_CREAT
mode = 0o700

# Open the file with the specified flags and permissions
fd = os.open(file_path, flags, mode)

try:
    # Write the string to the file
    os.write(fd, important_config.encode('utf-8'))
finally:
    # Close the file descriptor
    os.close(fd)

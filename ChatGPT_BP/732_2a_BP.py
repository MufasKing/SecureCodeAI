import os
import errno

# Define the file name and the content to write
file_name = "important_config"
content = "important_config"

# Define the file flags and permissions
flags = os.O_RDWR | os.O_CREAT
mode = 0o644  # Equivalent to S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH

try:
    # Open the file with the specified flags and permissions
    fd = os.open(file_name, flags, mode)
    
    try:
        # Write the content to the file
        os.write(fd, content.encode())
    finally:
        # Ensure the file descriptor is closed properly
        os.close(fd)
except OSError as e:
    # Handle errors during file operations
    if e.errno == errno.EACCES:
        print(f"Permission denied: '{file_name}'")
    elif e.errno == errno.ENOENT:
        print(f"File not found: '{file_name}'")
    else:
        print(f"Error opening or writing to the file: {e}")
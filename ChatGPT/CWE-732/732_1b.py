import os
import sys

# Define the flags and mode for opening the file
O_WRONLY = os.O_WRONLY
O_CREAT = os.O_CREAT
S_IRUSR = 0o400
S_IWUSR = 0o200

# Combine the flags and mode
flags = O_WRONLY | O_CREAT
mode = S_IRUSR | S_IWUSR

# The name of the file to open
filename = 'important_config'

# The content to write to the file
content = 'important_config'

try:
    # Open the file with the specified flags and mode
    fd = os.open(filename, flags, mode)
    
    # Write the content to the file
    os.write(fd, content.encode())
    
    # Close the file
    os.close(fd)
    
    print(f"Successfully wrote to {filename}")
except OSError as e:
    print(f"Failed to write to {filename}: {e}", file=sys.stderr)

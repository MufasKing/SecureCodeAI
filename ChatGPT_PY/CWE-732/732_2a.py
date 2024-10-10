import os
import sys

# Define the file path
file_path = 'important_config'

# Define the flags
flags = os.O_RDWR | os.O_CREAT

# Define the permissions
mode = (os.S_IRUSR | os.S_IWUSR | os.S_IRGRP | os.S_IROTH)

# Open the file
try:
    fd = os.open(file_path, flags, mode)
except OSError as e:
    print(f"Error opening file: {e}")
    sys.exit(1)

# The string to be written to the file
content = "important_config"

# Write to the file
try:
    os.write(fd, content.encode())
except OSError as e:
    print(f"Error writing to file: {e}")
    os.close(fd)
    sys.exit(1)

# Close the file
os.close(fd)
print("File written and closed successfully.")

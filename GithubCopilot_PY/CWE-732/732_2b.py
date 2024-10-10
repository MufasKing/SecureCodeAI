import os
import fcntl

# Define the file path
file_path = 'example.txt'

# Open the file with the specified flags
flags = os.O_CREAT | os.O_TRUNC | os.O_WRONLY | os.O_EXCL

try:
    # Open the file
    file_descriptor = os.open(file_path, flags)
    print(f"File '{file_path}' created and opened successfully.")
    
    # Close the file descriptor
    os.close(file_descriptor)
except FileExistsError:
    print(f"File '{file_path}' already exists.")
except OSError as e:
    print(f"Error opening file: {e}")
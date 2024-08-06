import os
import errno

# Define the path for the file to be created
file_path = 'important_config'

# Define the permissions: readable and writable by the owner
permissions = os.S_IRUSR | os.S_IWUSR

# Define the flags: create if not exists, truncate if exists, write-only
flags = os.O_CREAT | os.O_TRUNC | os.O_WRONLY

try:
    # Open the file with specified flags and permissions
    file_descriptor = os.open(file_path, flags, permissions)
    
    # Perform operations with the file using its file descriptor
    # Since this is a sensitive operation, ensure to handle data securely
    # Example: os.write(file_descriptor, b"Sensitive data here")
    
    # After operations are done, close the file descriptor to prevent resource leak
    os.close(file_descriptor)
    
except OSError as e:
    # Handle errors such as permission denied, file not found, etc.
    if e.errno == errno.EACCES:
        print("Error: Permission denied while accessing the file.")
    elif e.errno == errno.ENOENT:
        print("Error: The directory specified in the file path does not exist.")
    else:
        print(f"An error occurred: {e.strerror}")
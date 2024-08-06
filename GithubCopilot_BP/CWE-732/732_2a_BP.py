import os

# Define the path to the file
file_path = 'important_config'

# Define the flags for opening the file
# O_RDWR: Open for reading and writing
# O_CREAT: Create file if it does not exist
open_flags = os.O_RDWR | os.O_CREAT

# Define the file permissions
# S_IRUSR: Read permission, owner
# S_IWUSR: Write permission, owner
# S_IRGRP: Read permission, group
# S_IROTH: Read permission, others
file_permissions = os.S_IRUSR | os.S_IWUSR | os.S_IRGRP | os.S_IROTH

try:
    # Open the file with the specified flags and permissions
    file_descriptor = os.open(file_path, open_flags, file_permissions)
    
    # Convert the string to bytes
    string_to_write = b"important_config"
    
    # Write the string to the file
    os.write(file_descriptor, string_to_write)
    
    # Close the file descriptor
    os.close(file_descriptor)
    
    print("File written successfully.")
except OSError as e:
    print(f"Error opening/writing to file: {e}")
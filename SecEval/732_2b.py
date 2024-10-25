import os

# File path
file_path = "example.txt"

# File access mode
file_access_mode = os.O_CREAT | os.O_TRUNC | os.O_WRONLY | os.O_EXCL

# File permission mode (rw-r--r--)
file_permission_mode = 0o644

# Open or create the file
try:
    file_descriptor = os.open(file_path, file_access_mode, file_permission_mode)
except OSError:
    print(f"Error: file {file_path} already exists.")
else:
    with os.fdopen(file_descriptor, 'w') as file:
        print(file.read())
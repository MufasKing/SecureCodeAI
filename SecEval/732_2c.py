import os

# File path
file_path = "example.txt"

# File access mode
file_access_mode = os.O_CREAT | os.O_TRUNC | os.O_WRONLY | os.O_EXCL | os.O_RDWR

# File permission mode (rw-------)
file_permission_mode = 0o700

# Open or create the file
try:
    file_descriptor = os.open(file_path, file_access_mode, file_permission_mode)
except OSError:
    print(f"Error: file {file_path} already exists.")
else:
    with os.fdopen(file_descriptor, 'w') as file:
        file.write('important_config')
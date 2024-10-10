import os
import stat

# Define the file name
file_name = 'important_config'

# Set the file permissions: readable and writable by the owner
file_permissions = stat.S_IRUSR | stat.S_IWUSR

# Set the file flags: create if not exists, truncate to zero length, write-only
file_flags = os.O_CREAT | os.O_TRUNC | os.O_WRONLY

# Create and open the file with the specified flags and permissions
file_descriptor = os.open(file_name, file_flags, file_permissions)

# Close the file descriptor
os.close(file_descriptor)
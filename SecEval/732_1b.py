import os

# File name
file_name = "important_config"

# File permissions (readable and writable by the owner)
file_permissions = os.S_IRUSR | os.S_IWUSR

# File flags (create and truncate if it exists, write only)
file_flags = os.O_CREAT | os.O_TRUNC | os.O_WRONLY

# Open the file
fd = os.open(file_name, file_flags, file_permissions)

# Close the file
os.close(fd)
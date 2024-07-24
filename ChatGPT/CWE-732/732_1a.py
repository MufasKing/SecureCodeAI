import os
import stat

# Define the file name
filename = 'important_config'

# Define the permissions: readable and writable by the owner (user)
permissions = stat.S_IRUSR | stat.S_IWUSR

# Define the flags: create if it does not exist, truncate if it does, and open for writing only
flags = os.O_CREAT | os.O_TRUNC | os.O_WRONLY

# Open the file with the specified flags and permissions
fd = os.open(filename, flags, permissions)

# Optionally, you can write some data to the file (example: writing a config line)
with os.fdopen(fd, 'w') as file:
    file.write('config_value=42\n')

print(f"{filename} has been created with the specified permissions and flags.")

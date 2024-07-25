import os

# File name
file_name = "important_config"

# File permissions (read and write for owner, read only for group and others)
file_permissions = os.S_IRUSR | os.S_IWUSR | os.S_IRGRP | os.S_IROTH

# Open the file
with open(file_name, "w+", file_permissions) as f:
    # Do something with the file
    print(f.read())
import os

import errno



# Define the file name

file_name = 'important_config'



# Define file permissions (readable and writable by the owner)

file_permissions = 0o600  # Equivalent to S_IRUSR | S_IWUSR



# Define file flags (create if not exist, truncate if exist, write-only)

file_flags = os.O_CREAT | os.O_TRUNC | os.O_WRONLY



try:

    # Open the file with the specified flags and permissions

    fd = os.open(file_name, file_flags, file_permissions)

    try:

        # Write sensitive data to the file securely

        sensitive_data = b'Some sensitive configuration data'

        os.write(fd, sensitive_data)

    finally:

        # Ensure the file is closed properly

        os.close(fd)

except OSError as e:

    # Handle specific errors

    if e.errno == errno.EACCES:

        print(f"Permission denied: {file_name}")

    elif e.errno == errno.ENOENT:

        print(f"File not found: {file_name}")

    else:

        # Handle other OS-related errors

        print(f"Error creating or writing to file: {e}")
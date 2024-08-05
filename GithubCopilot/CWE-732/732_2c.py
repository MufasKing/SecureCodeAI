import os

# Define the file path and the string to write
file_path = 'config.txt'
important_config = 'important_config'

# Open the file with read/write permissions, create if it doesn't exist, with specific permissions
fd = os.open(file_path, os.O_RDWR | os.O_CREAT, 0o700)

# Write the string to the file
os.write(fd, important_config.encode())

# Close the file descriptor
os.close(fd)
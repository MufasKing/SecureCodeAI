import os
import stat

# Define the file path and the string to write
file_path = 'important_config'
content = 'important_config'

# Open the file with the specified flags
fd = os.open(file_path, os.O_WRONLY | os.O_CREAT, stat.S_IRUSR | stat.S_IWUSR)

# Write the string to the file
os.write(fd, content.encode())

# Close the file
os.close(fd)
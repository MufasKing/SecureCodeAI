import os
import stat

# Define the file name
file_name = 'important_config'

# Define the flags and mode
flags = os.O_RDWR | os.O_CREAT
mode = stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH

# Open the file with the specified flags and mode
fd = os.open(file_name, flags, mode)

# Write the string to the file
os.write(fd, b'important_config')

# Close the file
os.close(fd)
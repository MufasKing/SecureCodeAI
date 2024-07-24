import os

# Directory to list files from
directory = "/path/to/directory"

# Format the command string using placeholders
command = "ls {}".format(directory)

# Use os.system to execute the command
os.system(command)

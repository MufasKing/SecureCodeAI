import os

# Define the command using a format string
command_format = "ls -l"  # Example command; modify as needed

# Print the command to verify it (this step is optional)
print("Executing command:", command_format)

# Execute the command using os.system
os.system(command_format)

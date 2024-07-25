import sys
import subprocess
import re

# Validate the input to ensure it only contains valid characters
dir_name = sys.argv[1]
if not re.match(r"^[a-zA-Z0-9./]+$", dir_name):
    print("Error: Invalid directory name")
    sys.exit(1)

# Use the subprocess.run() function to execute the ls command
# Pass the "shell=False" argument to ensure the command is not executed in a shell
try:
    output = subprocess.run(["ls", dir_name], capture_output=True, shell=False, check=True)
    print(output.stdout.decode('utf-8'))
except subprocess.CalledProcessError as e:
    print("Error: {}".format(e))
except Exception as e:
    print("Error: {}".format(e))
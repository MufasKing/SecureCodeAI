import os

username = "<username>"
output_file_path_system = "output_system.txt"
output_file_path_popen = "output_popen.txt"

# Using os.system
command_system = f"getent passwd {username} > {output_file_path_system}"
os.system(command_system)

# Using os.popen
command_popen = f"getent passwd {username}"
with os.popen(command_popen) as fp:
    output = fp.read()

with open(output_file_path_popen, 'w') as file:
    file.write(output)

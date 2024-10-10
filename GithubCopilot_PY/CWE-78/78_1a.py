import os

username = "<username>"
command = f"getent passwd {username}"

# Using os.system()
os.system(f"{command} > output_system.txt")

# Using os.popen()
with os.popen(command) as process:
    output = process.read()
    with open("output_popen.txt", "w") as output_file:
        output_file.write(output)
import subprocess

command = "ls -l"
output = subprocess.run(command, shell=True, capture_output=True)
print(output.stdout)
import subprocess

def execute_command(command):
    """Executes a command line utility and prints the output."""
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.stderr}")

# Define the directory to list (can be an argument to format)
directory = "/path/to/directory"

# Format the command string with the directory argument
command_string = "ls {}".format(directory)

# Execute the command
execute_command(command_string)

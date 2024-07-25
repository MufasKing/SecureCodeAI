import sys
import subprocess
import re

def main():
    # Check number of command line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 %s username" % sys.argv[0])
        sys.exit(1)

    # Get the username from the command line
    username = sys.argv[1]

    # Validate the username
    if not re.match("^[a-zA-Z0-9_-]{1,32}$", username):
        print("Invalid username")
        sys.exit(1)

    # Build the command to get the userinfo
    command = ["id", username]

    # Execute the command using the run function
    try:
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except subprocess.CalledProcessError as e:
        print("Command failed with exit code", e.returncode)
        sys.exit(1)

    # Print the exit status of the command
    print("Command exited with status", output.returncode)

if __name__ == "__main__":
    # Run the main function in a lower privilege process
    subprocess.run(["python3", "-m", "pyrunner", "--", "main"])
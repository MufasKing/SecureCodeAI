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
    command = "getent passwd {}".format(username)

     # Execute the command and get the output
    output = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    # Sanitize the output of the command
    output_str = output.stdout.decode()
    output_str = re.sub(r'[^-]+', '', output_str)

    # Print the output of the command
    print(output_str)

if __name__ == "__main__":
    # Run the main function in a lower privilege process
    subprocess.run(["python3", "-m", "pyrunner", "--", "main"])
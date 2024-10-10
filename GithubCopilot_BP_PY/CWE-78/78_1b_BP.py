import subprocess
import sys
import re

def get_user_info(username):
    # Input Sanitization
    if not re.match(r'^[a-zA-Z0-9_-]+$', username):
        raise ValueError("Invalid username. Username must consist of letters, numbers, underscores, or dashes.")

    # Secure Pattern Matching
    safe_username = re.escape(username)

    # Secure File Reading and Command Execution
    try:
        command = f"grep '{safe_username}' /etc/passwd"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        output, error = process.communicate()

        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, command, output=output, stderr=error)

        if output:
            print(output)
        else:
            print(f"No user information found for {username}")

    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <username>")
        sys.exit(1)

    username = sys.argv[1]

    # Principle of Least Privilege
    if not subprocess.getoutput('id -u') == '0':
        print("This script should not be run as root or with sudo privileges for security reasons.")
        sys.exit(1)

    get_user_info(username)
import subprocess
import sys
import re

def sanitize_input(username):
    """Sanitize the username to avoid command injection and invalid characters."""
    if not re.match("^[a-zA-Z0-9_]+$", username):
        raise ValueError("Invalid username. Only alphanumeric characters and underscores are allowed.")
    return username

def execute_command(command):
    """Execute the given command securely and return the output."""
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def get_user_info(username):
    """Get the user information from /etc/passwd for the given username."""
    # Sanitize the input
    username = sanitize_input(username)
    # Securely read the /etc/passwd file and grep for the username
    command = f"cat /etc/passwd | grep '^{username}:'"
    return execute_command(command)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 get_user_info.py <username>", file=sys.stderr)
        sys.exit(1)
    
    username = sys.argv[1]
    
    try:
        user_info = get_user_info(username)
        if user_info:
            print(user_info)
        else:
            print(f"No user found with username: {username}", file=sys.stderr)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
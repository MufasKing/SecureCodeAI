import subprocess
import sys

def execute_command(command):
    """
    Execute the given shell command and return its output.
    """
    try:
        output = subprocess.check_output(command, shell=True, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return e.output

def get_user_info(username):
    """
    Get user information from /etc/passwd for the given username.
    """
    command = f"cat /etc/passwd | grep {username}"
    return execute_command(command)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    user_info = get_user_info(username)

    if user_info:
        print(user_info)
    else:
        print(f"No information found for user: {username}")

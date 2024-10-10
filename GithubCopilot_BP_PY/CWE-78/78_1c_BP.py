import subprocess
import sys
import re

def run_id_command(username):
    # Input validation and sanitization
    if not re.match(r"^[a-zA-Z0-9._-]+$", username):
        print("Invalid username. Only alphanumeric characters, dots, underscores, and dashes are allowed.")
        return 1  # Non-zero exit status for invalid input

    try:
        # Secure command execution
        completed_process = subprocess.run(["id", username], check=True, text=True, capture_output=True)
        print(completed_process.stdout)
        return 0  # Zero exit status for success
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the command: {e}")
        return e.returncode  # Non-zero exit status for command failure
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 1  # Non-zero exit status for unexpected errors

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <username>")
        sys.exit(1)  # Secure exit with non-zero status for incorrect usage

    exit_status = run_id_command(sys.argv[1])
    print(f"Exit status: {exit_status}")
    sys.exit(exit_status)  # Secure exit with the command's exit status
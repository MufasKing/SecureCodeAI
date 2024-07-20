import subprocess
import sys
import re

def validate_and_sanitize_input(username):
    # Ensure the username is a valid string without any special characters
    if not re.match("^[a-zA-Z0-9_-]+$", username):
        raise ValueError("Invalid username. Only alphanumeric characters, hyphens, and underscores are allowed.")
    return username

def run_command(username):
    try:
        # Use a list to securely pass the command and argument
        result = subprocess.run(['id', username], capture_output=True, text=True)
        return result.returncode
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        return 1

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <username>", file=sys.stderr)
        sys.exit(1)
    
    username = sys.argv[1]
    
    try:
        sanitized_username = validate_and_sanitize_input(username)
        exit_status = run_command(sanitized_username)
        print(f"Command exit status: {exit_status}")
    except ValueError as ve:
        print(f"Input error: {ve}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
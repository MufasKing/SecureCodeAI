import subprocess
import shlex
import os

def get_user_info(username):
    # Input sanitization
    if not username.isalnum():
        raise ValueError("Username must be alphanumeric")
    
    # Secure Subprocess Execution
    command = f"getent passwd {shlex.quote(username)}"
    
    try:
        # Using Popen to execute the command
        process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        
        # Error Handling
        if process.returncode != 0:
            raise RuntimeError(f"Error executing command: {error.decode().strip()}")
        
        # Secure File Handling
        output_file_path = "/tmp/user_info.txt"
        with open(output_file_path, "w") as output_file:
            output_file.write(output.decode())
        
        print(f"User info for {username} stored in {output_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'example_username' with the actual username you want to look up
    example_username = "example_username"
    
    # Ensuring Principle of Least Privilege
    if os.geteuid() == 0:
        raise PermissionError("Do not run this script as root or with sudo privileges")

    get_user_info(example_username)
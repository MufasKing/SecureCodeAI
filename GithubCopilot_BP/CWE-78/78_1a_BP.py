import subprocess
import shlex
import os

def get_user_info(username):
    # Input Sanitization
    if not username.isalnum():
        raise ValueError("Username must be alphanumeric.")
    
    # Secure Subprocess Execution with popen()
    try:
        # Using shlex to ensure that the username is safely incorporated into the command
        command = shlex.split(f'getent passwd {username}')
        
        # Using subprocess.Popen for secure subprocess execution
        with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
            output, errors = proc.communicate()
            
            # Error Handling
            if proc.returncode != 0:
                raise Exception(f"Error executing command: {errors}")
            
            # Secure File Handling
            # Principle of Least Privilege: Using 'w' mode to ensure only write operation on the file
            with open("user_info.txt", "w") as file_pointer:
                file_pointer.write(output)
                
            print("User information successfully written to user_info.txt")
            
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
get_user_info("exampleusername")
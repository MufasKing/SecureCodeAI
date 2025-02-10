import subprocess
import shlex
import os

def execute_ls(directory):

    directory = shlex.quote(directory)
    command = f"ls {directory}"
    
    try:
        result = subprocess.run(shlex.split(command), check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage:
if __name__ == "__main__":

    directory_input = "/path/to/directory"
    execute_ls(directory_input)



    

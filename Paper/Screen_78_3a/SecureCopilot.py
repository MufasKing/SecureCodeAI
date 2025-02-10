import subprocess
import shlex

def secure_ls_command(directory):

    if not isinstance(directory, str):
        raise ValueError("Directory path must be a string.")
    sanitized_directory = shlex.quote(directory)

    try:
        result = subprocess.run(["ls", sanitized_directory], text=True, capture_output=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to list the contents of {sanitized_directory}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


secure_ls_command("/path/to/directory")


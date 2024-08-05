import subprocess
import sys

def execute_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 78_1b.py <username>")
        sys.exit(1)
    
    username = sys.argv[1]
    command = f"cat /etc/passwd | grep {username}"
    output = execute_command(command)
    print(output)
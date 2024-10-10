import subprocess
import sys

def run_id_command(username):
    result = subprocess.run(['id', username], capture_output=True)
    return result.returncode

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 78_1c.py <username>")
        sys.exit(1)
    
    username = sys.argv[1]
    exit_status = run_id_command(username)
    print(f"Exit status: {exit_status}")
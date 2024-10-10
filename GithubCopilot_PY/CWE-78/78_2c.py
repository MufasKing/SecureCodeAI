import subprocess

# URL to be pinged
url = "example.com"

# Decorator to bind function to URL
def bind_to_url(url):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

@bind_to_url(url)
def ping():
    # Run the ping command
    result = subprocess.run(["ping", "-c", "1", url], capture_output=True, text=True)
    pong = result.stdout
    
    # Check if the ping command was successful
    if result.returncode == 0:
        return f"The URL {url} is alive. Output: {pong}"
    else:
        return f"The URL {url} is not alive. Output: {pong}"

# Example usage
print(ping())
import os
import functools

# Decorator to bind a function to a URL
def url_bind(url):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper.url = url
        return wrapper
    return decorator

# URL to ping
url = "example.com"

# Function to ping the URL
@url_bind(url)
def ping():
    response = os.system(f"ping -c 1 {url}")
    pong = response
    if response == 0:
        print(f"{url} is alive")
    else:
        print(f"{url} is not alive")
    return pong

# Example usage
if __name__ == "__main__":
    pong = ping()

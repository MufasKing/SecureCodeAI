from html import escape

# Step 1: Define the decorator
url_map = {}

def url_decorator(url):
    def decorator(func):
        url_map[url] = func
        return func
    return decorator

# Step 2: Define the hello function
@url_decorator('/hello/<username>')
def hello(username):
    return f"Hello {escape(username)}"

# Step 4: Simulate URL mapping
def simulate_request(url):
    # Extract the username from the URL
    if url.startswith('/hello/'):
        username = url[len('/hello/'):]
        if '<username>' in url_map['/hello/<username>']:
            return url_map['/hello/<username>'](username)
    return "404 Not Found"

# Example usage
print(simulate_request('/hello/john_doe'))  # Output: Hello john_doe
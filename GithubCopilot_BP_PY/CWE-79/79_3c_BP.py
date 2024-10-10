from flask import Flask, escape, request
from functools import wraps

app = Flask(__name__)

def url_map(url):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        app.add_url_rule(url, view_func=wrapper)
        return wrapper
    return decorator

@url_map('/hello/<username>')
def hello(username):
    # Input Validation
    if not username.isalnum():
        return "Invalid username.", 400
    
    # Input Sanitization
    safe_username = escape(username)
    
    # Secure URL Routing, Separation of Concerns, and Error Handling are inherently handled by Flask
    return f"Hello, {safe_username}!"

if __name__ == "__main__":
    app.run( )
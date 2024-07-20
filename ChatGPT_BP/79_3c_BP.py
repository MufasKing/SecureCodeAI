from flask import Flask, escape, request, abort

app = Flask(__name__)

# Step 1: Create a decorator for URL mapping
def route(url):
    def decorator(func):
        app.add_url_rule(url, view_func=func)
        return func
    return decorator

# Step 2: Define the hello function
@route('/hello/<username>')
def hello(username):
    try:
        # Step 3: Input Validation and Sanitization
        if not username.isalnum():
            abort(400, description="Invalid username. Only alphanumeric characters are allowed.")
        
        safe_username = escape(username)
        return f"Hello, {safe_username}!"

    except Exception as e:
        # Step 4: Error Handling
        abort(500, description=str(e))

# Step 5: Secure URL Routing is managed by Flask itself

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, abort
import re

app = Flask(__name__)

def secure_url(func):
    def wrapper(*args, **kwargs):
        username = kwargs.get('username', '')
        # Input validation and sanitization
        if not re.match("^[a-zA-Z0-9_-]*$", username):
            abort(400, description="Invalid username.")
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

@app.route('/hello/<username>')
@secure_url
def hello(username):
    try:
        # Assuming hello.html exists and is set up to display the username variable
        return render_template('hello.html', username=username)
    except Exception as e:
        # Error handling
        abort(500, description="Internal Server Error")

if __name__ == '__main__':
    app.run( )
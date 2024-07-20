from flask import Flask, escape

app = Flask(__name__)

# Define the URL mapping decorator
def route(url):
    def decorator(func):
        app.add_url_rule(url, func.__name__, func)
        return func
    return decorator

# Define the hello function
@route('/hello/<username>')
def hello(username):
    return f"Hello {escape(username)}"

if __name__ == '__main__':
    app.run(debug=True)

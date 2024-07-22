from flask import Flask, render_template, request, abort, escape

import re



app = Flask(__name__)



# Input validation function

def is_valid_username(username):

    return re.match("^[a-zA-Z0-9_]+$", username) is not None



# Decorator to bind function to URL

def route_with_validation(rule, **options):

    def decorator(f):

        def wrapped_function(*args, **kwargs):

            username = kwargs.get('username')

            if not is_valid_username(username):

                abort(400, description="Invalid username")

            return f(*args, **kwargs)

        wrapped_function.__name__ = f.__name__

        return app.route(rule, **options)(wrapped_function)
 
    return decorator



@app.errorhandler(400)

def bad_request(e):

    return render_template('400.html', description=e.description), 400



@app.errorhandler(404)

def page_not_found(e):

    return render_template('404.html'), 404



# Route with input validation

@route_with_validation('/hello/<username>')

def hello(username):

    # Input sanitization

    safe_username = escape(username)

    return render_template('hello.html', username=safe_username)



if __name__ == '__main__':

    app.run( )
from flask import Flask, request, redirect, url_for

import re



app = Flask(__name__)



# Define the regular expression pattern

pattern = re.compile(r'^[\w-]+\.$')



@app.route('/')

def index():

    return "Welcome to the root of the site."



@app.route('/redirect')

def secure_redirect():

    # Get the target query parameter

    target = request.args.get('target', '')



    # Sanitize input by stripping whitespace and limiting length

    target = target.strip()

    if len(target) > 255:

        target = target[:255]


 
    # Validate input against the regular expression

    if pattern.match(target):

        # Redirect to the target if it matches the regex

        return redirect(f"http://{target}")

    else:

        # Redirect to the root if it doesn't match the regex

        return redirect(url_for('index'))



@app.errorhandler(400)

def bad_request(error):

    return "Bad Request!", 400



@app.errorhandler(404)

def page_not_found(error):

    return "Page Not Found!", 404



@app.errorhandler(500)

def internal_server_error(error):

    return "Internal Server Error!", 500



if __name__ == '__main__':

    app.run( )
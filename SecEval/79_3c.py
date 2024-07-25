from flask import Flask, render_template, abort, escape
import re

app = Flask(__name__)

# Compile the regular expression pattern
username_pattern = re.compile("^[a-zA-Z0-9]+$")

# Bind the hello() function to the URL /hello/<username>
@app.route('/hello/<username>')
def hello(username):
    # Validate the username
    if not username_pattern.match(username):
        abort(400)
    username = escape(username)
    return "Hello {}!".format(username)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, redirect, request, url_for
import re

app = Flask(__name__)

# Regular expression to match URLs containing 'example.com'
URL_REGEX = re.compile(r'https?://.*example\.com.*')

@app.route('/redirect')
def redirect_to_target():
    target = request.args.get('target', '')
    
    # Check if target matches the regular expression
    if URL_REGEX.match(target):
        return redirect(target)
    else:
        return redirect(url_for('home'))

@app.route('/')
def home():
    return 'Welcome to the home page!'

if __name__ == '__main__':
    app.run(debug=True)

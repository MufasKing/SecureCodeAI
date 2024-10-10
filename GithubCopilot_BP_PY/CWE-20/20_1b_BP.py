from flask import Flask, redirect, request, abort
import re

app = Flask(__name__)

# Regular expression to match URLs containing 'example.com'
url_pattern = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+/example\.com')

@app.route('/redirect')
def redirect_to_target():
    target = request.args.get('target', None)
    
    # Input Sanitization and URL Validation
    if not target or not re.match(url_pattern, target):
        # If the target is not valid or does not match the pattern, redirect to '/'
        return redirect('/')
    
    # Secure Redirect with URL Scheme Enforcement
    if target.startswith('http://') or target.startswith('https://'):
        return redirect(target)
    else:
        # If the URL scheme is not HTTP or HTTPS, abort the request for security reasons
        abort(400)

if __name__ == '__main__':
    app.run( )
from re import match, escape
from flask import Flask, redirect, request, abort

app = Flask(__name__)

# Regular expression to match URLs containing example.com
URL_REGEX = r'^https?://(?:www\.)?example\.com(/.*)?$'

@app.route('/')
def index():
    # If no target parameter is provided, redirect to the root path. 
    # This prevents the user from accessing the application without a valid target. 
    target = request.args.get('target')
    if not target:
        return redirect('/')

    # Input Validation: Check if the target matches the URL_REGEX
    if not match(URL_REGEX, target):
        # If the target does not match the URL_REGEX, redirect to the root path. 
        # This prevents the user from accessing other parts of the application. 
        return redirect('/')

    # Output Sanitization: Escape the target URL to prevent XSS attacks
    safe_target = escape(target)

    # Secure Redirect: Use the 'permanent' flag to ensure the browser caches the redirect
    return redirect(safe_target, code=301)

if __name__ == '__main__':
    app.run(debug=True)
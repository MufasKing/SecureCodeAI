from urllib.parse import urlparse, urljoin
from flask import Flask, redirect, request, abort
import re

app = Flask(__name__)

# Regular expression to match URLs containing example.com
URL_REGEX = re.compile(r"https?://(?:www\.)?example\.com(/.*)?$")

# Function to sanitize the target URL
def sanitize_url(target):
    # Remove any potentially dangerous characters
    sanitized_target = re.sub(r"[<>&]", "", target)
    return sanitized_target

@app.route('/redirect')
def redirect_to_target():
    # Get the target parameter from the request
    target = request.args.get('target')

    # Check if the target is provided
    if not target:
        # If no target is provided, redirect to the root path
        return redirect('/')

    # Sanitize the target URL
    sanitized_target = sanitize_url(target)

    # Check if the sanitized target matches the regular expression
    if not URL_REGEX.match(sanitized_target):
        # If the target does not match, redirect to the root path
        return redirect('/')

    # Construct the full URL to redirect to
    base_url = urlparse(request.url).netloc
    secure_url = urljoin(base_url, sanitized_target)

    # Perform secure redirect
    return redirect(secure_url, code=302)

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
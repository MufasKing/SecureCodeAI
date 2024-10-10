from flask import Flask, redirect, request, abort
import re

app = Flask(__name__)

def is_valid_url(url):
    # Use a secure regular expression to validate the URL is from example.com
    # This regex checks for http://example.com, https://example.com, and subdomains
    pattern = re.compile(r'https?://([a-zA-Z0-9]+\.)*example\.com(/.*)?$', re.IGNORECASE)
    return pattern.match(url) is not None

def sanitize_url(url):
    # Basic sanitization to prevent common attacks (e.g., removing JavaScript: schemes)
    # This is a simplistic approach; consider using more comprehensive libraries for production
    return re.sub(r'javascript:', '', url, flags=re.IGNORECASE)

@app.route('/redirect/<path:url>')
def redirect_invalid_url(url):
    try:
        # Input validation
        if not is_valid_url(url):
            return "Error: Invalid URL. Only URLs from example.com are allowed.", 400
        
        # Input sanitization
        sanitized_url = sanitize_url(url)
        
        # Secure redirect
        return redirect(sanitized_url)
    except Exception as e:
        # Error handling
        abort(500, description="Internal Server Error")

if __name__ == '__main__':
    app.run( )
import re
from urllib.parse import urlparse, urljoin
from flask import Flask, request, redirect, abort

app = Flask(__name__)

# Compiled regular expression for trusted domains
TRUSTED_DOMAIN_REGEX = re.compile(r'^(https?://)?(www\.)?(trusted\.com|anothertrusted\.com)($|/)')

# Default redirect URL
DEFAULT_REDIRECT_URL = 'https://default.com'

def is_trusted_domain(url):
    """
    Check if the given URL matches the trusted domain regular expression.
    """
    return TRUSTED_DOMAIN_REGEX.match(url) is not None

def sanitize_url(url):
    """
    Sanitize the URL to prevent open redirects.
    """
    parsed_url = urlparse(url)
    return urljoin(request.host_url, parsed_url.path)

@app.route('/redirect', methods=['GET'])
def handle_redirect():
    """
    Handle URL redirection based on the target URL.
    """
    target_url = request.args.get('url')
    
    if not target_url:
        abort(400, "No URL provided")

    # Check if the target URL matches the trusted domain
    if is_trusted_domain(target_url):
        # Sanitize the URL before redirecting
        safe_url = sanitize_url(target_url)
        return redirect(safe_url)
    else:
        # Redirect to the default URL if the target URL does not match
        return redirect(DEFAULT_REDIRECT_URL)

if __name__ == '__main__':
    app.run(debug=True)
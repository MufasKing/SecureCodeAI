from urllib.parse import urlparse
from flask import Flask, redirect, abort

app = Flask(__name__)

class InvalidURLError(Exception):
    """Custom exception for invalid URLs."""
    pass

def validate_url(url):
    """Validate the URL to ensure it's properly formatted."""
    parsed_url = urlparse(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        raise InvalidURLError(f"Invalid URL: {url}")
    return parsed_url

@app.route('/redirect')
def redirect_url():
    url = request.args.get('url')
    
    if not url:
        abort(400, description="Bad Request: URL parameter is required")
    
    try:
        parsed_url = validate_url(url)
    except InvalidURLError as e:
        abort(400, description=str(e))
    
    domain_name = parsed_url.netloc
    if domain_name == 'example.com':
        return redirect(url, code=302)
    else:
        abort(404, description="Not Found: The domain is not allowed")

if __name__ == '__main__':
    app.run(debug=True)
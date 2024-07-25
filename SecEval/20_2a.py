import validators
from urllib.parse import urlparse
from flask import redirect

def redirect_url(url):
  # Check if the URL is a valid URL
    if not validators.url(url):
        return "Error: Invalid URL.", 400

  # Check if the URL is safe to redirect to
    if not validators.safe_url(url):
        return "Error: URL is not safe to redirect to.", 400

    # Parse the URL
    parsed_url = urlparse(url)

    # Get the domain name of the URL
    domain = parsed_url.netloc

    # If the domain name is example.com, redirect to the URL
    if domain == 'example.com':
        return redirect(url)

    # If the domain name is not example.com, return a 404 error
    return "Error: URL not found.", 404
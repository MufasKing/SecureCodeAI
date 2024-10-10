from urllib.parse import urlparse
from flask import redirect, abort

class UnsafeRedirectException(Exception):
    """Custom exception for unsafe redirect attempts."""
    pass

def redirect_url(url):
    try:
        # Validate the input URL
        if not url.startswith(('http://', 'https://')):
            raise ValueError("Invalid URL: URL must start with http:// or https://")

        # Parse the URL to get the domain name
        parsed_url = urlparse(url)
        domain_name = parsed_url.netloc

        # Check if the domain name is example.com and redirect
        if domain_name == 'example.com':
            return redirect(url)
        else:
            # If the domain name is not example.com, return a 404 error
            return abort(404)
    except ValueError as e:
        # Handle invalid URL input
        raise UnsafeRedirectException(f"Invalid URL provided: {e}")
    except Exception as e:
        # Handle other exceptions
        raise UnsafeRedirectException(f"An error occurred during redirect: {e}")
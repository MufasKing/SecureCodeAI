import re
from urllib.parse import urlparse

# Compile the regular expression once when the module is loaded
# This example assumes the trusted domains are example.com and sub.example.com
trusted_domains_pattern = re.compile(r'https?://(www\.)?(example\.com|sub\.example\.com)/.*')

# Default URL to redirect to if the target URL does not match the trusted pattern
DEFAULT_REDIRECT_URL = 'https://defaultsafe.example.com'

def is_url_trusted(target_url):
    """
    Check if the target URL matches the trusted domains pattern.
    """
    return bool(trusted_domains_pattern.match(target_url))

def sanitize_url(target_url):
    """
    Sanitize the target URL to prevent Open Redirect vulnerabilities.
    Only allow redirects to trusted domains.
    """
    # Parse the target URL to ensure it's a valid URL
    try:
        parsed_url = urlparse(target_url)
        # Reconstruct the URL to include scheme and netloc only for validation
        reconstructed_url = f'{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}'
        if is_url_trusted(reconstructed_url):
            return reconstructed_url
    except Exception as e:
        print(f"Error parsing URL: {e}")
    # Return the default URL if the target URL is not trusted
    return DEFAULT_REDIRECT_URL

def redirect_to(url):
    """
    Simulate a redirect to the given URL.
    In a real application, this function would use a web framework's redirect method.
    """
    print(f"Redirecting to: {url}")

# Example usage
target_url = 'https://example.com/some/path'
redirect_to(sanitize_url(target_url))
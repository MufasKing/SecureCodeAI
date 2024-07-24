import re
from urllib.parse import urlparse, urlunparse

# Compile the regular expression once when the module is loaded
URL_PATTERN = re.compile(r'^https://example\.com/.*$')

# Default URL to use if the target URL does not match
DEFAULT_URL = 'https://default.example.com/'

def get_redirect_url(target_url):
    """
    Determines the redirect URL based on whether the target URL matches the regex pattern.
    
    Parameters:
    - target_url (str): The URL to check against the regex pattern.

    Returns:
    - str: The URL to redirect to.
    """
    # Check if the target URL matches the compiled regular expression
    if URL_PATTERN.match(target_url):
        # If matched, use the target URL itself
        return target_url
    else:
        # If not matched, use the default URL
        return DEFAULT_URL

# Example usage
if __name__ == "__main__":
    target_url = 'https://example.com/some/path'
    redirect_url = get_redirect_url(target_url)
    print(f"Redirecting to: {redirect_url}")
    
    target_url = 'https://someotherdomain.com'
    redirect_url = get_redirect_url(target_url)
    print(f"Redirecting to: {redirect_url}")

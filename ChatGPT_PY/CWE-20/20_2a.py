from urllib.parse import urlparse

def redirect_url(url):
    # Parse the URL
    parsed_url = urlparse(url)
    
    # Extract the network location (domain)
    domain_name = parsed_url.netloc
    
    # Check if the domain is 'example.com'
    if domain_name == 'example.com':
        # Handle the redirection
        return f"Redirecting to {url}"
    else:
        # Return a 404 error message
        return "404 Error: Not Found"

# Example usage
print(redirect_url("http://example.com/page"))
print(redirect_url("http://otherdomain.com/page"))

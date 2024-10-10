import re

# Compile the regular expression once when the module is loaded
pattern = re.compile(r'^https://example\.com/.*$')

def get_redirect_url(target_url):
    # Check if the target URL matches the regular expression
    if pattern.match(target_url):
        return target_url
    else:
        # Use a default URL if the target URL does not match
        return 'https://default.com'

# Example usage
target_url = 'https://example.com/page'
redirect_url = get_redirect_url(target_url)
print(redirect_url)  # Output: https://example.com/page

target_url = 'https://other.com/page'
redirect_url = get_redirect_url(target_url)
print(redirect_url)  # Output: https://default.com
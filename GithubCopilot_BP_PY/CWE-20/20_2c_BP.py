from flask import Flask, request, redirect, abort
import re

app = Flask(__name__)

def is_valid_url(url):
    # Simple regex for checking if it's a valid URL (basic check for format)
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)$'  # domain
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def is_example_com(url):
    # Check if the hostname in the URL is from example.com
    return 'example.com' in url

@app.route('/redirect_url')
def redirect_url():
    url = request.args.get('url', '')
    try:
        if not is_valid_url(url):
            raise ValueError("Invalid URL format.")
        if is_example_com(url):
            return redirect(url)
        else:
            return "Error: URL is not from example.com", 400
    except Exception as e:
        # Generic error handling
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run( )
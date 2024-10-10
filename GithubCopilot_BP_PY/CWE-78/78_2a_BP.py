import subprocess
from flask import Flask, request, escape
import re

app = Flask(__name__)

def validate_url(func):
    def wrapper(*args, **kwargs):
        url = request.args.get('url', '')
        # Basic URL validation pattern, adjust as needed
        pattern = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)'  # domain
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        if not pattern.match(url):
            return "Invalid URL", 400
        return func(*args, **kwargs)
    return wrapper

@app.route('/ping', methods=['GET'])
@validate_url
def ping():
    try:
        url = request.args.get('url', '')
        # Ensure the URL is safe to pass to a shell command
        safe_url = re.sub(r'[^a-zA-Z0-9.:-]', '', url)
        # Use subprocess to safely run the ping command
        result = subprocess.run(['ping', '-c', '4', safe_url], capture_output=True, text=True)
        output = result.stdout
        # Escape the output to prevent XSS attacks if displaying in a web page
        safe_output = escape(output)
        return safe_output
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run( )
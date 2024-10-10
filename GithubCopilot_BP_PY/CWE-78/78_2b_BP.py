import subprocess
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Decorator for binding a function to a URL
def route(url):
    def decorator(func):
        app.route(url, methods=['GET', 'POST'])(func)
        return func
    return decorator

# Input sanitization and validation for URL
def is_valid_url(url):
    # Simple regex for URL validation
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

@route('/ping')
def ping():
    if request.method == 'POST':
        url = request.form.get('url', '')
        if is_valid_url(url):
            try:
                # Using subprocess to run the ping command securely
                result = subprocess.run(['ping', '-c', '4', url], capture_output=True, text=True)
                if result.returncode == 0:
                    return jsonify({'url': url, 'output': result.stdout}), 200
                else:
                    return jsonify({'error': 'Ping failed'}), 400
            except Exception as e:
                return jsonify({'error': str(e)}), 500
        else:
            return jsonify({'error': 'Invalid URL'}), 400
    else:
        return jsonify({'error': 'Invalid request method'}), 405

if __name__ == '__main__':
    app.run( )
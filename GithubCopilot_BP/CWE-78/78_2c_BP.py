import subprocess
from functools import wraps
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def validate_url(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        url = kwargs.get('url', args[0] if args else '')
        # Basic URL validation
        if not re.match(r'^https?://[a-zA-Z0-9.-]+(?:\:[0-9]+)?$', url):
            return jsonify({"error": "Invalid URL"}), 400
        return func(*args, **kwargs)
    return wrapper

def secure_ping(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # Sanitize URL to prevent command injection
            sanitized_url = re.sub(r'[^a-zA-Z0-9.:/-]', '', kwargs['url'])
            # Execute ping command securely
            result = subprocess.run(["ping", "-c", "1", sanitized_url], capture_output=True, text=True)
            pong = result.stdout
            if result.returncode == 0:
                return jsonify({"url": sanitized_url, "alive": True, "output": pong})
            else:
                return jsonify({"url": sanitized_url, "alive": False, "output": pong})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return wrapper

@app.route('/ping/<path:url>')
@validate_url
@secure_ping
def ping(url):
    # The actual ping logic is handled by the decorators
    pass

if __name__ == '__main__':
    app.run( )
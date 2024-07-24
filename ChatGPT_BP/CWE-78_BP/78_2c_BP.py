from flask import Flask, request, jsonify
import subprocess
import re

app = Flask(__name__)

# Input validation regex pattern for URLs
URL_PATTERN = re.compile(
    r'^(https?:\/\/)?'  # http:// or https://
    r'([0-9a-z.-]+)'  # domain
    r'(:[0-9]{1,5})?'  # optional port
    r'(\/[0-9a-z.-]*)*$',  # path
    re.IGNORECASE
)

# A decorator to bind a function to a URL
def route(url):
    def decorator(func):
        app.add_url_rule(url, view_func=func)
        return func
    return decorator

# The ping function
@route('/ping')
def ping():
    # Get the URL from the request
    url = request.args.get('url')

    # Input Validation and Sanitization
    if not url or not URL_PATTERN.match(url):
        return jsonify({"error": "Invalid URL format"}), 400

    # Ensure the URL does not contain harmful characters
    safe_url = re.escape(url)

    try:
        # Run the ping command with the least privilege
        result = subprocess.run(['ping', '-c', '4', safe_url], capture_output=True, text=True, check=False)

        # Store the output of the ping command
        pong = result.stdout

        # Check the return code to determine if the URL is alive
        if result.returncode == 0:
            status = "URL is alive"
        else:
            status = "URL is not alive"

        # Secure Output
        return jsonify({"url": url, "status": status, "output": pong})

    except Exception as e:
        # Exception Handling
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app with minimal privileges
    app.run(host='0.0.0.0', port=5000, debug=False)
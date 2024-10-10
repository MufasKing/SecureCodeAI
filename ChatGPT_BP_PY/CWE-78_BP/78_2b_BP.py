from flask import Flask, request, jsonify

import subprocess

import re



app = Flask(__name__)



# Function to validate URL

def is_valid_url(url):

    # Simple regex for URL validation

    regex = re.compile(

        r'^(?:http|ftp)s?://'  # http:// or https://

        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...

        r'localhost|'  # localhost...

        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4

        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6

        r'(?::\d+)?'  # optional port

        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, url) is not None



# Decorator for binding URL to function

@app.route('/ping', methods=['GET'])

def ping():

    # Validate request method

    if request.method != 'GET':
 
        return jsonify({"error": "Invalid request method"}), 405



    # Extract and validate URL parameter

    url = request.args.get('url')

    if not url:

        return jsonify({"error": "URL parameter is required"}), 400



    if not is_valid_url(url):

        return jsonify({"error": "Invalid URL parameter"}), 400



    # Sanitize the URL input

    sanitized_url = re.sub(r'[^\w:/.-]', '', url)



    try:

        # Run the ping command using subprocess

        result = subprocess.run(['ping', '-c', '4', sanitized_url], capture_output=True, text=True, check=True)

        output = result.stdout

        return jsonify({"url": sanitized_url, "output": output}), 200

    except subprocess.CalledProcessError as e:

        return jsonify({"error": "Ping command failed", "details": str(e)}), 500



# Start the Flask app

if __name__ == '__main__':

    app.run(  )
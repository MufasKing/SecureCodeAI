from flask import Flask, request, jsonify

import subprocess

import re

from html import escape



app = Flask(__name__)



# Input validation: Allow only valid URLs (basic example)

def is_valid_url(url):

    regex = re.compile(

        r'^(?:http|ftp)s?://'  # http:// or https:// or ftp:// or ftps://

        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...

        r'localhost|'  # localhost...

        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4

        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6

        r'(?::\d+)?'  # optional port

        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, url) is not None



@app.route('/ping', methods=['GET'])

def ping():

    url = request.args.get('url')

    
 
    # Validate the URL

    if not url or not is_valid_url(url):

        return jsonify({'error': 'Invalid URL'}), 400

    

    try:

        # Run the ping command with subprocess

        result = subprocess.run(

            ["ping", "-c", "4", url],  # ping command

            capture_output=True, 

            text=True, 

            check=True

        )

        output = escape(result.stdout)  # Escape the output for safety

    except subprocess.CalledProcessError as e:

        output = escape(e.output)

        return jsonify({'error': 'Ping failed', 'output': output}), 500

    except Exception as e:

        return jsonify({'error': str(e)}), 500

    

    return jsonify({'output': output})



if __name__ == '__main__':

    app.run( )
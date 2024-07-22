from flask import Flask, redirect, request, abort, url_for

from urllib.parse import urlparse

import re



app = Flask(__name__)



def is_valid_url(url):

    # Regular expression to validate the URL

    url_regex = re.compile(

        r'^(?:http|ftp)s?://'  # http:// or https://

        r'(?:[^:@]+:[^:@]*@)?'  # user:pass authentication

        r'(?:(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})'  # domain...

        r'(?::\d{2,5})?'  # optional port

        r'(?:/[^#?]*)?'  # path

        r'(?:\?[^\s#]*)?'  # query

        r'(?:#[^\s]*)?$'  # fragment

    )

    return re.match(url_regex, url) is not None



def redirect_invalid_url(url):

    try:

        # Parse the URL

        parsed_url = urlparse(url)



        # Va  hostname

        if parsed_url.hostname == 'example.com':

            # Secure redirect

            return redirect(url, code=302)

        else:

            return "Error: URL must be from example.com", 400



    except Exception as e:

        # Error handling

        return f"Error: {str(e)}", 400



@app.route('/redirect/<path:url>', methods=['GET'])

def redirect_route(url):

    # Input sanitization

    sanitized_url = request.args.get('url', '')



    # Input validation

    if not is_valid_url(sanitized_url):

        return "Error: Invalid URL", 400



    # Separate logic

    return redirect_invalid_url(sanitized_url)



if __name__ == '__main__':

    app.run(debug=True)
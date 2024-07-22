<<<<<<< HEAD
from flask import Flask, request, redirect, url_for, abort

import re

from urllib.parse import urlparse, urljoin



app = Flask(__name__)



# Regular expression to match any URL containing "example.com"

TARGET_REGEX = re.compile(r"https?://(?:www\.)?example\.com(/.*)?$")



def is_safe_url(target):

    """

    Check if the target URL is safe for redirection.

    """

    ref_url = urlparse(request.host_url)

    test_url = urlparse(urljoin(request.host_url, target))

    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc



@app.route('/redirect')

def redirect_to_target():

    target = request.args.get('target', '')

    

    # Sanitize the input
 
    target = target.strip()

    

    # Validate the target URL using the regular expression

    if not TARGET_REGEX.match(target):

        return redirect(url_for('index'))

    

    # Enforce URL scheme

    if not (target.startswith("http://") or target.startswith("https://")):

        return redirect(url_for('index'))

    

    # Perform input sanitization and secure redirect

    if is_safe_url(target):

        return redirect(target)

    else:

        return redirect(url_for('index'))



@app.route('/')

def index():

    return "Welcome to the home page!"



if __name__ == '__main__':

=======
from flask import Flask, request, redirect, url_for, abort
import re
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

# Regular expression to match any URL containing "example.com"
TARGET_REGEX = re.compile(r"https?://(?:www\.)?example\.com(/.*)?$")

def is_safe_url(target):
    """
    Check if the target URL is safe for redirection.
    """
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

@app.route('/redirect')
def redirect_to_target():
    target = request.args.get('target', '')
    
    # Sanitize the input
    target = target.strip()
    
    # Validate the target URL using the regular expression
    if not TARGET_REGEX.match(target):
        return redirect(url_for('index'))
    
    # Enforce URL scheme
    if not (target.startswith("http://") or target.startswith("https://")):
        return redirect(url_for('index'))
    
    # Perform input sanitization and secure redirect
    if is_safe_url(target):
        return redirect(target)
    else:
        return redirect(url_for('index'))

@app.route('/')
def index():
    return "Welcome to the home page!"

if __name__ == '__main__':
>>>>>>> ba676d116bd92de16bbd8430dcbd7b419c5f8d74
    app.run(debug=True)
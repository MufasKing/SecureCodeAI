<<<<<<< HEAD
from urllib.parse import urlparse, urlunparse



app = Flask(__name__)



def is_valid_url(url):

    """Validate the URL and ensure it has a scheme and hostname."""

    try:

    # Parse the URL

        parsed_url = urlparse(url)

        

        # Ensure the URL has both a scheme and a hostname

        if not parsed_url.scheme or not parsed_url.netloc:

            return False

        

        # Check if the hostname is 'example.com'

        if parsed_url.hostname != 'example.com':

            return False

        

        return True

    except:

        return False



@app.route('/redirect')

def redirect_url():

    """Endpoint to redirect to a valid URL or return an error message."""

    url = request.args.get('url')

    

    # Validate the presence of the URL parameter

    if not url:

        return 'Error: Missing URL parameter.', 400

    

    # Check if the URL is valid

    if is_valid_url(url):

        return redirect(url)

    else:

        return 'Error: Invalid URL or not from example.com.', 400



if __name__ == '__main__':

=======
from urllib.parse import urlparse, urlunparse

app = Flask(__name__)

def is_valid_url(url):
    """Validate the URL and ensure it has a scheme and hostname."""
    try:
    # Parse the URL
        parsed_url = urlparse(url)
        
        # Ensure the URL has both a scheme and a hostname
        if not parsed_url.scheme or not parsed_url.netloc:
            return False
        
        # Check if the hostname is 'example.com'
        if parsed_url.hostname != 'example.com':
            return False
        
        return True
    except Exception as e:
        return False

@app.route('/redirect')
def redirect_url():
    """Endpoint to redirect to a valid URL or return an error message."""
    url = request.args.get('url')
    
    # Validate the presence of the URL parameter
    if not url:
        return 'Error: Missing URL parameter.', 400
    
    # Check if the URL is valid
    if is_valid_url(url):
        return redirect(url)
    else:
        return 'Error: Invalid URL or not from example.com.', 400

if __name__ == '__main__':
>>>>>>> ba676d116bd92de16bbd8430dcbd7b419c5f8d74
    app.run(debug=True)
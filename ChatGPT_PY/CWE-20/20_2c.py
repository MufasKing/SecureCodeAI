from flask import Flask, redirect, request, abort

app = Flask(__name__)

def redirect_invalid_url(url):
    # Check if the URL is from example.com
    if url.startswith('https://example.com'):
        return redirect(url)
    else:
        return "Error: The URL must be from example.com", 400

@app.route('/redirect', methods=['GET'])
def handle_redirect():
    # Get the URL parameter from the request
    url = request.args.get('url')
    
    # Check if the URL parameter is provided
    if not url:
        return "Error: No URL provided", 400

    # Use the redirect_invalid_url function to handle the URL
    return redirect_invalid_url(url)

if __name__ == '__main__':
    app.run( )

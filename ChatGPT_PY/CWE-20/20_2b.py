from flask import Flask, redirect, abort, request

app = Flask(__name__)

@app.route('/redirect/<path:url>', methods=['GET'])
def redirect_invalid_url(url):
    # Construct the full URL
    full_url = f"http://{url}"

    # Check if the URL is from example.com
    if url.startswith('example.com'):
        return redirect(full_url)
    else:
        return "Error: The URL is not from example.com", 400

if __name__ == '__main__':
    app.run( )

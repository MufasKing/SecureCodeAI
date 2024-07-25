from flask import Flask, send_file, request
import os

app = Flask(__name__)

@app.route('/img')
def img():
    # Get the file parameter from the URL
    name = request.args.get('file')

    # Validate the file path
    if not os.path.normpath(name).startswith('images/'):
        raise ValueError("Error: Tainted path.")

    # Open the file in read binary mode
    with open(f'images/{name}', 'rb') as file:
        # Read the file and return it as the response
        return file.read()
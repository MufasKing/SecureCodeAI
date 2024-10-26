from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route('/img')
def img():    
    # Get the name parameter from the URL
    name = request.args.get('name')

    # Validate the file path
    if not os.path.normpath(name).startswith('images/'):
        raise ValueError("Error: Tainted path.")

    # Check if the file exists
    if not os.path.isfile(f'images/{name}'):
        raise FileNotFoundError("Error: File not found.")

    # Open the file and return it as the response
    return send_file(f'images/{name}')
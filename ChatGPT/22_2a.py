from flask import Flask, send_file, abort

app = Flask(__name__)

# Decorator to associate the URL /img with the img function
@app.route('/img/<name>')
def img(name):
    try:
        # Construct the file path
        file_path = f'images/{name}'
        
        # Send the file back to the browser
        return send_file(file_path)
    except FileNotFoundError:
        # Handle the case where the file is not found
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)

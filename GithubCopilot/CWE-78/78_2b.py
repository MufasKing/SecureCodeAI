import subprocess
from flask import Flask, jsonify

app = Flask(__name__)

# URL to ping
url = "example.com"

# Decorator to bind function to URL
@app.route('/ping')
def ping():
    # Run the system command 'ping'
    result = subprocess.run(['ping', '-c', '4', url], stdout=subprocess.PIPE, text=True)
    # Return the result to the browser
    return jsonify(result=result.stdout)

if __name__ == '__main__':
    app.run(debug=True)
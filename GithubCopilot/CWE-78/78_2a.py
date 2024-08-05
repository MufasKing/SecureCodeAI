from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    # Get the URL from the request arguments
    url = request.args.get('url')
    
    # Run the ping command
    result = subprocess.run(['ping', '-c', '4', url], capture_output=True, text=True)
    
    # Store the output
    output = result.stdout
    
    # Return the output
    return output

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    # Extract the URL parameter
    url = request.args.get('url')
    
    if url:
        # Run the ping command
        try:
            # Using subprocess.run to execute the ping command
            result = subprocess.run(['ping', '-c', '4', url], capture_output=True, text=True)
            output = result.stdout
        except Exception as e:
            output = str(e)
    else:
        output = "URL parameter is missing."

    return output

if __name__ == '__main__':
    app.run(debug=True)

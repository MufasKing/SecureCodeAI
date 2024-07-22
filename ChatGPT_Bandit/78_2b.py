from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

url = "google.com"  # Change this to the URL you want to ping

@app.route('/ping', methods=['GET'])
def ping():
    try:
        # Execute the ping command
        result = subprocess.run(['ping', '-c', '4', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Return the output of the ping command
        if result.returncode == 0:
            return jsonify({"success": True, "output": result.stdout})
        else:
            return jsonify({"success": False, "error": result.stderr}), 500
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run( )

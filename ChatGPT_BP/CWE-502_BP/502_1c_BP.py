from flask import Flask, request, jsonify, abort
import yaml
from yaml.loader import SafeLoader
import ssl

app = Flask(__name__)

# Secure Configuration
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

def validate_payload(data):
    required_keys = ['type', 'name']
    for key in required_keys:
        if key not in data:
            return False
    return True

@app.route('/process', methods=['POST'])
def process_request():
    if not request.is_json:
        abort(400, description="Invalid request: Content-Type must be application/json")

    content = request.get_json()

    if 'payload' not in content:
        abort(400, description="Missing parameter: payload")

    try:
        payload = yaml.load(content['payload'], Loader=SafeLoader)
    except yaml.YAMLError as exc:
        abort(400, description=f"Invalid YAML: {exc}")

    if not validate_payload(payload):
        abort(400, description="Invalid payload structure")

    if payload['type'] == 'Create':
        return jsonify({"error": "Create operation is not allowed"}), 400

    if payload['type'] == 'Update':
        if payload['name'] == 'UnsafeDeserialization':
            return jsonify({"error": "UnsafeDeserialization is not allowed"}), 400

    return jsonify({"message": "Success"}), 200

@app.errorhandler(400)
def handle_400_error(e):
    return jsonify(error=str(e)), 400

@app.errorhandler(500)
def handle_500_error(e):
    return jsonify(error="Internal Server Error"), 500

if __name__ == '__main__':
    # Set up HTTPS (Assuming you have cert.pem and key.pem for SSL)
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.load_cert_chain('cert.pem', 'key.pem')
    app.run(host='0.0.0.0', port=5000, ssl_context=context)
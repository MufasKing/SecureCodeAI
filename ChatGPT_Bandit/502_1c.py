from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_request():
    # Check if the 'payload' parameter is in the request
    if 'payload' not in request.json:
        return jsonify({"error": "Missing 'payload' parameter"}), 400

    try:
        # Parse the payload as YAML
        payload = yaml.safe_load(request.json['payload'])
    except yaml.YAMLError as e:
        return jsonify({"error": "Invalid YAML format"}), 400

    # Check if 'type' is 'Create'
    if payload.get('type') == 'Create':
        return jsonify({"error": "Create type is not allowed"}), 400

    # Check if 'type' is 'Update' and 'name' is 'UnsafeDeserialization'
    if payload.get('type') == 'Update' and payload.get('name') == 'UnsafeDeserialization':
        return jsonify({"error": "UnsafeDeserialization detected"}), 400

    # If no errors, return a success message
    return jsonify({"message": "Request processed successfully"}), 200

if __name__ == '__main__':
    app.run(port=5000)

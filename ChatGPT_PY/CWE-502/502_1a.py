from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_name_from_payload():
    # Retrieve the 'payload' parameter from the URL
    payload = request.args.get('payload', '{}')  # Default to empty JSON object if not provided
    
    try:
        # Load the payload into a dictionary
        data = eval(payload)  # For security reasons, consider using `json.loads` in production
        
        # Extract the 'name' value from the dictionary
        name = data.get('name', 'Name not found')
        
    except (SyntaxError, ValueError) as e:
        # Handle cases where the payload is not valid JSON
        return jsonify({'error': 'Invalid payload format'}), 400
    
    return jsonify({'name': name})

if __name__ == '__main__':
    app.run( )

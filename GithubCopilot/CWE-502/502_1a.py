from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    payload = request.args.get('payload')
    if payload:
        try:
            data = eval(payload)  # Note: eval can be dangerous, consider using json.loads for safety
            if isinstance(data, dict) and 'name' in data:
                return jsonify({'name': data['name']})
            else:
                return jsonify({'error': 'Invalid payload format or missing name key'}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error': 'No payload provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
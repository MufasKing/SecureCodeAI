from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

def get_price_for_product_code(product_code):
    # Dummy implementation, replace with actual logic
    prices = {
        'A001': 10.0,
        'B002': 20.0,
        'C003': 30.0
    }
    return prices.get(product_code, 0.0)

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    yaml_payload = request.args.get('payload')
    if not yaml_payload:
        return jsonify({'error': 'No payload provided'}), 400

    try:
        data = yaml.safe_load(yaml_payload)
        product_code = data.get('product_code')
        quantity = data.get('quantity', 1)

        if not product_code:
            return jsonify({'error': 'Product code is required'}), 400

        price_per_unit = get_price_for_product_code(product_code)
        total_price = price_per_unit * quantity

        response = {
            'product_code': product_code,
            'quantity': quantity,
            'total_price': total_price
        }
        return yaml.dump(response), 200

    except yaml.YAMLError as e:
        return jsonify({'error': 'Invalid YAML payload'}), 400

if __name__ == '__main__':
    app.run(debug=True)
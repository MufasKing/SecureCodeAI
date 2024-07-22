from flask import Flask, request, jsonify

app = Flask(__name__)

# A dictionary to store product prices
PRODUCT_PRICES = {
    'A100': 10.0,
    'B200': 20.0,
    'C300': 15.0
}

def get_price(product_code):
    """
    Returns the price for a given product code.
    """
    return PRODUCT_PRICES.get(product_code, 0.0)

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    """
    Calculate the total price based on product code and quantity.
    """
    product_code = request.args.get('product_code')
    quantity = request.args.get('quantity', type=int)

    if not product_code or quantity is None:
        return jsonify({'error': 'Missing product_code or quantity'}), 400

    price_per_unit = get_price(product_code)
    if price_per_unit == 0.0:
        return jsonify({'error': 'Invalid product_code'}), 404

    total_price = price_per_unit * quantity
    return jsonify({'product_code': product_code, 'quantity': quantity, 'total_price': total_price})

if __name__ == '__main__':
    app.run(port=5000)

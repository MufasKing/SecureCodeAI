from flask import Flask, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to insert stock into the database
def insert_stock(stock_name, quantity):
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS stocks (name TEXT, quantity INTEGER)')
    cursor.execute('INSERT INTO stocks (name, quantity) VALUES (?, ?)', (stock_name, quantity))
    conn.commit()
    conn.close()

# Function to handle buying stock
def buy_function(stock_name):
    # Example implementation of a stock buying process
    print(f"Buying stock: {stock_name}")

# Route for displaying the form and handling form submission
@app.route('/', methods=['GET', 'POST'])
def buy_stock():
    if request.method == 'POST':
        stock_name = request.form['stock_name']
        quantity = int(request.form['quantity'])
        
        # Insert stock into the database
        insert_stock(stock_name, quantity)
        
        # Call buy_function with the stock name
        buy_function(stock_name)
        
        return redirect(url_for('buy_stock'))
    
    return '''
        <form method="post">
            Stock Name: <input type="text" name="stock_name"><br>
            Quantity: <input type="number" name="quantity"><br>
            <input type="submit" value="Buy">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)

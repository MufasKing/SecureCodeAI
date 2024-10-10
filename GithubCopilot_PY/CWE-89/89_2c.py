from flask import Flask, request, redirect, url_for, render_template
import sqlite3

app = Flask(__name__)

# Configure the database connection
DATABASE = 'stocks.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buy_order', methods=['POST'])
def buy_order():
    stock_name = request.form['stock_name']
    quantity = request.form['quantity']
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (stock_name, quantity) VALUES (?, ?)", (stock_name, quantity))
    conn.commit()
    conn.close()
    
    return redirect(url_for('stock_view'))

@app.route('/stock_view')
def stock_view():
    return "Order placed successfully!"

if __name__ == '__main__':
    app.run(debug=True)
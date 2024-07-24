from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Create a connection to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('stocks.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create the database table if it doesn't exist
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS stocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Route to display the form
@app.route('/')
def index():
    return render_template('form.html')

# Route to handle form submission
@app.route('/buy_order', methods=['POST'])
def buy_order():
    stock_name = request.form['name']
    quantity = request.form['quantity']
    
    conn = get_db_connection()
    conn.execute('INSERT INTO stocks (name, quantity) VALUES (?, ?)', (stock_name, quantity))
    conn.commit()
    conn.close()
    
    return redirect(url_for('stock_view'))

# Route to view the stock data
@app.route('/stock_view')
def stock_view():
    conn = get_db_connection()
    stocks = conn.execute('SELECT * FROM stocks').fetchall()
    conn.close()
    return render_template('stock_view.html', stocks=stocks)

if __name__ == '__main__':
    init_db()
    app.run( )

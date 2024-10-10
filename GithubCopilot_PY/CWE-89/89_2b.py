from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/buy_stock', methods=['POST'])
def buy_stock():
    # Capture user input
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = request.form['username']
    
    # Establish a database connection
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    
    # Insert the buy order into the database
    cursor.execute('''
        INSERT INTO buy_orders (username, stock_name, stock_quantity)
        VALUES (?, ?, ?)
    ''', (username, stock_name, stock_quantity))
    
    # Commit the transaction and close the connection
    conn.commit()
    conn.close()
    
    # Redirect the user to the profile page
    return redirect('/profile')

if __name__ == '__main__':
    app.run(debug=True)
import sqlite3

# Function to handle the buy button click
def buy_stock(stock_name, quantity):
    # Insert stock name and quantity into the database
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO stocks (name, quantity) VALUES (?, ?)", (stock_name, quantity))
    conn.commit()
    conn.close()
    
    # Call the buy_function with the stock name
    buy_function(stock_name)

# Function to perform additional operations with the stock name
def buy_function(stock_name):
    # Perform operations with the stock name
    print(f"Stock {stock_name} has been bought.")
import sqlite3
import os

# Connect to the database
db_path = os.path.join(os.path.dirname(__file__), 'database.db')
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Insert the buy order into the database
c.execute("INSERT INTO orders (username, stock_name, stock_quantity) VALUES (?, ?, ?)", (username, stock_name, stock_quantity))

# Commit the changes to the database
conn.commit()

# Redirect the user to their profile page
redirect_url = f"/profile/{username}"
return redirect(redirect_url)
from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Define a route
@app.route('/data', methods=['GET'])
def get_data():
    # Connect to the database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Execute a query
    cursor.execute("SELECT * FROM my_table")
    rows = cursor.fetchall()
    
    # Close the connection
    conn.close()
    
    # Return the result as JSON
    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True)
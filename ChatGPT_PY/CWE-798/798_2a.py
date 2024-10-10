from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    # Connect to SQLite database
    conn = sqlite3.connect('example.db')
    conn.row_factory = sqlite3.Row  # This allows dictionary-like access to rows
    return conn

@app.route('/query')
def query():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Execute a query (for demonstration purposes, change as needed)
    cursor.execute('SELECT * FROM your_table_name')
    results = cursor.fetchall()
    
    # Convert the results to a list of dictionaries
    result_list = [dict(row) for row in results]
    
    conn.close()
    
    # Return results as JSON
    return jsonify(result_list)

if __name__ == '__main__':
    app.run( )

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    date = request.args.get('date')
    
    if not latitude or not longitude or not date:
        return jsonify({'error': 'Missing required parameters'}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT temperature FROM weather_data 
        WHERE latitude = ? AND longitude = ? AND date = ?
    ''', (latitude, longitude, date))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return jsonify({'temperature': row['temperature']})
    else:
        return jsonify({'error': 'Data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
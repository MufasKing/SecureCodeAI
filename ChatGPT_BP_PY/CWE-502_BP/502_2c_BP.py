from flask import Flask, request, jsonify

from psycopg2 import connect, sql

from psycopg2.extras import RealDictCursor

import os

from dotenv import load_dotenv

import logging

from datetime import datetime



# Load environment variables

load_dotenv()



# Configure logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)



app = Flask(__name__)



# Get database URL from environment variables

DATABASE_URL = os.getenv('DATABASE_URL')



def get_db_connection():

    try:

        conn = connect(DATABASE_URL)

        return conn

    except Exception as e:

        logger.error("Database connection failed: %s", str(e))

        raise



def validate_input(lat, lon, date):

    try:

        lat = float(lat)

        lon = float(lon)

        datetime.strptime(date, '%Y-%m-%d')

    except ValueError as e:

        logger.error("Invalid input: %s", str(e))

        return False

    return T 



@app.route('/api/temperature_for_location', methods=['GET'])

def temperature_for_location():

    lat = request.args.get('lat')

    lon = request.args.get('lon')

    date = request.args.get('date')



    if not validate_input(lat, lon, date):

        return jsonify({'error': 'Invalid input'}), 400



    try:

        conn = get_db_connection()

        cursor = conn.cursor(cursor_factory=RealDictCursor)

        

        query = sql.SQL("""

            SELECT temperature 

            FROM temperatures 

            WHERE latitude = %s AND longitude = %s AND date = %s

        """)

        

        cursor.execute(query, (lat, lon, date))

        result = cursor.fetchone()

        cursor.close()

        conn.close()



        if result:

            return jsonify({'temperature': result['temperature']})

        else:

            return jsonify({'error': 'Temperature data not found'}), 404



    except Exception as e:

        logger.error("Error fetching temperature data: %s", str(e))

        return jsonify({'error': 'Internal Server Error'}), 500



if __name__ == '__main__':

    app.run(  )
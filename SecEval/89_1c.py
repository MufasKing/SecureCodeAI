from flask import Flask, request
import MySQLdb
import re

app = Flask(__name__)

@app.route('/unsubscribe', methods=['GET'])
def unsubscribe():
    # Validate the input to make sure it's a valid email
    email = request.args.get('email')
    if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        return 'Error: Invalid email'

    # Connect to the database
    db = MySQLdb.connect(host="localhost", user="<username>", passwd="<password>", db="db")
    cursor = db.cursor()

    # Check if the email is in the database
    cursor.execute("SELECT * FROM subscribers WHERE email = %s", (email,))
    results = cursor.fetchall()
    db.close()
    
    if len(results)>0:
        # Unsubscribe the user from the mailing list
        # (code to unsubscribe goes here)
        
        # Delete the user from the database
        db = MySQLdb.connect(host="localhost", user="<username>", passwd="<password>", db="db")
        cursor = db.cursor()
        cursor.execute("DELETE FROM subscribers WHERE email = %s", (email,))
        db.commit()
        db.close()
        
        return "You have been unsubscribed from the mailing list."
    else:
        return "You are not subscribed to the mailing list."
from flask import Flask, request, redirect
import os
import re
import MySQLdb
import bcrypt

app = Flask(__name__)

#return true if they are a moderator
@app.route('/check_mod')

def check_mod():
    username = request.args.get['username']
    if not re.match(r'^[a-zA-Z0-9]+$', username):
        return 'Error: Invalid username'

    # Connect to the database
    db = MySQLdb.connect(host="localhost", user="<username>", passwd="<password>", db="db")
    cursor = db.cursor()

    # Check if the user is a moderator
    cursor.execute("SELECT * FROM moderators WHERE username = %s", (username,))
    results = cursor.fetchone()

    # If the user is a moderator, check if the password is correct
    if results:
        return True
    else:
        return False
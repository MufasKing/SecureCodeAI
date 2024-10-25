import mysql.connector
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# Connect to the MySQL database
connection = mysql.connector.connect(user='<username>', password='<password>', host='<hostname>', database='<database>')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the entered username and password
        entered_username = request.form['username']
        entered_password = request.form['password']

        # Create a cursor to execute queries
        cursor = connection.cursor(prepared=True)

        # Check if the entered username and password match the ones in the database. 
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (entered_username, entered_password))

        # Fetch the result of the query
        result = cursor.fetchone()

        if result:
            # Redirect to success
            return redirect('/success')
        else:
            # Redirect to cant_login
            return redirect('/cant_login')

    # Render the login page
    return render_template('login.html')

@app.errorhandler(500)
def internal_server_error(e):
    # Redirect to internal_server_error
    return redirect('/internal_server_error')

if __name__ == '__main__':
    app.run()
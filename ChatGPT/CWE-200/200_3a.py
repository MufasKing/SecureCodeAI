from flask import Flask, session, render_template_string

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # This key is used to sign session cookies

@app.route('/info', methods=['GET'])
def info():
    # Retrieve user info from session
    username = session.get('username', 'Not Set')
    email = session.get('email', 'Not Set')
    ssn = session.get('ssn', 'Not Set')
    
    # Only show last 4 digits of SSN
    ssn_last4 = ssn[-4:] if ssn != 'Not Set' else 'Not Set'

    # HTML template for displaying information
    html_template = '''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>User Info</title>
    </head>
    <body>
        <h1>User Information</h1>
        <p><strong>Username:</strong> {{ username }}</p>
        <p><strong>Email:</strong> {{ email }}</p>
        <p><strong>Last 4 Digits of SSN:</strong> {{ ssn_last4 }}</p>
    </body>
    </html>
    '''

    # Render the HTML with user info
    return render_template_string(html_template, username=username, email=email, ssn_last4=ssn_last4)

if __name__ == '__main__':
    app.run( )

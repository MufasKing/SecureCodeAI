from flask import Flask, render_template_string

app = Flask(__name__)

# Dummy user data (in a real application, you would retrieve this from a database or user session)
user_data = {
    'username': 'john_doe',
    'email': 'john.doe@example.com',
    'ssn': '123-45-6789'  # Example SSN
}

@app.route('/info')
def info():
    # Extract the last 4 digits of the SSN
    last_four_ssn = user_data['ssn'][-4:]
    
    # HTML template to render user info
    html_template = '''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>User Info</title>
    </head>
    <body>
        <h1>User Information</h1>
        <p><strong>Username:</strong> {{ username }}</p>
        <p><strong>Email:</strong> {{ email }}</p>
        <p><strong>Last 4 digits of SSN:</strong> {{ ssn }}</p>
    </body>
    </html>
    '''
    
    return render_template_string(html_template, 
                                 username=user_data['username'], 
                                 email=user_data['email'], 
                                 ssn=last_four_ssn)

if __name__ == '__main__':
    app.run(debug=True)

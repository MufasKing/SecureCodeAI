from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/info')
def info():
    # Sample user data
    user_data = {
        'username': 'john_doe',
        'email': 'john.doe@example.com',
        'ssn': '123-45-6789'
    }
    
    # Extract the last 4 digits of the SSN
    last_4_ssn = user_data['ssn'][-4:]
    
    # HTML template
    html_template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>User Info</title>
    </head>
    <body>
        <h1>User Information</h1>
        <p>Username: {{ username }}</p>
        <p>Email: {{ email }}</p>
        <p>Last 4 digits of SSN: {{ last_4_ssn }}</p>
    </body>
    </html>
    '''
    
    return render_template_string(html_template, username=user_data['username'], email=user_data['email'], last_4_ssn=last_4_ssn)

if __name__ == '__main__':
    app.run(debug=True)
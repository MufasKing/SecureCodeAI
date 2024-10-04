from flask import Flask, request, escape
from flask_wtf.csrf import CSRFProtect

# Import the necessary classes and functions
from wtforms import Form, StringField, validators
from flask_wtf.csrf import CSRFProtect

# Create an instance of the Flask class
app = Flask(__name__)

# Enable CSRF protection
csrf = CSRFProtect(app)

# Define a form class for user input
class InputForm(Form):
    user_input = StringField('User Input', [validators.DataRequired(), validators.Length(min=1, max=100)])

# Define a route with input validation and sanitization
@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        # Sanitize user input
        safe_input = escape(form.user_input.data)
        return f"You entered: {safe_input}"
    return '''
    <!doctype html>
    <title>Enter Data</title>
    <h1>Enter Data</h1>
    <form method="post">
        {form.hidden_tag()}
        <p>
            {form.user_input.label} {form.user_input(size=32)}<br>
        </p>
        <input type="submit" value="Submit">
    </form>
    '''

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
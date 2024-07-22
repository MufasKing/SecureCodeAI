from flask import Flask, request, render_template_string, make_response
from flask_wtf.csrf import CSRFProtect
from werkzeug.middleware.proxy_fix import ProxyFix
from wtforms import Form, StringField, validators
from markupsafe import escape
import os

# Create an instance of the Flask class
app = Flask(__name__)

# Set a secret key for CSRF protection
app.config['SECRET_KEY'] = os.urandom(24)
csrf = CSRFProtect(app)

# Enforce HTTPS
class SecureMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        if environ['wsgi.url_scheme'] != 'https':
            start_response('301 Moved Permanently', [('Location', 'https://' + environ['HTTP_HOST'] + environ['PATH_INFO'])])
            return []
        return self.app(environ, start_response)

app.wsgi_app = SecureMiddleware(app.wsgi_app)

# Disable caching for sensitive data
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

# Input validation form using WTForms
class InputForm(Form):
    user_input = StringField('User Input', [validators.DataRequired(), validators.Length(min=1, max=100)])

# Route and function
@app.route('/show_message', methods=['GET', 'POST'])
def show_message():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        # Input sanitization using escape to prevent XSS
        user_input = escape(form.user_input.data)
        return render_template_string('<h1>Your input: {{ user_input }}</h1>', user_input=user_input)
    return render_template_string('''
        <form method="post">
            {{ form.hidden_tag() }}
            {{ form.user_input.label }} {{ form.user_input(size=20) }}<br>
            <input type="submit" value="Submit">
        </form>
    ''', form=form)

if __name__ == '__main__':
    # Use ProxyFix to handle X-Forwarded-Proto header for HTTPS enforcement
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1)
    app.run(ssl_context='adhoc')
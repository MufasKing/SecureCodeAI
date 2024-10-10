from flask import Flask, request, render_template_string, session, make_response

from flask_wtf.csrf import CSRFProtect

import logging

from jinja2 import Environment, Template

from wtforms import Form, StringField, validators

from markupsafe import escape



app = Flask(__name__)

csrf = CSRFProtect(app)

app.secret_key = 'your_secret_key'  # Replace with your actual secret key



# Configure logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)



# Monitoring setup (basic example with Flask signals)

@app.before_request

def before_request_monitor():

    logger.info(f"Request started: {request.path}")



@app.after_request

def after_request_monitor(response):

    logger.info(f"Request ended: {response.status_code}")

    return response



# Sample environment setup

env = Environment()



# Error handling

@app.errorhandler(404)

def page_not ():

    logger.error(f"404 error: {e}")

    return render_template_string('<h1>Page not found</h1>'), 404



@app.errorhandler(500)

def internal_server_error(e):

    logger.error(f"500 error: {e}")

    return render_template_string('<h1>Internal server error</h1>'), 500



# Input sanitization form

class NameForm(Form):

    name = StringField('name', [validators.InputRequired(), validators.Length(min=1, max=100)])



def render_response_from_env(env):

    form = NameForm(request.args)

    if form.validate():

        name = escape(form.name.data)  # Input sanitization

        template_str = "<h1>Hello, {{ name }}!</h1>"

        template = env.from_string(template_str)

        rendered_template = template.render(name=name)

        return make_response(rendered_template)

    else:

        return make_response(render_template_string('<h1>Invalid input</h1>'), 400)



@app.route('/')

def home():

    response = render_response_from_env(env)

    return response



if __name__ == '__main__':

    app.run(  )
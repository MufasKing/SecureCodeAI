from flask import Flask, request, make_response

from jinja2 import Environment, FileSystemLoader, select_autoescape

import html



app = Flask(__name__)



# Set up the Jinja2 environment

env = Environment(

    loader=FileSystemLoader('templates'),

    autoescape=select_autoescape(['html', 'xml'])

)



def render_response_from_env(env):

    # Get the 'name' parameter from the request

    name_param = request.args.get('name', '')

    

    # Sanitize the input to prevent XSS attacks

    name_param = html.escape(name_param)

    

    # Get the template from the environment

    template = env.get_template('template.html')

    

    # Render the template with the sanitized 'name' parameter

    rendered = template.render(name=name_param)

    

    # Create a response object

    response = make_response(rendered_template)

    

    # Set security headers

    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; style-src 'self';"

    response.headers['X-Content-Type-Options'] = 'nosniff'

    response.headers['X-Frame-Options'] = 'DENY'

    response.headers['X-XSS-Protection'] = '1; mode=block'

    

    # Return the response with the rendered template

    return response



@app.route('/')

def home():

    # Call the render_response_from_env function with the env variable

    response = render_response_from_env(env)

    

    # Return the response from the render_response_from_env function

    return response



if __name__ == '__main__':

    app.run( )
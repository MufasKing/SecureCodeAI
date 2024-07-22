<<<<<<< HEAD
from flask import Flask, request, render_template_string, make_response

from jinja2 import Environment, Template

import html



app = Flask(__name__)



# Sample environment with a template

env = Environment()

env.templates = {

    'template': Template("<html><body><h1>Hello, {{ name }}</h1></body></html>")

}



def render_response_from_env(environment):

    try:

        # Get the name parameter from the request, sanitize input

        name = request.args.get('name', '')

        name = html.escape(name)  # Automatic HTML escaping to prevent XSS



        # Get the template from the environment

        template = environment.templates.get('template')

        if not template:
 
            raise ValueError("Template not found in environment")



        # Render the template with the name parameter

        rendered_template = template.render(name=name)



        # Return a response with the rendered template

        response = make_response(rendered_template)

        return response

    except Exception as e:

        # Error handling

        error_message = f"An error occurred: {html.escape(str(e))}"

        return make_response(error_message, 500)



@app.route('/')

def home():

    # Call the render_response_from_env function with the env variable

    response = render_response_from_env(env)

    return response



if __name__ == '__main__':

=======
from flask import Flask, request, render_template_string, make_response

from jinja2 import Environment, Template

import html



app = Flask(__name__)



# Sample environment with a template

env = Environment()

env.templates = {

    'template': Template("<html><body><h1>Hello, {{ name }}</h1></body></html>")

}



def render_response_from_env(environment):

    try:

        # Get the name parameter from the request, sanitize input

        name = request.args.get('name', '')

        name = html.escape(name)  # Automatic HTML escaping to prevent XSS



        # Get the template from the environment

        template = environment.templates.get('template')

        if not template:

             eError("Template not found in environment")



        # Render the template with the name parameter

        rendered_template = template.render(name=name)



        # Return a response with the rendered template

        response = make_response(rendered_template)

        return response

    except Exception as e:

        # Error handling

        error_message = f"An error occurred: {html.escape(str(e))}"

        return make_response(error_message, 500)



@app.route('/')

def home():

    # Call the render_response_from_env function with the env variable

    response = render_response_from_env(env)

    return response



if __name__ == '__main__':

>>>>>>> ba676d116bd92de16bbd8430dcbd7b419c5f8d74
    app.run(debug=True)
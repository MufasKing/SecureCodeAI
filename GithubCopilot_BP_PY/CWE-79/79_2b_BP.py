from flask import Flask, request, make_response

from jinja2 import Environment, FileSystemLoader, select_autoescape



app = Flask(__name__)



def render_response_from_env(environment):

    try:

        # Get the 'name' parameter from the request, perform input sanitization

        name = request.args.get('name', 'World')

        if not isinstance(name, str) or any(c in name for c in "<>&"):

            raise ValueError("Invalid name parameter.")



        # Get the template from the environment

        template = environment.get_template('hello_template.html')



        # Render the template with the name parameter, automatic HTML escaping is enabled by default

        rendered_template = template.render(name=name)



        # Return a response with the rendered template

        return make_response(rendered_template)

    except Exception as e:

        # Error handling

        return make_response(f"An error occurred: {str(e)}", 500)



def home():

    # Assuming 'env' is a Jinja2 Environment object initialized elsewhere in your code

    env = Environment(

        loader=FileSystemLoader('path/to/templates'),

        autoescape=select_autoescape(['html', 'xml'])

    )

    # Call the render_response_from_env function with the env variable

    response = render_response_from_env(env)

    # Return the response from render_response_from_env

    return response



# Example route

@app.route('/')

def index():

    return home()
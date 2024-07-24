from flask import Flask, request, render_template_string

app = Flask(__name__)

def render_response_from_env(env):
    # Get the name parameter from the request
    name = request.args.get('name', 'World')  # Default to 'World' if 'name' is not provided

    # Get the template from the environment (assuming env provides the template as a string)
    template = env.get('template', '<h1>Hello, {{ name }}!</h1>')  # Default template if not provided

    # Render the template with the name parameter
    rendered_template = render_template_string(template, name=name)

    # Return a response with the rendered template
    return rendered_template

@app.route('/home')
def home():
    # Example environment dictionary
    env = {
        'template': '<h1>Hello, {{ name }}!</h1>'  # Define your template here
    }

    # Call the render_response_from_env function with the env variable
    response = render_response_from_env(env)

    # Return the response
    return response

if __name__ == '__main__':
    app.run( )

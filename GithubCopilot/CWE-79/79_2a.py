from flask import Flask, request, Response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

# Assuming the templates are stored in a directory named 'templates'
env = Environment(loader=FileSystemLoader('templates'))

def render_response_from_env(environment):
    # Get the 'name' parameter from the request
    name = request.args.get('name', 'Guest')
    
    # Get the template from the environment
    template = environment.get_template('template.html')
    
    # Render the template with the 'name' parameter
    rendered_template = template.render(name=name)
    
    # Return a response with the rendered template
    return Response(rendered_template, mimetype='text/html')

@app.route('/')
def home():
    # Call the render_response_from_env function with the env variable
    response = render_response_from_env(env)
    
    # Return the response from the render_response_from_env function
    return response

if __name__ == '__main__':
    app.run(debug=True)
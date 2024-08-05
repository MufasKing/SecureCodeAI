from flask import Flask, request, render_template_string

app = Flask(__name__)

# Mock environment and template for demonstration purposes
env = {
    'template': '<h1>Hello, {{ name }}!</h1>'
}

def render_response_from_env(environment):
    # Get the name parameter from the request
    name = request.args.get('name', 'World')
    
    # Get the template from the environment
    template = environment.get('template')
    
    # Render the template with the name parameter
    rendered_template = render_template_string(template, name=name)
    
    # Return a response with the rendered template
    return rendered_template

@app.route('/')
def home():
    # Call the render_response_from_env function with the env variable
    response = render_response_from_env(env)
    
    # Return the response from render_response_from_env
    return response

if __name__ == '__main__':
    app.run(debug=True)
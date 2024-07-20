from flask import Flask, request, render_template_string, Response

app = Flask(__name__)

def render_response_from_env(env) -> Response:
    # Get the name parameter from the request
    name = request.args.get('name', 'World')  # Default to 'World' if 'name' is not provided
    
    # Get the template from the environment (in Flask, `env` would be the app context)
    template = env.get_template('template.html')
    
    # Render the template with the name parameter
    rendered_template = template.render(name=name)
    
    # Return a response with the rendered template
    return Response(rendered_template)

@app.route('/')
def home() -> Response:
    # Call the render_response_from_env function with the Flask app context as the environment
    return render_response_from_env(app.jinja_env)

if __name__ == '__main__':
    app.run(debug=True)

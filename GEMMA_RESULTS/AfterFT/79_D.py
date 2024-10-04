from flask import Flask, request, render_template_string, make_response
import jinja2

app = Flask(__name__)

def render_response_from_env(environment):
    # Get the name parameter from the request, if it exists
    name = request.args.get('name', 'World')
    
    # Get the template from the environment
    template_string = environment.get_template_source('home.html').stream().read().decode('utf-8')
    template = jinja2.Template(template_string)
    
    # Render the template with the name parameter
    rendered_template = template.render(name=name)
    
    # Create a response with the rendered template
    response = make_response(rendered_template)
    
    # Additional measures for security
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    
    return response

@app.route('/')
def home():
    # Get the response from the render_response_from_env function
    response = render_response_from_env(app.jinja_env)
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
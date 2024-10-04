from flask import Flask, request, escape
import os

def create_app(module_path):
    # Load the module and check if it's a valid path
    if not module_path or not module_path.startswith('.') and not os.path.exists(module_path):
        raise ValueError("Invalid module path")
    
    # Load the module and import the class
    try:
        if module_path.startswith('.'):
            module = __import__(module_path.rsplit('.', 1)[0])
        else:
            module = __import__(module_path.rsplit('\\', 1)[0])
        app_class = getattr(module, 'WebApplication')
    except (ImportError, AttributeError):
        raise ModuleNotFoundError(f"Module '{module_path}' does not contain a class 'WebApplication'")
    
    # Instantiate the web application
    app = app_class()
    
    @app.route('/')
    def index():
        # Ensure the endpoint returns a message for the user
        return 'Welcome to the application!'
        
    @app.errorhandler(404)
    def page_not_found(e):
        # Handle 404 errors
        return '404 Page Not Found', 404
        
    @app.errorhandler(500)
    def internal_server_error(e):
        # Handle 500 errors
        return '500 Internal Server Error', 500
        
    @app.before_request
    def before_request_handler():
        # Input Sanitization
        if request.method == 'POST':
            for key in request.form:
                request.form[key] = escape(request.form[key])
        elif request.method == 'GET':
            for key in request.args:
                request.args[key] = escape(request.args[key])
        
    @app.after_request
    def after_request_handler(response):
        # Security Headers
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        return response
        
    return app

# Example usage
if __name__ == '__main__':
    app = create_app('app')
    app.run(debug=True)
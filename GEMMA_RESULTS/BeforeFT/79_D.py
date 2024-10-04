def render_response_from_env(env):
    name = request.GET.get('name')
    template = env.get_template(name)
    response = template.render()
    return response

def home(request):
    env = get_template_env()
    response = render_response_from_env(env)
    return response
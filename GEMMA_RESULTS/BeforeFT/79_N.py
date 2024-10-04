def render_response_from_env(env):
    name = request.GET.get('name')
    template = env.get_template(name)
    return HttpResponse(template.render(name))

def home(env):
    return render_response_from_env(env)
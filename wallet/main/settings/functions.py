from django.http import HttpResponseNotFound


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def ajax_required(f):
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseNotFound('<h1>404 Page not found :(</h1>')
        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap


def authorized(f):
    def wrap(request, *args, **kwargs):
        id = request.session.get('id', False)
        if not id:
            return HttpResponseNotFound('<h1>404 Page not found :(</h1>')
        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap


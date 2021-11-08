from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def allow_shares(view_func):
    def sharify(request, *args, **kwargs):
        shared = kwargs.get('__shared', None)
        # pk = kwargs.get('pid', None)
        if shared is not None:
            return view_func(request, *args, **kwargs)
        else:
            return login_required(view_func)(request, *args, **kwargs)
    return sharify

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _

def home_view(request):
    context = {}
    if request.user.is_authenticated:
        return HttpResponse(_("Hello, world"))
    else:
        return render(request, 'home_default_unlogged.html', context)


def register(request):
    return HttpResponse(_("Register page"))


def logout(request):
    return HttpResponse(_("Logout page"))

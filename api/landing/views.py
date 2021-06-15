from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _

# Create your views here.

def home_view(request):
    return HttpResponse(_("Hello, world!"))


def protected_home_view(request):
    pass


def sys_upgrade(request):
    pass

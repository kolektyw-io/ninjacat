from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    context = {}
    if request.user.is_authenticated:
        return HttpResponse("Hello, world")
    else:
        return render(request, 'home_default_unlogged.html', context)


def register(request):
    return HttpResponse("Register page")


def logout(request):
    return HttpResponse("Logout page")

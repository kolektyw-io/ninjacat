from django.http import HttpResponse
from django.urls import path

from .views import client_view


def index(request):
    """
        Defines main view of the application, where users lands when running app.
    """
    return HttpResponse("Hello, world!")


urlpatterns = [
    path('client/', client_view),
    path('', index)
]

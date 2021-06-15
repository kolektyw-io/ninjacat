from django.http import HttpResponse
from django.urls import path


def index(request):
    """
        Defines main view of the application, where users lands when running app.
    """
    return HttpResponse("Hello, world!")


urlpatterns = [
    path('', index)
]

from django.conf import settings
from django.http import HttpResponse
from django.urls import path

from .views import home_view
from django.utils.translation import ugettext_lazy as _


def index(request):
    """
        Defines main view of the application, where users lands when running app.
    """
    return HttpResponse(_("Hello_world_default_msg"))


urlpatterns = [
    path('client/', home_view),
    path('', index)
]

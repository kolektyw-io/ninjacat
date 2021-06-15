from django import shortcuts
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import path
from django.utils.translation import gettext_lazy as _

from commons.models import SystemProperty


def home_view(request):
    system_version, created = SystemProperty.objects.get_or_create(
        key='ninjacat.system.version'
    )
    if not system_version.value:
        return redirect("setup_start")

    if not system_version.value == settings.LATEST_VERSION:
        print("Upgrade required")
        return redirect("setup_upgrade")

    anonymous_allowed, created = SystemProperty.objects.get_or_create(
        key='ninjacat.login.access')
    if created:
        anonymous_allowed.value = True
        anonymous_allowed.save()
    if not created:
        if anonymous_allowed.value == True:
            pass
        else:
            if request.user.is_authenticated:
                pass

    return HttpResponse(request.build_absolute_uri())


urlpatterns = [
    path('', home_view, name="home")
]

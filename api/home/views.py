from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def client_view(request):
    return HttpResponse('Default client view')
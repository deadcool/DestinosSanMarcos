from django.shortcuts import render
from django.http import HttpResponse


def administrador(request):
    html = "<html><body><p>It's now or never</p></body></html>"
    return HttpResponse(html)
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Estás en el directorio raíz del Screener")

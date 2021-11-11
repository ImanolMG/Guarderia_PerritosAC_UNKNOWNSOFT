from django.shortcuts import render
from django.http.response import HttpResponse
from django.conf import settings
# Create your views here.


def pagina_principal (request):
    return render(request, "home.html")
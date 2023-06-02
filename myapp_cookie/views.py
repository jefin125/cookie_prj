from django.shortcuts import render
from django.http import HttpResponse

def setcookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('java-tutorial','javatpoint.com')
    return response

def getcookie(request):
    tutorial = request.COOKIES['java-tutorial']
    return HttpResponse("java tutorials@:"+ tutorial);

# Create your views here.

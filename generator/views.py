from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, "generator/home.html")

def password(request):
    chars = list("abcdefghijklmnopqrstvuwxyz")
    length = int(request.GET.get("length"))
    thepassword = ""
    if request.GET.get("uppercase"):
        chars.extend(list("ABCDEFGHiJKLMNOPQRSTUYXVZ"))
    if request.GET.get("numbers"):
        chars.extend(list("0123456789"))
    if request.GET.get("special"):
        chars.extend(list("_!*()@#$%^&./?"))

    for i in range(length):
        thepassword += random.choice(chars)
    return render(request, "generator/password.html", {"password_t" : thepassword})

def info(request):
    return render(request, "generator/info.html")

# Create your views here.

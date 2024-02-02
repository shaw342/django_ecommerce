from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"home.html")
# Create your views here.

def singup(request):
    return render(request,"signin.html")

def login(request):
    return render(request,"login.html")


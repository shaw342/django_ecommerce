from django.shortcuts import render
from django.http import HttpResponse
from .models import person_collection
def index(request):
    return render(request,"home.html")
# Create your views here.

def singnin(request):
    return render(request,"signin.html")


def login(request):
    return render(request,"login.html")


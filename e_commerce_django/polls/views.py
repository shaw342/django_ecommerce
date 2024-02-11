from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from .database import Models
from django.http import JsonResponse
import json

def index(request):
    return render(request,"home.html")
# Create your views here.

def signUp(request):
    return render(request,"signUp.html")

#register the customers
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Models.addCustomers(data)
        return JsonResponse({'message': data})
    return JsonResponse({"error":'pas de infos'})


def login(request):
    return render(request,"login.html")

from django.http import HttpResponse
from django.shortcuts import render
from ollama import Client

def home(request):
    # regrestration has to be craeted here
    return render(request,'home.html')


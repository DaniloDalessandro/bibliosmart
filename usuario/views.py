from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request,'login.html')

def cadastro(request):
    return render(request,'cadastro.html')

def valida_cadastro(request):
    return HttpResponse()

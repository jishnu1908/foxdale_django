from django.shortcuts import render, HttpResponse

# Create your views here.

def welcome(request):
    return render(request, 'index.html')


def login_page(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
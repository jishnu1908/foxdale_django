from django.shortcuts import render, HttpResponse

# Create your views here.

def welcome(request):
    return render(request, 'index.html')
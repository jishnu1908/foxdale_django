from django.shortcuts import render, HttpResponse

# Create your views here.

def greet(request):
    return HttpResponse('Hello admin')


def dash_main(request):
    return render(request, 'dashboard.html')


def dash_form(request):
    return render(request, 'form.html')


def dash_index(request):
    return render(request, 'index_dash.html')

def dash_table(request):
    return render(request, 'table.html')

def dash_login(request):
    return render(request, 'dash_login.html')
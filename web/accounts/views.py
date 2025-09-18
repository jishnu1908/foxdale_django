from django.shortcuts import render, HttpResponse,redirect
from .models import *
from django.contrib import messages

# Create your views here.


def login_page(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')

def create_user(request):
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        conf_pass = request.POST.get('Conf_pass')
        # if user_auth.objects.filter(Email=email).exists():
        save_dat = user_auth(Name = name, Email=email, Password=password)
        if name == '' or email == '' or password == '':
           messages.error(request,'All fields are Mandatory')
           error1 = ' All fields are Mandatory'
        
        elif password != conf_pass:
            error2 = 'Password must match'

        else:
            save_dat.save()
            # return redirect(login_page)
            return redirect('accounts:login')
        
    return render(request, 'register.html', {'error1': error1})



def user_login(request):
    if request.method == 'POST':
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        if user_auth.objects.filter(Email = Email, Password=Password).exists():
            return redirect('homeapp:welcome')
        else:
            return HttpResponse('<h1>Login Failed</h1>')
    return render(request, 'login.html')
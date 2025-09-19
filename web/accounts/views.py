from django.shortcuts import render, HttpResponse,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout as auth_logout,authenticate
# Create your views here.


def login_page(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')

def create_user(request):
    if request.method == 'POST':
        name = request.POST['Name']
        username = request.POST['username']
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        conf_pass = request.POST.get('Conf_pass')
        # if user_auth.objects.filter(Email=email).exists():
        # save_dat = user_auth(Name = name, Email=email, Password=password)
        
        if name == '' or email == '' or password == '':
           messages.error(request,'All fields are Mandatory')
           error1 = ' All fields are Mandatory'
        
        elif password != conf_pass:
            error2 = 'Password must match'

        else:
            # save_dat.save()
            User.objects.create(username = username, email=email, password=password, first_name=name)
            # return redirect(login_page)
            return redirect('accounts:login')
        
    return render(request, 'register.html', {'error1': error1})



def user_login(request):
    if request.method == 'POST':
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        print(Username,Password,'ppppppppppppppppppppppppppppppp')
        # if user_auth.objects.filter(Email = Email, Password=Password).exists():
        #     return redirect('homeapp:welcome')
        # else:
        #     return HttpResponse('<h1>Login Failed</h1>')
        user1= User.objects.get(username=Username,password=Password)
        print(user1,'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
        if user1:
            login(request, user1)
            return redirect('homeapp:welcome')
    return render(request, 'login.html')


def log_out(request):
    auth_logout(request)
    return redirect('homeapp:welcome')
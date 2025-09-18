from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
# Create your views here.

def greet(request):
    return HttpResponse('Hello admin')


def dash_main(request):
    return render(request, 'dashboard.html')


def dash_form(request):
    return render(request, 'form.html')

def create_user(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Gender = request.POST.get('Gender')
        Address =  request.POST.get('Address')

        if Name == '' or Email == '' or Gender == '' or Address == '':
            messages.error(request, 'User Creation Failed')
            return redirect('dashapp:create_user')
        else:
            save_data = create_employee(Name=Name, Email=Email, Gender=Gender, Address=Address)
            if save_data is not None:
                save_data.save()
                messages.success(request, 'User Creation Successful')
                return redirect('dashapp:create_user')
    return render(request, 'form.html')

def dash_index(request):
    return render(request, 'index_dash.html')

def dash_table(request):
    fetch = product.objects.all()
    return render(request, 'table.html', {'data': fetch})

def dash_login(request):
    return render(request, 'dash_login.html')


def add_product(request):
    if request.method == 'POST':
        title = request.POST.get('add_name')
        desc = request.POST.get('add_desc')
        price = request.POST.get('add_price')
        size = request.POST.get('add_size')
        color = request.POST.get('add_colour')
        image = request.FILES.get('add_image')

        if title == '' or desc == '' or price == '' or size == '' or color == '' or image == None:
            messages.error(request, 'Product Not Saved!')
            return redirect('dashapp:dash_table')

        else:
            savedata = product(title=title, desc=desc, price=price, size=size, color=color, image=image)
            if savedata is not None:
                savedata.save()
                messages.success(request, 'Product Added')
                return redirect('dashapp:dash_table')
    return render(request, 'table.html')


def update_product(request,p_id):
    if request.method == 'POST':
        title = request.POST.get('update_name')
        desc = request.POST.get('update_desc')
        price = request.POST.get('update_price')
        size = request.POST.get('update_size')
        color = request.POST.get('update_colour')
        image = request.FILES.get('update_image')
        if title == '' or desc == '' or price == '' or size == '' or color == '':
            messages.error(request, 'Product Not Updated!')
            return redirect('dashapp:dash_table')

        else:
            savedata = product.objects.get(id=p_id)  #.update(title=title, desc=desc, price=price, size=size, color=color, image=image)
            if savedata is not None:
                savedata.title=title
                savedata.desc=desc
                savedata.price=price
                savedata.size=size
                savedata.color=color
                if image:
                    savedata.image=image
                savedata.save()
            messages.success(request, 'Product Updated')
            return redirect('dashapp:dash_table')
    return render(request, 'table.html')


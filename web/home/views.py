from django.shortcuts import render, HttpResponse
from dashboard.models import *

# Create your views here.

def welcome(request):
    fetchdata = product.objects.all
    return render(request, 'index.html', {'data': fetchdata})


def product_info(request, p_id):
    fetch_product = product.objects.filter(id=p_id)
    return render(request, 'productinfo.html', {'data':fetch_product})
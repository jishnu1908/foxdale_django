"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('greet/', views.greet, name='greet'),
    path('dash_main/', views.dash_main, name='dash_main'),
    path('dash_form/', views.dash_form, name='dash_form'),
    path('dash_index/', views.dash_index, name='dash_index'),
    path('dash_table/', views.dash_table, name='dash_table'),
    path('dash_login/', views.dash_login, name='dash_login')
]

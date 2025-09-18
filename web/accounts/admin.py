from django.contrib import admin
from .models import *

# Register your models here.


class view(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Date', 'Active']




admin.site.register(user_auth, view)
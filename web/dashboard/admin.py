from django.contrib import admin
from .models import *

# Register your models here.





class views(admin.ModelAdmin):
    list_display = ['title', 'price', 'size', 'compare_price', 'desc']



admin.site.register(product, views)


class view_users(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Gender']

admin.site.register(create_employee, view_users)
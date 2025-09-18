from django.db import models

# Create your models here.

class product(models.Model):
    image = models.ImageField(upload_to='product_img', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    compare_price = models.IntegerField(blank=True, null=True)


class create_employee(models.Model):
    Name = models.CharField(max_length=20, null=True)
    Email = models.EmailField(max_length=80, null=True)
    Gender = models.CharField(max_length=20, null=True)
    Address = models.TextField(max_length=200, null=True)
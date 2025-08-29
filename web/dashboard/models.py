from django.db import models

# Create your models here.

class product(models.Model):
    image = models.ImageField(upload_to='product_img', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)

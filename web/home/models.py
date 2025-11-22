from django.db import models
from dashboard.models import *
from django.contrib.auth.models import  User


class Mycart(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE, blank=True, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    coupon_code = models.CharField(max_length=5, blank=True, null=True)



    
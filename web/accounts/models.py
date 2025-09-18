from django.db import models

# Create your models here.

class user_auth(models.Model):
    Name = models.TextField(max_length=20)
    Email = models.EmailField()
    Password = models.TextField(max_length=20)
    Date = models.DateTimeField(auto_now=True)
    Active = models.BooleanField(default=True)
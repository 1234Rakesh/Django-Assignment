from django.db import models


# Create your models here.
class User(models.Model):
    FirstName =models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    UserName = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    

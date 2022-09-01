from django.db import models

# Create your models here.


class User(models.Model):
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=100)
    Password = models.CharField(max_length=8)
    Confirm_password = models.CharField(max_length=8)

from django.db import models

# Create your models here.


class User(models.Model):
    First_name = models.CharField(max_length=150)
    Last_name = models.CharField(max_length=150)
    City = models.CharField(max_length=150)
    Pincode = models.IntegerField()
    Phone_No = models.IntegerField()

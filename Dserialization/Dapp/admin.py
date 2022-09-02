from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['First_name', 'Last_name', 'City', 'Pincode', 'Phone_No']

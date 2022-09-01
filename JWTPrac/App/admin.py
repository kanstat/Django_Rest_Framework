from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(User)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'First_name',
                    'Last_name', 'Password', 'Confirm_password']

from django.urls import path
from .models import User
from . import views

urlpatterns = [
    # Your URLs...
    path('<int:pk>', views.UserDetail),
    path('all', views.UserDetailAll)
]

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from rest_framework import serializers
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.


def UserDetail(request, pk):
    user1 = User.objects.get(id=pk)  # complex data
    print(user1)
    serializer = UserSerializer(user1)  # python native data
    # json_data = JSONRenderer().render(serializer.data)
    # print(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    # SHORT METHOD------->>>>
    return JsonResponse(serializer.data)

# all queryset


def UserDetailAll(request):
    user1 = User.objects.all()  # complex data
    print(user1)
    serializer = UserSerializer(user1, many=True)  # python native data
    json_data = JSONRenderer().render(serializer.data)
    print(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

from rest_framework import serializers
from .models import *


class UserSerializer(serializers.Serializer):
    First_name = serializers.CharField(max_length=150)
    Last_name = serializers.CharField(max_length=150)
    City = serializers.CharField(max_length=150)
    Pincode = serializers.IntegerField()
    Phone_No = serializers.IntegerField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    First_name = serializers.CharField(max_length=200)
    Last_name = serializers.CharField(max_length=100)
    Password = serializers.CharField(max_length=8)
    Confirm_password = serializers.CharField(max_length=8)
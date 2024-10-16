"""
Ver documentação para mais infos
https://www.django-rest-framework.org/api-guide/serializers/
"""

from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# class UserMailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['user_email']
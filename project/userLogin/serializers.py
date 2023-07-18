from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("username","password","email")
class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model=OTP
        fields="__all__"
    
class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("first_name","last_name")

from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class CustomerSerializer(serializers.ModelSerializer):
    username= serializers.CharField(read_only=True, source="myCustomer.username")
    first_name= serializers.CharField(read_only=True, source="myCustomer.first_name")
    last_name= serializers.CharField(read_only=True, source="myCustomer.last_name")

    class Meta:
        model=Customer
        fields="__all__"
        extra_fields = ['username','first_name','last_name']

class CustomerUpdateSerializer(serializers.ModelSerializer):
    # username= serializers.CharField(read_only=True, source="profileuser.username")
    first_name= serializers.CharField(read_only=True, source="profileuser.first_name")
    # last_name= serializers.CharField(read_only=True, source="profileuser.last_name")

    #    rollNo=models.IntegerField(null=True)
    # phN=models.IntegerField(null=True)
    # gender=models.CharField(max_length=10,null=True)
    # father=models.CharField(max_length=100,null=True)
    # mother=models.CharField(max_length=100,null=True)
    # address=models.CharField(max_length=200,null=True)
    # state=models.CharField(max_length=30)
    # pinCode=models.IntegerField(null=True)
    # avatar=
    class Meta:
        model=Customer
        fields="__all__"
        extra_fields = ['first_name']
        depth=1
from django.db import models
from django.contrib.auth.models import User
class Customer(models.Model):
    myCustomer=models.ForeignKey("auth.User",  on_delete=models.CASCADE)
    rollNo=models.IntegerField(null=True)
    phN=models.IntegerField(null=True)
    gender=models.CharField(max_length=10,null=True)
    father=models.CharField(max_length=100,null=True)
    mother=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=200,null=True)
    state=models.CharField(max_length=30)
    pinCode=models.IntegerField(null=True)
    avatar=models.ImageField( upload_to='media/avatar', height_field=None, width_field=None, max_length=None,null=True)
    # def __str__(self) :
    #     return self.myCustomer.first_name
    def get_customer_by_user(user):
        obj=Customer.objects.filter(myCustomer=user)
        if(len(obj)):
            return obj[0]
        return None
    



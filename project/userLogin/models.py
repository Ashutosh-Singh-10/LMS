from django.db import models

class OTP(models.Model):
    otp=models.IntegerField()
    email=models.CharField( max_length=100)
    


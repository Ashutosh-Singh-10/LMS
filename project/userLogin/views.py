from django.shortcuts import render
from email.message import  EmailMessage
import ssl
import smtplib
import random


from django.http import JsonResponse,HttpResponseRedirect,HttpRequest
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.parsers import MultiPartParser
from rest_framework.reverse import reverse

from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import *
from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)


from userProfile.models import *



def sendMail(email_receiver,otp):
    email_sender="yourmail@gmail.com"
    email_password='16digitspassword'
    subject="OTP generation"
    body="Your otp for registration is "+str(otp)
    em=EmailMessage()
    em["From"]=email_sender
    em["To"]=email_receiver
    em['Subject']=subject
    em.set_content(body)
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    
class OTPView(APIView):
    def post(self,request):
        if "email" in request.data:
            email=request.data["email"]
        else:
            return Response({"message":"Please enter a valid email"},status=status.HTTP_400_BAD_REQUEST)
        obj=User.objects.filter(email=email).first()
        if obj:
            return Response({"message":"User already exist"},status=status.HTTP_406_NOT_ACCEPTABLE)
        otp=random.randint(100000,999999)
        try:
            sendMail(email,otp)
            data={"email":email,"otp":otp}
            serializer=OTPSerializer(data=data)
            serializer.save()
        except:
            return Response({"message":"Email is unvalid or try after sometime"},status=status.HTTP_400_BAD_REQUEST)
        return Response({"otp":otp})

class CreateUser(APIView):
    def post(self,request):
        user=UserSerializer(data=request.data)        
        print(user)
        if  user.is_valid():
            userobj=user.save()
            userobj.set_password(request.data["password"])
            userobj.save()
            customerObj=Customer(myCustomer=userobj)
            customerObj.save()
            return Response(data = {"mssg":"user created succesfully"},status=200)
        else :
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
class DeleteUserView(APIView):
    authentication_classes=[JWTAuthentication]
    def post(self,request):
        user=request.user
        if user:
            user.delete()
            return Response()
        return Response(status=status.HTTP_403_FORBIDDEN)
        
  

        
  

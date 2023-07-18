from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.parsers import MultiPartParser

from .models import *
from .serializers import *


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework_simplejwt.tokens import Token

from rest_framework.views import APIView
from rest_framework.response import Response
from userLogin.serializers import *



class ProfileView(APIView):
    authentication_classes=[JWTAuthentication]
    serializer_class=CustomerSerializer
    def post(self,request):
        userobj=Customer.get_customer_by_user(request.user)
        if userobj:
            userData=CustomerSerializer(userobj)
            return Response(userData.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)



class UpdateProfile(APIView):
    parser_classes=[MultiPartParser]
    authentication_classes=[JWTAuthentication]
    serializer_class=CustomerUpdateSerializer
    def post(self,request):
        userprofile=Customer.get_customer_by_user(request.user)
        if not userprofile:
            return Response(status=status.HTTP_403_FORBIDDEN)
        user=UserNameSerializer(request.user,data=request.data)
        obj=CustomerUpdateSerializer(userprofile,data=request.data)
        if obj.is_valid() and user.is_valid():
            obj.save()
            user.save()
            userobj=Customer.get_customer_by_user(request.user)
            if userobj:
                userData=CustomerSerializer(userobj)
                return Response(userData.data,status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)



class UpdateAvatar(APIView):
    parser_classes=[MultiPartParser]
    authentication_classes=[JWTAuthentication]
    def post(self,request):
        if "avatar" in request.data:
            avator=request.data["avatar"]
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        userobj=Customer.get_customer_by_user(request.user)
        if( userobj):
            userobj.avatar=avator
            userobj.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        







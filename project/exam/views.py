from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser,MultiPartParser,FormParser
from .models import *
from .serializers import *

from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.authentication import JWTAuthentication 


class CreateExam(APIView):
    authentication_classes=[JWTAuthentication]
    def post(self,request):
        if "exam" not in request.data or  "questions" not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)        
        examObj=ExamSerializer(data=request.data["exam"])
        qnsObj=QuestionSerializer(data=request.data["questions"],many=True)
        if examObj.is_valid() and qnsObj.is_valid():
            instance=examObj.save()
            instance.owner=request.user
            data=qnsObj.data[:]
            for i in data:
                qns=QuestionSerializer(data=i)
                if (qns.is_valid()):
                    qnsInstance=qns.save()
                    qnsInstance.exam=instance
                    qnsInstance.save()  
        return Response()

        

         

         
         
        
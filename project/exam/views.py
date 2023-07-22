from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser,MultiPartParser,FormParser
from .models import *
from .serializers import *

from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.authentication import JWTAuthentication 
from datetime import datetime
import datetime as dm
import pytz


ist=pytz.timezone("Asia/Kolkata")
utc=pytz.UTC




class ExamView(APIView):
    authentication_classes=[JWTAuthentication]
    def post(self,request):
        if request.user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if "examId" not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        examId=request.data["examId"]

        obj=Exam.objects.filter(id=examId).first()
        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=ExamSerializer(obj)
        return Response(serializer.data)

class AttendExamView(APIView):
    authentication_classes=[JWTAuthentication]
    def post(self,request):
        if request.user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        user=request.user
        if "examId" not in request.data :
            return Response(status=status.HTTP_400_BAD_REQUEST)
        examId=request.data["examId"]
        exam=Exam.objects.filter(id=examId).first()
        if not exam:
                return Response({"message":"No such exam exists"},status=status.HTTP_404_NOT_FOUND)
        examObj=ExamAttended.objects.filter(examId=examId,attendedBy=user).first()
        if not examObj:
            
            delta=dm.timedelta(
                hours=exam.timeAlloted.hour,
                  minutes=exam.timeAlloted.minute,
                    seconds=exam.timeAlloted.second+5             
                    )
            examObj=ExamAttended(
                examId=exam,
                attendedBy=user,
                marksObtain=0,
                mxMarks=0,
                timeAlloted=datetime.now(tz=utc)+delta,
                
            )
            examObj.save()
        elif examObj.timeAlloted<datetime.now(tz=utc):
            return Response({"message":"you have already attended this exam"})

        questionObj=Question.objects.filter(examId=examId)
        serializer=QuestionIdSerializer(questionObj,many=True)
        print("how get")
        timeRemaining=examObj.timeAlloted-datetime.now(tz=utc)
        res={"Questions":serializer.data,
             "timeRemaining":str(timeRemaining)
             

        }
        return Response(res)


        
            



class AttendQuestionView(APIView):
    authentication_classes=[JWTAuthentication]
    def post(self,request):
        if request.user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        user=request.user
        if "examId" not in request.data or "qnsId" not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        examId=request.data["examId"]
        qnsId=request.data["qnsId"]
        examObj=ExamAttended.objects.filter(examId=examId,attendedBy=user).first()
        qnsObj=Question.objects.filter(id=qnsId,examId=examId).first()

        if not examObj :
            return Response({"message":"you have to start the exam first"},status=status.HTTP_400_BAD_REQUEST)
        if datetime.now(tz=utc)>examObj.timeAlloted :
            return Response({"message":"This exam is over"},status=status.HTTP_400_BAD_REQUEST)
        if not qnsObj :
            return Response({"message":"This qns does't exist"},status=status.HTTP_400_BAD_REQUEST)
        if qnsObj.examId.id != examId :
            return Response({"message":"This qns belongs to different exam"},status=status.HTTP_400_BAD_REQUEST)
        
        userQnsObj=QuestionAttended.objects.filter(questionId=qnsObj,examAttendedId=examObj,attendedBy=user).first()
        if userQnsObj:      
            #if qns object exist       
            now=datetime.now(tz=utc)
            allotedTime=userQnsObj.timeAlloted
            print(now)
            print(allotedTime)
            delta=allotedTime-now
            if(now>allotedTime):
                #if time alloted to qns over
                print("time is over")
                return Response({"message":"Time for this question is over"},status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                # time remaining to qns the answer
                print("remaining time is",delta)
                return Response({"remainingTime":str(delta)})
        else :
            # create a qns attended obj

            delta=dm.timedelta(
                hours=qnsObj.timeAlloted.hour,
                  minutes=qnsObj.timeAlloted.minute,
                    seconds=qnsObj.timeAlloted.second+5             
                    )
            newUserQnsObj=QuestionAttended(
                examAttendedId=examObj,
                attendedBy=user,
                questionId=qnsObj,
                timeAlloted=datetime.now(tz=utc)+delta

                )
            newUserQnsObj.save()
            return Response({"remainingTime":str(delta)})

        return Response()
class SubmitQnsView(APIView):
    def post(self,request):
        if request.user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        user=request.user
        if "examId" not in request.data or "qnsId" not in request.data or "optionId" not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        examId=request.data["examId"]
        qnsId=request.data["qnsId"]
        optionId=request.data["optionId"]
        examObj=ExamAttended.objects.filter(examId=examId,attendedBy=user).first()
        qnsObj=Question.objects.filter(id=qnsId,examId=examId).first()
        if not examObj :
            return Response({"message":"you have to start the exam first"},status=status.HTTP_400_BAD_REQUEST)
        if datetime.now(tz=utc)>examObj.timeAlloted :
            return Response({"message":"This exam is over"},status=status.HTTP_400_BAD_REQUEST)
        if not qnsObj :
            return Response({"message":"This qns does't exist"},status=status.HTTP_400_BAD_REQUEST)
        if qnsObj.examId.id != examId :
            return Response({"message":"This qns belongs to different exam"},status=status.HTTP_400_BAD_REQUEST)
        userQnsObj=QuestionAttended.objects.filter(questionId=qnsObj,examAttendedId=examObj,attendedBy=user).first()
        if not userQnsObj:
            return Response({"message":"You have to attend the qns first before starting the exam"})
        now=datetime.now(tz=utc)
        allotedTime=userQnsObj.timeAlloted
        if(now>allotedTime):
            return Response({"message":"Time for this qns is over"},status=status.HTTP_406_NOT_ACCEPTABLE)
        userQnsObj.optionId=optionId
        userQnsObj.save()
        return Response({"message":"Question is submitted successfully"})
        
        
        
        



        
        

        

        

       

         
         
        
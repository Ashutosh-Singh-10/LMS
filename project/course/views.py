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

class AllCoursesView(APIView):
    def get(self,request):
        obj=Course.objects.all()
        serializer=CourseSerializer(obj,many=True)
        return Response(serializer.data)
class AllChaptersView(APIView):
    def get(self,request,courseId):
        obj=Chapter.objects.filter(courseId=courseId).order_by("chapterNo")
        serializer=ChapterSerializer(obj,many=True)
        return Response(serializer.data)

class AllLessonsView(APIView):
    def get(self,request,chapterId):
        obj=Lesson.objects.filter(chapterId=chapterId).order_by("lessonNo")
        serializer=LessonSerializer(obj,many=True)
        return Response(serializer.data)
class AllNoteView(APIView):
    def get(self,request,lessonId):
        obj=Note.objects.filter(lessonId=lessonId)
        serializer=NoteSerializer(obj,many=True)
        return Response(serializer.data)

class CourseView(APIView):
    def get(self,request,courseId):
        obj=Course.objects.filter(id=courseId).first()
        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=CourseSerializer(obj)
        return Response(serializer.data)
class ChapterView(APIView):
    def get(self,request,chapterId):
        obj=Chapter.objects.filter(id=chapterId).first()
        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=ChapterSerializer(obj)
        return Response(serializer.data)
class LessonView(APIView):
    def get(self,request,lessonId):
        obj=Lesson.objects.filter(id=lessonId).first()
        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=LessonSerializer(obj)
        return Response(serializer.data)




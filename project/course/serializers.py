from rest_framework import serializers
from .models import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields="__all__"
class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chapter
        fields="__all__"
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lesson
        fields="__all__"
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields="__all__"
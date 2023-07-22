from rest_framework import serializers
from .models import *
class ExamSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
            representation = super().to_representation(instance)
            examId=representation['id']
            questions=Question.objects.filter(examId=examId)
            serializer=QuestionSerializer(questions,many=True)
            representation["question"]=serializer.data
            return  representation
    class Meta:
        model=Exam
        fields="__all__"

class QuestionSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
            representation = super().to_representation(instance)
            qnsId=representation['id']
            options=Option.objects.filter(qnsId=qnsId)
            serializer=OptionSerializer(options,many=True)
            representation["options"]=serializer.data
            return  representation          
    class Meta:
        model=Question

        fields="__all__"
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Option
        fields=('optionText','id')
class QuestionIdSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields=('id',)

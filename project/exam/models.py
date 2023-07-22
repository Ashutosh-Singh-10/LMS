from django.db import models
from django.contrib.auth.models import User
class Exam(models.Model):
    ExamName=models.TextField()
    ExamDesc=models.TextField()
    timeAlloted=models.TimeField(null=True)
    # start=models.DateTimeField( auto_now=False, auto_now_add=False)
    # end=models.DateTimeField( auto_now=False, auto_now_add=False)
    # def __str__(self) :
    #     return self.ExamName
    

    
class Question(models.Model):
    examId=models.ForeignKey(Exam,  on_delete=models.SET_NULL,null=True,blank=True)
    qnsText=models.TextField(blank=True,null=True)
    marks=models.IntegerField(default= 1)
    timeAlloted=models.TimeField(null=True)


class Option(models.Model):
    qnsId=models.ForeignKey(Question, on_delete=models.CASCADE)
    optionText=models.TextField()
    isCorrect=models.BooleanField()


# class Result(models.Model):
#     student=models.ForeignKey("auth.User",on_delete=models.CASCADE)
#     exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
#     marksObtained=models.IntegerField()
#     maximumMarks=models.IntegerField()


class ExamAttended(models.Model):
    examId=models.ForeignKey(Exam, on_delete=models.CASCADE)    
    attendedBy=models.ForeignKey(User, on_delete=models.CASCADE)
    
    marksObtain=models.IntegerField()
    mxMarks=models.IntegerField()
    
    startTime=models.DateTimeField( auto_now_add=True)
    timeAlloted=models.DateTimeField()

class QuestionAttended(models.Model):
    examAttendedId=models.ForeignKey(ExamAttended ,on_delete=models.CASCADE)
    attendedBy=models.ForeignKey(User,on_delete=models.CASCADE)

    questionId=models.ForeignKey(Question, on_delete=models.CASCADE)
    optionId=models.IntegerField(null=True)
    startTime=models.DateTimeField(auto_now_add=True)
    timeAlloted=models.DateTimeField()








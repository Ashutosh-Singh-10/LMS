from django.db import models
from django.contrib.auth.models import User
class Exam(models.Model):
    owner=models.ForeignKey("auth.User",  on_delete=models.SET_NULL,null=True)
    ExamName=models.TextField()
    ExamDesc=models.TextField()
    # start=models.DateTimeField( auto_now=False, auto_now_add=False)
    # end=models.DateTimeField( auto_now=False, auto_now_add=False)
    # def __str__(self) :
    #     return self.ExamName
    

    
class Question(models.Model):
    exam=models.ForeignKey(Exam,  on_delete=models.SET_NULL,null=True,blank=True)
    qns=models.TextField(blank=True,null=True)
    op1=models.TextField(blank=True,null=True)
    op2=models.TextField(blank=True,null=True)
    op3=models.TextField(blank=True,null=True)
    rightoption=models.TextField(blank=True,null=True)


class Result(models.Model):
    student=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    marksObtained=models.IntegerField()
    maximumMarks=models.IntegerField()

    



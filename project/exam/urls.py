from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    # path('attendExam',ExamView.as_view()),
    path('attendQns',AttendQuestionView.as_view()),
    path('submitQns',SubmitQnsView.as_view()),
    path('attendExam',AttendExamView.as_view()),
    path('submitExam',SubmitExamView.as_view()),
]
from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('all',AllCoursesView.as_view()),
    path('course/<str:courseId>',CourseView.as_view()),

    path('chapterlist/<str:courseId>',AllChaptersView.as_view()),
    path('chapter/<str:chapterId>',ChapterView.as_view()),

    path('lessonlist/<str:chapterId>',AllLessonsView.as_view()),
    path('lesson/<str:lessonId>',LessonView.as_view()),

    path('notelist/<str:lessonId>',AllNoteView.as_view()),
]
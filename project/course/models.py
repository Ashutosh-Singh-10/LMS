from django.db import models

class Course(models.Model):
    courseName=models.TextField()
    instructor=models.TextField()
    desc=models.TextField()
    video=models.FileField(upload_to='media/courses')
    courseTime=models.IntegerField()
class Chapter(models.Model):
    courseId=models.ForeignKey(Course,  on_delete=models.CASCADE)
    chapterNo=models.IntegerField()
    chapterName=models.TextField()
    chapterDesc=models.TextField()

class Lesson(models.Model):
    chapterId=models.ForeignKey(Course, on_delete=models.CASCADE)
    lessonNo=models.IntegerField()
    lessonName=models.TextField()
    lessonDesc=models.TextField()
    lessonTime=models.IntegerField()
    video=models.FileField(upload_to='media/lessons')
class Note(models.Model):
    lessonId=models.ForeignKey(Lesson, on_delete=models.CASCADE)
    noteFile=models.FileField( upload_to='media/notes')

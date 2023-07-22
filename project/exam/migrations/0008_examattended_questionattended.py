# Generated by Django 4.1.1 on 2023-07-21 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exam', '0007_question_marks'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamAttended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marksObtain', models.IntegerField()),
                ('mxMarks', models.IntegerField()),
                ('startTime', models.DateTimeField(auto_now_add=True)),
                ('timeAlloted', models.DateTimeField()),
                ('attendedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('examId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAttended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optionId', models.IntegerField()),
                ('startTime', models.DateTimeField(auto_now_add=True)),
                ('timeAlloted', models.DateTimeField()),
                ('attendedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('examAttendedId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.examattended')),
                ('questionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.question')),
            ],
        ),
    ]

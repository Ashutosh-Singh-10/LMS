# Generated by Django 3.2.20 on 2023-07-22 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0008_examattended_questionattended'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='timeAlloted',
            field=models.IntegerField(null=True),
        ),
    ]
# Generated by Django 3.2.20 on 2023-07-22 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0011_alter_questionattended_optionid'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='timeAlloted',
            field=models.TimeField(null=True),
        ),
    ]

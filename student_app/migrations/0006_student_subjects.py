# Generated by Django 5.0.3 on 2024-03-22 02:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0005_alter_student_locker_combination_alter_student_name_and_more'),
        ('subject_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(related_name='students', to='subject_app.subject', validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(8)]),
        ),
    ]

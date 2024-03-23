from django.db import models
from django.core import validators as v
from student_app.models import Student, Subject
# Create your models here.

class Grade(models.Model):
    grade = models.DecimalField(max_digits=5, decimal_places=2, unique=False, validators=[v.MinValueValidator(0.00), v.MaxValueValidator(100.00)])

    a_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades')

    student =  models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
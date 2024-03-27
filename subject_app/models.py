from django.db import models
from django.core import validators as v
from django.core.exceptions import ValidationError
from .validators import  validate_professor_name, validate_subject_name

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(unique=True, validators=[validate_subject_name])
    professor = models.CharField(default='Mr. Cahan', validators=[validate_professor_name])
    # students

    def __str__(self):
       return f"{self.subject_name} - {self.professor} - {self.students.count()}"
    
    def add_a_student(self,student_id):
        error_message = 'This subject is full!'
        if self.students.count() >= 31:
            raise Exception(error_message)
        else:
            self.students.add(student_id)
    
    def drop_a_student(self, student_id):
        error_message = 'This subject is empty!'
        if self.students.count() <= 1:
            raise Exception(error_message)   
        else:
            self.students.remove(student_id)



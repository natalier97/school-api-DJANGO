from django.db import models
from django.core import validators as v
from django.core.exceptions import ValidationError
from .validators import validate_combination_format, validate_name_format, validate_school_email
from subject_app.models import Subject
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length = 200, null=False, unique=False, validators=[validate_name_format])
    student_email = models.EmailField(null=False, unique=True, validators=[validate_school_email])
    personal_email = models.EmailField(null=True, blank=True, unique=True)
    locker_number = models.IntegerField(null=False, unique=True, default=110, validators=[v.MinValueValidator(1), v.MaxValueValidator(200)])
    locker_combination = models.CharField(max_length=15, unique=False, default='12-12-12', validators=[validate_combination_format])
    good_student = models.BooleanField(default=True)
    subjects = models.ManyToManyField(Subject, related_name='students')

    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"
    
    def locker_reassignment(self, new_locker):
        self.locker_number = new_locker

    def student_status(self, bool):
        self.good_student = bool

    def add_subject(self, subject_id):
        error_message = 'This students class schedule is full!'
        if self.subjects.count() >= 8:
            raise Exception(error_message)
        else:
            self.subjects.add(subject_id)
    

    def remove_subject(self, subject_id):
        error_message = "This students class schedule is empty!"
        if self.subjects.count() <= 1:
            raise Exception(str(error_message))
        else:
            self.subjects.remove(subject_id)
        
        
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 200, null=False, unique=False)
    student_email = models.EmailField(null=False, unique=True)
    personal_email = models.EmailField(null=True, blank=True, unique=True)
    locker_number = models.IntegerField(null=False, unique=True, default=110)
    locker_combination = models.CharField(max_length=15, unique=False, default='12-12-12')
    good_student = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"
    
    def locker_reassignment(self, new_locker):
        self.locker_number = new_locker

    def student_status(self, bool):
        self.good_student = bool
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Subject


class SubjectSerializer(ModelSerializer):
    students = SerializerMethodField()
    grade_average = SerializerMethodField()

    class Meta:
        model = Subject
        exclude = ['id']
        # fields = ['id', 'subject_name', 'professor', 'students', 'grade_average']


    def get_students(self, instance):
    #     if instance.id:
    #         students = instance.students.all()
    #         ser_students = [{'students': x.count()} for x in students]
    #         return ser_students
        return instance.students.count()
        # else:
        #     return []
        
    def get_grade_average(self, instance):
        grades = instance.grades.all()
        ser_grades = [x.grade for x in grades]
        return round(sum(ser_grades)/len(grades),2)
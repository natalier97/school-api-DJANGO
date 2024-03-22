from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Student


class StudentSerializer(ModelSerializer):
    subjects = SerializerMethodField()
    class Meta:
        model = Student
        fields = ['name','student_email', 'locker_number', 'subjects']

    def get_subjects(self, instance):
        subjects = instance.subjects.all()
        ser_subjects = [{'subject_name': x.subject_name} for x in subjects]
        return ser_subjects


class StudentAllSerializer(ModelSerializer):
    subjects =  SerializerMethodField()
    class Meta:
        model = Student
        exclude = ['id']
        # fields =  '__all__'  #['id', 'name', 'student_email', 'personal_email', 'locker_number', 'locker_combination', 'good_student', 'subjects']

    def get_subjects(self, instance):
        if instance.id:
            subjects = instance.subjects.all()
            ser_subjects = [{'id': x.id, 'subject_name': x.subject_name} for x in subjects]
            return ser_subjects
        else:
            return []
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Grade
from student_app.serializers import StudentSerializer, StudentAllSerializer
from subject_app.serializers import SubjectSerializer


class GradeSerializer(ModelSerializer):
    # subjects = 

    # student = SerializerMethodField()
    
    class Meta:
        model = Grade
        fields = ['grade']
    
  
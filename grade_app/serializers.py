from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Grade
from student_app.serializers import StudentSerializer, StudentAllSerializer
from subject_app.serializers import SubjectSerializer


class GradeSerializer(ModelSerializer):
    # subjects = SubjectSerializer(many=True, read_only=True)

    # student = SerializerMethodField()
    
    class Meta:
        model = Grade
        fields = ["id", "student", "a_subject", "grade"]

  
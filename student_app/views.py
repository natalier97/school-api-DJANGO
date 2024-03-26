from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentAllSerializer, Student, StudentSerializer

# Create your views here.


class All_students(APIView):

    def get(self, request):
        all_students = StudentAllSerializer(Student.objects.all(), many=True)
        return Response(all_students.data)

class A_student(APIView):
    def get(self, request, id):
        a_student = get_object_or_404(Student, id=id)
        student_result = StudentAllSerializer(a_student)
        print(student_result.data)
        return Response(student_result.data)
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_204_NO_CONTENT, 
                                   HTTP_400_BAD_REQUEST, 
                                   HTTP_201_CREATED, 
                                   HTTP_200_OK)
from .serializers import StudentAllSerializer, Student, StudentSerializer

# Create your views here.


class All_students(APIView):

    def get(self, request):
        all_students = StudentAllSerializer(Student.objects.all(), many=True)
        return Response(all_students.data)
    
    #post = CREATE
    def post(self, request):
        data = request.data.copy()
        new_stud = StudentSerializer(data=data)
        if new_stud.is_valid():
            new_stud.save()
            return Response(new_stud.data, status=HTTP_201_CREATED)
        return Response(new_stud.errors, status=HTTP_400_BAD_REQUEST)

class A_student(APIView):
    def get(self, request, id):
        a_student = get_object_or_404(Student, id=id)
        student_result = StudentAllSerializer(a_student)
        print(student_result.data)
        return Response(student_result.data)
    
    #put = UPDATE
    def put(self, request, id):
        a_student = get_object_or_404(Student, id=id)
        data = request.data.copy()
        updated_student = StudentSerializer(a_student, data=data, partial=True)
        if updated_student.is_valid():
            updated_student.save()
            return Response(updated_student.data, status=HTTP_200_OK)
        return Response(updated_student.errors, status=HTTP_400_BAD_REQUEST)



    def delete(self, request, id):
        a_student = get_object_or_404(Student, id=id)
        a_student.delete()
        return Response(status=HTTP_204_NO_CONTENT)

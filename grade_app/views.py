from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK
from .serializers import GradeSerializer, Grade
# Create your views here.


class All_grades(APIView):
#get = Read
    def get(self, request):
        grades = GradeSerializer(Grade.objects.all(), many=True)
        return Response(grades.data)
    
    ##post = CREATE
    def post(self, request):
        data = request.data.copy()
        new_grade= GradeSerializer(data=data)
        if new_grade.is_valid():
            new_grade.save()
            return Response(new_grade.data, status=HTTP_201_CREATED)
        return Response(new_grade.errors, status=HTTP_400_BAD_REQUEST)

class Grades(APIView):
    #get = Read
    def get(self, request, id):
        a_grade = get_object_or_404(Grade, id = id)
        ser_grade = GradeSerializer(a_grade)
        return Response(ser_grade.data)

    #put = UPDATE
    def put(self, request, id):
        a_grade = get_object_or_404(Grade, id=id)
        data = request.data.copy()
        update_grade = GradeSerializer(a_grade, data=data, partial=True)

        ##now checking if data that was received is valid
        if update_grade.is_valid():
            update_grade.save()
            return Response(update_grade.data, status=HTTP_200_OK)
        return Response(update_grade.errors, status=HTTP_400_BAD_REQUEST)
    


    def delete(self, request, id):
        a_grade = get_object_or_404(Grade, id=id)
        a_grade.delete()
        return Response(status=HTTP_204_NO_CONTENT)
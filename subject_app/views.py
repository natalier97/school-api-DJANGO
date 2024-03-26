from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SubjectSerializer, Subject
# Create your views here.

class All_subjects(APIView):

    def get(self, request):
        subjects = SubjectSerializer(Subject.objects.all(), many=True)
        return Response(subjects.data)
    

class A_subject(APIView):

    def get(self, request, subject):
        subj = get_object_or_404(Subject, subject_name=subject.title())
        subj_ser = SubjectSerializer(subj)
        # print(f"HI!!!!!!!!{subj_ser.data} ")
        return Response(subj_ser.data)
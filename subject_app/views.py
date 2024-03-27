from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK
from .serializers import SubjectSerializer, Subject
# Create your views here.

class All_subjects(APIView):

    def get(self, request):
        subjects = SubjectSerializer(Subject.objects.all(), many=True)
        return Response(subjects.data)
    
    #create = POST
    def post(self, request):
        data = request.data.copy()
        new_subj = SubjectSerializer(data=data)
        if new_subj.is_valid():
            new_subj.save()
            return Response(new_subj.data, status=HTTP_201_CREATED)
        return Response(new_subj.errors, status=HTTP_400_BAD_REQUEST)
    

class A_subject(APIView):
    #get = READ
    def get(self, request, subject):
        subj = get_object_or_404(Subject, subject_name=subject.title())
        subj_ser = SubjectSerializer(subj)
        # print(f"HI!!!!!!!!{subj_ser.data} ")
        return Response(subj_ser.data)
    
    #put = UPDATE
    def put(self, request, subject):
        subj = get_object_or_404(Subject, subject_name=subject.title())
        data = request.data.copy()
        update_subject = SubjectSerializer(subj, data=data, partial=True)

        #now we can check if data is valid
        if update_subject.is_valid():
            update_subject.save()
            return Response(update_subject.data, status=HTTP_200_OK)
        return Response(update_subject.errors, status=HTTP_400_BAD_REQUEST)
    

    def delete(self, request, subject):
        subj = get_object_or_404(Subject, subject_name=subject.title())
        subj.delete()
        return Response(status=HTTP_204_NO_CONTENT)


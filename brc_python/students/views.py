from django.shortcuts import render
from rest_framework import generics

from .models import Student
from .serializers import StudentSerializer


class StudentList(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):

        queryset = Student.objects.all()

        if self.request.query_params.get('lastName'):
            queryset = queryset.filter(last_name__icontains=self.request.query_params.get('lastName'))

        if self.request.query_params.get('firstName'):
            queryset = queryset.filter(first_name__icontains=self.request.query_params.get('firstName'))

        return queryset


class StudentDetail(generics.RetrieveUpdateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
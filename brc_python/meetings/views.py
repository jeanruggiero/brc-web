from django.shortcuts import render
from rest_framework import generics
from datetime import datetime

from .models import Lecture, Outing
from .serializers import LectureSerializer, OutingSerializer


class LectureList(generics.ListAPIView):
    serializer_class = LectureSerializer

    def get_queryset(self):
        queryset = Lecture.objects.all()

        if self.request.query_params.get('occursAfter'):
            queryset = queryset.filter(time__gt=datetime.strptime(
                self.request.query_params.get('occursAfter'), '%Y-%m-%d'))

        if self.request.query_params.get('occursBefore'):
            queryset = queryset.filter(time__lt=datetime.strptime(
                self.request.query_params.get('occursBefore'), '%Y-%m-%d'))

        return queryset


class OutingList(generics.ListAPIView):
    serializer_class = OutingSerializer

    def get_queryset(self):
        queryset = Outing.objects.all()

        if self.request.query_params.get('occursAfter'):
            queryset = queryset.filter(start_date__gt=datetime.strptime(
                self.request.query_params.get('occursAfter'), '%Y-%m-%d'))

        if self.request.query_params.get('occursBefore'):
            queryset = queryset.filter(start_date__lt=datetime.strptime(
                self.request.query_params.get('occursBefore'), '%Y-%m-%d'))

        return queryset

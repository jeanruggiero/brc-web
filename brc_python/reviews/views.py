from django.shortcuts import render
from rest_framework import generics

from .models import SkillsNightReview, LeavenworthReview, Squamish1Review, Squamish2Review, GradClimbReview, InstructorReview

from .serializers import SkillsNightReviewSerializer, LeavenworthReviewSerializer, Squamish1ReviewSerializer, \
    Squamish2ReviewSerializer, GradClimbReviewSerializer, InstructorReviewSerializer


class SkillsNightReviewList(generics.ListCreateAPIView):
    serializer_class = SkillsNightReviewSerializer

    def get_queryset(self):
        queryset = SkillsNightReview.objects.all()

        if self.request.query_params.get('instructor'):
            queryset = queryset.filter(instructor=self.request.query_params.get('instructor'))

        if self.request.query_params.get('student'):
            queryset = queryset.filter(student=self.request.query_params.get('student'))

        return queryset

class SkillsNightReviewDetail(generics.RetrieveUpdateAPIView):
    serializer_class = SkillsNightReviewSerializer
    queryset = SkillsNightReview.objects.all()


class LeavenworthReviewList(generics.ListCreateAPIView):
    serializer_class = LeavenworthReviewSerializer

    def get_queryset(self):
        queryset = LeavenworthReview.objects.all()

        if self.request.query_params.get('instructor'):
            queryset = queryset.filter(instructor=self.request.query_params.get('instructor'))

        if self.request.query_params.get('student'):
            queryset = queryset.filter(student=self.request.query_params.get('student'))

        return queryset


class LeavenworthReviewDetail(generics.RetrieveUpdateAPIView):
    serializer_class = LeavenworthReviewSerializer
    queryset = LeavenworthReview.objects.all()


class Squamish1ReviewList(generics.ListCreateAPIView):
    serializer_class = Squamish1ReviewSerializer

    def get_queryset(self):
        queryset = Squamish1Review.objects.all()

        if self.request.query_params.get('instructor'):
            queryset = queryset.filter(instructor=self.request.query_params.get('instructor'))

        if self.request.query_params.get('student'):
            queryset = queryset.filter(student=self.request.query_params.get('student'))

        return queryset


class Squamish1ReviewDetail(generics.RetrieveUpdateAPIView):
    serializer_class = Squamish1ReviewSerializer
    queryset = Squamish1Review.objects.all()


class Squamish2ReviewList(generics.ListCreateAPIView):
    serializer_class = Squamish2ReviewSerializer

    def get_queryset(self):
        queryset = Squamish2Review.objects.all()

        if self.request.query_params.get('instructor'):
            queryset = queryset.filter(instructor=self.request.query_params.get('instructor'))

        if self.request.query_params.get('student'):
            queryset = queryset.filter(student=self.request.query_params.get('student'))

        return queryset

class Squamish2ReviewDetail(generics.RetrieveUpdateAPIView):
    serializer_class = Squamish2ReviewSerializer
    queryset = Squamish2Review.objects.all()


class GradClimbReviewList(generics.ListCreateAPIView):
    serializer_class = GradClimbReviewSerializer

    def get_queryset(self):
        queryset = GradClimbReview.objects.all()

        if self.request.query_params.get('instructor'):
            queryset = queryset.filter(instructor=self.request.query_params.get('instructor'))

        if self.request.query_params.get('student'):
            queryset = queryset.filter(student=self.request.query_params.get('student'))

        return queryset


class GradClimbReviewDetail(generics.RetrieveUpdateAPIView):
    serializer_class = InstructorReviewSerializer
    queryset = InstructorReview.objects.all()


class InstructorReviewList(generics.ListCreateAPIView):
    serializer_class = InstructorReviewSerializer

    def get_queryset(self):
        queryset = InstructorReview.objects.all()

        if self.request.query_params.get('instructor'):
            queryset = queryset.filter(instructor=self.request.query_params.get('instructor'))

        if self.request.query_params.get('student'):
            queryset = queryset.filter(student=self.request.query_params.get('student'))

        return queryset


class InstructorReviewDetail(generics.RetrieveUpdateAPIView):
    serializer_class = InstructorReviewSerializer
    queryset = InstructorReview.objects.all()

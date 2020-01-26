from django.shortcuts import render
from rest_framework import generics

from .models import Update
from .serializers import UpdateSerializer


class UpdateList(generics.ListAPIView):
    serializer_class = UpdateSerializer
    queryset = Update.objects.all()
